"""Scrip to check if torch is working"""
#pylint: disable=C0304

import torch
print(torch.backends.mps.is_available())  # Should print True
print(torch.backends.mps.is_built())      # Should print True