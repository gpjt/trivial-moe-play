import random
import time

import numpy as np
import pandas as pd
import torch
from torch.utils.data import DataLoader, Dataset

from non_moe_model import NonMoEModel


class MyDataset(Dataset):

    def __init__(self, filename):
        self.raw_data = torch.tensor(
            pd.read_csv(filename, header=None).values,
            dtype=torch.float
        )


    def __len__(self):
        return len(self.raw_data)


    def __getitem__(self, ix):
        row = self.raw_data[ix]
        return (
            row[:2],
            row[2],
        )


BATCH_SIZE = 64
EPOCHS = 3000
LR = 1e-2
WEIGHT_DECAY = 0


def calculate_loss(results, targets):
    return ((results - targets) ** 2).mean()


def train(model, dataloader):
    optimizer = torch.optim.AdamW(
        model.parameters(),
        lr=LR, weight_decay=WEIGHT_DECAY
    )

    start = time.time()
    for epoch in range(EPOCHS):
        losses = []
        for xs, ys in dataloader:
            optimizer.zero_grad()

            results = model(xs).squeeze()

            loss = calculate_loss(results, ys)
            loss.backward()
            losses.append(loss.item())

            optimizer.step()
        avg_loss = sum(losses) / len(losses)
        print(f"Epoch {epoch + 1}: loss is {avg_loss:.2f}")
    end = time.time()

    print(f"Trained in {end - start:.1f}s, final loss {avg_loss:.2f}")
    print(f"Last results: {results}")
    print(f"Last targets: {ys}")


def main():
    seed = 42
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)

    dataset = MyDataset("data.csv")
    dataloader = DataLoader(dataset, batch_size=BATCH_SIZE, shuffle=True)

    model = NonMoEModel()

    train(model, dataloader)


if __name__ == "__main__":
    main()
