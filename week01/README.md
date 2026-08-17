# 第一周：重新建立节奏并跑通 PyTorch

## 本周目标

- 建立每天稳定开始的习惯
- 跑通 Python、NumPy 和 PyTorch
- 理解 Tensor 与自动求导
- 完成第一个线性回归训练程序
- 完成 7 道简单算法题

前三天每天完成 2 个 25 分钟专注块，后四天每天完成 3 个。每天的最低目标是完成 1 个专注块。

## 每日安排

| 天数 | 技术任务 | 算法题 | 成果文件 |
|---|---|---|---|
| Day 1 | Python 基础自测、熟悉 Git | 两数之和 | `python_basics/python_review.py` |
| Day 2 | NumPy、矩阵乘法与广播 | 有效的括号 | `python_basics/numpy_basics.py` |
| Day 3 | Tensor 与 Autograd | 买卖股票的最佳时机 | `pytorch_basics/` |
| Day 4 | 线性回归、MSE、梯度下降 | 二分查找 | `linear_regression/train_manual.py` |
| Day 5 | `nn.Module`、Loss、Optimizer | 合并两个有序链表 | `linear_regression/train_pytorch.py` |
| Day 6 | 代码整理与 Loss 可视化 | 最大子数组和 | 项目 README 与图片 |
| Day 7 | 闭卷复现与复盘 | 爬楼梯 | `notes/week01_review.md` |

## 每天开始前

```text
手机离开桌面
→ 打开当天文件
→ 写下唯一最小任务
→ 设置 25 分钟
→ 开始
```

## 运行方式

在仓库根目录创建虚拟环境并安装依赖，然后运行相应脚本。第一周使用 CPU 即可，不要求 GPU。

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python week01\python_basics\python_review.py
```

## 完成定义

“完成”必须同时满足：

1. 代码能够运行。
2. 自己能够解释核心步骤。
3. 更新打卡和每日记录。
4. 提交本次成果。
