"""使用 PyTorch 标准组件完成线性回归。"""

import torch
from torch import nn
import matplotlib.pyplot as plt


class LinearRegressionModel(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        # TODO: 创建一个输入维度为 1、输出维度为 1 的线性层。
        self.linear = nn.Linear(
            in_features=1,
            out_features=1
        )


    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        # TODO: 返回模型预测。

        return self.linear(inputs)


def main() -> None:
    torch.manual_seed(42)

    # TODO 1: 构造训练数据。
    inputs = torch.linspace(-2, 2, steps=200).reshape(-1, 1)
    targets = 3 * inputs + 2
    # TODO 2: 创建模型、MSELoss 和 SGD 优化器。
    model = LinearRegressionModel()

    loss_function = nn.MSELoss()

    optimizer = torch.optim.SGD(
        model.parameters(),
        lr=0.005
    )
    print(model.linear.weight)
    print(model.linear.bias)    
    # TODO 3: 完成 zero_grad、forward、loss、backward、step 训练循环。
    epochs = 1000
    loss_history = []

    for epoch in range(epochs):
        # 1. 清空上一轮梯度
        optimizer.zero_grad()

        # 2. 前向传播
        predictions = model(inputs)

        # 3. 计算Loss
        loss = loss_function(predictions, targets)

        loss_history.append(loss.item())

        # 4. 反向传播
        loss.backward()

        # 5. 更新模型参数
        optimizer.step()

        # 每100轮输出一次
        if epoch % 100 == 0 or epoch == epochs - 1:
            print(
                f"epoch={epoch}, "
                f"loss={loss.item():.6f}, "
                f"weight={model.linear.weight.item():.4f}, "
                f"bias={model.linear.bias.item():.4f}"
            )
    # TODO 4: 输出最终参数并与 w=3、b=2 比较。
    learned_weight = model.linear.weight.item()
    learned_bias = model.linear.bias.item()

    plt.plot(loss_history)
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.title("Training Loss")
    plt.grid(True)
    plt.savefig("projects/linear-regression/loss_curve.png")
    # 用训练完成后的模型重新预测
    with torch.no_grad():
        fitted_values = model(inputs)

    # 新建一张图
    plt.figure()
    plt.scatter(
        inputs[:, 0].tolist(),
        targets[:, 0].tolist(),
        label="True values",
        s=12
    )
    plt.plot(
        inputs[:, 0].tolist(),
        fitted_values[:, 0].tolist(),
        color="red",
        label="Model predictions"
    )
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Linear Regression Fit")
    plt.legend()
    plt.grid(True)
    plt.savefig("projects/linear-regression/fit_result.png")
    plt.close()

    print("记录了多少轮 Loss:", len(loss_history))
    print("第一轮 Loss:", loss_history[0])
    print("最后一轮 Loss:", loss_history[-1])
    print("训练完成")
    print("学习到的weight:", learned_weight)
    print("学习到的bias:", learned_bias)

    assert abs(learned_weight - 3.0) < 0.1
    assert abs(learned_bias - 2.0) < 0.1


if __name__ == "__main__":
    main()
