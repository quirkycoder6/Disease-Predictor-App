### Import statements
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, recall_score
import warnings

warnings.filterwarnings('ignore')

class HP():
    def __init__(self, input_data):
        self.input_data = input_data
        self.dataset = pd.read_csv('heart.csv')
        # data splitting
        self.X = self.dataset.drop(columns='target', axis=1)
        self.Y = self.dataset['target']
        self.knn = KNeighborsClassifier(n_neighbors=5)

    def details(self, train_acc, test_acc):
        print('(rows, columns) = ', self.dataset.shape)
        print('\n\n\t\t\t\nDatapoints\n', self.dataset.head(n=15))
        print('\n\n\t\t\nStats\n', self.dataset.describe())
        print('\n\n\t\t\t\nTarget counts\n', self.dataset['target'].value_counts())

    def model(self):
        X_train, X_test, Y_train, Y_test = train_test_split(self.X, self.Y, test_size=0.3, random_state=0)
        self.knn.fit(X_train, Y_train)
        X_train_prediction = self.knn.predict(X_train)
        X_train_acc = accuracy_score(Y_train, X_train_prediction)
        X_test_prediction = self.knn.predict(X_test)
        X_test_acc = accuracy_score(Y_test, X_test_prediction)
        print(f"Accuracy score on training data : {X_train_acc*100} %")
        print(f"Accuracy score on the testing data : {X_test_acc*100} %")

        input_data_as_np_array = np.asarray(self.input_data)
        input_data_reshaped = input_data_as_np_array.reshape(1, -1)
        # predicting outcome
        prediction = self.knn.predict(input_data_reshaped)

        return prediction[0]

