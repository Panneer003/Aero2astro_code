import tensorflow as tf
from tensorflow.python.keras.engine import input_layer

def resnet_50(resnet,training=False):
 
    if not training:  # For lyers freeze
        print('Resnet layers are freezed...')
        for layer in resnet.layers:
            layer.trainable = False
    else :              # For layers training
        print('Resnet layers are trainable...')
        for layer in resnet.layers :
            layer.trainable=True
    
    #print(resnet.summary())

    c3 = resnet.get_layer('conv3_block4_out').output
    c4 = resnet.get_layer('conv4_block6_out').output
    c5 = resnet.get_layer('conv5_block3_out').output
    print('c1 , c2 , c3 layers loaded sucessfully..')



    return c3 , c4 , c5
 