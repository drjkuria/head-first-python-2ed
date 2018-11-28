import mysql.connector

class UseDatabase:

    def __init__(self, config: dict) -> None:
        self.configuration = config
