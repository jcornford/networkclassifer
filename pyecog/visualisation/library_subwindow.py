# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'library_window.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LibraryManagement(object):
    def setupUi(self, LibraryManagement):
        LibraryManagement.setObjectName("LibraryManagement")
        LibraryManagement.resize(1026, 850)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LibraryManagement.sizePolicy().hasHeightForWidth())
        LibraryManagement.setSizePolicy(sizePolicy)
        LibraryManagement.setMinimumSize(QtCore.QSize(790, 833))
        font = QtGui.QFont()
        font.setKerning(True)
        LibraryManagement.setFont(font)
        LibraryManagement.setSizeGripEnabled(False)
        LibraryManagement.setModal(False)
        self.gridLayout_2 = QtWidgets.QGridLayout(LibraryManagement)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_7 = QtWidgets.QLabel(LibraryManagement)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 9, 2, 1, 3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.gridLayout.setHorizontalSpacing(12)
        self.gridLayout.setObjectName("gridLayout")
        self.label_3 = QtWidgets.QLabel(LibraryManagement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 3, 1, 1)
        self.chunk_length = QtWidgets.QLineEdit(LibraryManagement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chunk_length.sizePolicy().hasHeightForWidth())
        self.chunk_length.setSizePolicy(sizePolicy)
        self.chunk_length.setMinimumSize(QtCore.QSize(50, 0))
        self.chunk_length.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.chunk_length.setSizeIncrement(QtCore.QSize(0, 0))
        self.chunk_length.setBaseSize(QtCore.QSize(0, 0))
        self.chunk_length.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.chunk_length.setObjectName("chunk_length")
        self.gridLayout.addWidget(self.chunk_length, 0, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(LibraryManagement)
        self.label_2.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(140, 0))
        self.label_2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 7, 3, 1, 1)
        self.new_library = QtWidgets.QPushButton(LibraryManagement)
        self.new_library.setMinimumSize(QtCore.QSize(200, 0))
        self.new_library.setObjectName("new_library")
        self.gridLayout_2.addWidget(self.new_library, 2, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(LibraryManagement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.line_3.sizePolicy().hasHeightForWidth())
        self.line_3.setSizePolicy(sizePolicy)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_2.addWidget(self.line_3, 12, 0, 1, 5)
        self.label = QtWidgets.QLabel(LibraryManagement)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 5, 0, 1, 5)
        self.progressBar = QtWidgets.QProgressBar(LibraryManagement)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 15, 0, 1, 5)
        self.label_5 = QtWidgets.QLabel(LibraryManagement)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setIndent(-1)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 5)
        self.label_6 = QtWidgets.QLabel(LibraryManagement)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setIndent(-1)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 3, 0, 1, 5)
        self.add_labels = QtWidgets.QPushButton(LibraryManagement)
        self.add_labels.setObjectName("add_labels")
        self.gridLayout_2.addWidget(self.add_labels, 8, 0, 1, 2)
        self.progressBar_lable_above1 = QtWidgets.QLabel(LibraryManagement)
        self.progressBar_lable_above1.setObjectName("progressBar_lable_above1")
        self.gridLayout_2.addWidget(self.progressBar_lable_above1, 14, 0, 1, 5)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(LibraryManagement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.fs_box = QtWidgets.QLineEdit(LibraryManagement)
        self.fs_box.setMaximumSize(QtCore.QSize(50, 16777215))
        self.fs_box.setObjectName("fs_box")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fs_box)
        self.gridLayout_2.addLayout(self.formLayout_2, 2, 4, 1, 1)
        self.overwrite_box = QtWidgets.QCheckBox(LibraryManagement)
        self.overwrite_box.setObjectName("overwrite_box")
        self.gridLayout_2.addWidget(self.overwrite_box, 11, 0, 1, 5)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.annotations_display = QtWidgets.QLineEdit(LibraryManagement)
        self.annotations_display.setMinimumSize(QtCore.QSize(0, 31))
        self.annotations_display.setDragEnabled(True)
        self.annotations_display.setReadOnly(True)
        self.annotations_display.setObjectName("annotations_display")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.annotations_display)
        self.select_annotations = QtWidgets.QPushButton(LibraryManagement)
        self.select_annotations.setMinimumSize(QtCore.QSize(200, 0))
        self.select_annotations.setObjectName("select_annotations")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.select_annotations)
        self.select_h5_folder = QtWidgets.QPushButton(LibraryManagement)
        self.select_h5_folder.setMinimumSize(QtCore.QSize(200, 0))
        self.select_h5_folder.setObjectName("select_h5_folder")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.select_h5_folder)
        self.h5_folder_display = QtWidgets.QLineEdit(LibraryManagement)
        self.h5_folder_display.setMinimumSize(QtCore.QSize(0, 31))
        self.h5_folder_display.setObjectName("h5_folder_display")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.h5_folder_display)
        self.gridLayout_2.addLayout(self.formLayout, 1, 0, 1, 5)
        self.set_library = QtWidgets.QPushButton(LibraryManagement)
        self.set_library.setObjectName("set_library")
        self.gridLayout_2.addWidget(self.set_library, 7, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(LibraryManagement)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 8, 2, 1, 3)
        self.library_path_display = QtWidgets.QLineEdit(LibraryManagement)
        self.library_path_display.setMinimumSize(QtCore.QSize(500, 0))
        self.library_path_display.setReadOnly(True)
        self.library_path_display.setObjectName("library_path_display")
        self.gridLayout_2.addWidget(self.library_path_display, 6, 0, 1, 5)
        self.add_features = QtWidgets.QPushButton(LibraryManagement)
        self.add_features.setObjectName("add_features")
        self.gridLayout_2.addWidget(self.add_features, 9, 0, 1, 2)
        self.clear_library = QtWidgets.QPushButton(LibraryManagement)
        self.clear_library.setObjectName("clear_library")
        self.gridLayout_2.addWidget(self.clear_library, 7, 1, 1, 2)
        self.line_2 = QtWidgets.QFrame(LibraryManagement)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_2.addWidget(self.line_2, 4, 0, 1, 5)
        self.use_peaks = QtWidgets.QCheckBox(LibraryManagement)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.use_peaks.sizePolicy().hasHeightForWidth())
        self.use_peaks.setSizePolicy(sizePolicy)
        self.use_peaks.setObjectName("use_peaks")
        self.gridLayout_2.addWidget(self.use_peaks, 10, 0, 1, 5)
        self.add_to_library = QtWidgets.QPushButton(LibraryManagement)
        self.add_to_library.setMinimumSize(QtCore.QSize(200, 0))
        self.add_to_library.setObjectName("add_to_library")
        self.gridLayout_2.addWidget(self.add_to_library, 2, 1, 1, 2)
        self.progressBar_label_above2 = QtWidgets.QLabel(LibraryManagement)
        self.progressBar_label_above2.setMaximumSize(QtCore.QSize(16777215, 31))
        self.progressBar_label_above2.setText("")
        self.progressBar_label_above2.setObjectName("progressBar_label_above2")
        self.gridLayout_2.addWidget(self.progressBar_label_above2, 13, 2, 1, 1)

        self.retranslateUi(LibraryManagement)
        QtCore.QMetaObject.connectSlotsByName(LibraryManagement)

    def retranslateUi(self, LibraryManagement):
        _translate = QtCore.QCoreApplication.translate
        LibraryManagement.setWindowTitle(_translate("LibraryManagement", "Dialog"))
        self.label_7.setText(_translate("LibraryManagement", "Warning, this will be slow! Labels added automatically."))
        self.label_3.setText(_translate("LibraryManagement", "s"))
        self.chunk_length.setText(_translate("LibraryManagement", "5"))
        self.label_2.setText(_translate("LibraryManagement", "Chunk length"))
        self.new_library.setText(_translate("LibraryManagement", "New library"))
        self.label.setText(_translate("LibraryManagement", "Library path:"))
        self.label_5.setText(_translate("LibraryManagement", "Make Library"))
        self.label_6.setText(_translate("LibraryManagement", "Add Features and Labels"))
        self.add_labels.setText(_translate("LibraryManagement", "Add labels to library"))
        self.progressBar_lable_above1.setText(_translate("LibraryManagement", "Progress"))
        self.label_8.setToolTip(_translate("LibraryManagement", "Sampling Frequency"))
        self.label_8.setText(_translate("LibraryManagement", "Fs (Hz)"))
        self.fs_box.setText(_translate("LibraryManagement", "512"))
        self.overwrite_box.setText(_translate("LibraryManagement", "Overwrite previously calculated features in library"))
        self.select_annotations.setText(_translate("LibraryManagement", "Select annotations"))
        self.select_h5_folder.setText(_translate("LibraryManagement", "Select H5 folder"))
        self.set_library.setText(_translate("LibraryManagement", "Set library"))
        self.label_4.setText(_translate("LibraryManagement", "Quickly add labels for looking at how it chunks up in main gui."))
        self.add_features.setText(_translate("LibraryManagement", "Add features to library"))
        self.clear_library.setText(_translate("LibraryManagement", "Clear library path "))
        self.use_peaks.setText(_translate("LibraryManagement", "Use peaks and valleys features, slower!"))
        self.add_to_library.setText(_translate("LibraryManagement", "Add to library"))
