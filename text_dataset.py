import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim

class TextDatset(torch.utils.data.Dataset):
    """Some Information about TextDatset"""
    def __init__(self, tokenizer, *dir_path_list):
        super(TextDatset, self).__init__()

    def __getitem__(self, index):
        return 

    def __len__(self):
        return 