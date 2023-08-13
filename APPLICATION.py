from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, RiseInTransition
from diabetes import DP
from heart import HP
from liver import LP

Builder.load_file('APP.kv')


class MainScreen(Screen):
    pass

class DiabetesPredictor(Screen):
    data1 = []
    pregnancies1, glucose1, blood_pressure1, skin_thickness1, insulin1, age1 = 0, 0, 0, 0, 0, 0
    bmi1, diabetes_pedigree_function1 = 0.0, 0.0

    def process1(self, key):
        if key == 'f11':
            self.pregnancies1 = self.ids.f11.text
            print(self.pregnancies1)
        elif key == 'f12':
            self.glucose1 = self.ids.f12.text
        elif key == 'f13':
            self.blood_pressure1 = self.ids.f13.text
        elif key == 'f14':
            self.skin_thickness1 = self.ids.f14.text
        elif key == 'f15':
            self.insulin1 = self.ids.f15.text
        elif key == 'f16':
            self.bmi1 = self.ids.f16.text
        elif key == 'f17':
            self.diabetes_pedigree_function1 = self.ids.f17.text
        elif key == 'f18':
            self.age1 = self.ids.f18.text

    def calculate1(self):
        self.data1 = [int(self.pregnancies1), int(self.glucose1), int(self.blood_pressure1), int(self.skin_thickness1),
                      int(self.insulin1), float(self.bmi1), float(self.diabetes_pedigree_function1), int(self.age1)]
        results = DP(self.data1).model()

        if (results == 0):
            self.ids.result1.color = (45 / 255, 227 / 255, 189 / 255, 1)
            self.ids.result1.text = 'Not Diabetic !'
        else:
            self.ids.result1.color = (245 / 255, 0 / 255, 19 / 255, 1)
            self.ids.result1.text = 'Diabetic !!'


class HeartDiseasePredictor(Screen):
    data2 = []
    age2, sex2, cp2, trestbps2, chol2, fbs2, restecg2, thalach2, exang2, slope2, ca2, thal2 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    oldpeak2 = 0.0

    def process2(self, key):
        if key == 'f21':
            self.age2 = self.ids.f21.text
        elif key == 'f22':
            self.sex2 = self.ids.f22.text
        elif key == 'f23':
            self.cp2 = self.ids.f23.text
        elif key == 'f24':
            self.trestbps2 = self.ids.f24.text
        elif key == 'f25':
            self.chol2 = self.ids.f25.text
        elif key == 'f26':
            self.fbs2 = self.ids.f26.text
        elif key == 'f27':
            self.restecg2 = self.ids.f27.text
        elif key == 'f28':
            self.thalach2 = self.ids.f28.text
        elif key == 'f29':
            self.exang2 = self.ids.f29.text
        elif key == 'f210':
            self.oldpeak2 = self.ids.f210.text
        elif key == 'f211':
            self.slope2 = self.ids.f211.text
        elif key == 'f212':
            self.ca2 = self.ids.f212.text
        elif key == 'f213':
            self.thal2 = self.ids.f213.text

    def calculate2(self):
        self.data2 = [int(self.age2), int(self.sex2), int(self.cp2), int(self.trestbps2), int(self.chol2),
                      int(self.fbs2), int(self.restecg2), int(self.thalach2), int(self.exang2), float(self.oldpeak2),
                      int(self.slope2), int(self.ca2), int(self.thal2)]
        results = HP(self.data2).model()

        if (results == 0):
            self.ids.result2.color = (45 / 255, 227 / 255, 189 / 255, 1)
            self.ids.result2.text = 'No Heart Disease !'
        else:
            self.ids.result2.color = (245 / 255, 0 / 255, 19 / 255, 1)
            self.ids.result2.text = 'Heart Disease !!'


class LiverDiseasePredictor(Screen):
    data3 = []
    age3, sex3, alkph3, alamtr3, asamtr3 = 0, 0, 0, 0, 0
    tbilrb3, dbilrb3, tpr3, alb3, albglbr3 = 0.0, 0.0, 0.0, 0.0, 0.0

    def process3(self, key):
        if key == 'f31':
            self.age3 = self.ids.f31.text
        elif key == 'f32':
            self.sex3 = self.ids.f32.text
        elif key == 'f33':
            self.tbilrb3 = self.ids.f33.text
        elif key == 'f34':
            self.dbilrb3 = self.ids.f34.text
        elif key == 'f35':
            self.alkph3 = self.ids.f35.text
        elif key == 'f36':
            self.alamtr3 = self.ids.f36.text
        elif key == 'f37':
            self.asamtr3 = self.ids.f37.text
        elif key == 'f38':
            self.tpr3 = self.ids.f38.text
        elif key == 'f39':
            self.alb3 = self.ids.f39.text
        elif key == 'f310':
            self.albglbr3 = self.ids.f310.text

    def calculate3(self):
        self.data3 = [int(self.age3), int(self.sex3), float(self.tbilrb3), float(self.dbilrb3), int(self.alkph3),
                     int(self.alamtr3), int(self.asamtr3), float(self.tpr3), float(self.alb3), float(self.albglbr3)]
        results = LP(self.data3).model()

        if (results == 0):
            self.ids.result3.color = (45 / 255, 227 / 255, 189 / 255, 1)
            self.ids.result3.text = 'No Liver Disease !'
        else:
            self.ids.result3.color = (245 / 255, 0 / 255, 19 / 255, 1)
            self.ids.result3.text = 'Liver Disease !!'



screen_manager = ScreenManager(transition = RiseInTransition())
screen_manager.add_widget(MainScreen(name ="MainScreen"))
screen_manager.add_widget(DiabetesPredictor(name ="DiabetesPredictor"))
screen_manager.add_widget(HeartDiseasePredictor(name ="HeartDiseasePredictor"))
screen_manager.add_widget(LiverDiseasePredictor(name ="LiverDiseasePredictor"))

class DiseasePredictorApp(App):
    def build(self):
        return screen_manager



if __name__ == "__main__":
    DiseasePredictorApp().run()