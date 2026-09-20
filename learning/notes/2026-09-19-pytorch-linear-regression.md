# 2026-09-19：PyTorch 标准组件版线性回归

## 今日核心

- `nn.Module` 是模型基类；`super().__init__()` 先初始化父类，随后才能注册 `self.linear`。
- `nn.Linear(1, 1)` 表示每条数据有 1 个输入特征、产生 1 个输出；内部有可学习的 `weight`（形状 `(1, 1)`）和 `bias`（形状 `(1,)`）。
- `model(inputs)` 调用模型的前向计算，得到预测值；`nn.MSELoss()` 将预测值与目标值的平方误差取平均。
- `torch.optim.SGD(model.parameters(), lr=0.01)` 管理模型参数的更新；`model.parameters()` 提供要学习的参数，`lr` 控制步长。

## 一轮训练：清 → 算 → 比 → 反 → 改

```python
optimizer.zero_grad()                       # 清空旧梯度
predictions = model(inputs)                 # 前向计算
loss = loss_function(predictions, targets)  # 计算误差
loss.backward()                             # 求参数梯度
optimizer.step()                            # 更新参数
```

`backward()` 只求梯度，`step()` 才更新参数。标准组件没有改变手写版的数学过程，只是封装了参数管理、MSE 和更新操作。

## 易错点与结果

- `__init__()` 中使用 `self.linear`；在 `model = LinearRegressionModel()` 完成后，才可使用 `model.linear`。
- 本练习每轮使用全部 200 条数据，因此一次循环就是一个 epoch；以后分小批训练时，一个 epoch 会包含多次参数更新。
- 已运行 `train_pytorch.py`：最终 `weight ≈ 3.0000`、`bias ≈ 2.0000`，断言通过。

下次：对比手动版与标准版，并尝试改变学习率观察 Loss 曲线。
