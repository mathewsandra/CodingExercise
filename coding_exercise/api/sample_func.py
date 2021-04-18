from flask_restful import Resource,abort
from controller.sample_func_controller import hello_controller



helloController = hello_controller()

class sample_func(Resource):

    def get(self):
        try:
            print("sample_func")
            data = helloController.hello()
            return data
        except Exception as e: 
            print(e)
        
class hello_world(Resource):
    
    def get(self):
        try:
            data = 'Hello World'
        except Exception as e: 
            print(e)
            abort(500, error_message='Internal Server Error')    
        return data