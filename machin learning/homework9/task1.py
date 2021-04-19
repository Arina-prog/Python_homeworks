import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import tensorflow.keras as keras

mnist = keras.datasets.mnist     #tvyalnern enq qashum

(X_train, y_train), (X_test, y_test) = mnist.load_data()
plt.imshow(X_train[0], cmap=plt.cm.binary)
plt.show()
# print(X_train[0])
X_train = keras.utils.normalize(X_train, axis=1) #tvyalneri normalizacum 0ic 1,kam -1ic 1,amen piqsel funkcia e 0-ic 255
X_test = keras.utils.normalize(X_test, axis=1)
# print(X_train[0])
model = keras.models.Sequential()
model.add(keras.layers.Flatten())#28x28 darcnuma 1x784
model.add(keras.layers.Dense(128, activation=tf.nn.relu))
model.add(keras.layers.Dense(128, activation=tf.nn.relu))
model.add(keras.layers.Dense(10, activation=tf.nn.softmax))
model.compile(optimizer="adam", loss='sparse_categorical_crossentropy', metrics=["accuracy"])
model.fit(X_train, y_train, epochs=3)
val_loss, val_acc = model.evaluate(X_test, y_test)
print(val_loss)
print(val_acc)

model.save("epic_num_reader.model")
new_model = keras.models.load_model('epic_num_reader.model')
predictions = new_model.predict(X_test)
print(predictions)
print(np.argmax(predictions[0]))
plt.imshow(X_test[0], cmap=plt.cm.binary)
plt.show()