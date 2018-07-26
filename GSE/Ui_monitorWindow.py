# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\andre\Documents\BruinSpace\Rapid\Rapid-Blue-Dawn-Ground-Testing\GSE\monitorWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Monitor(object):
    def setupUi(self, Monitor):
        Monitor.setObjectName("Monitor")
        Monitor.resize(1182, 755)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/MainLogo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Monitor.setWindowIcon(icon)
        self.verticalLayoutWidget = QtWidgets.QWidget(Monitor)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 1161, 741))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.monitor_wrapper = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.monitor_wrapper.setContentsMargins(0, 0, 0, 0)
        self.monitor_wrapper.setObjectName("monitor_wrapper")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bd_groupbox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.bd_groupbox.setObjectName("bd_groupbox")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.bd_groupbox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 20, 561, 461))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.voltage_name = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.voltage_name.setObjectName("voltage_name")
        self.gridLayout_2.addWidget(self.voltage_name, 5, 0, 1, 1)
        self.current_name = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.current_name.setObjectName("current_name")
        self.gridLayout_2.addWidget(self.current_name, 4, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_19.setObjectName("label_19")
        self.gridLayout_2.addWidget(self.label_19, 6, 0, 1, 1)
        self.mosfet_state = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.mosfet_state.setObjectName("mosfet_state")
        self.gridLayout_2.addWidget(self.mosfet_state, 2, 1, 1, 1)
        self.timer = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.timer.setObjectName("timer")
        self.gridLayout_2.addWidget(self.timer, 3, 1, 1, 1)
        self.timer_name = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.timer_name.setObjectName("timer_name")
        self.gridLayout_2.addWidget(self.timer_name, 3, 0, 1, 1)
        self.flow_rate = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.flow_rate.setObjectName("flow_rate")
        self.gridLayout_2.addWidget(self.flow_rate, 1, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_21.setObjectName("label_21")
        self.gridLayout_2.addWidget(self.label_21, 8, 0, 1, 1)
        self.current = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.current.setObjectName("current")
        self.gridLayout_2.addWidget(self.current, 4, 1, 1, 1)
        self.spacecraft_time = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.spacecraft_time.setObjectName("spacecraft_time")
        self.gridLayout_2.addWidget(self.spacecraft_time, 0, 1, 1, 1)
        self.flow_rate_name = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.flow_rate_name.setObjectName("flow_rate_name")
        self.gridLayout_2.addWidget(self.flow_rate_name, 1, 0, 1, 1)
        self.spacecraft_time_name = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.spacecraft_time_name.setObjectName("spacecraft_time_name")
        self.gridLayout_2.addWidget(self.spacecraft_time_name, 0, 0, 1, 1)
        self.mosfet_state_name = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.mosfet_state_name.setObjectName("mosfet_state_name")
        self.gridLayout_2.addWidget(self.mosfet_state_name, 2, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_20.setObjectName("label_20")
        self.gridLayout_2.addWidget(self.label_20, 7, 0, 1, 1)
        self.voltage = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.voltage.setObjectName("voltage")
        self.gridLayout_2.addWidget(self.voltage, 5, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bd_acceleration_x = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.bd_acceleration_x.setObjectName("bd_acceleration_x")
        self.horizontalLayout_2.addWidget(self.bd_acceleration_x)
        self.bd_acceleration_y = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.bd_acceleration_y.setObjectName("bd_acceleration_y")
        self.horizontalLayout_2.addWidget(self.bd_acceleration_y)
        self.bd_acceleration_z = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.bd_acceleration_z.setObjectName("bd_acceleration_z")
        self.horizontalLayout_2.addWidget(self.bd_acceleration_z)
        self.gridLayout_2.addLayout(self.horizontalLayout_2, 6, 1, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.bd_mag_x = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.bd_mag_x.setObjectName("bd_mag_x")
        self.horizontalLayout_3.addWidget(self.bd_mag_x)
        self.bd_mag_y = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.bd_mag_y.setObjectName("bd_mag_y")
        self.horizontalLayout_3.addWidget(self.bd_mag_y)
        self.bd_mag_z = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.bd_mag_z.setObjectName("bd_mag_z")
        self.horizontalLayout_3.addWidget(self.bd_mag_z)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 7, 1, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bd_ang_vel_x = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.bd_ang_vel_x.setObjectName("bd_ang_vel_x")
        self.horizontalLayout_4.addWidget(self.bd_ang_vel_x)
        self.bd_ang_vel_y = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.bd_ang_vel_y.setObjectName("bd_ang_vel_y")
        self.horizontalLayout_4.addWidget(self.bd_ang_vel_y)
        self.bd_ang_vel_z = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.bd_ang_vel_z.setObjectName("bd_ang_vel_z")
        self.horizontalLayout_4.addWidget(self.bd_ang_vel_z)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 8, 1, 1, 1)
        self.gridLayout_2.setColumnStretch(0, 1)
        self.gridLayout_2.setColumnStretch(1, 2)
        self.horizontalLayout.addWidget(self.bd_groupbox)
        self.nff_groupbox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.nff_groupbox.setObjectName("nff_groupbox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.nff_groupbox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 19, 561, 461))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.velocity_x = QtWidgets.QLabel(self.gridLayoutWidget)
        self.velocity_x.setObjectName("velocity_x")
        self.horizontalLayout_5.addWidget(self.velocity_x)
        self.velocity_y = QtWidgets.QLabel(self.gridLayoutWidget)
        self.velocity_y.setObjectName("velocity_y")
        self.horizontalLayout_5.addWidget(self.velocity_y)
        self.velocity_z = QtWidgets.QLabel(self.gridLayoutWidget)
        self.velocity_z.setObjectName("velocity_z")
        self.horizontalLayout_5.addWidget(self.velocity_z)
        self.gridLayout.addLayout(self.horizontalLayout_5, 3, 1, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.attitude_x = QtWidgets.QLabel(self.gridLayoutWidget)
        self.attitude_x.setObjectName("attitude_x")
        self.horizontalLayout_6.addWidget(self.attitude_x)
        self.attitude_y = QtWidgets.QLabel(self.gridLayoutWidget)
        self.attitude_y.setObjectName("attitude_y")
        self.horizontalLayout_6.addWidget(self.attitude_y)
        self.attitude_z = QtWidgets.QLabel(self.gridLayoutWidget)
        self.attitude_z.setObjectName("attitude_z")
        self.horizontalLayout_6.addWidget(self.attitude_z)
        self.gridLayout.addLayout(self.horizontalLayout_6, 4, 1, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.acceleration_x = QtWidgets.QLabel(self.gridLayoutWidget)
        self.acceleration_x.setObjectName("acceleration_x")
        self.horizontalLayout_7.addWidget(self.acceleration_x)
        self.acceleration_y = QtWidgets.QLabel(self.gridLayoutWidget)
        self.acceleration_y.setObjectName("acceleration_y")
        self.horizontalLayout_7.addWidget(self.acceleration_y)
        self.acceleration_z = QtWidgets.QLabel(self.gridLayoutWidget)
        self.acceleration_z.setObjectName("acceleration_z")
        self.horizontalLayout_7.addWidget(self.acceleration_z)
        self.gridLayout.addLayout(self.horizontalLayout_7, 5, 1, 1, 1)
        self.label_27 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_27.setObjectName("label_27")
        self.gridLayout.addWidget(self.label_27, 5, 0, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 3, 0, 1, 1)
        self.label_29 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_29.setObjectName("label_29")
        self.gridLayout.addWidget(self.label_29, 7, 0, 1, 1)
        self.label_30 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_30.setObjectName("label_30")
        self.gridLayout.addWidget(self.label_30, 8, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 4, 0, 1, 1)
        self.label_28 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_28.setObjectName("label_28")
        self.gridLayout.addWidget(self.label_28, 6, 0, 1, 1)
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_33.setObjectName("label_33")
        self.gridLayout.addWidget(self.label_33, 11, 0, 1, 1)
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 10, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_31 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_31.setObjectName("label_31")
        self.gridLayout.addWidget(self.label_31, 9, 0, 1, 1)
        self.exp_time = QtWidgets.QLabel(self.gridLayoutWidget)
        self.exp_time.setObjectName("exp_time")
        self.gridLayout.addWidget(self.exp_time, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.flight_state = QtWidgets.QLabel(self.gridLayoutWidget)
        self.flight_state.setObjectName("flight_state")
        self.gridLayout.addWidget(self.flight_state, 0, 1, 1, 1)
        self.altitude = QtWidgets.QLabel(self.gridLayoutWidget)
        self.altitude.setObjectName("altitude")
        self.gridLayout.addWidget(self.altitude, 2, 1, 1, 1)
        self.liftoff_warning = QtWidgets.QLabel(self.gridLayoutWidget)
        self.liftoff_warning.setObjectName("liftoff_warning")
        self.gridLayout.addWidget(self.liftoff_warning, 7, 1, 1, 1)
        self.label_34 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_34.setObjectName("label_34")
        self.gridLayout.addWidget(self.label_34, 12, 0, 1, 1)
        self.rcs_warning = QtWidgets.QLabel(self.gridLayoutWidget)
        self.rcs_warning.setObjectName("rcs_warning")
        self.gridLayout.addWidget(self.rcs_warning, 8, 1, 1, 1)
        self.chute_warning = QtWidgets.QLabel(self.gridLayoutWidget)
        self.chute_warning.setObjectName("chute_warning")
        self.gridLayout.addWidget(self.chute_warning, 10, 1, 1, 1)
        self.escape_warning = QtWidgets.QLabel(self.gridLayoutWidget)
        self.escape_warning.setObjectName("escape_warning")
        self.gridLayout.addWidget(self.escape_warning, 9, 1, 1, 1)
        self.fault_warning = QtWidgets.QLabel(self.gridLayoutWidget)
        self.fault_warning.setObjectName("fault_warning")
        self.gridLayout.addWidget(self.fault_warning, 12, 1, 1, 1)
        self.landing_warning = QtWidgets.QLabel(self.gridLayoutWidget)
        self.landing_warning.setObjectName("landing_warning")
        self.gridLayout.addWidget(self.landing_warning, 11, 1, 1, 1)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.ang_vel_x = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ang_vel_x.setObjectName("ang_vel_x")
        self.horizontalLayout_8.addWidget(self.ang_vel_x)
        self.ang_vel_y = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ang_vel_y.setObjectName("ang_vel_y")
        self.horizontalLayout_8.addWidget(self.ang_vel_y)
        self.ang_vel_z = QtWidgets.QLabel(self.gridLayoutWidget)
        self.ang_vel_z.setObjectName("ang_vel_z")
        self.horizontalLayout_8.addWidget(self.ang_vel_z)
        self.gridLayout.addLayout(self.horizontalLayout_8, 6, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 2)
        self.horizontalLayout.addWidget(self.nff_groupbox)
        self.monitor_wrapper.addLayout(self.horizontalLayout)
        self.groupBox_3 = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.monitor_wrapper.addWidget(self.groupBox_3)
        self.monitor_wrapper.setStretch(0, 2)
        self.monitor_wrapper.setStretch(1, 1)

        self.retranslateUi(Monitor)
        QtCore.QMetaObject.connectSlotsByName(Monitor)

    def retranslateUi(self, Monitor):
        _translate = QtCore.QCoreApplication.translate
        Monitor.setWindowTitle(_translate("Monitor", "Bruin Space GSE Monitor"))
        self.bd_groupbox.setTitle(_translate("Monitor", "Blue Dawn"))
        self.voltage_name.setText(_translate("Monitor", "Voltage"))
        self.current_name.setText(_translate("Monitor", "Current"))
        self.label_19.setText(_translate("Monitor", "Accel Vector"))
        self.mosfet_state.setText(_translate("Monitor", "Value"))
        self.timer.setText(_translate("Monitor", "Value"))
        self.timer_name.setText(_translate("Monitor", "Timer"))
        self.flow_rate.setText(_translate("Monitor", "Value"))
        self.label_21.setText(_translate("Monitor", "Ang Vel Vector"))
        self.current.setText(_translate("Monitor", "Value"))
        self.spacecraft_time.setText(_translate("Monitor", "Value"))
        self.flow_rate_name.setText(_translate("Monitor", "Flow Rate"))
        self.spacecraft_time_name.setText(_translate("Monitor", "Spacecraft Time"))
        self.mosfet_state_name.setText(_translate("Monitor", "MOSFET State"))
        self.label_20.setText(_translate("Monitor", "Mag Vector"))
        self.voltage.setText(_translate("Monitor", "Value"))
        self.bd_acceleration_x.setText(_translate("Monitor", "Value"))
        self.bd_acceleration_y.setText(_translate("Monitor", "Value"))
        self.bd_acceleration_z.setText(_translate("Monitor", "Value"))
        self.bd_mag_x.setText(_translate("Monitor", "Value"))
        self.bd_mag_y.setText(_translate("Monitor", "Value"))
        self.bd_mag_z.setText(_translate("Monitor", "Value"))
        self.bd_ang_vel_x.setText(_translate("Monitor", "Value"))
        self.bd_ang_vel_y.setText(_translate("Monitor", "Value"))
        self.bd_ang_vel_z.setText(_translate("Monitor", "Value"))
        self.nff_groupbox.setTitle(_translate("Monitor", "NFF Data"))
        self.velocity_x.setText(_translate("Monitor", "Value"))
        self.velocity_y.setText(_translate("Monitor", "Value"))
        self.velocity_z.setText(_translate("Monitor", "Value"))
        self.attitude_x.setText(_translate("Monitor", "Value"))
        self.attitude_y.setText(_translate("Monitor", "Value"))
        self.attitude_z.setText(_translate("Monitor", "Value"))
        self.acceleration_x.setText(_translate("Monitor", "Value"))
        self.acceleration_y.setText(_translate("Monitor", "Value"))
        self.acceleration_z.setText(_translate("Monitor", "Value"))
        self.label_27.setText(_translate("Monitor", "Accel Vector"))
        self.label_11.setText(_translate("Monitor", "Velocity Vector"))
        self.label_29.setText(_translate("Monitor", "Liftoff Warning"))
        self.label_30.setText(_translate("Monitor", "RCS warning"))
        self.label_12.setText(_translate("Monitor", "Atitude Vector"))
        self.label_28.setText(_translate("Monitor", "Ang Vel Vector"))
        self.label_33.setText(_translate("Monitor", "Landing Warning"))
        self.label_32.setText(_translate("Monitor", "Chute Warning"))
        self.label.setText(_translate("Monitor", "Exp Time"))
        self.label_2.setText(_translate("Monitor", "Altitude"))
        self.label_31.setText(_translate("Monitor", "Escape Warning"))
        self.exp_time.setText(_translate("Monitor", "Value"))
        self.label_4.setText(_translate("Monitor", "Flight State"))
        self.flight_state.setText(_translate("Monitor", "Value"))
        self.altitude.setText(_translate("Monitor", "Value"))
        self.liftoff_warning.setText(_translate("Monitor", "Value"))
        self.label_34.setText(_translate("Monitor", "Fault Warning"))
        self.rcs_warning.setText(_translate("Monitor", "Value"))
        self.chute_warning.setText(_translate("Monitor", "Value"))
        self.escape_warning.setText(_translate("Monitor", "Value"))
        self.fault_warning.setText(_translate("Monitor", "Value"))
        self.landing_warning.setText(_translate("Monitor", "Value"))
        self.ang_vel_x.setText(_translate("Monitor", "Value"))
        self.ang_vel_y.setText(_translate("Monitor", "Value"))
        self.ang_vel_z.setText(_translate("Monitor", "Value"))
        self.groupBox_3.setTitle(_translate("Monitor", "Command"))

