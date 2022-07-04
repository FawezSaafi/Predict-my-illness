from tkinter import *
import numpy as np
import pandas as pd
import keras
# from sklearn.metrics import confusion_matrix, zero_one_loss
# from sklearn.metrics import classification_report
# from sklearn.metrics import f1_score

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from sklearn.ensemble import StackingClassifier
import keras



#List of the symptoms is listed here in list l1.

l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
'yellow_crust_ooze']

#List of Diseases is listed in list disease.

disease = ['Fungal infection', 'Allergy', 'GERD', 'Chronic cholestasis', 'Drug Reaction','Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',' Migraine','Cervical spondylosis','Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A','Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis','Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)','Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis','Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis','Impetigo']

l2=[]

for i in range(0,len(l1)):
    l2.append(0)

df=pd.read_csv("Prototype.csv")

#Replace the values in the imported file by pandas by the inbuilt function replace in pandas.

df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

#check the df
#print(df.head())

X= df[l1]

#print(X)

y = df[["prognosis"]]
np.ravel(y)

#print(y)

#Read a csv named Testing.csv

tr = pd.read_csv("Prototype-1.csv")

#Use replace method in pandas.

tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]

#print(y_test)

np.ravel(y_test)


def LogisticReg():
    scaler = preprocessing.StandardScaler().fit(X)
    X_scaled = scaler.transform(X)
    logreg = LogisticRegression(C=5, penalty="l2", solver='lbfgs', max_iter=100)
    logreg.fit(X_scaled, np.ravel(y))

    y_pred = logreg.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    # print(accuracy_score(y_test, y_pred, normalize=False))

    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

    for k in range(0, len(l1)):
        for z in psymptoms:
            if (z == l1[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = logreg.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(disease)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")


def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X, np.ravel(y))

    # calculating accuracy
    from sklearn.metrics import accuracy_score
    y_pred = clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))

    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

    for k in range(0, len(l1)):
        for z in psymptoms:
            if (z == l1[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(disease)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        t2.delete("1.0", END)
        t2.insert(END, disease[a])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")


def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb = gnb.fit(X, np.ravel(y))

    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred, normalize=False))


    # print(classification_report(y_test, y_pred))
    # print(f1_score(y_test, y_pred, average='micro'))

    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]
    for k in range(0, len(l1)):
        for z in psymptoms:
            if (z == l1[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(disease)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")



def knnClass():
    from sklearn.neighbors import KNeighborsClassifier
    knn = KNeighborsClassifier(n_neighbors=1)
    knn.fit(X, y)
    knn_predict = knn.predict(X_test)
    # cmG = confusion_matrix(y_test, knn_predict)
    # sns.heatmap(cmG, annot=True)
    # print(classification_report(y_test, knn_predict))
    # print(confusion_matrix(y_test, knn_predict))
    print(accuracy_score(y_test, knn_predict))

    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

    for k in range(0, len(l1)):
        for z in psymptoms:
            if (z == l1[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = knn.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(disease)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        t4.delete("1.0", END)
        t4.insert(END, disease[a])
    else:
        t4.delete("1.0", END)
        t4.insert(END, "Not Found")



def adaboost():
    from sklearn.ensemble import AdaBoostClassifier

    abc = AdaBoostClassifier(n_estimators=80, learning_rate=0.1)
    model = abc.fit(X, y)
    y_pred = model.predict(X_test)
    print(accuracy_score(y_test, y_pred))

    psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

    for k in range(0, len(l1)):
        for z in psymptoms:
            if (z == l1[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = abc.predict(inputtest)
    predicted = predict[0]

    h = 'no'
    for a in range(0, len(disease)):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        t5.delete("1.0", END)
        t5.insert(END, disease[a])
    else:
        t5.delete("1.0", END)
        t5.insert(END, "Not Found")
# Press the green button in the gutter to run the script.


if __name__ == '__main__':
    # GUI stuff..............................................................................

    root = Tk()
    # Adjust size
    root.geometry("500x300")
    bg = PhotoImage(file="Capture.png")
    mylabel = Label(root, image=bg)
    mylabel.place(x=0, y=0, relwidth=1, relheight=1)
    ws=root.config(bg='grey')
    # Add image file


    #root.configure(background=bg)
    print('I am here ')


    Symptom1 = StringVar()
    Symptom1.set("Select Here")

    Symptom2 = StringVar()
    Symptom2.set("Select Here")

    Symptom3 = StringVar()
    Symptom3.set("Select Here")

    Symptom4 = StringVar()
    Symptom4.set("Select Here")

    Symptom5 = StringVar()
    Symptom5.set("Select Here")

    Name = StringVar()


    w2 = Label(root, justify=LEFT, text="Bootcamp AI - Week 2 - Disease Predictor using Machine Learning", fg="white",bg="#87CEEB" )
    w2.config(font=("Times", 30, "bold italic"))
    w2.grid(row=1, column=0, columnspan=1, padx=100)
    # w2 = Label(root, justify=LEFT, text="A Project by Shrimad Mishra", fg="Pink", bg="Blue")
    # w2.config(font=("Times", 30, "bold italic"))
    # w2.grid(row=2, column=0, columnspan=2, padx=100)

    # NameLb = Label(root, text="Name of the Patient", fg="Red", bg="Sky Blue")
    # NameLb.config(font=("Times", 15, "bold italic"))
    # NameLb.grid(row=6, column=0, pady=15, sticky=W)

    S1Lb = Label(root, text="Symptom 1", fg="white",bg="#87CEEB")
    S1Lb.config(font=("Times", 20, "bold italic"))
    S1Lb.grid(row=7, column=0, pady=10, sticky=W)

    S2Lb = Label(root, text="Symptom 2", fg="white",bg="#87CEEB")
    S2Lb.config(font=("Times", 20, "bold italic"))
    S2Lb.grid(row=8, column=0, pady=10, sticky=W)

    S3Lb = Label(root, text="Symptom 3", fg="white",bg="#87CEEB")
    S3Lb.config(font=("Times", 20, "bold italic"))
    S3Lb.grid(row=9, column=0, pady=10, sticky=W)

    S4Lb = Label(root, text="Symptom 4", fg="white",bg="#87CEEB")
    S4Lb.config(font=("Times", 20, "bold italic"))
    S4Lb.grid(row=10, column=0, pady=10, sticky=W)

    S5Lb = Label(root, text="Symptom 5", fg="white",bg="#87CEEB")
    S5Lb.config(font=("Times", 20, "bold italic"))
    S5Lb.grid(row=11, column=0, pady=10, sticky=W)

    lrLb = Label(root, text="LogisticRegression", fg="white",bg="#87CEEB")
    lrLb.config(font=("Times", 25, "bold italic"))
    lrLb.grid(row=15, column=0, pady=10, sticky=W)

    destreeLb = Label(root, text="RandomForest", fg="white",bg="#87CEEB")
    destreeLb.config(font=("Times", 25, "bold italic"))
    destreeLb.grid(row=17, column=0, pady=10, sticky=W)

    ranfLb = Label(root, text="NaiveBayes", fg="white",bg="#87CEEB" )
    ranfLb.config(font=("Times", 25, "bold italic"))
    ranfLb.grid(row=19, column=0, pady=10, sticky=W)

    knLb = Label(root, text="KNN", fg="white",bg="#87CEEB")
    knLb.config(font=("Times", 25, "bold italic"))
    knLb.grid(row=21, column=0, pady=10, sticky=W)

    adaLb = Label(root, text="AdaBoost", fg="white",bg="#87CEEB")
    adaLb.config(font=("Times", 25, "bold italic"))
    adaLb.grid(row=23, column=0, pady=10, sticky=W)

    OPTIONS = sorted(l1)

    # NameEn = Entry(root, textvariable=Name)
    # NameEn.grid(row=6, column=1)

    S1 = OptionMenu(root, Symptom1, *OPTIONS)
    S1.grid(row=7, column=0)

    S2 = OptionMenu(root, Symptom2, *OPTIONS)
    S2.grid(row=8, column=0)

    S3 = OptionMenu(root, Symptom3, *OPTIONS)
    S3.grid(row=9, column=0)

    S4 = OptionMenu(root, Symptom4, *OPTIONS)
    S4.grid(row=10, column=0)

    S5 = OptionMenu(root, Symptom5, *OPTIONS)
    S5.grid(row=11, column=0)

    dst = Button(root, text="Prediction 1", command=LogisticReg,  fg="black")
    dst.config(font=("Times", 15, "bold italic"))
    dst.grid(row=15, column=0, padx=10)

    rnf = Button(root, text="Prediction 2", command=randomforest,  fg="black")
    rnf.config(font=("Times", 15, "bold italic"))
    rnf.grid(row=17, column=0, padx=10)

    lr = Button(root, text="Prediction 3", command=NaiveBayes,  fg="black")
    lr.config(font=("Times", 15, "bold italic"))
    lr.grid(row=19, column=0, padx=10)

    kn = Button(root, text="Prediction 4", command=knnClass,  fg="black")
    kn.config(font=("Times", 15, "bold italic"))
    kn.grid(row=21, column=0, padx=10)

    adab = Button(root, text="Prediction 4", command=adaboost,bg="blue", fg="black")
    adab.config(font=("Times", 15, "bold italic"))
    adab.grid(row=23, column=0, padx=10)

    t1 = Text(root, height=2, width=30, fg="black")
    t1.config(font=("Times", 15, "bold italic"))
    t1.grid(row=15, column=1, padx=5)

    t2 = Text(root, height=2, width=30, fg="black")
    t2.config(font=("Times", 15, "bold italic"))
    t2.grid(row=17, column=1, padx=5)

    t3 = Text(root, height=2, width=30,  fg="black")
    t3.config(font=("Times", 15, "bold italic"))
    t3.grid(row=19, column=1, padx=5)

    t4 = Text(root, height=2, width=30,  fg="black")
    t4.config(font=("Times", 15, "bold italic"))
    t4.grid(row=21, column=1, padx=5)

    t5 = Text(root, height=2, width=30,  fg="black")
    t5.config(font=("Times", 15, "bold italic"))
    t5.grid(row=23 , column=1, padx=5)

    # canvas = Canvas(root, width=50, height=50)
    # canvas.pack()
    # img = PhotoImage(file="/Users/macbookair/Desktop/logo-talan.png")
    # canvas.create_image(10, 10, anchor=NW, image=img)
    img = PhotoImage(file="logo-talan.png")
    panel = Label(root, image=img)
    panel.grid(row=3, column=1)
    #panel.config(bg="grey")


    root.mainloop()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
