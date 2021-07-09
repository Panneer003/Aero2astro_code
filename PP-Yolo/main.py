import tensorflow as tf
from core.fpn import fpn
from core.resnet_50 import resnet_50
from core.head import head

from tensorflow.python.framework.ops import disable_eager_execution
disable_eager_execution()

def model():

    resnet = tf.keras.applications.ResNet50(include_top = False,weights='imagenet',input_shape=(224,224,3))
    c3 , c4 , c5 = resnet_50(resnet)


    output_1 = fpn(c3 , c4,c5)
    output_2 = head(output_1)

    model = tf.keras.Model(inputs = resnet.input,outputs=output_2 )



    #print(model.summary())
    return model