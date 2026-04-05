import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QRadioButton, QPushButton, 
    QStackedWidget, QProgressBar, QMessageBox, QDateEdit, QTextEdit
)
from PySide6.QtCore import Qt

# ===============================
# MODERN STYLE SHEET (FIXED)
# ===============================
STYLE_SHEET = """
QWidget {
    background-color: #f8f9fa;
    font-family: 'Segoe UI', Arial;
    font-size: 14px;
    color: #000000;
}
QLineEdit, QDateEdit, QTextEdit {
    padding: 10px;
    border: 1px solid #ced4da;
    border-radius: 6px;
    background-color: white;
    color: #000000;
}
QLineEdit:focus, QTextEdit:focus, QDateEdit:focus {
    border: 2px solid #0d6efd;
}
QPushButton {
    padding: 10px 20px;
    border-radius: 6px;
    font-weight: bold;
}
QPushButton#PrimaryBtn {
    background-color: #0d6efd;
    color: #ffffff;
    border: none;
}
QPushButton#PrimaryBtn:disabled {
    background-color: #a0c4ff;
}
QPushButton#SecondaryBtn {
    background-color: #e9ecef;
    color: #000000;
    border: 1px solid #ced4da;
}
QLabel#Header {
    font-size: 22px;
    font-weight: bold;
    margin-bottom: 10px;
}
QLabel#StepIndicator {
    color: #495057;
    font-weight: bold;
    font-size: 12px;
}
"""

