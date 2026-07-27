from torch import nn
import torch.nn.functional as F


class NonMoEModel(nn.Module):

    def __init__(self):
        super().__init__()
        self.layer_1 = nn.Linear(2, 4, bias=True)
        self.layer_2 = nn.Linear(4, 2, bias=True)
        self.layer_3 = nn.Linear(2, 1, bias=True)


    def forward(self, xs):
        xs = F.relu(self.layer_1(xs))
        xs = F.relu(self.layer_2(xs))
        xs = F.relu(self.layer_3(xs))
        return xs

