from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np

dataset = np.loadtxt("./data/ThoraricSurgery3.csv", delimiter=",")
X = dataset[:,0:16]
y = dataset[:,16]

model = Sequential()
model.add(Dense(30, input_dim=16, activation="relu"))
model.add(Dense(1, activation="sigmoid"))

model.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])
history = model.fit(X, y, epochs=10000, batch_size=512)