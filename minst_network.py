from torch import nn


class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        self.stack = nn.Sequential(
            nn.Conv2d(
                28,
            ),
            nn.MaxPool2d(2),
            nn.Conv2d(28),
            nn.MaxPool2d(2),
            nn.Conv2d(28),
        )
        # Define layers here

    def forward(self, x):
        # Define forward pass here
        x = self.stack(x)
        return x
