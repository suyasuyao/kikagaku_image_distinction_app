import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
from torchvision import transforms
from torchvision import datasets
import pytorch_lightning as pl
import torchmetrics
from torchmetrics.functional import accuracy
import torchsummary
from torchsummary import summary
from pytorch_lightning.loggers import CSVLogger

from PIL import Image

from torchvision.models import resnet18


class Net(pl.LightningModule):

    def __init__(self):
        super().__init__()

# resnet18 を使って推論　推論結果が1000として出力
        self.feature = resnet18(pretrained=True)
        # １０００を１０に結合
        self.fc = nn.Linear(1000, 4)


    def forward(self, x):
        h = self.feature(x)
        h = self.fc(h)
        return h


    def training_step(self, batch, batch_idx):
        x, t = batch
        y = self(x)
        loss = F.cross_entropy(y, t)
        self.log('train_loss', loss, on_step=False, on_epoch=True)
        self.log('train_acc', accuracy(y.softmax(dim=-1), t), on_step=False, on_epoch=True)
        return loss


    def validation_step(self, batch, batch_idx):
        x, t = batch
        y = self(x)
        loss = F.cross_entropy(y, t)
        self.log('val_loss', loss, on_step=False, on_epoch=True)
        self.log('val_acc', accuracy(y.softmax(dim=-1), t), on_step=False, on_epoch=True)
        return loss


    def test_step(self, batch, batch_idx):
        x, t = batch
        y = self(x)
        loss = F.cross_entropy(y, t)
        self.log('test_loss', loss, on_step=False, on_epoch=True)
        self.log('test_acc', accuracy(y.softmax(dim=-1), t), on_step=False, on_epoch=True)
        return loss


    def configure_optimizers(self):
        optimizer = torch.optim.SGD(self.parameters(), lr=0.01)
        return optimizer




#pd.Series(y, name='class').to_csv('submission.csv', index=None)



            # data = ModelFile.objects.order_by('id').reverse().values_list('image')

            # x = np.array([data[0]])
            # y = loaded_model.predict(x)
            # y_proba = loaded_model.predict_proba(x)
            # y_proba = y_proba * 100 # 追加
            # y, y_proba = y[0], y_proba[0] # 追加