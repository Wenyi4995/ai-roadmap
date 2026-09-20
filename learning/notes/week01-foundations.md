# Week 01：Python、NumPy 与 PyTorch 基础笔记

> 最近更新：2026-09-16  
> 用途：整理学习过程中提出的问题，保留可长期复习的结论与最小示例。

## 整理规则

每个知识点尽量包含：

1. 曾经的误解；
2. 正确理解；
3. 最小示例；
4. 一句话记忆。

---

## 1. Python 基础

### 1.1 `print()` 是什么

**曾经的误解：** 不清楚 `print()` 在代码中的角色。

**正确理解：** `print()` 是 Python 内置函数，用于把文字、变量或表达式结果输出到终端。

**最小示例：**

```python
age = 23
print("年龄：", age)
```

**一句话记忆：** `print()` 负责显示，不负责计算。

### 1.2 属性与方法有什么区别

**曾经的误解：** 认为 `features.shape` 是调用 `features` 包下面的函数。

**正确理解：** `features` 是 Tensor 对象，不是包；`shape` 是对象的属性。通常有括号的是方法，没有括号的是属性。

**最小示例：**

```python
print(features.shape)          # 读取属性
new_features = features.reshape(2, 3)  # 调用方法
```

**一句话记忆：** `对象.属性` 读取信息，`对象.方法()` 执行操作。

### 1.3 `if __name__ == "__main__"` 的作用

**曾经的误解：** 将双下划线写成 Markdown 的 `**name**`。

**正确理解：** 当文件被直接运行时，Python 会把 `__name__` 设置为 `"__main__"`，于是调用 `main()`；被其他文件导入时则不会自动调用。

**最小示例：**

```python
def main():
    print("程序开始")


if __name__ == "__main__":
    main()
```

**一句话记忆：** 它是 Python 文件直接运行时的入口判断。

### 1.4 `assert` 的作用

**曾经的误解：** 不清楚它是判断、输出还是计算。

**正确理解：** `assert` 用于确认一个本应成立的条件；条件为假时抛出 `AssertionError`，常用于练习检查和测试。

**最小示例：**

```python
result = 2 + 3
assert result == 5, "计算结果不正确"
```

**一句话记忆：** `assert` 是“如果这件事不成立，程序就报错”。

### 1.5 `item()` 的作用

**曾经的误解：** 不确定它是不是把 Tensor 转换成数字。

**正确理解：** `item()` 把只含一个元素的 Tensor 转成普通 Python 数字；多元素 Tensor 不能直接调用 `item()`。

**最小示例：**

```python
x = torch.tensor(2.0)
number = x.item()  # 2.0，类型为 float
```

**一句话记忆：** 单元素 Tensor 用 `item()` 取出普通数字，多元素 Tensor 可用 `tolist()`。

### 1.6 `for row in features` 为什么每次得到一行

**曾经的误解：** 认为 Python 是看到变量名 `row` 后才知道它代表一行。

**正确理解：** 变量名可以任意修改；遍历二维数组时，每次取第一维中的一个元素，而这个元素恰好是一行。只有调用 `append()` 才会向结果列表增加数据。

**最小示例：**

```python
result = []

for row in features:
    result.append(row)
```

**一句话记忆：** 数据结构决定每次取出什么，变量名不决定行为。

---

## 2. NumPy 基础

### 2.1 `np` 是什么

**曾经的误解：** 不清楚 `np.` 是特殊语法还是缩写。

**正确理解：** `np` 是导入 NumPy 时指定的别名；点号表示使用这个库提供的功能。

**最小示例：**

```python
import numpy as np

numbers = np.array([1, 2, 3])
average = np.mean(numbers)
```

**一句话记忆：** `np` 是 NumPy 的常用简称，也是区分功能来源的命名空间。

### 2.2 NumPy 与 Java `Math` 的区别

**曾经的误解：** 认为 NumPy 是 Python 自带、类似 Java `Math` 的基础类。

**正确理解：** Python 自带的 `math` 更接近 Java `Math`；NumPy 是第三方库，主要用于数组、向量和矩阵的批量计算。

**最小示例：**

```python
import math
import numpy as np

single = math.sqrt(16)
many = np.sqrt(np.array([1, 4, 9, 16]))
```

