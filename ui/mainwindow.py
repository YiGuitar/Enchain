# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 725)
        MainWindow.setMouseTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_2.addWidget(self.progressBar)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 25))
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        self.menuLabelling = QtWidgets.QMenu(self.menubar)
        self.menuLabelling.setObjectName("menuLabelling")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        self.menuManagement = QtWidgets.QMenu(self.menubar)
        self.menuManagement.setObjectName("menuManagement")
        self.menuPreprocess = QtWidgets.QMenu(self.menubar)
        self.menuPreprocess.setObjectName("menuPreprocess")
        self.menuImages = QtWidgets.QMenu(self.menuPreprocess)
        self.menuImages.setObjectName("menuImages")
        self.menuVideo = QtWidgets.QMenu(self.menuPreprocess)
        self.menuVideo.setObjectName("menuVideo")
        self.menuDataCleansing = QtWidgets.QMenu(self.menuPreprocess)
        self.menuDataCleansing.setObjectName("menuDataCleansing")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidgetRight = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetRight.setAccessibleName("")
        self.dockWidgetRight.setObjectName("dockWidgetRight")
        self.dockWidgetContentsRight = QtWidgets.QWidget()
        self.dockWidgetContentsRight.setAccessibleName("")
        self.dockWidgetContentsRight.setObjectName("dockWidgetContentsRight")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContentsRight)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.listView = QtWidgets.QListView(self.dockWidgetContentsRight)
        self.listView.setObjectName("listView")
        self.verticalLayout_3.addWidget(self.listView)
        self.dockWidgetRight.setWidget(self.dockWidgetContentsRight)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(2), self.dockWidgetRight)
        self.dockWidgetLeft = QtWidgets.QDockWidget(MainWindow)
        self.dockWidgetLeft.setObjectName("dockWidgetLeft")
        self.dockWidgetContentsLeft = QtWidgets.QWidget()
        self.dockWidgetContentsLeft.setObjectName("dockWidgetContentsLeft")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.dockWidgetContentsLeft)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.treeWidget = QtWidgets.QTreeWidget(self.dockWidgetContentsLeft)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.verticalLayout_4.addWidget(self.treeWidget)
        self.dockWidgetLeft.setWidget(self.dockWidgetContentsLeft)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidgetLeft)
        self.actionAuthor_Info = QtWidgets.QAction(MainWindow)
        self.actionAuthor_Info.setObjectName("actionAuthor_Info")
        self.actionOnline_Help = QtWidgets.QAction(MainWindow)
        self.actionOnline_Help.setObjectName("actionOnline_Help")
        self.actionCheck_Update = QtWidgets.QAction(MainWindow)
        self.actionCheck_Update.setObjectName("actionCheck_Update")
        self.actionOpenImageFolder = QtWidgets.QAction(MainWindow)
        self.actionOpenImageFolder.setObjectName("actionOpenImageFolder")
        self.actionQuit = QtWidgets.QAction(MainWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionOpenVideo = QtWidgets.QAction(MainWindow)
        self.actionOpenVideo.setObjectName("actionOpenVideo")
        self.actionOpenImage = QtWidgets.QAction(MainWindow)
        self.actionOpenImage.setObjectName("actionOpenImage")
        self.actionSaveImage = QtWidgets.QAction(MainWindow)
        self.actionSaveImage.setObjectName("actionSaveImage")
        self.actionCutImage = QtWidgets.QAction(MainWindow)
        self.actionCutImage.setObjectName("actionCutImage")
        self.actionDatasetInput = QtWidgets.QAction(MainWindow)
        self.actionDatasetInput.setObjectName("actionDatasetInput")
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.actionShow_guidance = QtWidgets.QAction(MainWindow)
        self.actionShow_guidance.setObjectName("actionShow_guidance")
        self.actionSaveSliceTo = QtWidgets.QAction(MainWindow)
        self.actionSaveSliceTo.setObjectName("actionSaveSliceTo")
        self.actionSelectSource = QtWidgets.QAction(MainWindow)
        self.actionSelectSource.setObjectName("actionSelectSource")
        self.actionSelectDestination = QtWidgets.QAction(MainWindow)
        self.actionSelectDestination.setObjectName("actionSelectDestination")
        self.actionAssignment = QtWidgets.QAction(MainWindow)
        self.actionAssignment.setObjectName("actionAssignment")
        self.actionAbout_Qt = QtWidgets.QAction(MainWindow)
        self.actionAbout_Qt.setObjectName("actionAbout_Qt")
        self.actionAbout_Enchain = QtWidgets.QAction(MainWindow)
        self.actionAbout_Enchain.setObjectName("actionAbout_Enchain")
        self.actionCreateVOCFolder = QtWidgets.QAction(MainWindow)
        self.actionCreateVOCFolder.setObjectName("actionCreateVOCFolder")
        self.actionOpenVideoFolder = QtWidgets.QAction(MainWindow)
        self.actionOpenVideoFolder.setObjectName("actionOpenVideoFolder")
        self.actionSaveSliceSetTo = QtWidgets.QAction(MainWindow)
        self.actionSaveSliceSetTo.setObjectName("actionSaveSliceSetTo")
        self.actionConvertSliceToVideo = QtWidgets.QAction(MainWindow)
        self.actionConvertSliceToVideo.setObjectName("actionConvertSliceToVideo")
        self.menuHelp.addAction(self.actionOnline_Help)
        self.menuHelp.addAction(self.actionAuthor_Info)
        self.menuHelp.addAction(self.actionCheck_Update)
        self.menuHelp.addAction(self.actionAbout_Enchain)
        self.menuHelp.addAction(self.actionAbout_Qt)
        self.menuLabelling.addAction(self.actionShow_guidance)
        self.menuTools.addAction(self.actionCreateVOCFolder)
        self.menuTools.addAction(self.actionCutImage)
        self.menuTools.addAction(self.actionConvertSliceToVideo)
        self.menuManagement.addAction(self.actionDatasetInput)
        self.menuImages.addAction(self.actionOpenImageFolder)
        self.menuImages.addAction(self.actionOpenImage)
        self.menuImages.addAction(self.actionSaveImage)
        self.menuVideo.addAction(self.actionOpenVideo)
        self.menuVideo.addAction(self.actionSaveSliceTo)
        self.menuVideo.addSeparator()
        self.menuVideo.addAction(self.actionOpenVideoFolder)
        self.menuVideo.addAction(self.actionSaveSliceSetTo)
        self.menuVideo.addSeparator()
        self.menuDataCleansing.addAction(self.actionSelectSource)
        self.menuDataCleansing.addAction(self.actionSelectDestination)
        self.menuDataCleansing.addSeparator()
        self.menuPreprocess.addAction(self.menuVideo.menuAction())
        self.menuPreprocess.addAction(self.menuImages.menuAction())
        self.menuPreprocess.addSeparator()
        self.menuPreprocess.addAction(self.menuDataCleansing.menuAction())
        self.menuPreprocess.addSeparator()
        self.menuPreprocess.addAction(self.actionAssignment)
        self.menuPreprocess.addSeparator()
        self.menuPreprocess.addAction(self.actionClose)
        self.menuPreprocess.addAction(self.actionQuit)
        self.menubar.addAction(self.menuPreprocess.menuAction())
        self.menubar.addAction(self.menuLabelling.menuAction())
        self.menubar.addAction(self.menuManagement.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.treeWidget, self.listView)
        MainWindow.setTabOrder(self.listView, self.graphicsView)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Enchain"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.menuLabelling.setTitle(_translate("MainWindow", "Labelling"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.menuManagement.setTitle(_translate("MainWindow", "Management"))
        self.menuPreprocess.setTitle(_translate("MainWindow", "Preprocess"))
        self.menuImages.setTitle(_translate("MainWindow", "Images"))
        self.menuVideo.setTitle(_translate("MainWindow", "Video"))
        self.menuDataCleansing.setTitle(_translate("MainWindow", "DataCleansing"))
        self.actionAuthor_Info.setText(_translate("MainWindow", "Connect Author"))
        self.actionOnline_Help.setText(_translate("MainWindow", "Online Help"))
        self.actionCheck_Update.setText(_translate("MainWindow", "Check Update"))
        self.actionOpenImageFolder.setText(_translate("MainWindow", "OpenImageFolder"))
        self.actionQuit.setText(_translate("MainWindow", "Quit"))
        self.actionOpenVideo.setText(_translate("MainWindow", "OpenVideo"))
        self.actionOpenImage.setText(_translate("MainWindow", "OpenImage"))
        self.actionSaveImage.setText(_translate("MainWindow", "SaveImage"))
        self.actionCutImage.setText(_translate("MainWindow", "CutImage"))
        self.actionDatasetInput.setText(_translate("MainWindow", "DatasetManage"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionShow_guidance.setText(_translate("MainWindow", "Guidance Wiki"))
        self.actionSaveSliceTo.setText(_translate("MainWindow", "SaveSliceTo"))
        self.actionSelectSource.setText(_translate("MainWindow", "SelectSource"))
        self.actionSelectDestination.setText(_translate("MainWindow", "SelectDestination"))
        self.actionAssignment.setText(_translate("MainWindow", "Assignment"))
        self.actionAbout_Qt.setText(_translate("MainWindow", "About Qt"))
        self.actionAbout_Enchain.setText(_translate("MainWindow", "About Enchain"))
        self.actionCreateVOCFolder.setText(_translate("MainWindow", "CreateVOCFolder"))
        self.actionOpenVideoFolder.setText(_translate("MainWindow", "OpenVideoFolder"))
        self.actionSaveSliceSetTo.setText(_translate("MainWindow", "SaveSliceSetTo"))
        self.actionConvertSliceToVideo.setText(_translate("MainWindow", "ConvertSliceToVideo"))

