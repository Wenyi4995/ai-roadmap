"""Day 3: PyTorch Tensor 基础。"""

import torch


def main() -> None:
    features = torch.tensor([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    weights = torch.tensor([0.5, -0.25])

    # TODO 1: 打印 features 的形状和数据类型。
    # TODO 2: 通过矩阵乘法计算预测结果。
    # TODO 3: 将 features 改造成形状为 (2, 3) 的张量。


if __name__ == "__main__":
    main()
