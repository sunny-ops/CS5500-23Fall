class Logger:
    _instance = None  # Private class variable to hold the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)

            def init_logger(logger_instance):
                logger_instance.messages = []

            init_logger(cls._instance)
            print("Logger created exactly once")
        else:
            print("logger already created")
        return cls._instance
    
    # def init_Logger(self):
    #     self.messages = []

    def add_message(self, message):
        self.messages.append(message)


def main():
    # Logger should only be initialized one time if it is properly
    # refactored as a singleton class
    for i in range(3):
        logger = Logger()
        logger.add_message(f"Adding message number: {i}")
    print(logger.messages)
    logger1 = Logger()
    assert(logger1 == logger)

if __name__ == "__main__":
    main()
