# gui/__init__.py
# Initialized GUI window classes


# Imports
from PySide6 import QtCore as Qt
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QApplication, QMainWindow

import src.dates as dates
import src.stats as stats

from statistics import StatisticsError

from . import ui_main


# Definitions
class MainWindow(QMainWindow, ui_main.Ui_MainWindow):
    """The main window for the application"""
    
    def __init__(self, app: QApplication) -> None:
        """Init"""
        
        super(MainWindow, self).__init__()
        self.setupUi(self)
        
        self.app = app

        # Connect buttons clicks
        self.itHappenedButton.clicked.connect(self.it_happened)
        self.undoTodayButton.clicked.connect(self.undo_today)
        self.refreshButton.clicked.connect(self.refresh)

        self.refresh()
    
    
    def closeEvent(self, event) -> None:
        """Quit the app when the main window is closed"""
        
        self.app.quit()
    
    # Button methods
    def it_happened(self) -> None:
        if not dates.save():
            print('\a', end='\r')
        self.refresh()
    

    def undo_today(self) -> None:
        if not dates.undo_today():
            print('\a', end='\r')
        self.refresh()
        

    def refresh(self) -> None:
        try:
            self.totalStat.setText(f"Total times: {len(dates.all())}")
        except TypeError:
            self.totalStat.setText("Total times: 0")
        
        try:
            self.averageBetweenStat.setText(f"Average days between: {stats.average_between()}")
            self.averageDeviationStat.setText(f"Average deviation: {stats.average_deviation()}")
        except (StatisticsError, TypeError):
            self.averageBetweenStat.setText(f"Average days between: None")
            self.averageDeviationStat.setText(f"Average deviation: None")
        
        try:
            self.nextDatePrediction.setText(f"Next predicted date: {stats.predict_next_date()}")
            self.nextDateRangePrediction.setText(f"Next predicted date range: ±{(stats.predict_next_date_range()[1] - stats.predict_next_date()).days}")
        except (StatisticsError, TypeError):
            self.nextDatePrediction.setText(f"Next predicted date: None")
            self.nextDateRangePrediction.setText(f"Next predicted date range: None")


def create_windows(app) -> None:
    """Create all of the windows"""
    
    # Declare global variables
    global main_window
    
    # Set values
    main_window = MainWindow(app)