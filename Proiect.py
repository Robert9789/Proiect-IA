from tkinter import *
import numpy as np
import pandas as pd

lista1=['dureri_de_spate','oboseala','durere_abdominală','durere_de_cap','febra','dureri',
'îngălbenirea_ochilor','insuficiență_hiperactivă_acută','exces_fluid','umflarea_stomacului',
'noduri_limfatice_umflate','disconfort','vedere_încețoșată','nas_iritat','gat_iritat',
'ochi_rosi','presiunea_de_la_nivelul_sinusurilor','nas_infundat','congestie','durere_toracică','fragilitate_membre',
'palpitati','dureri_intestinale','probleme_la_coloana','sangerari',
'iritație','durere_de_gât','amețeli','crampe','contuzii','obezitate','picioare_umflate',
'vasele_de_sânge_umflate','ochii_umflați','tiroidă_mărită','unghii_fragile',
'extremititatile_membrelor_umflate','înfometare','inflamatii','buze_uscate',
'vorbire_greoaie','durere_de_genunchi','durere_articulație_de_șold','slăbirea_musculară','gât_înțepenit','umflarea_articulațiilor',
'mișcare_cu_dificultate','ameteli','pierdere_de_echilibru','nesiguranță',
'fragilitatea_unei_părți_a_corpului','pierdere_mirosului','disconfort','lipsa_miros',
'dureri_stomacale','dureri_spate','iritatie','aspect_palid',
'depresie','nervozitate','dureri_musculare','alterarea_simturilor','pete_roșii_pe_corp','dureri_de_stomac',
'menstruație_anormală','pete_pe_corp','iritatia_ochilor','apetit_crecut','poliurie','anemie','dureri_nas',
'gust_amar','lipsa_de_concentrare','halucinati','transfuziei_de_sânge',
'transmitere_prin_sange','coma','hemoragie_stomacală','umflare_a_abdomenului',
'istoric_de_consum_de_alcool','exces_de_fluide','sângerari','venele_proeminente',
'palpitații','mers_dureros','coșuri','puncte_negre_corp','sângerari_grave','exfolierea_pielii',
'expunere_la_chimicale','răni_la_unghii','unghii_nesanatoase_inflamate','cos','nas_imflamat',
'infectie']

afectiunea=['Infecția_fungica','Alergie','Reflux_gastrointestinal','Colestază_cronică','Reacție_la_medicamente',
'Tulburări_ulcer','HIV','Diabet','Gastroenterită','Astm','Hipertensiune_arterială',
' Migrenă','Spondiloza_cervicală',
'Paralizie_hemoragie_cerebrală','Icter','Malarie','Varicelă','Febra','Tifoidă','Hepatita_A',
'Hepatita_B','Hepatita_C','Hepatita_D','Hepatita_E','Hepatita','Tuberculoză',
'Răceală','Pneumonie','Hemoroizi ',
'Atac_de_cord','Varice','Hipotiroidism','Hipertiroidism','Hipoglicemie','Osteoartroză',
'Artrita','Vertij','Acne','Infecția_tractului','Psoriazis',
'Infectia_pieli']

lista2=[]
for x in range(0,len(lista1)):
    lista2.append(0)

df=pd.read_csv("test.csv")
df.replace({'prognosis':{'Infecția_fungica':0,'Alergie':1,'Reflux_gastrointestinal':2,'Colestază_cronică':3,'Reacție_la_medicamente':4,
'Tulburări_ulcer':5,'HIV':6,'Diabet ':7,'Gastroenterită':8,'Astm':9,'Hipertensiune_arterială ':10,
'Migrenă':11,'Spondiloza_cervicală':12,
'Paralizie_hemoragie_cerebrală':13,'Icter':14,'Malarie':15,'Varicelă':16,'Febra':17,'Tifoidă':18,'Hepatita_A':19,
'Hepatita_B':20,'Hepatita_C':21,'Hepatita_D':22,'Hepatita_E':23,'Hepatita':24,'Tuberculoză':25,
'Răceală':26,'Pneumonie':27,'Hemoroizi':28,'Heart attack':29,'Varice':30,'Hipotiroidism':31,
'Hipertiroidism':32,'Hipoglicemie':33,'Osteoartroză':34,'Artrita':35,
'Vertij':36,'Acne':37,'Infecția_tractului':38,'Psoriazis':39,
'Infectia_pieli':40}},inplace=True)

