"""线性回归基础巩固题：学习 y = -2x + 1。"""

import torch


def main() -> None:
    torch.manual_seed(7)

    # TODO 1：
    # 在 -3 到 3 之间均匀生成 120 个 x，
    # 并将形状改成 (120, 1)。
    x = torch.linspace(-3,3,steps=120).reshape(-1,1)

    # TODO 2：
    # 生成与 x 形状相同的随机噪声，噪声强度为 0.15。
    # 根据 y = -2x + 1 + noise 生成真实标签。
    noise = torch.randn_like(x)*0.15
    y = -2*x + 1 + noise

    print("x shape:",x.shape)
    print("y shape",y.shape)
    print("前5个x为:\n",x[:5])
    print("前5个y为:\n",y[:5])


    # TODO 3：
    # 创建初始值为 0.0 的参数 w 和 b，
    # 并设置 requires_grad=True。
    w = torch.tensor(0.0,requires_grad=True)
    b = torch.tensor(0.0,requires_grad=True)

    learning_rate = 0.02
    epochs = 800

    # TODO 4：
    # 使用 for 循环训练 800 轮。
    #
    # 每一轮依次完成：
    # 1. predictions = w*x+b
    # 2. 计算 MSE Loss
    # 3. loss.backward()
    # 4. 在 torch.no_grad() 中更新 w、b
    # 5. 清空 w、b 的梯度
    for epoch in range(epochs):
        predictions = w*x+b
        errors = predictions - y
        loss = (errors**2).mean()
        loss.backward()

        assert w.grad is not None
        assert b.grad is not None

        with torch.no_grad():
            w -= learning_rate*w.grad
            b -= learning_rate*b.grad

        w.grad.zero_()
        b.grad.zero_()
    # TODO 5：
    # 每隔 100 轮打印 epoch、Loss、w 和 b。
        if epoch % 100 == 0 :
            print(
                f"epoch={epoch},"
                f"loss={loss},"
                f"w={w},"
                f"b={b}"
            )
    # TODO 6：
    # 训练结束后检查：
    # w 应接近 -2
    # b 应接近 1
    assert abs(w.item() - (-2.0)) < 0.1
    assert abs(b.item() - 1.0) < 0.1


if __name__ == "__main__":
    main()