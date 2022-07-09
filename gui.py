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
class Gui:
    """Holds gui elemets and methods"""

    # Subclasses
    class Elements:
        # Gui elements

        # Init
        def __init__(self, super_self) -> None:
            self.super_self = super_self

            # Elements
            # App, window, and frame
            self.app = QApplication([])
            with open("style.qss", 'rt') as file:
                self.app.setStyleSheet(file.read())

            self.window = QWidget()
            self.window.setWindowTitle("Niagara")

            self.window_layout = QGridLayout(self.window)

            # Date settings
            self.it_happened_button = QPushButton("It happened")
            self.window_layout.addWidget(self.it_happened_button, 0, 0)
            self.it_happened_button.clicked.connect(self.it_happened)

            self.undo_today_button = QPushButton("Undo today")
            self.window_layout.addWidget(self.undo_today_button, 0, 1)
            self.undo_today_button.clicked.connect(self.undo_today)

            # Stats
            self.stats_group = QGroupBox("Stats:")
            self.window_layout.addWidget(self.stats_group, 1, 0, 1, 2)
            self.stats_group_layout = QVBoxLayout(self.stats_group)

            self.stats_group_layout.addSpacing(10)

            self.total_stat = QLabel(f"Total times: {len(dates.all())}")
            self.stats_group_layout.addWidget(self.total_stat)

            self.average_between_stat = QLabel(f"Average days between: {stats.average_between()}")
            self.stats_group_layout.addWidget(self.average_between_stat)

            self.average_deviation_stat = QLabel(f"Average deviation: {stats.average_deviation()}")
            self.stats_group_layout.addWidget(self.average_deviation_stat)


        # Button methods
        def it_happened(self) -> None:
            if not dates.save():
                print('\a')
        

        def undo_today(self) -> None:
            if not dates.undo_today():
                print('\a')


    # Methods
    def __init__(self) -> None:
        self.elements = self.Elements(self)


    def show(self) -> None:
        self.elements.window.show()
    

    def loop(self) -> None:
        self.elements.app.exec_()
    
gui = Gui()