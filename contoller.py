import cv2
from src.plugin_interface import PluginInterface
from PyQt6.QtWidgets import QWidget
from .ui_main import Ui_Form


class Controller(QWidget):
    def __init__(self, model):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.model = model
        self.set_stylesheet()
        # self.connect_to_button()

    def set_stylesheet(self):
        # label title
        self.ui.title_3.setStyleSheet(self.model.style_label_title())
        self.ui.title_4.setStyleSheet(self.model.style_label_title())
        self.ui.title_5.setStyleSheet(self.model.style_label_title())
        self.ui.title_6.setStyleSheet(self.model.style_label_title())
        self.ui.title_7.setStyleSheet(self.model.style_label_title())
        self.ui.title_8.setStyleSheet(self.model.style_label_title())
        self.ui.eventLog.setStyleSheet(self.model.style_label_title())
        self.ui.interfaceSts.setStyleSheet(self.model.style_label_title())

        #  label
        self.ui.dateTime.setStyleSheet(self.model.style_label())
        self.ui.dateTimeVal.setStyleSheet(self.model.style_label())
        self.ui.originTpr.setStyleSheet(self.model.style_label())
        self.ui.destinationTpr.setStyleSheet(self.model.style_label())

        # scroll area
        self.ui.scrollArea.setStyleSheet(self.model.style_scroll_area())
        self.ui.verticalScrollBar.setStyleSheet(self.model.style_scroll_area())

        # button
        self.ui.resetStsBtn_8.setStyleSheet(self.model.style_pushbutton())
        self.ui.requestRouteBtn_8.setStyleSheet(self.model.style_pushbutton())
        self.ui.dispatchBtn_8.setStyleSheet(self.model.style_pushbutton())

        self.ui.resetStsBtn_3.setStyleSheet(self.model.style_pushbutton())
        self.ui.requestRouteBtn_3.setStyleSheet(self.model.style_pushbutton())
        self.ui.dispatchBtn_3.setStyleSheet(self.model.style_pushbutton())

        self.ui.resetStsBtn_4.setStyleSheet(self.model.style_pushbutton())
        self.ui.requestRouteBtn_4.setStyleSheet(self.model.style_pushbutton())
        self.ui.dispatchBtn_4.setStyleSheet(self.model.style_pushbutton())

        self.ui.resetStsBtn_5.setStyleSheet(self.model.style_pushbutton())
        self.ui.requestRouteBtn_5.setStyleSheet(self.model.style_pushbutton())
        self.ui.dispatchBtn_5.setStyleSheet(self.model.style_pushbutton())

        self.ui.resetStsBtn_6.setStyleSheet(self.model.style_pushbutton())
        self.ui.requestRouteBtn_6.setStyleSheet(self.model.style_pushbutton())
        self.ui.dispatchBtn_6.setStyleSheet(self.model.style_pushbutton())

        self.ui.resetStsBtn_7.setStyleSheet(self.model.style_pushbutton())
        self.ui.requestRouteBtn_7.setStyleSheet(self.model.style_pushbutton())
        self.ui.dispatchBtn_7.setStyleSheet(self.model.style_pushbutton())

        # self.ui.openLogFolderBtn.setStyleSheet(self.model.style_pushbutton())

        # self.ui.jl20.setStyleSheet(self.model.style_pushbutton())
        # self.ui.j22a.setStyleSheet(self.model.style_pushbutton())
        # self.ui.j22b.setStyleSheet(self.model.style_pushbutton())
        # self.ui.j24.setStyleSheet(self.model.style_pushbutton())

        # self.ui.jl10.setStyleSheet(self.model.style_pushbutton())
        # self.ui.j12a.setStyleSheet(self.model.style_pushbutton())
        # self.ui.j12b.setStyleSheet(self.model.style_pushbutton())
        # self.ui.j14.setStyleSheet(self.model.style_pushbutton())

        # self.ui.x20.setStyleSheet(self.model.style_pushbutton())
        # self.ui.j22aDes.setStyleSheet(self.model.style_pushbutton())
        # self.ui.j22bDes.setStyleSheet(self.model.style_pushbutton())
        # self.ui.j24Des.setStyleSheet(self.model.style_pushbutton())

        # self.ui.x10.setStyleSheet(self.model.style_pushbutton())
        # self.ui.j12aDes.setStyleSheet(self.model.style_pushbutton())
        # self.ui.j12bDes.setStyleSheet(self.model.style_pushbutton())
        # self.ui.j14Des.setStyleSheet(self.model.style_pushbutton())

        # frame object => frame yg tunggal(local frame)
        self.ui.gridFrame_4.setStyleSheet(self.model.style_frame_object())
        self.ui.gridFrame_5.setStyleSheet(self.model.style_frame_object())
        self.ui.gridFrame_6.setStyleSheet(self.model.style_frame_object())
        self.ui.gridFrame_7.setStyleSheet(self.model.style_frame_object())
        self.ui.gridFrame_8.setStyleSheet(self.model.style_frame_object())
        self.ui.gridFrame_9.setStyleSheet(self.model.style_frame_object())

        # frame main => frame yg sebagai container atau box(global frame)
        self.ui.frame.setStyleSheet(self.model.style_frame_main())
        self.ui.frame_2.setStyleSheet(self.model.style_frame_main())
        self.ui.frame_3.setStyleSheet(self.model.style_frame_main())
        self.ui.frame_4.setStyleSheet(self.model.style_frame_main())

        # line
        self.ui.line.setStyleSheet(self.model.style_line())
        self.ui.line_2.setStyleSheet(self.model.style_line())
        self.ui.line_3.setStyleSheet(self.model.style_line())
        self.ui.line_4.setStyleSheet(self.model.style_line())

    # def connect_to_button(self):
    #     self.ui.open_file.clicked.connect(self.onclick_open)
    #
    #     # setting configuration recenter
    #     self.ui.doubleSpinBox.valueChanged.connect(self.recenter_image)
    #     self.ui.doubleSpinBox_2.valueChanged.connect(self.recenter_image)
    #     self.ui.doubleSpinBox_3.valueChanged.connect(self.recenter_image)

    # def onclick_open(self):
    #     cam_type, media_source, params_name = self.model.select_media_source()
    #     if cam_type:
    #         if params_name:
    #             self.moildev = self.model.connect_to_moildev(parameter_name=params_name)
    #         self.image_ori = cv2.imread(media_source)
    #         self.image = self.image_ori.copy()
    #         self.show_to_ui()
    #         self.recenter_image()

    # def show_to_ui(self):
    #     map_x, map_y = self.moildev.maps_anypoint_mode2(0, 0, 0, 4)
    #     draw_img = self.model.draw_polygon(self.image, map_x, map_y)
    #     self.model.show_image_to_label(self.ui.label_5, draw_img, 900)

    # def recenter_image(self):
    #     alpha_max = self.ui.doubleSpinBox.value()
    #     ic_alpha = self.ui.doubleSpinBox_2.value()
    #     ic_beta = self.ui.doubleSpinBox_3.value()
    #
    #     self.remap = self.moildev.recenter(self.image, alpha_max, ic_alpha, ic_beta)
    #     self.model.show_image_to_label(self.ui.label_6, self.remap, 900)

class FtdcPtLen(PluginInterface):
    def __init__(self):
        super().__init__()
        self.widget = None
        self.description = "This is a plugins application"

    def set_plugin_widget(self, model):
        self.widget = Controller(model)
        return self.widget

    def set_icon_apps(self):
        return "icon.png"

    def change_stylesheet(self):
        self.widget.set_stylesheet()

