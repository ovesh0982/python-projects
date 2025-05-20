# -*- coding: utf-8 -*-

"""This module provides views to manage the contacts table."""

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)
from .model import ContactsModel


class Window(QMainWindow):
    class AddDialog(QDialog):
        """Main Window."""
        def __init__(self, parent=None):
            """Initializer."""
            super().__init__(parent=parent)
            self.setWindowTitle("Add Contact")
            self.layout = QVBoxLayout()
            self.setLayout(self.layout)
            self.data = None

            self.contactModel = ContactsModel()
            self.setupUI()

        def setupUI(self):
            self.clearAllButton = QPushButton("Clear All")
            self.clearAllButton.clicked.connect(self.clearContacts)
            self.deleteButton = QPushButton("Delete")
            self.deleteButton.clicked.connect(self.deleteContact)
            self.addButton = QPushButton("Add...")
            self.addButton.click.connect(self.openAddDialog)
            self.setWindowTitle("RP Contacts")
            self.resize(550, 250)
            self.centralWidget = QWidget()
            self.setCentralWidget(self.centralWidget)
            self.layout = QHBoxLayout()
            self.centralWidget.setLayout(self.layout)
    
    
            """Setup the main window's GUI."""
            # Create line edits for data fields
            self.nameField = QLineEdit()
            self.nameField.setObjectName("Name")
            self.jobField = QLineEdit()
            self.jobField.setObjectName("Job")
            self.emailField = QLineEdit()
            self.emailField.setObjectName("Email")
            # Create the table view widget
            self.table = QTableView()
            self.table.setModel(self.contactModel.model)
            self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.table.resizeColumnsToContents()
            # Create buttons
            self.addButton = QPushButton("Add...")
            self.deleteButton = QPushButton("Delete")
            self.clearAllButton = QPushButton("Clear All")
            # Lay out the GUI
            layout = QVBoxLayout()
            layout.addWidget(self.addButton)
            layout.addWidget(self.deleteButton)
            layout.addStretch()
            layout.addWidget(self.clearAllButton)
            self.layout.addWidget(self.table)
            # Lay out the data fields
            layout = QFormLayout()
            layout.addRow("Name:", self.nameField)
            layout.addRow("Job:", self.jobField)
            layout.addRow("Email:", self.emailField)
            self.layout.addLayout(layout)
            # Add standard buttons to the dialog and connect them
            self.buttonsBox = QDialogButtonBox(self)
            self.buttonsBox.setOrientation(Qt.Horizontal)
            self.buttonsBox.setStandardButtons(
                QDialogButtonBox.Ok | QDialogButtonBox.Cancel
            )
            self.buttonsBox.accepted.connect(self.accept)
            self.buttonsBox.rejected.connect(self.reject)
            self.layout.addWidget(self.buttonsBox)
    

        def openAddDialog(self):
            """Open the Add Contact dialog."""
            dialog = AddDialog(self)
            if dialog.exec() == QDialog.Accepted:
                self.contactsModel.addContact(dialog.data)
                self.table.resizeColumnsToContents()

        def deleteContact(self):
            """Delete the selected contact from the database."""
            row = self.table.currentIndex().row()
            if row < 0:
                return

            messageBox = QMessageBox.warning(
                self,
                "Warning!",
                "Do you want to remove the selected contact?",
                QMessageBox.Ok | QMessageBox.Cancel,
            )

            if messageBox == QMessageBox.Ok:
                self.contactsModel.deleteContact(row)

        
        def clearContacts(self):
            """Remove all contacts from the database."""
            messageBox = QMessageBox.warning(
                self,
                "Warning!",
                "Do you want to remove all your contacts?",
                QMessageBox.Ok | QMessageBox.Cancel,
            )

            if messageBox == QMessageBox.Ok:
                self.contactsModel.clearContacts()



        def accept(self):
            """Accept the data provided through the dialog."""
            self.data = []
            for field in (self.nameField, self.jobField, self.emailField):
                if not field.text():
                    QMessageBox.critical(
                        self,
                        "Error!",
                        f"You must provide a contact's {field.objectName()}",
                    )
                    self.data = None  # Reset .data
                    return

                self.data.append(field.text())
                
                

                super().accept()