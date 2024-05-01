from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QApplication, QTableWidgetItem, QMessageBox
def addition(a,b):
    return a+b
def sous(a,b):
    return a-b
def puis(a,b):
    if b==1:
        return a
    else:
        return a * puis(a,b-1)
def dev(a,b):
    return a/b
def multi(a,b):
    return a*b
def bt1_click():
    #addition
    a=window.le1.text()
    b=window.le2.text()
    if  a=="":
        msg="Veuillez saisir Le 1ere"
        QMessageBox.critical(window,"erreur",msg)
    elif b=="":
        msg="Veuillez saisir 2eme Nombre"
        QMessageBox.critical(window,"erreur",msg)
    else:
        a=float(a)
        b=float(b)
        window.res.setText(str(addition(a,b)))
def bt3_click():
    #puissance
    a=window.le1.text()
    b=window.le2.text()
    if  a=="":
        msg="Veuillez saisir Le 1ere"
        QMessageBox.critical(window,"erreur",msg)
    elif b=="":
        msg="Veuillez saisir 2eme Nombre"
        QMessageBox.critical(window,"erreur",msg)
    else:
        a=float(a)
        b=float(b)
        window.res.setText(str(puis(a,b)))
def bt4_click():
    #devision
    a=window.le1.text()
    b=window.le2.text()
    if  a=="":
        msg="Veuillez saisir Le 1ere"
        QMessageBox.critical(window,"erreur",msg)
    elif b=="":
        msg="Veuillez saisir 2eme Nombre"
        QMessageBox.critical(window,"erreur",msg)
    else:
        a=float(a)
        b=float(b)
        window.res.setText(str(dev(a,b)))
def bt2_click():
    #soustraction
    a=window.le1.text()
    b=window.le2.text()
    if  a=="":
        msg="Veuillez saisir Le 1ere"
        QMessageBox.critical(window,"erreur",msg)
    elif b=="":
        msg="Veuillez saisir 2eme Nombre"
        QMessageBox.critical(window,"erreur",msg)
    else:
        a=float(a)
        b=float(b)
        window.res.setText(str(sous(a,b)))

def bt5_click():
    #multiplication
    a=window.le1.text()
    b=window.le2.text()
    if  a=="":
        msg="Veuillez saisir Le 1ere"
        QMessageBox.critical(window,"erreur",msg)
    elif b=="":
        msg="Veuillez saisir 2eme Nombre"
        QMessageBox.critical(window,"erreur",msg)
    else:
        a=float(a)
        b=float(b)
        window.res.setText(str(multi(a,b)))

app = QApplication([])
window = loadUi ("/home/dell/Desktop/calculatrice/cal.ui")
window.show()
window.bt1.clicked.connect ( bt1_click )
window.bt3.clicked.connect ( bt3_click )
window.bt4.clicked.connect ( bt4_click )
window.bt2.clicked.connect ( bt2_click )
window.bt5.clicked.connect ( bt5_click )

app.exec_()