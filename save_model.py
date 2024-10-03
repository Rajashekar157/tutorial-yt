import torch
import torch.nn as nn
import torch.optim as optim

class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(10, 2)  

    def forward(self, x):
        return self.fc(x)


model = SimpleModel()


torch.save(model.state_dict(), 'my_model.pt')
print("Model saved as my_model.pt")
