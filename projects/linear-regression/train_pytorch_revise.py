import torch
from torch import nn

def main() -> None:
    torch.manual_seed(42)

    inputs = torch.linspace(-2, 2, steps=100).reshape(-1, 1)
    targets = 3 * inputs + 2

    model = nn.Linear(1, 1)
    loss_function = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=0.01)

    for epoch in range(500):
        # 1. 清空旧梯度
        optimizer.zero_grad()
        # 2. 用模型计算预测值
        predictions = model(inputs)  
        # 3. 计算预测值与 targets 的 Loss
        loss = loss_function(predictions,targets)
        # 4. 计算梯度
        loss.backward()
        # 5. 更新参数
        optimizer.step()
    print("weight:", model.weight.item())
    print("bias:", model.bias.item())

if __name__ == "__main__":
    main()
