"""Day 5: 使用 PyTorch 标准组件完成线性回归。"""

import torch
from torch import nn


class LinearRegressionModel(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        # TODO: 创建一个输入维度为 1、输出维度为 1 的线性层。

    def forward(self, inputs: torch.Tensor) -> torch.Tensor:
        # TODO: 返回模型预测。
        raise NotImplementedError


def main() -> None:
    torch.manual_seed(42)

    # TODO 1: 构造训练数据。
    # TODO 2: 创建模型、MSELoss 和 SGD 优化器。
    # TODO 3: 完成 zero_grad、forward、loss、backward、step 训练循环。
    # TODO 4: 输出最终参数并与 w=3、b=2 比较。
    raise NotImplementedError


if __name__ == "__main__":
    main()