X= df[lista1]

y = df[["prognosis"]]
np.ravel(y)

tr=pd.read_csv("testare.csv")
tr.replace({'prognosis':{'Infecția_fungica':0,'Alergie':1,'Reflux_gastrointestinal':2,'Colestază_cronică':3,'Reacție_la_medicamente':4,
'Tulburări_ulcer':5,'HIV':6,'Diabet ':7,'Gastroenterită':8,'Astm':9,'Hipertensiune_arterială ':10,
'Migrenă':11,'Spondiloza_cervicală':12,
'Paralizie_hemoragie_cerebrală':13,'Icter':14,'Malarie':15,'Varicelă':16,'Febra':17,'Tifoidă':18,'Hepatita_A':19,
'Hepatita_B':20,'Hepatita_C':21,'Hepatita_D':22,'Hepatita_E':23,'Hepatita':24,'Tuberculoză':25,
'Răceală':26,'Pneumonie':27,'Hemoroizi':28,'Heart attack':29,'Varice':30,'Hipotiroidism':31,
'Hipertiroidism':32,'Hipoglicemie':33,'Osteoartroză':34,'Artrita':35,
'Vertij':36,'Acne':37,'Infecția_tractului':38,'Psoriazis':39,
'Infectia_pieli':40}},inplace=True)

X_test= tr[lista1]
y_test = tr[["prognosis"]]
np.ravel(y_test)

def DecisionTree():

    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier() 
    clf3 = clf3.fit(X,y)

    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))


    psymptoms = [Simptom1.get(),Simptom2.get(),Simptom3.get(),Simptom4.get(),Simptom5.get()]

    for k in range(0,len(lista1)):

        for z in psymptoms:
            if(z==lista1[k]):
                lista2[k]=1

    inputtest = [lista2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(afectiunea)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, afectiunea[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")


def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))


    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))


    psymptoms = [Simptom1.get(),Simptom2.get(),Simptom3.get(),Simptom4.get(),Simptom5.get()]

    for k in range(0,len(lista1)):
        for z in psymptoms:
            if(z==lista1[k]):
                lista2[k]=1

    inputtest = [lista2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(afectiunea)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, afectiunea[a])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")


def NaiveBayes():
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))


    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(accuracy_score(y_test, y_pred,normalize=False))


    psymptoms = [Simptom1.get(),Simptom2.get(),Simptom3.get(),Simptom4.get(),Simptom5.get()]
    for k in range(0,len(lista1)):
        for z in psymptoms:
            if(z==lista1[k]):
                lista2[k]=1

    inputtest = [lista2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(afectiunea)):
        if(predicted == a):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, afectiunea[a])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")



root = Tk()
root.configure(background='green')

Simptom1 = StringVar()
Simptom1.set(None)
Simptom2 = StringVar()
Simptom2.set(None)
Simptom3 = StringVar()
Simptom3.set(None)
Simptom4 = StringVar()
Simptom4.set(None)
Simptom5 = StringVar()
Simptom5.set(None)
Simptom6 = StringVar()
Simptom6.set(None)
Simptom7 = StringVar()
Name = StringVar()


w2 = Label(root, justify=CENTER, text="Predictia bolilor", fg="white", bg="blue")
w2.config(font=("Elephant", 32))
w2.grid(row=1, column=0, columnspan=2, padx=100)
w2 = Label(root, justify=CENTER, text="Proiect AI", fg="white", bg="blue")
w2.config(font=("Aharoni", 32))
w2.grid(row=2, column=0, columnspan=2, padx=100)


