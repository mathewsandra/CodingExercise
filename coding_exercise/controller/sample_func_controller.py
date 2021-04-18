from models.sample_func_model import hello_model
from flask_restful import Resource,abort

sample_funcModel = hello_model()


class hello_controller():

    def hello(self):
        try:
            data = sample_funcModel.hello()
        
        except Exception as e:
            print(e)
            abort(500, error_message='Internal Server Error')
        return data
        