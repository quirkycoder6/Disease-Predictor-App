import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import warnings

warnings.filterwarnings('ignore')

class DP():
    def __init__(self, input_data):
        self.dataset = pd.read_csv('diabetes.csv')
        self.input_data = input_data
        self.X = self.dataset.drop(columns='Outcome', axis=1)
        self.Y = self.dataset['Outcome']
        self.scaler = StandardScaler()
        self.classifier = svm.SVC(kernel='linear')

    def details(self, train_acc, test_acc):
        print('(rows, columns) = ', self.dataset.shape)
        print('\n\n\t\t\t\nDatapoints\n', self.dataset.head(n=15))
        print('\n\n\t\t\nStats\n', self.dataset.describe())
        print('\n\n\t\t\t\nOutcome counts\n', self.dataset['Outcome'].value_counts())

    def model(self):
        self.scaler.fit(self.X)
        standardized_data = self.scaler.transform(self.X)
        self.X = standardized_data
        self.Y = self.dataset['Outcome']
        X_train, X_test, Y_train, Y_test = train_test_split(self.X, self.Y, test_size=.2, stratify=self.Y, random_state=2)
        self.classifier.fit(X_train, Y_train)
        X_train_prediction = self.classifier.predict(X_train)
        X_train_acc = accuracy_score(X_train_prediction, Y_train)
        X_test_prediction = self.classifier.predict(X_test)
        X_test_acc = accuracy_score(X_test_prediction, Y_test)
        print("Accuracy score on training data : ", X_train_acc)
        print("Accuracy score on the testing data : ", X_test_acc)

        input_data_as_np_array = np.asarray(self.input_data)
        input_data_reshaped = input_data_as_np_array.reshape(1, -1)
        standard_data = self.scaler.transform(input_data_reshaped)
        # predicting outcome
        prediction = self.classifier.predict(standard_data)

        return prediction[0]

