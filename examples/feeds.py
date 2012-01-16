from pyqidiq import QidiqAPI

q = QidiqAPI(api_key = "4ADOWCW3TMJKXEVIUQ4R")
r = q.get_question(question_id = 406009)
print r
