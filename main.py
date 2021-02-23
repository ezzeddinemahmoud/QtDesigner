import sys
from random import randint
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUi

application=QApplication(sys.argv)
# ------------------------------------------
class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("main.ui",self)
#------------------------------------------        
class MyApp1(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("form2.ui",self)
#-----------------------------------------

form1=MyApp() # Création d'un objet de la classe MyApp (instance)
form1.show() # Afficher la fenetre
form2=MyApp1()
form2.pushButton_3.setEnabled(False)
form2.pushButton_4.setEnabled(False)
form2.pushButton_5.setEnabled(False)
form2.pushButton_6.setEnabled(False)
# Saisie -----------------------------------
def saisie():
    form2.lineEdit.setText(str(randint(1,100)))
    form2.lineEdit_2.setText(str(randint(1,100)))
    form2.pushButton_3.setEnabled(True)
    form2.pushButton_4.setEnabled(True)
    form2.pushButton_5.setEnabled(True)
    form2.pushButton_6.setEnabled(True)
    form2.lineEdit_3.setText("")
    form2.lineEdit_4.setText("")
    form2.lineEdit_5.setText("")
    form2.lineEdit_6.setText("")
    form2.lineEdit_7.setText("")
    form2.lineEdit_8.setText("")
# PGCD ------------------------------------------    
    
def pgcd(a,b):
    if b==0:
        return a
    else:
        r=a%b
        return pgcd(b,r)
def calculer_pgcd():
     form2.lineEdit_4.setText(str(pgcd(int(form2.lineEdit.text()),int(form2.lineEdit_2.text()))))   
# --- PPCM --------------------------
def ppcm(a,b):
    if (a==0) or (b==0):
        return 0
    else:
        return (a*b)//pgcd(a,b)
def calculer_ppcm():
    form2.lineEdit_3.setText(str(ppcm(int(form2.lineEdit.text()),int(form2.lineEdit_2.text()))))   
# ------ Cancel --------------------
def cancel():
    form1.destroy()
def fermer():
    form2.destroy()
    form1.show()
    form1.lineEdit.setText("")
    form1.lineEdit_2.setText("")
# -----Premier -------
def tester(x):
    s=0
    for i in range(1,int(x)+1):
        if int(x)%i==0:
            s=s+i
    return s
def premier():
    x=form2.lineEdit.text()
    if tester(int(x))==int(x)+1:
        form2.lineEdit_5.setText("Premier")
    else:
        form2.lineEdit_5.setText("Non Premier")
    x=form2.lineEdit_2.text()
    if tester(int(x))==int(x)+1:
        form2.lineEdit_7.setText("Premier")
    else:
        form2.lineEdit_7.setText("Non Premier")
# ------ Parfaits --------------
def parfait(x):
    s=0
    for i in range(1,x):
        if x%i==0:
            s=s+i
    return x==s
def parfaits():
    if parfait(int(form2.lineEdit.text())):
        form2.lineEdit_6.setText("Parfait")
    else:
        form2.lineEdit_6.setText("Non Parfait")
    if parfait(int(form2.lineEdit_2.text())):
        form2.lineEdit_8.setText("Parfait")
    else:
        form2.lineEdit_8.setText("Non Parfait")


# ------------------------------
def connecter():
    msg=QMessageBox()
    msg.setWindowTitle("Warning")
    if form1.lineEdit.text()=="user" and form1.lineEdit_2.text()=="user":
        form2.show()
        form1.hide()
    elif form1.lineEdit.text()!="user":
        msg.setText("Username incorrect")
        msg.exec_()
    elif form1.lineEdit_2.text()!="user":
        msg.setText("Password incorrect")
        msg.exec_()
# -------Connections------------------------------
form2.pushButton.clicked.connect(saisie)
form1.pushButton.clicked.connect(connecter)
form1.pushButton_2.clicked.connect(cancel)
form2.pushButton_2.clicked.connect(fermer)
form2.pushButton_3.clicked.connect(calculer_pgcd)
form2.pushButton_4.clicked.connect(calculer_ppcm)
form2.pushButton_5.clicked.connect(premier)
form2.pushButton_6.clicked.connect(parfaits)

application.exec_() # boucle infinie