# import logging
# logging.basicConfig(filename="file_opertaions.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='a')
# logger=logging.getLogger()
# logger.setLevel(logging.ERROR)
#
# def read_file(file_name):
#
#     try:
#         with open(file_name,'r') as file:
#             content=file.read()
#             print(content)
#
#     except FileNotFoundError:
#         error=f'file topilmadi {file_name}'
#         logger.error(error)
#
#         print("Xato:",error)
#
#     except Exception:
#         print("Umumiy xatolik")
#
# # read_file('txt.file')
#
# def read_log_file():
#
#     try:
#         with open('file_operations','r') as log_file:
#             logs=log_file.read()
#             print(logs)
#
#     except FileNotFoundError:
#         print("fayl xali yaratilmagan")
#
# read_file('txt.file')
# read_log_file()