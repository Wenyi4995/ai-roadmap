# 2026 Week 01：重新建立节奏并跑通 PyTorch

## 本周三个核心成果

1. 建立每天稳定开始的习惯，连续 7 天留下记录。
2. 完成 Python、NumPy、Tensor 和 Autograd 基础练习。
3. 完成线性回归的手动实现与 PyTorch 标准实现。

前三天每天计划 2 个 25 分钟专注块，后四天每天计划 3 个。每天最低目标是完成 1 个专注块。

## 每日安排

| 天数 | 技术任务 | 算法题 | 成果位置 |
|---|---|---|---|
| Day 1 | Python 基础自测、熟悉 Git | 两数之和 | `learning/python/exercises/week01/python_review.py` |
| Day 2 | NumPy、矩阵乘法与广播 | 有效的括号 | `learning/python/exercises/week01/numpy_basics.py` |
| Day 3 | Tensor 与 Autograd | 买卖股票的最佳时机 | `learning/pytorch/exercises/week01/` |
| Day 4 | 线性回归、MSE、梯度下降 | 二分查找 | `projects/linear-regression/train_manual.py` |
| Day 5 | `nn.Module`、Loss、Optimizer | 合并两个有序链表 | `projects/linear-regression/train_pytorch.py` |
| Day 6 | 代码整理与 Loss 可视化 | 最大子数组和 | 项目 README 与实验结果 |
| Day 7 | 闭卷复现与复盘 | 爬楼梯 | `logs/2026/08/week-01.md` |

## 每天开始前

```text
手机离开桌面
→ 打开当天文件
→ 写下唯一最小任务
→ 设置 25 分钟
→ 开始
```

## 环境与运行

第一周使用 CPU 即可，不要求 GPU。

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python learning\python\exercises\week01\python_review.py
```

## 完成定义

1. 代码能够运行。
2. 自己能够解释核心步骤。
3. 更新本周日志和算法题记录。
4. 使用清晰的提交信息保存成果。

## 降级方案

- 状态差：只完成 1 个 25 分钟专注块。
- 环境配置失败：记录完整报错，先完成不依赖环境的算法题或原理笔记。
- 漏掉一天：第二天恢复正常计划，不补偿、不加倍。
