class NetworkError(Exception):
    def __init__(self):
        self.message = "An unknown network error seems to have occurred"
        