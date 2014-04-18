# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'desktop_window.ui'
#
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from tank.platform.qt import QtCore, QtGui

class Ui_DesktopWindow(object):
    def setupUi(self, DesktopWindow):
        DesktopWindow.setObjectName("DesktopWindow")
        DesktopWindow.resize(460, 780)
        DesktopWindow.setMinimumSize(QtCore.QSize(460, 780))
        DesktopWindow.setMaximumSize(QtCore.QSize(450, 780))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/res/default_systray_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DesktopWindow.setWindowIcon(icon)
        DesktopWindow.setStyleSheet("")
        DesktopWindow.setDockNestingEnabled(False)
        self.center = QtGui.QWidget(DesktopWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.center.sizePolicy().hasHeightForWidth())
        self.center.setSizePolicy(sizePolicy)
        self.center.setObjectName("center")
        self.border_layout = QtGui.QVBoxLayout(self.center)
        self.border_layout.setSpacing(0)
        self.border_layout.setContentsMargins(0, 0, 0, 0)
        self.border_layout.setObjectName("border_layout")
        self.header = QtGui.QFrame(self.center)
        self.header.setFrameShape(QtGui.QFrame.NoFrame)
        self.header.setFrameShadow(QtGui.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.header)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setContentsMargins(30, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.apps_button = QtGui.QPushButton(self.header)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apps_button.sizePolicy().hasHeightForWidth())
        self.apps_button.setSizePolicy(sizePolicy)
        self.apps_button.setMinimumSize(QtCore.QSize(0, 0))
        self.apps_button.setMouseTracking(True)
        self.apps_button.setFlat(True)
        self.apps_button.setObjectName("apps_button")
        self.horizontalLayout_2.addWidget(self.apps_button)
        self.inbox_button = QtGui.QPushButton(self.header)
        self.inbox_button.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.inbox_button.sizePolicy().hasHeightForWidth())
        self.inbox_button.setSizePolicy(sizePolicy)
        self.inbox_button.setMinimumSize(QtCore.QSize(0, 0))
        self.inbox_button.setMouseTracking(True)
        self.inbox_button.setFlat(True)
        self.inbox_button.setObjectName("inbox_button")
        self.horizontalLayout_2.addWidget(self.inbox_button)
        self.my_tasks_button = QtGui.QPushButton(self.header)
        self.my_tasks_button.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.my_tasks_button.sizePolicy().hasHeightForWidth())
        self.my_tasks_button.setSizePolicy(sizePolicy)
        self.my_tasks_button.setMinimumSize(QtCore.QSize(0, 0))
        self.my_tasks_button.setMouseTracking(True)
        self.my_tasks_button.setFlat(True)
        self.my_tasks_button.setObjectName("my_tasks_button")
        self.horizontalLayout_2.addWidget(self.my_tasks_button)
        self.versions_button = QtGui.QPushButton(self.header)
        self.versions_button.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versions_button.sizePolicy().hasHeightForWidth())
        self.versions_button.setSizePolicy(sizePolicy)
        self.versions_button.setMinimumSize(QtCore.QSize(0, 0))
        self.versions_button.setMouseTracking(True)
        self.versions_button.setFlat(True)
        self.versions_button.setObjectName("versions_button")
        self.horizontalLayout_2.addWidget(self.versions_button)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.border_layout.addWidget(self.header)
        self.stack = QtGui.QStackedWidget(self.center)
        self.stack.setObjectName("stack")
        self.project_browser_page = QtGui.QWidget()
        self.project_browser_page.setObjectName("project_browser_page")
        self.verticalLayout = QtGui.QVBoxLayout(self.project_browser_page)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.subheader = QtGui.QFrame(self.project_browser_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.subheader.sizePolicy().hasHeightForWidth())
        self.subheader.setSizePolicy(sizePolicy)
        self.subheader.setMaximumSize(QtCore.QSize(16777215, 60))
        self.subheader.setStyleSheet("")
        self.subheader.setFrameShape(QtGui.QFrame.NoFrame)
        self.subheader.setFrameShadow(QtGui.QFrame.Plain)
        self.subheader.setLineWidth(1)
        self.subheader.setMidLineWidth(0)
        self.subheader.setObjectName("subheader")
        self.horizontalLayout = QtGui.QHBoxLayout(self.subheader)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setContentsMargins(20, 15, 20, 15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.subheader_label = QtGui.QLabel(self.subheader)
        font = QtGui.QFont()
        self.subheader_label.setFont(font)
        self.subheader_label.setMouseTracking(True)
        self.subheader_label.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.subheader_label.setObjectName("subheader_label")
        self.horizontalLayout.addWidget(self.subheader_label)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.project_button = QtGui.QPushButton(self.subheader)
        self.project_button.setFlat(True)
        self.project_button.setObjectName("project_button")
        self.horizontalLayout.addWidget(self.project_button)
        self.search_frame = QtGui.QFrame(self.subheader)
        self.search_frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.search_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.search_frame.setProperty("collapsed", False)
        self.search_frame.setObjectName("search_frame")
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.search_frame)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.search_magnifier = QtGui.QLabel(self.search_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_magnifier.sizePolicy().hasHeightForWidth())
        self.search_magnifier.setSizePolicy(sizePolicy)
        self.search_magnifier.setMaximumSize(QtCore.QSize(17, 17))
        self.search_magnifier.setText("")
        self.search_magnifier.setPixmap(QtGui.QPixmap(":/res/search.png"))
        self.search_magnifier.setScaledContents(True)
        self.search_magnifier.setObjectName("search_magnifier")
        self.horizontalLayout_6.addWidget(self.search_magnifier)
        self.search_text = QtGui.QLineEdit(self.search_frame)
        self.search_text.setObjectName("search_text")
        self.horizontalLayout_6.addWidget(self.search_text)
        self.search_button = QtGui.QPushButton(self.search_frame)
        self.search_button.setMaximumSize(QtCore.QSize(17, 17))
        self.search_button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/res/x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon1)
        self.search_button.setIconSize(QtCore.QSize(17, 17))
        self.search_button.setFlat(True)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout_6.addWidget(self.search_button)
        self.horizontalLayout.addWidget(self.search_frame)
        self.verticalLayout.addWidget(self.subheader)
        self.projects = QtGui.QListView(self.project_browser_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.projects.sizePolicy().hasHeightForWidth())
        self.projects.setSizePolicy(sizePolicy)
        self.projects.setMaximumSize(QtCore.QSize(460, 16777215))
        self.projects.setMouseTracking(True)
        self.projects.setFrameShape(QtGui.QFrame.NoFrame)
        self.projects.setFrameShadow(QtGui.QFrame.Plain)
        self.projects.setLineWidth(0)
        self.projects.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.projects.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.projects.setProperty("showDropIndicator", False)
        self.projects.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.projects.setMovement(QtGui.QListView.Static)
        self.projects.setFlow(QtGui.QListView.LeftToRight)
        self.projects.setProperty("isWrapping", True)
        self.projects.setResizeMode(QtGui.QListView.Fixed)
        self.projects.setLayoutMode(QtGui.QListView.SinglePass)
        self.projects.setSpacing(16)
        self.projects.setViewMode(QtGui.QListView.IconMode)
        self.projects.setUniformItemSizes(True)
        self.projects.setSelectionRectVisible(False)
        self.projects.setObjectName("projects")
        self.verticalLayout.addWidget(self.projects)
        self.stack.addWidget(self.project_browser_page)
        self.project_page = QtGui.QWidget()
        self.project_page.setObjectName("project_page")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.project_page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.recents_shelf = QtGui.QFrame(self.project_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recents_shelf.sizePolicy().hasHeightForWidth())
        self.recents_shelf.setSizePolicy(sizePolicy)
        self.recents_shelf.setMaximumSize(QtCore.QSize(16777215, 120))
        self.recents_shelf.setFrameShape(QtGui.QFrame.NoFrame)
        self.recents_shelf.setFrameShadow(QtGui.QFrame.Plain)
        self.recents_shelf.setLineWidth(0)
        self.recents_shelf.setObjectName("recents_shelf")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.recents_shelf)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setContentsMargins(20, 20, 5, 5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.recent_projects = QtGui.QListView(self.recents_shelf)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recent_projects.sizePolicy().hasHeightForWidth())
        self.recent_projects.setSizePolicy(sizePolicy)
        self.recent_projects.setFrameShape(QtGui.QFrame.NoFrame)
        self.recent_projects.setFrameShadow(QtGui.QFrame.Plain)
        self.recent_projects.setLineWidth(0)
        self.recent_projects.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.recent_projects.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.recent_projects.setProperty("showDropIndicator", False)
        self.recent_projects.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self.recent_projects.setProperty("isWrapping", False)
        self.recent_projects.setResizeMode(QtGui.QListView.Fixed)
        self.recent_projects.setLayoutMode(QtGui.QListView.SinglePass)
        self.recent_projects.setSpacing(10)
        self.recent_projects.setGridSize(QtCore.QSize(100, 140))
        self.recent_projects.setViewMode(QtGui.QListView.IconMode)
        self.recent_projects.setUniformItemSizes(True)
        self.recent_projects.setWordWrap(True)
        self.recent_projects.setObjectName("recent_projects")
        self.horizontalLayout_5.addWidget(self.recent_projects)
        self.all_projects_button = QtGui.QPushButton(self.recents_shelf)
        self.all_projects_button.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/res/ellipses.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.all_projects_button.setIcon(icon2)
        self.all_projects_button.setIconSize(QtCore.QSize(60, 60))
        self.all_projects_button.setFlat(True)
        self.all_projects_button.setObjectName("all_projects_button")
        self.horizontalLayout_5.addWidget(self.all_projects_button)
        self.verticalLayout_2.addWidget(self.recents_shelf)
        self.project_subheader = QtGui.QFrame(self.project_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_subheader.sizePolicy().hasHeightForWidth())
        self.project_subheader.setSizePolicy(sizePolicy)
        self.project_subheader.setMaximumSize(QtCore.QSize(16777215, 60))
        self.project_subheader.setStyleSheet("")
        self.project_subheader.setFrameShape(QtGui.QFrame.NoFrame)
        self.project_subheader.setFrameShadow(QtGui.QFrame.Plain)
        self.project_subheader.setLineWidth(1)
        self.project_subheader.setMidLineWidth(0)
        self.project_subheader.setObjectName("project_subheader")
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.project_subheader)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setContentsMargins(20, 0, 20, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.project_arrow = QtGui.QPushButton(self.project_subheader)
        self.project_arrow.setMaximumSize(QtCore.QSize(30, 62))
        self.project_arrow.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/res/down_carat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.project_arrow.setIcon(icon3)
        self.project_arrow.setIconSize(QtCore.QSize(20, 20))
        self.project_arrow.setFlat(True)
        self.project_arrow.setObjectName("project_arrow")
        self.horizontalLayout_4.addWidget(self.project_arrow)
        self.project_icon = QtGui.QPushButton(self.project_subheader)
        self.project_icon.setMaximumSize(QtCore.QSize(42, 62))
        self.project_icon.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/res/missing_thumbnail_project.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.project_icon.setIcon(icon4)
        self.project_icon.setIconSize(QtCore.QSize(32, 32))
        self.project_icon.setFlat(True)
        self.project_icon.setObjectName("project_icon")
        self.horizontalLayout_4.addWidget(self.project_icon)
        self.project_name = QtGui.QPushButton(self.project_subheader)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_name.sizePolicy().hasHeightForWidth())
        self.project_name.setSizePolicy(sizePolicy)
        self.project_name.setFlat(True)
        self.project_name.setObjectName("project_name")
        self.horizontalLayout_4.addWidget(self.project_name)
        self.project_menu = QtGui.QPushButton(self.project_subheader)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_menu.sizePolicy().hasHeightForWidth())
        self.project_menu.setSizePolicy(sizePolicy)
        self.project_menu.setMaximumSize(QtCore.QSize(35, 35))
        self.project_menu.setText("")
        self.project_menu.setFlat(True)
        self.project_menu.setObjectName("project_menu")
        self.horizontalLayout_4.addWidget(self.project_menu)
        self.verticalLayout_2.addWidget(self.project_subheader)
        self.project_commands = ProjectCommandsWidget(self.project_page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.project_commands.sizePolicy().hasHeightForWidth())
        self.project_commands.setSizePolicy(sizePolicy)
        self.project_commands.setStyleSheet("")
        self.project_commands.setObjectName("project_commands")
        self.verticalLayout_2.addWidget(self.project_commands)
        self.stack.addWidget(self.project_page)
        self.border_layout.addWidget(self.stack)
        self.footer = QtGui.QFrame(self.center)
        self.footer.setFrameShape(QtGui.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtGui.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.footer)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setContentsMargins(5, 0, 5, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.shotgun_frame = QtGui.QFrame(self.footer)
        self.shotgun_frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.shotgun_frame.setFrameShadow(QtGui.QFrame.Raised)
        self.shotgun_frame.setLineWidth(0)
        self.shotgun_frame.setObjectName("shotgun_frame")
        self.horizontalLayout_7 = QtGui.QHBoxLayout(self.shotgun_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.shotgun_button = QtGui.QPushButton(self.shotgun_frame)
        self.shotgun_button.setMaximumSize(QtCore.QSize(122, 16))
        self.shotgun_button.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/res/shotgun_logo_light_medium.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shotgun_button.setIcon(icon5)
        self.shotgun_button.setIconSize(QtCore.QSize(122, 16))
        self.shotgun_button.setFlat(True)
        self.shotgun_button.setObjectName("shotgun_button")
        self.horizontalLayout_7.addWidget(self.shotgun_button)
        self.shotgun_arrow = QtGui.QPushButton(self.shotgun_frame)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.shotgun_arrow.sizePolicy().hasHeightForWidth())
        self.shotgun_arrow.setSizePolicy(sizePolicy)
        self.shotgun_arrow.setMaximumSize(QtCore.QSize(20, 20))
        self.shotgun_arrow.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/res/up_right_arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.shotgun_arrow.setIcon(icon6)
        self.shotgun_arrow.setFlat(True)
        self.shotgun_arrow.setObjectName("shotgun_arrow")
        self.horizontalLayout_7.addWidget(self.shotgun_arrow)
        self.horizontalLayout_3.addWidget(self.shotgun_frame)
        spacerItem2 = QtGui.QSpacerItem(173, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.user_button = QtGui.QPushButton(self.footer)
        self.user_button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/res/default_user_thumb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_button.setIcon(icon7)
        self.user_button.setIconSize(QtCore.QSize(30, 30))
        self.user_button.setFlat(True)
        self.user_button.setObjectName("user_button")
        self.horizontalLayout_3.addWidget(self.user_button)
        self.border_layout.addWidget(self.footer)
        DesktopWindow.setCentralWidget(self.center)
        self.actionQuit = QtGui.QAction(DesktopWindow)
        self.actionQuit.setObjectName("actionQuit")
        self.actionPin_to_Menu = QtGui.QAction(DesktopWindow)
        self.actionPin_to_Menu.setObjectName("actionPin_to_Menu")
        self.actionSign_Out = QtGui.QAction(DesktopWindow)
        self.actionSign_Out.setObjectName("actionSign_Out")
        self.actionKeep_on_Top = QtGui.QAction(DesktopWindow)
        self.actionKeep_on_Top.setCheckable(True)
        self.actionKeep_on_Top.setObjectName("actionKeep_on_Top")
        self.actionAll_Projects = QtGui.QAction(DesktopWindow)
        self.actionAll_Projects.setCheckable(True)
        self.actionAll_Projects.setObjectName("actionAll_Projects")
        self.actionFavorite_Projects = QtGui.QAction(DesktopWindow)
        self.actionFavorite_Projects.setCheckable(True)
        self.actionFavorite_Projects.setObjectName("actionFavorite_Projects")
        self.actionRecent_Projects = QtGui.QAction(DesktopWindow)
        self.actionRecent_Projects.setCheckable(True)
        self.actionRecent_Projects.setObjectName("actionRecent_Projects")
        self.actionProject_Filesystem_Folder = QtGui.QAction(DesktopWindow)
        self.actionProject_Filesystem_Folder.setObjectName("actionProject_Filesystem_Folder")

        self.retranslateUi(DesktopWindow)
        self.stack.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(DesktopWindow)

    def retranslateUi(self, DesktopWindow):
        DesktopWindow.setWindowTitle(QtGui.QApplication.translate("DesktopWindow", "Shotgun", None, QtGui.QApplication.UnicodeUTF8))
        self.apps_button.setText(QtGui.QApplication.translate("DesktopWindow", "Apps", None, QtGui.QApplication.UnicodeUTF8))
        self.inbox_button.setText(QtGui.QApplication.translate("DesktopWindow", "Inbox", None, QtGui.QApplication.UnicodeUTF8))
        self.my_tasks_button.setText(QtGui.QApplication.translate("DesktopWindow", "My Tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.versions_button.setText(QtGui.QApplication.translate("DesktopWindow", "Versions", None, QtGui.QApplication.UnicodeUTF8))
        self.subheader_label.setText(QtGui.QApplication.translate("DesktopWindow", "<big>PROJECTS</big>", None, QtGui.QApplication.UnicodeUTF8))
        self.project_button.setText(QtGui.QApplication.translate("DesktopWindow", "Recent", None, QtGui.QApplication.UnicodeUTF8))
        self.search_frame.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Filter Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.search_magnifier.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Filter Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.search_text.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Filter Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.search_text.setPlaceholderText(QtGui.QApplication.translate("DesktopWindow", "Search Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.search_button.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Filter Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.all_projects_button.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Back to Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.project_name.setText(QtGui.QApplication.translate("DesktopWindow", "Project", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_frame.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Open in Shotgun", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_button.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Open in Shotgun", None, QtGui.QApplication.UnicodeUTF8))
        self.shotgun_arrow.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Open in Shotgun", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("DesktopWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setToolTip(QtGui.QApplication.translate("DesktopWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setShortcut(QtGui.QApplication.translate("DesktopWindow", "Meta+Q", None, QtGui.QApplication.UnicodeUTF8))
        self.actionPin_to_Menu.setText(QtGui.QApplication.translate("DesktopWindow", "Pin to Menu", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSign_Out.setText(QtGui.QApplication.translate("DesktopWindow", "Sign Out", None, QtGui.QApplication.UnicodeUTF8))
        self.actionKeep_on_Top.setText(QtGui.QApplication.translate("DesktopWindow", "Keep on Top", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAll_Projects.setText(QtGui.QApplication.translate("DesktopWindow", "All Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFavorite_Projects.setText(QtGui.QApplication.translate("DesktopWindow", "Favorite Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRecent_Projects.setText(QtGui.QApplication.translate("DesktopWindow", "Recent Projects", None, QtGui.QApplication.UnicodeUTF8))
        self.actionProject_Filesystem_Folder.setText(QtGui.QApplication.translate("DesktopWindow", "Project Filesystem Folder", None, QtGui.QApplication.UnicodeUTF8))

from ..project_commands_widget import ProjectCommandsWidget
from . import resources_rc
