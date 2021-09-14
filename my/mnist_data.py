import os

from paddle.vision.datasets.mnist import MNIST

data_set_dir = "/home/dong/tmp/mnist"
mode = "test"

data = MNIST(mode=mode)
os.makedirs(data_set_dir, exist_ok=True)
with open(data_set_dir + "/" + mode + ".txt", mode="wt") as f:
    for i in range(len(data)):
        sample = data[i]
        img_dir = data_set_dir + "/" + str(sample[1][0])
        os.makedirs(img_dir, exist_ok=True)
        sample[0].save(img_dir + "/" + mode + str(i) + ".jpg")
        print(str(sample[1][0]) + "/" + mode + str(i) + ".jpg " + str(sample[1][0]), file=f)