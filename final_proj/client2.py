import sys
import socket
import os
import threading
import time
import pyrebase

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import (QApplication, QAction, QMainWindow,
QLabel, QWidget, QPushButton, QLineEdit, QVBoxLayout,
QMessageBox, QStackedWidget, QFileDialog, QFormLayout, QDialog, QDialogButtonBox)
from PyQt5.QtGui import QCloseEvent, QFont
from PyQt5.QtCore import QFile, QTextStream, Qt, QThread

from sidebar import Ui_MainWindow
from startpage import Ui_MainWindow_1
from loginpage import Ui_MainWindow_2
from signuppage import Ui_MainWindow_3
from GUI_Receiver import Ui_MainWindow_4
# from progressbar import Ui_Dialog

# Thông tin server
# 0.tcp.ap.ngrok.io
HOST = "192.168.0.103"
SERVER_PORT = 9999
FORMAT = "utf8"

# option
LOGIN = "login" 
END = "end"
SEND = "senddata"
GET = "get"
LOGOUT = "logout"
SENDF = "sendfile"
SIGNUP = "signup"
TEST = "test" 

# Khởi tạo kết nối đến Firebase
firebaseConfig = {
                    "apiKey": "AIzaSyChBPQ6dvYqXNY0FyQ48bATRyKz8Kh9J3w",
                    "authDomain": "objectdetection-87ddc.firebaseapp.com",
                    "databaseURL": "https://objectdetection-87ddc-default-rtdb.firebaseio.com",
                    "projectId": "objectdetection-87ddc",
                    "storageBucket": "objectdetection-87ddc.appspot.com",
                    "messagingSenderId": "952580339973",
                    "appId": "1:952580339973:web:c50eec021a4b6289205f6c",
                    "measurementId": "G-DF1804SSXP"
                }

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()

# Khởi tạo kết nối tới Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, SERVER_PORT))

