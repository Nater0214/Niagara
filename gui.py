# gui.py
# Handles the gui and elements
# Isolates it from other scripts to remove clutter


# Imports
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton

import dates
import stats


# Classes
class MainGui:
    """Holds gui elemets and methods"""

    class Elements:
        # Gui elements

        # Init
        def __init__(self, super_self) -> None:
            self.super_self = super_self

            # Elements
            # Everything in here should be self-explanatory

            # App, window, and frame
            self.app = QApplication([])
            with open("style.qss", 'rt') as file:
                self.app.setStyleSheet(file.read())

            self.main_window = QWidget()
            self.main_window.setWindowTitle("Niagara")
            self.main_window.setFixedSize(400,200)
            self.window_layout = QGridLayout(self.main_window)

            # Date settings
            self.it_happened_button = QPushButton("It happened")
            self.window_layout.addWidget(self.it_happened_button, 0, 0)
            self.it_happened_button.clicked.connect(self.it_happened)

            self.undo_today_button = QPushButton("Undo today")
            self.window_layout.addWidget(self.undo_today_button, 0, 1)
            self.undo_today_button.clicked.connect(self.undo_today)

            # Stats
            self.stats_group = QGroupBox("Stats:")
            self.window_layout.addWidget(self.stats_group, 1, 0, 2, 2)
            self.stats_group_layout = QVBoxLayout(self.stats_group)

            self.stats_group_layout.addSpacing(10)

            self.total_stat = QLabel(f"Total times: {len(dates.all())}")
            self.stats_group_layout.addWidget(self.total_stat)

            self.average_between_stat = QLabel(f"Average days between: {stats.average_between()}")
            self.stats_group_layout.addWidget(self.average_between_stat)

            self.average_deviation_stat = QLabel(f"Average deviation: {stats.average_deviation()}")
            self.stats_group_layout.addWidget(self.average_deviation_stat)

            # Prediction
            self.prediction_group = QGroupBox("Prediction:")
            self.window_layout.addWidget(self.prediction_group, 0, 2, 2, 2)
            self.prediction_group_layout = QVBoxLayout(self.prediction_group)

            self.prediction_group_layout.addSpacing(10)

            self.date_prediction = QLabel(f"Next predicted date: {stats.predict_next_date()}")
            self.prediction_group_layout.addWidget(self.date_prediction)

            self.range_prediction = QLabel(f"Next predicted date range: ±{(stats.predict_next_date_range()[1] - stats.predict_next_date()).days}")
            self.prediction_group_layout.addWidget(self.range_prediction)

            # Refresh and settings
            self.refresh_button = QPushButton("Refresh")
            self.window_layout.addWidget(self.refresh_button, 2, 2)
            self.refresh_button.clicked.connect(self.refresh)

            self.settings_button = QPushButton("Settings")
            self.window_layout.addWidget(self.settings_button, 2, 3)
            self.settings_button.clicked.connect(self.open_settings)


        # Button methods
        def it_happened(self) -> None:
            if not dates.save():
                print('\a')
            self.refresh()
        

        def undo_today(self) -> None:
            if not dates.undo_today():
                print('\a')
            self.refresh()
        

        def refresh(self) -> None:
            self.total_stat.setText(f"Total times: {len(dates.all())}")
            self.average_between_stat.setText(f"Average days between: {stats.average_between()}")
            self.average_deviation_stat.setText(f"Average deviation: {stats.average_deviation()}")
        

        def open_settings(self) -> None:
            pass


    # Methods
    def __init__(self) -> None:
        self.elements = self.Elements(self)


    def show(self) -> None:
        self.elements.main_window.show()
    

    def loop(self) -> None:
        self.elements.app.exec_()
    
gui = MainGui()


class SettingsGui: # I have decided to work on this later.
    """Holds settingss"""

    class Elements:
        pass