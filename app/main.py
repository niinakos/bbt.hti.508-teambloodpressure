# This file will start the application

from data.json_repository import JsonRepository
from services.data_service import DataService
from controllers.data_controller import DataController
from gui.main_window import MainWindow

def main():
    repository = JsonRepository("database/json_database.json")
    service = DataService(repository)
    controller = DataController(service)
    main_window = MainWindow(controller)

    main_window.run()

if __name__ == "__main__":
    main()