class Step1(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        layout.addWidget(QLabel("Data Pribadi", objectName="Header"))
        
        self.nama = QLineEdit()
        self.nama.setPlaceholderText("Min. 3 karakter")
        
        self.tanggal = QDateEdit()
        self.tanggal.setCalendarPopup(True)

        gender_box = QHBoxLayout()
        self.laki = QRadioButton("Laki-laki")
        self.perempuan = QRadioButton("Perempuan")
        gender_box.addWidget(self.laki)
        gender_box.addWidget(self.perempuan)

        self.btn_next = QPushButton("Lanjut", objectName="PrimaryBtn")
        self.btn_next.setEnabled(False)

        layout.addWidget(QLabel("<b>Nama Lengkap:</b>"))
        layout.addWidget(self.nama)
        layout.addWidget(QLabel("<b>Tanggal Lahir:</b>"))
        layout.addWidget(self.tanggal)
        layout.addWidget(QLabel("<b>Jenis Kelamin:</b>"))
        layout.addLayout(gender_box)
        layout.addStretch()
        layout.addWidget(self.btn_next, alignment=Qt.AlignRight)

        # Connect signals
        self.nama.textChanged.connect(self.validate)
        self.laki.toggled.connect(self.validate)
        self.perempuan.toggled.connect(self.validate)

    def validate(self):
        # Fix: Pastikan nama tidak hanya spasi
        is_nama_valid = len(self.nama.text().strip()) >= 3
        is_gender_valid = self.laki.isChecked() or self.perempuan.isChecked()
        self.btn_next.setEnabled(is_nama_valid and is_gender_valid)

class Step2(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        layout.addWidget(QLabel("Informasi Kontak", objectName="Header"))

        self.email = QLineEdit()
        self.email.setPlaceholderText("contoh@mail.com")
        self.telepon = QLineEdit()
        self.telepon.setPlaceholderText("Min. 10 digit angka")
        self.alamat = QTextEdit()
        self.alamat.setPlaceholderText("Alamat lengkap rumah...")
        self.alamat.setMaximumHeight(80)

        btn_layout = QHBoxLayout()
        self.btn_back = QPushButton("Kembali", objectName="SecondaryBtn")
        self.btn_next = QPushButton("Lanjut", objectName="PrimaryBtn")
        self.btn_next.setEnabled(False)
        
        btn_layout.addWidget(self.btn_back)
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_next)

        layout.addWidget(QLabel("<b>Email:</b>"))
        layout.addWidget(self.email)
        layout.addWidget(QLabel("<b>Nomor Telepon:</b>"))
        layout.addWidget(self.telepon)
        layout.addWidget(QLabel("<b>Alamat Lengkap:</b>"))
        layout.addWidget(self.alamat)
        layout.addStretch()
        layout.addLayout(btn_layout)

        self.email.textChanged.connect(self.validate)
        self.telepon.textChanged.connect(self.validate)
        self.alamat.textChanged.connect(self.validate)

    def validate(self):
        # Fix: Validasi email sederhana & telepon harus angka
        email_ok = "@" in self.email.text() and "." in self.email.text()
        telp_ok = self.telepon.text().isdigit() and len(self.telepon.text()) >= 10
        alamat_ok = len(self.alamat.toPlainText().strip()) > 5
        self.btn_next.setEnabled(email_ok and telp_ok and alamat_ok)

class Step3(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout(self)
        layout.setSpacing(10)

        layout.addWidget(QLabel("Keamanan Akun", objectName="Header"))

        self.username = QLineEdit()
        self.password = QLineEdit()
        self.password.setEchoMode(QLineEdit.Password)
        self.confirm = QLineEdit()
        self.confirm.setEchoMode(QLineEdit.Password)

        btn_layout = QHBoxLayout()
        self.btn_back = QPushButton("Kembali", objectName="SecondaryBtn")
        self.btn_submit = QPushButton("Daftar Sekarang", objectName="PrimaryBtn")
        self.btn_submit.setEnabled(False)

        btn_layout.addWidget(self.btn_back)
        btn_layout.addStretch()
        btn_layout.addWidget(self.btn_submit)

        layout.addWidget(QLabel("<b>Username:</b>"))
        layout.addWidget(self.username)
        layout.addWidget(QLabel("<b>Password:</b>"))
        layout.addWidget(self.password)
        layout.addWidget(QLabel("<b>Konfirmasi Password:</b>"))
        layout.addWidget(self.confirm)
        layout.addStretch()
        layout.addLayout(btn_layout)

        self.username.textChanged.connect(self.validate)
        self.password.textChanged.connect(self.validate)
        self.confirm.textChanged.connect(self.validate)

    def validate(self):
        user_ok = len(self.username.text().strip()) >= 4
        pass_ok = len(self.password.text()) >= 6
        match_ok = self.password.text() == self.confirm.text() and self.password.text() != ""
        self.btn_submit.setEnabled(user_ok and pass_ok and match_ok)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registrasi Member Baru")
        self.setFixedSize(450, 600)
        self.setStyleSheet(STYLE_SHEET)

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(30, 20, 30, 30)

        self.progress_label = QLabel("LANGKAH 1 DARI 3", objectName="StepIndicator")
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, 3)
        self.progress_bar.setValue(1)
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setFixedHeight(8)
        self.progress_bar.setStyleSheet("QProgressBar::chunk { background-color: #0d6efd; border-radius: 4px; }")

        main_layout.addWidget(self.progress_label)
        main_layout.addWidget(self.progress_bar)
        main_layout.addSpacing(15)

        self.stack = QStackedWidget()
        self.step1 = Step1()
        self.step2 = Step2()
        self.step3 = Step3()

        self.stack.addWidget(self.step1)
        self.stack.addWidget(self.step2)
        self.stack.addWidget(self.step3)

        main_layout.addWidget(self.stack)

        # Navigasi
        self.step1.btn_next.clicked.connect(lambda: self.change_step(1))
        self.step2.btn_next.clicked.connect(lambda: self.change_step(2))
        self.step2.btn_back.clicked.connect(lambda: self.change_step(0))
        self.step3.btn_back.clicked.connect(lambda: self.change_step(1))
        self.step3.btn_submit.clicked.connect(self.submit)

    def change_step(self, index):
        self.stack.setCurrentIndex(index)
        self.progress_bar.setValue(index + 1)
        self.progress_label.setText(f"LANGKAH {index + 1} DARI 3")

    def submit(self):
        QMessageBox.information(self, "Success", f"Selamat {self.step1.nama.text()}!\nRegistrasi Anda berhasil.")
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())