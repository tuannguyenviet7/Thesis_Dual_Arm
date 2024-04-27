import socket 
import threading 
import pyodbc

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

#192.168.1.119
HOST = "192.168.0.102" 
SERVER_PORT = 65432 
FORMAT = "utf8"

SERVER_NAME = 'DESKTOP-DHEAITB\SQLEXPRESS'
DATABASE_NAME = 'IOT'

LOGIN = "login"
CHECK = "check"
SEND = "senddata"
GET = "get"
LOGOUT = "logout"
SENDF = "sendfile"
SIGNUP = "signup"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((HOST, SERVER_PORT))
s.listen()

Live_Account = []

def Insert_New_Account(user,password):
    cursor=ConnectToDB()
    cursor.execute( "insert SignUp_Account values(?,?)",(user,password))
    cursor.commit()

def RecvFile(conn):
    try:
        file_name = conn.recv(1024).decode(FORMAT)
        print(file_name)
        file_size = conn.recv(1024).decode(FORMAT)
        print(file_size)
        
        with open(file_name, "wb") as fr:
            data = conn.recv(int(file_size))
            fr.write(data)
            fr.close()
            
        print("Done")
    
    except:
        print("Error")

def Insert_Data(conn):
    list = []
    
    item = conn.recv(1024).decode(FORMAT)
    
    while (item != "end"):
        list.append(item)
        #response
        conn.send(item.encode(FORMAT))
        item = conn.recv(1024).decode(FORMAT)
    
    print(list) 
    try:
        cursor=ConnectToDB()
        cursor.execute("insert RobotData values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        (list[0], list[1], list[2], list[3], list[4], list[5], list[6], list[7],
         list[8], list[9], list[10], list[11], list[12], list[13], list[4]))
        
        cursor.commit()
        
    except pyodbc.Error:
        print("Error")
        return False
    
    return True

def Get_Data(conn):
    
    cursor=ConnectToDB()
    cursor.execute("select * from RobotData")
    
    data = cursor.fetchone()
    
    if data == None:
        data = "No data available"
    else: 
        data = str(data)
        data = data[1:len(data)-1]
        data = data.replace("'", "")
        data = data.replace(" ", "")
        
    conn.send(data.encode(FORMAT))

def check_clientLogIn(username, password):
    cursor=ConnectToDB()
    cursor.execute("select username from Account")
    
    if Check_LiveAccount(username) == False:
        return 0
    
    for row in cursor:
        parse=str(row)
        parse_check =parse[2:]
        parse= parse_check.find("'")
        parse_check= parse_check[:parse]
        if parse_check == username:
            cursor.execute("select password from Account where username=(?)",(username))
            parse= str(cursor.fetchone())
            parse_check =parse[2:]
            parse= parse_check.find("'")
            parse_check= parse_check[:parse]
            if password== parse_check:
                return 1
            
    return 2

def Remove_LiveAccount(conn, addr):
    for row in Live_Account:
        parse= row.find("-")
        parse_check=row[:parse]
        if parse_check == str(addr):
            Live_Account.remove(row)
            conn.sendall("True".encode(FORMAT))

def Check_LiveAccount(username):
    for row in Live_Account:
        parse = row.find("-")
        parse_check = row[(parse+1):]
        if parse_check == username:
            return False
    return True

def clientLogIn(sck, addr):
    
    user = sck.recv(1024).decode(FORMAT)
    print("username:--" + user +"--")

    sck.sendall(user.encode(FORMAT))
    
    pswd = sck.recv(1024).decode(FORMAT)
    print("password:--" + pswd +"--")
    
    accepted = check_clientLogIn(user, pswd)
    
    if accepted == 1:
        account = str(addr) + "-" + user
        Live_Account.append(account)
        
    print("accept:", accepted)
    sck.sendall(str(accepted).encode(FORMAT))
    print("client" , addr, "connected")
    print("")
    
def check_clientSignUp(username):
    
    cursor=ConnectToDB()
    cursor.execute("select username from Account")
    for row in cursor:
        parse=str(row)
        parse_check =parse[2:]
        parse= parse_check.find("'")
        parse_check= parse_check[:parse]
        if parse_check == username:
            return False
    return True

def clientSignUp(sck, addr):

    user = sck.recv(1024).decode(FORMAT)
    print("username:--" + user +"--")

    sck.sendall(user.encode(FORMAT))

    pswd = sck.recv(1024).decode(FORMAT)
    print("password:--" + pswd +"--")

    #a = input("accepting...")
    accepted = check_clientSignUp(user)
    print("accept:", accepted)
    sck.sendall(str(accepted).encode(FORMAT))

    if accepted:
        Insert_New_Account(user, pswd)

    print("end-signup()")
    print("")
    
def ConnectToDB():
    cnxn = (pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server}; SERVER='
                      + SERVER_NAME +'; DATABASE='+ DATABASE_NAME +
                      ';Trusted_Connection=yes'))
    
    cursor = cnxn.cursor()
    return cursor   
        
def handleClient(conn: socket, addr):
    
    print("conn:", conn.getsockname())
    try:
        while True:
            option = conn.recv(1024).decode(FORMAT)
            if option == LOGIN:
                print("LOGIN REQUEST")
                clientLogIn(conn, addr)
            elif option == SEND:
                print("SEND REQUEST")
                Insert_Data(conn)
            elif option == GET:
                print("GET REQUEST")
                Get_Data(conn)
            elif option == LOGOUT:
                print("LOGOUT REQUEST")
                Remove_LiveAccount(conn, addr)
            elif option == SENDF:
                print("SEND FILE REQUEST")
                RecvFile(conn)
            elif option == SIGNUP:
                clientSignUp(conn, addr)
                
    except ConnectionResetError:
        pass
    finally:
        Remove_LiveAccount(conn, addr)
        print(addr, "closed")
            

#-----------------------main-------------

def runServer():
    try:
        print(HOST)
        print("Waiting for Client")
        
        while True:
            print("enter while loop")
            conn, addr = s.accept()

            clientThread = threading.Thread(target= handleClient, args=(conn,addr))
            clientThread.daemon = True 
            clientThread.start()
        
            #handle_client(conn, addr)
            print("end main-loop")
            
    except KeyboardInterrupt:
        print("error")
        s.close()
        
    finally:
        s.close()
        print("End")
        
class ServerSide(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        
        self.setObjectName("Server")
        self.resize(800, 600)
        self.setWindowTitle("Server")
        
        self.centralwidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralwidget)
        self.centralwidget.setObjectName("centralwidget")
        
        self.setupUi()
        
    def setupUi(self):
    
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 10, 141, 61))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setText("SERVER SIDE")
        
        self.list_account = QtWidgets.QListWidget(self.centralwidget)
        self.list_account.setGeometry(QtCore.QRect(90, 100, 421, 371))
        self.list_account.setObjectName("account_list")
        
        self.refresh_button = QtWidgets.QPushButton(self.centralwidget)
        self.refresh_button.setGeometry(QtCore.QRect(590, 250, 91, 41))
        self.refresh_button.setObjectName("refresh_button")
        self.refresh_button.setText("Refresh")
        self.refresh_button.clicked.connect(self.Update_LiveAccount)
    
    def Update_LiveAccount(self):
        try:
            self.list_account.clear()
            for i in range(len(Live_Account)):
                self.list_account.insertItem(i, Live_Account[i])
        except:
            print("No client access")
            
sThread = threading.Thread(target=runServer)
sThread.daemon = True 
sThread.start() 

app = QtWidgets.QApplication(sys.argv)
window = ServerSide()
window.show()
sys.exit(app.exec_())
