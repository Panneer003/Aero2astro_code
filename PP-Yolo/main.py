import tensorflow as tf
from tensorflow import keras
from core.fpn import fpn
from core.resnet_50 import resnet_50

from tensorflow.python.framework.ops import disable_eager_execution

disable_eager_execution()

resnet = tf.keras.applications.ResNet50(include_top = False,weights='imagenet',input_shape=(224,224,3))
c3 , c4 , c5 = resnet_50(resnet)


output = fpn(c3 , c4,c5)
model = tf.keras.Model(inputs = resnet.input,outputs=output )



print(model.summary())