**一句话记忆：** `math` 处理单个数字，NumPy 擅长批量数组和矩阵。

### 2.3 `mean` 与 `axis=0`

**曾经的误解：** 认为 `axis=0` 直接等于“列”。

**正确理解：** `mean` 表示平均值；`axis=0` 表示沿第 0 维计算并压缩这一维。二维矩阵第 0 维是行，因此留下每一列的结果。

**最小示例：**

```python
features = np.array([
    [1.0, 2.0],
    [3.0, 4.0],
    [5.0, 6.0],
])

column_mean = np.mean(features, axis=0)  # [3.0, 4.0]
row_mean = np.mean(features, axis=1)     # [1.5, 3.5, 5.5]
```

**一句话记忆：** `axis=0` 压缩行、保留每列结果；`axis=1` 压缩列、保留每行结果。

### 2.4 特征中心化与广播

**曾经的误解：** 没有显式循环，不理解为什么每一列都能减去自己的平均值。

**正确理解：** 中心化就是每个元素减去所在列的平均值；NumPy 会将形状为 `(2,)` 的列均值广播到 `(3, 2)` 的每一行。

**最小示例：**

```python
column_mean = np.mean(features, axis=0)
centered_features = features - column_mean
```

结果：

```text
[[-2, -2],
 [ 0,  0],
 [ 2,  2]]
```

**一句话记忆：** 广播相当于 NumPy 在底层替我们完成兼容形状的重复计算。

### 2.5 权重和偏置

**曾经的误解：** 不清楚 `weights`、`bias` 在预测中的意义。

**正确理解：** 权重决定每个特征影响结果的方向和强度；偏置是输入为零时的基础输出。

**最小示例：**

```python
weights = np.array([0.5, -0.25])
bias = 1.0
predictions = features @ weights + bias
```

**一句话记忆：** 权重控制斜率与影响，偏置负责整体平移。

---

## 3. PyTorch Tensor

### 3.1 Tensor 是什么

**曾经的误解：** 不知道 Tensor 与普通数字、列表、NumPy 数组的关系。

**正确理解：** Tensor 是可参与神经网络计算的多维数字容器，支持 GPU 计算和 Autograd 自动求导。

**最小示例：**

```python
scalar = torch.tensor(2.0)                   # 零维
vector = torch.tensor([1.0, 2.0])            # 一维
matrix = torch.tensor([[1.0, 2.0], [3.0, 4.0]])  # 二维
```

**一句话记忆：** Tensor 是神经网络中保存数据、参数和中间结果的基本容器。

### 3.2 `shape` 与 `dtype`

**曾经的误解：** 认为 `shape` 是函数，不清楚 `dtype` 中的 `d`。

**正确理解：** `shape` 是形状属性；`dtype` 是 data type 的缩写，表示元素的数据类型。

**最小示例：**

```python
print(features.shape)  # torch.Size([3, 2])
print(features.dtype)  # torch.float32
```

**一句话记忆：** `shape` 说明怎么排列，`dtype` 说明用什么类型保存。

### 3.3 一维向量与二维矩阵

**曾经的误解：** 将形状 `(2,)` 的向量理解成 `(1, 2)` 矩阵。

**正确理解：** `[a, b]` 是一维向量；`[[a, b]]` 才是一行两列的二维矩阵。

**最小示例：**

```python
vector = torch.tensor([0.5, -0.25])       # shape: (2,)
row = torch.tensor([[0.5, -0.25]])        # shape: (1, 2)
column = torch.tensor([[0.5], [-0.25]])   # shape: (2, 1)
```

**一句话记忆：** 中括号嵌套层数决定 Tensor 的维度。

### 3.4 `@` 与 `*`

**曾经的误解：** 不确定 `(3, 2)` 矩阵如何与 `(2,)` 向量相乘。

**正确理解：** `@` 是矩阵乘法；PyTorch 会把一维向量按矩阵—向量规则处理。`*` 是对应元素相乘，不会按矩阵规则求和。

**最小示例：**

```python
predictions = features @ weights  # (3, 2) @ (2,) -> (3,)
elementwise = features * weights  # 广播后得到 (3, 2)
```

