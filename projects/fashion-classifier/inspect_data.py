"""Provided data-preview tool. Run it before writing the classifier yourself."""

import argparse
import gzip
import hashlib
from pathlib import Path
import struct
import urllib.request

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import torch


PROJECT = Path(__file__).resolve().parent
DATA = PROJECT / "data"
SOURCE = "https://raw.githubusercontent.com/zalandoresearch/fashion-mnist/master/data/fashion/"
FILES = {
    "train-images-idx3-ubyte.gz": "8d4fb7e6c68d591d4c3dfef9ec88bf0d",
    "train-labels-idx1-ubyte.gz": "25c81989df183df01b3e8a0aad5dffbe",
}
CLASSES = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
           "Sandal", "Shirt", "Sneaker", "Bag", "Ankle boot"]


def load_training_data(download=False):
    """Return uint8 arrays: images (N, 28, 28), labels (N,)."""
    for filename, checksum in FILES.items():
        path = DATA / filename
        if not path.exists():
            if not download:
                raise FileNotFoundError("Missing dataset. Run this script with --download first.")
            DATA.mkdir(parents=True, exist_ok=True)
            print("Downloading:", filename, flush=True)
            with urllib.request.urlopen(SOURCE + filename, timeout=30) as response:
                content = response.read()
            if hashlib.md5(content).hexdigest() != checksum:
                raise ValueError("Downloaded dataset checksum mismatch: " + filename)
            path.write_bytes(content)
        if hashlib.md5(path.read_bytes()).hexdigest() != checksum:
            raise ValueError("Cached dataset checksum mismatch: " + str(path))

    with gzip.open(DATA / "train-images-idx3-ubyte.gz", "rb") as stream:
        magic, count, rows, columns = struct.unpack(">IIII", stream.read(16))
        if magic != 2051 or (rows, columns) != (28, 28):
            raise ValueError("Unexpected image header")
        images = np.frombuffer(stream.read(), dtype=np.uint8).reshape(count, rows, columns).copy()
    with gzip.open(DATA / "train-labels-idx1-ubyte.gz", "rb") as stream:
        magic, label_count = struct.unpack(">II", stream.read(8))
        labels = np.frombuffer(stream.read(), dtype=np.uint8).copy()
    if magic != 2049 or label_count != count or len(labels) != count:
        raise ValueError("Image/label counts do not match")
    return images, labels


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--download", action="store_true", help="Download the public training data if missing")
    args = parser.parse_args()
    images, labels = load_training_data(download=args.download)
    batch = torch.from_numpy(images[:32]).unsqueeze(1).float() / 255.0
    targets = torch.from_numpy(labels[:32]).long()
    print("Python environment: PyTorch", torch.__version__)
    print("Dataset images:", images.shape, "labels:", labels.shape)
    print("Input batch:", tuple(batch.shape), batch.dtype)
    print("Target batch:", tuple(targets.shape), targets.dtype)
    print("Pixel range:", batch.min().item(), "to", batch.max().item())

    figure, axes = plt.subplots(4, 4, figsize=(8, 8))
    for index, axis in enumerate(axes.flat):
        axis.imshow(images[index], cmap="gray", vmin=0, vmax=255)
        axis.set_title(CLASSES[int(labels[index])], fontsize=10)
        axis.axis("off")
    figure.tight_layout()
    output = PROJECT / "runs" / "data_preview.png"
    output.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output, dpi=120)
    plt.close(figure)
    print("Saved preview:", output)
    print("No model has been trained. Explain the batch dimensions before continuing.")


if __name__ == "__main__":
    main()
