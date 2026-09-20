"""不使用 nn.Linear，手动完成线性回归。

按 README 中的步骤逐项替换 TODO。完成前允许脚本不可运行。
"""

import torch


def main() -> None:
    torch.manual_seed(42)

    # TODO 1: 构造 x 和 y = 3x + 2 + noise。
    x = torch.linspace(-2, 2, steps=100).reshape(-1, 1)
    noise = torch.randn_like(x) * 0.2
    y = 3 * x + 2 + noise

    print("x shape:", x.shape)
    print("y shape:", y.shape)
    print("前5个x:\n", x[:5])
    print("前5个y:\n", y[:5])
    # TODO 2: 定义需要梯度的参数 w 和 b。
    w = torch.tensor(0.0, requires_grad=True)
    b = torch.tensor(0.0, requires_grad=True)

    print("初始w:", w.item())
    print("初始b:", b.item())
    print("w是否需要梯度:", w.requires_grad)
    print("b是否需要梯度:", b.requires_grad)
    learning_rate = 0.005
    epochs = 1000

    # TODO 5：重复训练
    for epoch in range(epochs):
        # 前向传播
        predictions = w * x + b
        loss = ((predictions - y) ** 2).mean()

        # 反向传播
        loss.backward()

        assert w.grad is not None
        assert b.grad is not None

        # 更新参数
        with torch.no_grad():
            w -= learning_rate * w.grad
            b -= learning_rate * b.grad

        # 清空梯度
        w.grad.zero_()
        b.grad.zero_()

        # 每100轮打印一次
        if epoch % 100 == 0 or epoch == epochs - 1:
            print(
                f"epoch={epoch}, "
                f"loss={loss.item():.6f}, "
                f"w={w.item():.4f}, "
                f"b={b.item():.4f}"
            )


if __name__ == "__main__":
    main()