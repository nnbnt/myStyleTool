try: 
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui 

ROOT_RESOURCE_DIR = 'C:/Users/Nennebi/Documents/MAYA/PROJECTS/2024/scripts/myStyleTool/reaources'

class MyStyleToolDialog(QtWidgets.QDialog):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setWindowTitle('My Tool')
		self.resize(300,100)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet('background-color: #2C3532;')
		#self.setStyleSheet('background-color: qlineargradient(x1:2, y0:0, x:0:0, y0:0, stop:0 #F2B263, stop:1 #F2E8DF);')

		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/image/Smile.png")
		scaled_pixmap = self.imagePixmap.scaled(
			QtCore.QSize(30,30),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation

			)

		self.imageLabel.setPixmap(scaled_pixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)


		self.imageLabel.setPixmap(self.imagePixmap)
		self.mainLayout.addWidget(self.imageLabel)

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)
		self.nameLabel = QtWidgets.QLabel('Name:')
		self.nameLabel.setStyleSheet(
			'''
				QLabel {
					background-color: #3E848C;
					color: red;
					
				}


			'''

		)
		self.nameLineEdit = QtWidgets.QLineEdit()

		self.nameLineEdit.setStyleSheet(
			'''
				QLineEdit {
					background-color: #3E848C;
					
				}


			'''

		)


		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)




		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		self.createButton = QtWidgets.QPushButton('Create')
		self.createButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #3E848C;
					color: white;
					border-radius: 10px;
					font-size: 16px;
					padding: 4px;
					font-family: Papyrus;
					font-weight: bold;
				}

				QPushButton:hover {
					background-color: #027373;

				}

				QPushButton:pressed {
					background-color: #F2668B;
				}


			'''

		)
		self.cancelButton = QtWidgets.QPushButton('Cancel')
		self.cancelButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #3E848C;
					color: white;
					border-radius: 10px;
					font-size: 16px;
					padding: 4px;
					font-family: Papyrus;
					font-weight: bold;
				}

				QPushButton:hover {
					background-color: #027373;

				}

				QPushButton:pressed {
					background-color: #F2668B;
				}
			'''

		)
		self.buttonLayout.addWidget(self.createButton)
		self.buttonLayout.addWidget(self.cancelButton)

		self.mainLayout.addStretch()

def run():
	global ui
	try:
		ui.close()
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)
	ui = MyStyleToolDialog(parent=ptr)
	ui.show()