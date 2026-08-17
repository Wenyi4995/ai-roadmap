"""Day 4: 不使用 nn.Linear，手动完成线性回归。

按 README 中的步骤逐项替换 TODO。完成前允许脚本不可运行。
"""

import torch


def main() -> None:
    torch.manual_seed(42)

    # TODO 1: 构造 x 和 y = 3x + 2 + noise。
    # TODO 2: 定义需要梯度的参数 w 和 b。
    # TODO 3: 完成前向计算和 MSE。
    # TODO 4: 反向传播并在 torch.no_grad() 中更新参数。
    # TODO 5: 每隔固定轮数打印 Loss、w 和 b。
    raise NotImplementedError


if __name__ == "__main__":
    main()
