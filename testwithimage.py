from pyexpat import model
import collections
import numpy as np
from detecto import core, utils, visualize
import numpy as np
from detecto.visualize import show_labeled_image


model = core.Model.load('heo_model_weights.pth', ['heo'])

image = utils.read_image('D:/NHAN_DIEN_HEO/NHANDIENHEO/download.jpg') 
labels, boxes, scores = model.predict(image)
filtr_ind=np.where(scores>0.798)
filtr_scr=scores[filtr_ind]
filtr_boxes=boxes[filtr_ind]
num_list = list(filtr_ind[0])
filtr_labels = []
for i in num_list:
  filtr_labels.append(labels[i] + "#" + str(i+1))
show_labeled_image(image, filtr_boxes, filtr_labels)
print(labels) 
print(boxes)
print(scores)

c = collections.Counter(filtr_labels)
print(c)
print(len(c))





