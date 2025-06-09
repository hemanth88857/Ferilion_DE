import  logging

class Logs:

    def __int__(self):
        logger = logging.getLogger("my_app")
        logger.setLevel(logging.DEBUG)
        if not logger.handlers:
            fh = logging.FileHandler("app_logs.log", mode='a')
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            fh.setFormatter(formatter)
            logger.addHandler(fh)
        return logger


# logger = logging.getLogger()
# # log_creation_func("exe_log.log")
#
# # logger.setLevel(logging.DEBUG)
# # if not logger.handlers:
# #
# #     file_handler = logging.FileHandler("exe_logs.log", mode='w')
# #     logger.setLevel(logging.DEBUG)
# #
# #     formatter = logging.Formatter('%(asctime)s : %(levelname)s :%(message)s')
# #     file_handler.setFormatter(formatter)
# #
# #     logger.addHandler(file_handler)


# logger.debug("Debug message")
# logger.info("Info message")
# logger.warning("Warning message")
# logger.error("Error message")
# logger.critical("Critical message")












def get_logger():
    logger = logging.getLogger("my_app")
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        fh = logging.FileHandler("app_logs.log", mode='a')
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        logger.addHandler(fh)
    return logger



def log_creation_func():
    logger = logging.getLogger("my_workflow")
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        file_handler = logging.FileHandler("workflow", mode='a')
        formatter = logging.Formatter('%(asctime)s : %(levelname)s :%(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger

def log_creation_file(log_filename):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    if not logger.handlers:
        file_handler = logging.FileHandler(log_filename, mode='a')
        formatter = logging.Formatter('%(asctime)s : %(levelname)s :%(message)s')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    return logger




# logger_config.py

# Configure the root logger

logging.basicConfig(
    filename='CommomApp.log',         # Common log file
    level=logging.INFO,         # Set the log level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