**一句话记忆：** `*` 是逐元素乘，`@` 是线性代数中的矩阵乘法。

### 3.5 `reshape()`、`-1` 与转置

**曾经的误解：** 认为 `reshape(-1, 1)` 中的 `-1` 是负数行数，并将转置与重塑混为一谈。

**正确理解：** `-1` 表示让 PyTorch 自动推断这一维；`reshape()` 按原数据顺序重新分组，转置则交换行列。

**最小示例：**

```python
reshaped = features.reshape(2, 3)
transposed = features.t()
```

原始数据：

```text
[[1, 2],
 [3, 4],
 [5, 6]]
```

重塑：

```text
[[1, 2, 3],
 [4, 5, 6]]
```

转置：

```text
[[1, 3, 5],
 [2, 4, 6]]
```

**一句话记忆：** `reshape` 改分组方式，转置交换行列。

---

## 4. Autograd

### 4.1 `requires_grad=True`

**曾经的误解：** 不清楚为什么创建 Tensor 时要添加这个参数。

**正确理解：** 它告诉 PyTorch 记录与这个 Tensor 有关的运算，以便后续计算 Loss 对它的梯度。

**最小示例：**

```python
x = torch.tensor(2.0, requires_grad=True)
y = x**3
y.backward()
print(x.grad)  # tensor(12.)
```

**一句话记忆：** 需要学习或求导的浮点 Tensor 才设置 `requires_grad=True`。

### 4.2 `backward()` 与 `.grad`

**曾经的误解：** 认为 `backward()` 直接返回梯度，或者 `.grad` 是目标参数。

**正确理解：** `backward()` 从标量结果沿计算图反向求导，并把梯度累加到叶子 Tensor 的 `.grad` 属性中。

**最小示例：**

```python
x = torch.tensor(2.0, requires_grad=True)
y = x**2 + 3 * x + 1
y.backward()
print(x.grad)  # 2x + 3 = 7
```

**一句话记忆：** `backward()` 负责算，`.grad` 负责存。

### 4.3 梯度为什么会累加

**曾经的误解：** 认为两次 `backward()` 会保存两个独立梯度。

**正确理解：** `.grad` 不是历史列表；连续反向传播时，新梯度会加到旧梯度上。

**最小示例：**

```python
x = torch.tensor(2.0, requires_grad=True)
y = x**2
z = 3 * x

y.backward()  # x.grad = 4
z.backward()  # x.grad = 4 + 3 = 7

x.grad.zero_()  # 清零
```

**一句话记忆：** PyTorch 默认累加梯度，独立计算或开始新一轮训练前要清零。

### 4.4 为什么 `loss.requires_grad` 会自动变成 `True`

**曾经的误解：** 认为只有创建 Tensor 时手动写了 `requires_grad=True`，这个 Tensor 才能参与求导。

**正确理解：** 如果一个计算结果依赖需要梯度的 Tensor，并且中间操作可求导，那么结果会自动带有求导信息。`w、b` 是叶子 Tensor，`loss` 是计算产生的非叶子 Tensor。

**最小示例：**

```python
w = torch.tensor(0.0, requires_grad=True)
loss = (w - 3) ** 2

print(loss.requires_grad)  # True
print(loss.is_leaf)        # False
print(loss.grad_fn)        # PowBackward0 等求导函数
```

**一句话记忆：** 只要计算链上有需要梯度的参数，后续可求导结果就会自动连接到计算图。

### 4.5 为什么更新参数要使用 `torch.no_grad()`

**曾经的误解：** 不清楚参数更新为什么不能像普通公式一样直接写。

**正确理解：** `with` 是 Python 通用的上下文管理语法，具体环境由它后面的对象决定。前向计算需要建立计算图，但根据梯度修改参数只是训练操作，不需要再次被 Autograd 记录；因此用 `with torch.no_grad():` 在缩进代码块中暂时关闭梯度追踪，离开代码块后自动恢复。

**最小示例：**

```python
with torch.no_grad():
    w -= learning_rate * w.grad
    b -= learning_rate * b.grad
```

参数更新后还要清空旧梯度：

```python
w.grad.zero_()
b.grad.zero_()
```

**一句话记忆：** `with` 负责进入和退出环境，`torch.no_grad()` 决定这个环境不记录梯度。

