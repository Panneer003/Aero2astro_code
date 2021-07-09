from core.blocks import conv_head


def head(features):

    p5 = features[0]
    p4 = features[1]
    p3 = features[2]
    
    head_1 = conv_head(p5)
    print(head_1.shape)
    head_2 = conv_head(p4)
    print(head_2.shape)
    head_3 = conv_head(p3)
    print(head_3.shape)

    return [head_1,head_2, head_3]


