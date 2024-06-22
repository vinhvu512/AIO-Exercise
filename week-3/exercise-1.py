import torch
import torch.nn as nn


class Softmax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        total = 0
        for i in range(len(x)):
            total += torch.exp(x[i])

        return torch.exp(x) / total


class SoftmaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x = x - torch.max(x)
        total = 0
        for i in range(len(x)):
            total += torch.exp(x[i]) - torch.max(x)

        return torch.exp(x) / total

