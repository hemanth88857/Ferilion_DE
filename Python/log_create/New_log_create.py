import logging

logging.basicConfig(
filename="app.log",
    encoding="utf-8",
    filemode="a",
    format="{asctime} - {levelname} - {message}",
    style="{",
    datefmt="%Y-%m-%d %H:%M",
    level=logging.DEBUG
)

logger = logging.getLogger("mylogger")
#
#
# # logging.basicConfig(format=" %(levelname)s :: %(filename)s :: %(asctime)s :: %(lineno)s :: %(message)s",
# #                     handlers=[logging.StreamHandler(), logging.FileHandler('info.log')], level=logging.INFO)
# #
# # info_logger = logging.getLogger("mylogger")
#
#
#
# # def log_function():
# #     log_f = logging.basicConfig(format=" %(levelname)s :: %(filename)s :: %(asctime)s :: %(lineno)s :: %(message)s",
# #                     handlers=[logging.StreamHandler(), logging.FileHandler('test.log')], level=logging.DEBUG)
# #
# #     return log_f
#
# # logger.debug("this is for debugging")
# # logger.info("this is for informational purpose")
# # logging.warning("low disk space")
# # logging.error("run time errors, HTTP errors")
# # logging.critical("app is at risk")






# logging.basicConfig(format=" %(levelname)s :: %(filename)s :: %(asctime)s :: %(lineno)s :: %(message)s",
#                     handlers=[logging.StreamHandler(), logging.FileHandler('test.log')], level=logging.DEBUG)
#

# Configure root logger
# logging.basicConfig(
#     format="%(levelname)s :: %(filename)s :: %(asctime)s :: %(lineno)s :: %(message)s",
#     handlers=[
#         logging.FileHandler("application.log"),
#         logging.StreamHandler()
#     ],
#     level=logging.DEBUG
# )
#
# # Optional: expose the logger
# logger = logging.getLogger()
