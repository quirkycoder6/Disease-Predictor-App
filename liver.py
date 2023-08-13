### Import statements
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report, recall_score
import warnings

warnings.filterwarnings('ignore')

def convert_gender(x):
    if x == 'Male':
        return 1
    return 0
def change_outcome(x):
    if x == 2:
        return 0
    return 1

class LP():
    def __init__(self, input_data):
        self.input_data = input_data
        self.dataset = pd.read_csv('indian_liver_patient.csv')
        # Preprocessing & data cleaning
        self.dataset['Outcome'] = self.dataset['Outcome'].map(change_outcome)
        self.dataset['Gender'] = self.dataset['Gender'].map(convert_gender)
        self.dataset = self.dataset.drop_duplicates()
        self.dataset = self.dataset[self.dataset.Aspartate_Aminotransferase <= 2500]
        self.dataset = self.dataset.dropna(how='any')
        print(self.dataset.shape)
        # data splitting
        self.X = self.dataset.drop(columns='Outcome', axis=1)
        self.Y = self.dataset['Outcome']
        self.rand_clf = RandomForestClassifier(criterion='entropy', max_depth=16, max_features='sqrt', min_samples_leaf=4, min_samples_split=2, n_estimators=130)

    def details(self, train_acc, test_acc):
        print('(rows, columns) = ', self.dataset.shape)
        print('\n\n\t\t\t\nDatapoints\n', self.dataset.head(n=15))
        print('\n\n\t\t\nStats\n', self.dataset.describe())
        print('\n\n\t\t\t\nTarget counts\n', self.dataset['Outcome'].value_counts())

    def model(self):
        X_train, X_test, Y_train, Y_test = train_test_split(self.X, self.Y, test_size=0.3, random_state=0)
        self.rand_clf.fit(X_train, Y_train)
        X_train_prediction = self.rand_clf.predict(X_train)
        X_train_acc = accuracy_score(Y_train, X_train_prediction)
        X_test_prediction = self.rand_clf.predict(X_test)
        X_test_acc = accuracy_score(Y_test, X_test_prediction)
        print(f"Accuracy score on training data : {X_train_acc*100} %")
        print(f"Accuracy score on the testing data : {X_test_acc*100} %")

        input_data_as_np_array = np.asarray(self.input_data)
        input_data_reshaped = input_data_as_np_array.reshape(1, -1)
        # predicting outcome
        prediction = self.rand_clf.predict(input_data_reshaped)

        return prediction[0]

