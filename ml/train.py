from torch import nn
import torch
from torch.utils.data import DataLoader, Dataset

import json
from copy import deepcopy

from fastai import *
from fastai.train import *
from fastai.basic_train import DataBunch, Learner
from fastai import metrics



INPUT_SIZE = 12


class KeyboardTrainDataset(Dataset):
	def __init__(self, dataset_location):
		for data in recorded_data:
			self.data 


class PredictiorFromResistanceModel(nn.Module):
	def __init__self():
		self.nn = nn.Sequential(nn.Linear(12, 36), nn.ReLU(), nn.Linear(36, 36))

	def forward(inpts):
		return self.nn(inpts)

model = PredictiorFromResistanceModel()

learner = Learner(data, model, metrics=[metrics.accuracy, metrics.Precision(), metrics.Recall()])