### 4.6 Autograd 计算图记录了什么

**曾经的误解：** 认为前向计算时 PyTorch 已经把每一步的具体梯度存好。

**正确理解：** 前向计算主要记录 Tensor 之间的依赖关系、执行过的运算以及相应的反向求导方法；具体梯度要等到对最终标量调用 `backward()` 时才沿图反向计算。在线性回归中，`w、b` 是需要梯度的参数，`x、y` 参与计算但默认不需要自己的梯度，`predictions、errors、loss` 是中间结果。

**最小示例：**

```python
w = torch.tensor(2.0, requires_grad=True)
result = w * 3

print(result.requires_grad)  # True
print(w.grad)                # None

result.backward()
print(w.grad)                # tensor(3.)
```

**一句话记忆：** 前向传播建图并保存求导路线，`backward()` 沿路线计算具体梯度。

---

## 5. 线性回归

### 5.1 为什么用已知公式生成数据

**曾经的误解：** 既然已经知道 `y=3x+2`，不理解为什么还要让模型重新学习。

**正确理解：** 人知道生成公式，但模型训练时只看到 `(x, y)` 数据对。已知答案相当于实验的标准答案，用于验证训练流程是否正确。

**最小示例：**

```python
x = torch.linspace(-2, 2, steps=100).reshape(-1, 1)
noise = torch.randn_like(x) * 0.2
y = 3 * x + 2 + noise
```

**一句话记忆：** 简单已知问题用于验证训练方法，真实任务中的参数通常未知。

### 5.2 `reshape(-1, 1)` 的意义

**曾经的误解：** 不理解 `-1`，以为它表示负数维度。

**正确理解：** `-1` 让 PyTorch 根据元素总数自动计算该维；`1` 表示每条数据有一个特征。

**最小示例：**

```python
x = torch.linspace(-2, 2, steps=100).reshape(-1, 1)
print(x.shape)  # torch.Size([100, 1])
```

**一句话记忆：** `(100, 1)` 表示100条样本、每条1个特征。

### 5.3 `noise` 的意义

**曾经的误解：** 不理解为什么不直接使用精确直线数据。

**正确理解：** 噪声模拟测量误差和现实中未纳入模型的因素，让数据在真实直线附近波动。`torch.manual_seed(42)` 固定随机数生成器的起点，使相同代码重复运行时得到相同的随机数序列。

**最小示例：**

```python
torch.manual_seed(42)
noise = torch.randn_like(x) * 0.2
y = 3 * x + 2 + noise
```

**一句话记忆：** 噪声让练习数据更接近现实；相同随机种子会复现同一组随机数序列，但同一次运行中的连续调用仍会得到不同数字。

### 5.4 `w` 和 `b` 为什么是可学习参数

**曾经的误解：** 认为 TODO 2 只是定义普通变量方便后续使用。

**正确理解：** `w`、`b` 不仅是变量，还是需要 Autograd 计算梯度并通过训练更新的参数。

**最小示例：**

```python
w = torch.tensor(0.0, requires_grad=True)
b = torch.tensor(0.0, requires_grad=True)
predictions = w * x + b
```

**一句话记忆：** `w`、`b` 是模型当前答案，训练会不断修改它们。

### 5.5 前向传播是什么

**曾经的误解：** 不清楚“前向传播”是否是一种额外的 PyTorch 函数。

**正确理解：** 前向传播不是某个固定函数名，而是输入数据按照当前参数依次经过计算，最终得到预测值和 Loss 的过程。

**最小示例：**

```python
predictions = w * x + b
loss = ((predictions - y) ** 2).mean()
```

**一句话记忆：** 从输入 `x` 出发，沿公式计算到预测值和 Loss，就是前向传播。

### 5.6 Error、Loss 与 MSE

**曾经的误解：** 认为 Loss 就是预测值减真实值。

**正确理解：** `prediction-y` 是单项误差；Loss 将一批误差按规则汇总。MSE 是平方误差的平均值，可避免正负误差抵消。

**最小示例：**

```python
error = predictions - y
loss = (error**2).mean()
```

**一句话记忆：** Error 是每条数据错多少，Loss 是模型整体错得多严重。

### 5.7 参数与梯度的区别

