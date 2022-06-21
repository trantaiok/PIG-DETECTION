from matplotlib import image
import matplotlib.pyplot as plt
from matplotlib.image import imread
from tensorflow import keras
from os import listdir
from numpy import asarray, save
from detecto import core


#mention you dataset path
dataset = core.Dataset('D:/NHAN_DIEN_HEO/NHANDIENHEO/image/')
#mention you object label here
model = core.Model(['heo'])


#train data
model.fit(dataset, epochs=15, verbose=1)

#save data
model.save ('heo_model_weights.pth')

