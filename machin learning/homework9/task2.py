import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import tensorflow.keras as keras

df_train = keras.datasets.mnist     #tvyalnern enq qashum

(X_train, y_train), (X_test, y_test) = df_train.load_data()


