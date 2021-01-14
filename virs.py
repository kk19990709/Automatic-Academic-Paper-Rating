# %%
import torch
checkpoint = './dataset_mini/checkpoint.pkl'
data = torch.load(checkpoint)
data.describe()
