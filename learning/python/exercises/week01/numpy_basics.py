"""Day 2: NumPy 与矩阵运算练习。"""

import numpy as np


def main() -> None:
    features = np.array([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])
    weights = np.array([0.5, -0.25])
    bias = 1.0

    # TODO 1: 计算每一列的平均值。
    column_mean = None

    # TODO 2: 对每列特征进行中心化。
    centered_features = None

    # TODO 3: 使用矩阵乘法计算 predictions = features @ weights + bias。
    predictions = None

    print("column_mean:", column_mean)
    print("centered_features:\n", centered_features)
    print("predictions:", predictions)


if __name__ == "__main__":
    main()