class KLTN(QStackedWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("KLTN")
        startpage = StartPage()
        
        self.addWidget(startpage)
        self.setFixedSize(950, 600)
        self.setCurrentIndex(0)
        
    def closeEvent(self, event: QCloseEvent):
        reply = QMessageBox.question(self, 'Error', 'Do you want to exit ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        
        if reply == QMessageBox.Yes:
            event.accept()
            try:
                option = LOGOUT
                client.sendall(option.encode(FORMAT))
            except:
                pass
        else: 
            event.ignore()
        QApplication.closeAllWindows()
            
        

class StartPage(QMainWindow):
    def __init__(self):
        # Khởi tạo trang khởi đầu LoginPage
        super(StartPage, self).__init__()
        self.ui_1 = Ui_MainWindow_1()
        self.ui_1.setupUi(self)
        
        self.ui_1.login_button.clicked.connect(self.openLoginPage)
        self.ui_1.signup_button.clicked.connect(self.openSignUpPage)
        
    def openLoginPage(self):
        loginpage = LoginPage()
        window.addWidget(loginpage)
        window.setCurrentIndex(window.currentIndex()+1)
        
    def openSignUpPage(self):
        signuppage = SignUpPage()
        window.addWidget(signuppage)
        window.setCurrentIndex(window.currentIndex()+1)
        
class LoginPage(QMainWindow):
    def __init__(self):
        # Khởi tạo trang khởi đầu LoginPage
        super(LoginPage, self).__init__()
        
        self.ui_2 = Ui_MainWindow_2()
        self.ui_2.setupUi(self)
        
        self.ui_2.login_button.clicked.connect(self.LogIn)

    def openSideBar(self):
        sidebar = SideBarPage()
        window.addWidget(sidebar)
        window.setCurrentIndex(window.currentIndex()+1)
        
    def LogIn(self):
        try: 
            username = self.ui_2.entry_user.text()
            password = self.ui_2.entry_password.text()
            
            if username == "" or password == "":
                self.ui_2.invalid_label.setText("Fields cannot be empty")
                self.ui_2.invalid_label.setStyleSheet("background-color: rgb(255, 255, 127)")
                return 
            
            print(username, password)
            
            # Gửi lệnh đăng nhâp "login"
            option = LOGIN
            client.sendall(option.encode(FORMAT))
                        
            
            client.sendall(username.encode(FORMAT))
            client.recv(1024)
            
            client.send(password.encode(FORMAT))
            
            accepted = client.recv(1024).decode(FORMAT)
            print("accepted: "+ accepted)
            
            if accepted == "2":
                self.ui_2.invalid_label.setText("Invalid username or password")
                self.ui_2.invalid_label.setStyleSheet("background-color: rgb(255, 0, 0)")
            elif accepted == "1":
                self.openSideBar()
            elif  accepted == "0":
                self.ui_2.invalid_label.setText("User already logged in")
                self.ui_2.invalid_label.setStyleSheet("background-color: rgb(255, 255, 127)")
        except:
            self.ui_2.invalid_label.setText("Server is not responding")
            print("Server is not responding")
            
class SignUpPage(QMainWindow):
    def __init__(self):
        super(SignUpPage, self).__init__()
        self.ui_3 = Ui_MainWindow_3()
        self.ui_3.setupUi(self)
        
        self.ui_3.signup_button.clicked.connect(self.SignUp)
        
    def SignUp(self):
        try:
            user = self.ui_3.user_entry.text()
            pswd = self.ui_3.pass_entry.text()
            cf_pswd = self.ui_3.confirm_entry.text()

            if user == "" or pswd == "":
                self.ui_3.notification_label.setText("Fields cannot be empty")
                self.ui_3.notification_label.setStyleSheet("background-color: rgb(255, 255, 127)")
                return 
            elif pswd != cf_pswd:
                self.ui_3.notification_label.setText("Password is not the same")
                self.ui_3.notification_label.setStyleSheet("background-color: rgb(255, 0, 127)")
                return 
       
            #notice server for starting log in
            option = SIGNUP
            client.sendall(option.encode(FORMAT))
            
            
            #send username and password to server
            client.sendall(user.encode(FORMAT))
            print("input:", user)

            client.recv(1024)
            print("user received")

            client.sendall(pswd.encode(FORMAT))

            # see if login is accepted
            accepted = client.recv(1024).decode(FORMAT)
            print("accepted: "+ accepted)

            if accepted == "True":
                self.ui_3.notification_label.setText("Sign up successfully - Waiting for Admin's permission")
                self.ui_3.notification_label.setStyleSheet("background-color: rgb(85, 255, 127)")           
            else:
                self.ui_3.notification_label.setText("Username is not availale")

        except:
            print("Error 404: Server is not responding")
        
class SideBarPage(QMainWindow):
    def __init__(self):
        super(SideBarPage, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.row = "0"
        self.threads={}
    
        self.ui.icon_only_widget.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.home_btn_2.setChecked(True)
        
        self.ui.sendata_button.clicked.connect(self.sendData)
        self.ui.getdata_button.clicked.connect(self.GetData)
        self.ui.exit_btn_1.clicked.connect(self.clientLogOut)
        self.ui.exit_btn_2.clicked.connect(self.clientLogOut)
        self.ui.browser_button.clicked.connect(self.browseFile)
        self.ui.sendfile_button.clicked.connect(self.sendFile)
        self.ui.choose_button.clicked.connect(self.openChooseRow)
        self.ui.passdata_button.clicked.connect(self.openPassDataPage)

        
        self.ui.pushButton_2.clicked.connect(self.start_send_thread)
        self.ui.pushButton_3.clicked.connect(self.start_recv_thread)
        self.ui.pushButton_4.clicked.connect(self.stop_recv_thread)
        self.ui.pushButton_5.clicked.connect(self.stop_send_thread)
        
    def start_send_thread(self):
        self.threads[1] = ThreadClass1(parent=None, index=1)
        self.threads[1].start()
        self.threads[1].any_signal.connect(self.my_function1)
        self.ui.pushButton_2.setEnabled(False)
        self.ui.pushButton_5.setEnabled(True)
    
    def start_recv_thread(self):
        self.threads[2] = ThreadClass2(parent=None, index=2)
        self.threads[2].start()
        self.threads[2].any_signal.connect(self.my_function2)
        self.ui.pushButton_3.setEnabled(False)
        self.ui.pushButton_4.setEnabled(True)
    
    def stop_send_thread(self):
        self.threads[1].stop()
        self.ui.pushButton_2.setEnabled(True)
        self.ui.pushButton_5.setEnabled(False)
    
    def stop_recv_thread(self):
        self.threads[2].stop()
        self.ui.pushButton_3.setEnabled(True)
        self.ui.pushButton_4.setEnabled(False)
        
    def my_function1(self, data):
        data_ = data.split(",")
        index = self.sender().index
        if index == 1:
            self.ui.lineEdit_11.setText(data_[0])
            self.ui.lineEdit_5.setText(data_[1])
            self.ui.lineEdit_4.setText(data_[2])
            self.ui.lineEdit_3.setText(data_[3])
            self.ui.lineEdit_6.setText(data_[4])
            self.ui.lineEdit.setText(data_[5])
    def my_function2(self, data):
        data_ = data.split(",")
        index = self.sender().index
        if index == 2:
            self.ui.lineEdit_12.setText(data_[0])
            self.ui.lineEdit_8.setText(data_[1])
            self.ui.lineEdit_9.setText(data_[2])
            self.ui.lineEdit_10.setText(data_[3])
            self.ui.lineEdit_7.setText(data_[4])
            self.ui.lineEdit_2.setText(data_[5])
        pass
    
    def is_decimal(self, string):
        try: 
            float(string)
            return True
        except ValueError:
            return False
    
    def browseFile(self):
        self.file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', "C:\\", 'All Files (*);; Text Files (*.txt)')
        if self.file_name:
            self.ui.link_entry.setText(self.file_name)
        
    def sendFile(self):
        try:
            if self.ui.link_entry.text() == "":
                print("Fields cannot be empty")
                return 
    
            option = SENDF
            client.send(option.encode(FORMAT))
            
            file_name = self.file_name
            file_size = os.path.getsize(file_name)
            index = file_name.rfind("/")
            file_name = file_name[index+1:]
            
            client.send(file_name.encode(FORMAT))
            print(file_name.encode(FORMAT))
            
            client.recv(1024)
            
            client.send(str(file_size).encode(FORMAT))
            print(str(file_size).encode(FORMAT))
            
            client.recv(1024)
            
            with open(self.file_name, "rb") as fs:  
                c = 0
                while c < file_size:  
                    data = fs.read(1024)
                    if not data:
                        break
                    client.sendall(data)
                    c += len(data)
                    print(c)

            print("Done!")
            
        except:
            print("Server is not responding (sendfile)")
       
    def sendData(self): 
        try:
            self.DataEntry()
            if self.data == None:
                print("No data was found")
            else:
                option = SEND
                client.send(option.encode(FORMAT))  

                print(self.data)
                for item in self.data:
                    client.send(item.encode(FORMAT))
                    #wait response
                    client.recv(1024)

                msg = END
                client.send(msg.encode(FORMAT))
        except:
            print("Server is not responding (sendData)")
        
    def DataEntry(self):
        self.data = []
        # [CHECK] Fields are not empty:
        for field in (self.ui.ux_entry, self.ui.vx_entry, self.ui.wx_entry,
                      self.ui.ux_entry, self.ui.vy_entry, self.ui.wy_entry,
                      self.ui.uz_entry, self.ui.vz_entry, self.ui.wz_entry,
                      self.ui.px_entry, self.ui.py_entry, self.ui.pz_entry,
                      self.ui.length_entry, self.ui.width_entry, self.ui.height_entry):
            
            if not field.text():
                # print(f'{field.objectName()} cannot be empty')
                QMessageBox.critical(
                    self,
                    'Error!',
                    f"You must provide data for {field.objectName()}",
                )
                # Reset data:
                self.data = None
                return
            else:
                if self.is_decimal(field.text()):
                    self.data.append(field.text())
                else: 
                    QMessageBox.critical(
                        self, 'Error!', f"Data in {field.objectName()} is not a number"
                        # Reset data
                    )
                    
                    # Reset data
                    self.data = None
                    return
                
    def GetData(self):
        try:
            option = GET
            client.send(option.encode(FORMAT))
            
            client.send(self.row.encode(FORMAT))
            
            data = client.recv(1024).decode(FORMAT)
            if data == None:
                print("Data not available")
                return
            else:
                data = data.split(",")
                del data[0]
                if len(data) == 15:
                    # data for sidebarpage
                    self.ui.ux_entry_2.setText(data[0])
                    self.ui.vx_entry_2.setText(data[1])
                    self.ui.wx_entry_2.setText(data[2])
                    self.ui.uy_entry_2.setText(data[3])
                    self.ui.vy_entry_2.setText(data[4])
                    self.ui.wy_entry_2.setText(data[5])
                    self.ui.uz_entry_2.setText(data[6])
                    self.ui.vz_entry_2.setText(data[7])
                    self.ui.wz_entry_2.setText(data[8])
                    self.ui.px_entry_2.setText(data[9])
                    self.ui.py_entry_2.setText(data[10])
                    self.ui.pz_entry_2.setText(data[11])
                    self.ui.length_entry_2.setText(data[12])
                    self.ui.width_entry_2.setText(data[13])
                    self.ui.height_entry_2.setText(data[14])
                    
                    # Data for passdatapage
                    self.gui.textBrowser_1.setText(data[0])
                    self.gui.x_left = float(data[0])
                    self.gui.textBrowser_2.setText(data[1])
                    self.gui.y_left = float(data[1])
                    self.gui.textBrowser_3.setText(data[2])
                    self.gui.z_left = float(data[2])
                    self.gui.textBrowser_4.setText(data[3])
                    self.gui.pitch_left = float(data[3])
                    self.gui.textBrowser_5.setText(data[4])
                    self.gui.roll_left = float(data[4])
                    self.gui.textBrowser_6.setText(data[5])
                    self.gui.Yaw_left = float(data[5])
                    self.gui.textBrowser_7.setText(data[6])
                    self.gui.x_right = float(data[6])
                    self.gui.textBrowser_8.setText(data[7])
                    self.gui.y_right = float(data[7])
                    self.gui.textBrowser_9.setText(data[8])
                    self.gui.z_right = float(data[8])
                    self.gui.textBrowser_10.setText(data[9])
                    self.gui.roll_right = float(data[9])
                    self.gui.textBrowser_11.setText(data[10])
                    self.gui.pitch_right = float(data[10])
                    self.gui.textBrowser_12.setText(data[11])
                    self.gui.Yaw_right = float(data[11])

                    
                else:
                    print("Not enough data!")
            
        except:
            print("Server is not responding (getData)")   
    
    def clientLogOut(self):
        try:
            option = LOGOUT
            client.sendall(option.encode(FORMAT))
            accepted = client.recv(1024).decode(FORMAT)
            print(accepted)
            if accepted == "True":
                self.openStartPage()
        except:
            print("Server is not responding")
    
    def openStartPage(self):
        startpage = StartPage()
        window.addWidget(startpage)
        window.setCurrentIndex(window.currentIndex()+1)
        
    def openChooseRow(self):
        dialog = AddDialog(self)
        dialog.resize(275, 80)
        if (dialog.exec() == QDialog.Accepted):
            self.ui.choose_label.setText("You choose row: " + dialog.row)
            self.row = dialog.row
    
    def openPassDataPage(self):
        self.window = QMainWindow()
        self.gui = Ui_MainWindow_4()
        self.gui.setupUi(self.window)
        self.window.show()

    ## Function for searching
    def on_search_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        search_text = self.ui.search_input.text().strip()
        if search_text:
            self.ui.search_label.setText(search_text)

    ## Function for changing page to user page
    def on_user_btn_clicked(self):
        self.ui.stackedWidget.setCurrentIndex(6)

    ## Change QPushButton Checkable status when stackedWidget index changed
    def on_stackedWidget_currentChanged(self, index):
        btn_list = self.ui.icon_only_widget.findChildren(QPushButton) \
                    + self.ui.full_menu_widget.findChildren(QPushButton)
        
        for btn in btn_list:
            if index in [5, 6]:
                btn.setAutoExclusive(False)
                btn.setChecked(False)
            else:
                btn.setAutoExclusive(True)
            
    ## functions for changing menu page
    def on_home_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)
    
    def on_home_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def on_dashborad_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_dashborad_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def on_orders_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_orders_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def on_products_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_products_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(3)

    def on_customers_btn_1_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

    def on_customers_btn_2_toggled(self):
        self.ui.stackedWidget.setCurrentIndex(4)

class AddDialog(QDialog):
    '''Add Contact dialog'''
    def __init__(self, parent=None):
        '''Initializer'''
        super().__init__(parent=parent)
        self.setWindowTitle('Choose row of data')
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        #self.resize(275, 80)
        self.row = None

        self.setupUI()

        self.sender()
    def setupUI(self):
        '''Setup the Add Contact dialog's GUI.'''
        # Create line edits for data fields:
        self.nameField = QLineEdit()
        self.nameField.setObjectName('row')
    
        # Lay out the data fields:
        layout = QFormLayout()
        layout.addRow('Row:', self.nameField)
        self.layout.addLayout(layout)
        
        # Add standard buttons to the dialog and connect them:
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)
        
    def accept(self):
        '''Accept the data provided through the dialog.'''
        # [CHECK] Fields are not empty:
        if not self.nameField.text():
            QMessageBox.critical(
                self,
                'Error!',
                f"You must provide an entry's {self.nameField.objectName()}",
            )
            # Reset data:
            self.row = None
            return
        else:
            self.row = self.nameField.text()
            
        super().accept()
        
class ThreadClass1(QThread):
    any_signal = QtCore.pyqtSignal(str)
    def __init__(self, parent=None, index=0):
        super(ThreadClass1, self).__init__(parent)
        self.index = index
        self.is_running = True
    def getFirebaseData(self):
        self.data = []
        data_name = ['P_x', 'P_y', 'P_z', 'U_x', 'U_y', 'U_z']
        
        for name in data_name:
            a = db.child(name).child('value').get().val()
            self.data.append(str(a))

        self.data = ",".join(self.data)
        
    def run(self):
        print('Starting Thread ...', self.index)
        try:
            while True:
                self.getFirebaseData()        
                self.any_signal.emit(self.data)
                print(self.data)

                client.send(TEST.encode(FORMAT))
                client.send(self.data.encode(FORMAT))
                
                time.sleep(0.5)
        except:
            print('Error!')
    
    def stop(self):
        self.is_running = False
        print('Stopping Thread ...', self.index)
        self.terminate()

class ThreadClass2(QThread):
    any_signal = QtCore.pyqtSignal(str)
    def __init__(self, parent=None, index=0):
        super(ThreadClass2, self).__init__(parent)
        self.index = index
        self.is_running = True
        
    def run(self):
        print('Starting Thread ...', self.index)
        try:
            while True:
                cnt = client.recv(1024).decode(FORMAT)
                print(cnt)
                self.any_signal.emit(cnt)
        except:
            print('Error!')
    
    def stop(self):
        self.is_running = False
        print('Stopping Thread ...', self.index)
        self.terminate()
        
app = QApplication(sys.argv)
style_file = QFile("style.qss")
style_file.open(QFile.ReadOnly | QFile.Text)
style_stream = QTextStream(style_file)
app.setStyleSheet(style_stream.readAll())

window = KLTN()
window.show()
sys.exit(app.exec_())
