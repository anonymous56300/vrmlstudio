import sys
import shutil
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QFileDialog,
    QListWidget, QVBoxLayout, QWidget, QMessageBox
)

class BackupApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Backup Application")
        self.setGeometry(300, 200, 600, 400)
        
        # Main layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        layout = QVBoxLayout(self.central_widget)
        
        # Widgets
        self.file_list = QListWidget()
        self.add_files_button = QPushButton("Add Files")
        self.backup_button = QPushButton("Backup Selected Files")
        
        # Add widgets to layout
        layout.addWidget(self.file_list)
        layout.addWidget(self.add_files_button)
        layout.addWidget(self.backup_button)
        
        # Connect signals to slots
        self.add_files_button.clicked.connect(self.add_files)
        self.backup_button.clicked.connect(self.backup_files)
        
        self.selected_files = []
    
    def add_files(self):
        """Add files to the list."""
        files, _ = QFileDialog.getOpenFileNames(self, "Select Files to Add")
        if files:
            self.selected_files.extend(files)
            self.file_list.addItems(files)
    
    def backup_files(self):
        """Backup selected files to a directory."""
        if not self.selected_files:
            QMessageBox.warning(self, "No Files", "No files selected for backup.")
            return
        
        backup_dir = QFileDialog.getExistingDirectory(self, "Select Backup Directory")
        if not backup_dir:
            return
        
        try:
            for file in self.selected_files:
                shutil.copy(file, backup_dir)
            QMessageBox.information(self, "Success", f"Files backed up to {backup_dir} successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to backup files: {e}")
        finally:
            self.selected_files.clear()
            self.file_list.clear()

# Main execution
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BackupApp()
    window.show()
    sys.exit(app.exec_())