**曾经的误解：** 认为真实权重为 `3`，所以 `w.grad` 应该是 `3`；认为偏置是常数，所以 `b.grad` 应该是 `0`。

**正确理解：** `w`、`b` 是当前参数；`w.grad`、`b.grad` 是 Loss 对当前参数的导数。梯度给出局部调整方向，不是最终正确参数。

**最小示例：**

```python
loss.backward()
print(w.grad)
print(b.grad)
```

在本练习初始 `w=0、b=0` 时，梯度大约为：

```text
w.grad ≈ -8.1536
b.grad ≈ -4.0239
```

**一句话记忆：** 参数是当前答案，梯度是调整答案的信号。

### 5.8 梯度下降公式是否固定

**曾经的误解：** 不确定 `参数 -= 学习率 × 梯度` 是临时写法还是通用规则。

**正确理解：** 这是最基础的梯度下降更新规则。梯度指向 Loss 上升最快方向，所以减去梯度以降低 Loss；不同优化器会进一步加工梯度。

**最小示例：**

```python
learning_rate = 0.01

with torch.no_grad():
    w -= learning_rate * w.grad
    b -= learning_rate * b.grad
```

**一句话记忆：** 梯度决定方向，学习率决定步长，优化器决定具体走法。

### 5.9 Epoch 与训练循环

**曾经的误解：** 认为完成一次前向传播和参数更新，模型就能直接得到正确参数。

**正确理解：** 一次完整的“预测、计算 Loss、反向传播、更新参数、清空梯度”称为一个训练轮次（epoch）。模型通常需要重复许多轮，参数才会逐渐接近较优值。

**最小示例：**

```python
for epoch in range(1000):
    predictions = w * x + b
    loss = ((predictions - y) ** 2).mean()
    loss.backward()

    with torch.no_grad():
        w -= learning_rate * w.grad
        b -= learning_rate * b.grad

    w.grad.zero_()
    b.grad.zero_()
```

**一句话记忆：** 一个 epoch 完成一次训练闭环，多次 epoch 让参数逐步逼近目标。

### 5.10 手工线性回归的完整训练流程

**曾经的误解：** 认为训练数据就是一批随机数，并且可以直接根据真实值和预测值计算参数梯度。

**正确理解：** 本练习先准备输入 `x` 和标签 `y`，其中 `x` 是均匀取点而不是随机数，只有噪声是随机的。模型先用当前参数得到预测值，再通过 Loss 汇总误差，最后对 Loss 反向传播得到参数梯度。

**最小流程：**

```text
准备训练数据 (x, y)
→ 初始化参数 w、b
→ predictions = w*x+b
→ loss = mean((predictions-y)²)
→ loss.backward()
→ 根据 w.grad、b.grad 更新参数
→ 清空梯度
→ 重复训练
```

**一句话记忆：** 数据提供目标，前向传播产生预测，Loss 衡量差距，梯度指导参数更新。

---

## 6. 与大模型的联系

### 6.1 Token 是什么，它等于 `x` 吗

**曾经的误解：** 认为 Token 就是线性回归中的 `x`。

**正确理解：** Token 是文本经 Tokenizer 切分得到的基本单位；它先转换成 Token ID，再转换成向量后参与模型计算。它与 `x` 都属于输入，但类型和结构不同。

**最小流程：**

```text
文本
→ Tokenizer
→ Token
→ Token ID
→ Embedding 向量
→ Transformer
```

**一句话记忆：** `x` 是当前练习的数值特征，Token 是大语言模型处理文本的基本单位。

---

## 7. 当前自测

- [ ] 能解释属性和方法的区别。
- [ ] 能解释 `axis=0` 为什么得到每列结果。
- [ ] 能区分一维向量 `(2,)` 和二维矩阵 `(1, 2)`。
- [ ] 能解释 `@` 与 `*` 的区别。
- [ ] 能解释 `reshape()` 与转置的区别。
- [ ] 能解释 `backward()` 和 `.grad` 的职责。
- [ ] 能解释梯度为什么要在每轮训练前清零。
- [ ] 能区分 Error、Loss、参数和梯度。
- [ ] 能解释学习率的作用。
- [ ] 能说出 Token 与数值输入 `x` 的异同。
