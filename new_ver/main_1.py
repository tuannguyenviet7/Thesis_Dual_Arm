from PyQt5.QtWidgets import QApplication
from test1 import MainWindow  # Import class MainWindow từ file test1
from GUI_Receiver import Ui_MainWindow_4  
from PyQt5 import QtWidgets
import sys
import subprocess
if __name__ == "__main__":
    # Khởi tạo ứng dụng PyQt
    app = QtWidgets.QApplication(sys.argv)

    # Hiển thị cửa sổ chính của test1
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_4()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # Chạy ứng dụng GUI_Receiver trong một tiến trình con
    

    # Thoát khỏi ứng dụng PyQt khi cửa sổ chính đóng
    sys.exit(app.exec_())
