from PyQt5.QtWidgets import QApplication
from test1 import MainWindow  # Import class MainWindow từ file test1
from GUI_Receiver import Ui_MainWindow_4  
import sys
import subprocess
if __name__ == "__main__":
    # Khởi tạo ứng dụng PyQt
    app = QApplication([])

    # Hiển thị cửa sổ chính của test1
    window = MainWindow()
    window.show()

    # Chạy ứng dụng GUI_Receiver trong một tiến trình con
    subprocess.Popen(['python', 'GUI_Receiver.py'])

    # Thoát khỏi ứng dụng PyQt khi cửa sổ chính đóng
    sys.exit(app.exec_())
