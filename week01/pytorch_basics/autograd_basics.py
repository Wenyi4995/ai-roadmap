"""Day 3: 使用 Autograd 验证手工求导结果。"""

import torch


def main() -> None:
    x = torch.tensor(2.0, requires_grad=True)
    y = x**2 + 3 * x + 1
    y.backward()

    expected_gradient = 2 * 2.0 + 3
    assert x.grad is not None
    assert x.grad.item() == expected_gradient
    print(f"x={x.item()}, y={y.item()}, dy/dx={x.grad.item()}")

    # TODO: 分别验证 y=x^3 和 y=2x^2+5x 在 x=2 时的梯度。


if __name__ == "__main__":
    main()
