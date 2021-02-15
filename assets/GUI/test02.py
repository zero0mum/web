from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile



class info:
    def __init__(self):
        self.ui = QUiLoader().load('GUI/test02.ui')
        # self.ui.listWidget.addItem(self.title)
        self.ui.listWidget.addItems(['【1】百年漫画网: https://www.bnmanhua.com/page/all.html','【2】漫画呗: https://www.manhuadai.com/','【3】古风漫画网: https://www.gufengmh8.com/'])
        self.ui.listWidget.itemClicked.connect(self.ClearShow)

    def Clear(self):
        self.ui.listWidget.clear()
    def ClearShow(self):
        selected_comic = self.ui.listWidget.currentItem().text()
        self.Clear()
        self.ui.listWidget.addItem(selected_comic)
        self.ui.lineEdit.setPlaceholderText('请在此输入想看的漫画名称并回车！')
        Comic_Name = self.ui.lineEdit.returnPressed.connect()
    
    def search(self):
        self.Clear()

app = QApplication([])
info = info()
info.ui.show()
app.exec_()
# app = QApplication([])
# info().ui.show()
# app.exec_()