NameLb = Label(root, text="Nume Prenume pacient:", fg="yellow", bg="black")
NameLb.grid(row=6, column=0, pady=15, sticky=W)


S1Lb = Label(root, text="Simptom  1", fg="orange", bg="black")
S1Lb.grid(row=7, column=0, pady=10, sticky=W)

S2Lb = Label(root, text="Simptom 2", fg="orange", bg="black")
S2Lb.grid(row=8, column=0, pady=10, sticky=W)

S3Lb = Label(root, text="Simptom 3", fg="orange", bg="black")
S3Lb.grid(row=9, column=0, pady=10, sticky=W)

S4Lb = Label(root, text="Simptom 4", fg="orange", bg="black")
S4Lb.grid(row=10, column=0, pady=10, sticky=W)

S5Lb = Label(root, text="Simptom 5", fg="orange", bg="black")
S5Lb.grid(row=11, column=0, pady=10, sticky=W)

S5Lb = Label(root, text="Simptom 6", fg="orange", bg="black")
S5Lb.grid(row=11, column=0, pady=10, sticky=W)

S6Lb = Label(root, text="Simptom 6", fg="orange", bg="black")
S6Lb.grid(row=11, column=0, pady=10, sticky=W)

S7Lb = Label(root, text="Simptom 6", fg="orange", bg="black")
S7Lb.grid(row=11, column=0, pady=10, sticky=W)

lrLb = Label(root, text="Algoritmul DecisionTree", fg="white", bg="teal")
lrLb.grid(row=15, column=0, pady=10,sticky=W)

destreeLb = Label(root, text="Algoritmul RandomForest", fg="white", bg="teal")
destreeLb.grid(row=17, column=0, pady=10, sticky=W)

ranfLb = Label(root, text="Algoritmul NaiveBayes", fg="white", bg="teal")
ranfLb.grid(row=19, column=0, pady=10, sticky=W)

OPTIONS = sorted(lista1)

NameEn = Entry(root, textvariable=Name)
NameEn.grid(row=6, column=1)

S1En = OptionMenu(root, Simptom1,*OPTIONS)
S1En.grid(row=7, column=1)

S2En = OptionMenu(root, Simptom2,*OPTIONS)
S2En.grid(row=8, column=1)

S3En = OptionMenu(root, Simptom3,*OPTIONS)
S3En.grid(row=9, column=1)

S4En = OptionMenu(root, Simptom4,*OPTIONS)
S4En.grid(row=10, column=1)

S5En = OptionMenu(root, Simptom5,*OPTIONS)
S5En.grid(row=11, column=1)

S6En = OptionMenu(root, Simptom5,*OPTIONS)
S6En.grid(row=11, column=1)

S7En = OptionMenu(root, Simptom5,*OPTIONS)
S7En.grid(row=11, column=1)

dst = Button(root, text="Algoritmul DecisionTree", command=DecisionTree,bg="green",fg="blue")
dst.grid(row=8, column=3)

rnf = Button(root, text="Algoritmul Randomforest", command=randomforest,bg="green",fg="blue")
rnf.grid(row=9, column=3,padx=10)

lr = Button(root, text="Algoritmul NaiveBayes", command=NaiveBayes,bg="green",fg="blue")
lr.grid(row=10, column=3,padx=10)

#textfileds
t1 = Text(root, height=1, width=40,bg="white",fg="black")
t1.grid(row=15, column=1, padx=10)

t2 = Text(root, height=1, width=40,bg="white",fg="black")
t2.grid(row=17, column=1 , padx=10)

t3 = Text(root, height=1, width=40,bg="white",fg="black")
t3.grid(row=19, column=1 , padx=10)

root.mainloop()
