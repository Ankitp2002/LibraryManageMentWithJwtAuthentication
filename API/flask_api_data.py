import os
import jwt
from datetime import datetime , timedelta
from flask import Flask ,make_response,session ,request , current_app,jsonify
from flask_mail import Mail , Message
from flask_restful import Resource , Api
from flask_cors import CORS
from starting_lib import *
from create_donner import *
from book_add_function import *
from book_type_function import *
from donner_for_new_lib import *
from library_function import *
from sql_api import *
from book_issue import *
from book_return import *
# from all_information import *
from loginLogoutApi import *
from booktypelist import *
from bookissuelist import *
from availableBooklist import *
from booklist import *
from sqlalchemy_db import *



app = Flask(__name__)

CORS(app)
cross = CORS(app , allow_headers="Access-Control-Allow-Origin" )
cors = CORS(app, resources={r"/*": {"Access-Control-Allow-Origin": "*"}})

api = Api(app)

app.config['SECRET_KEY']  = "ashu"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'ankitprajapati1205@gmail.com'
app.config['MAIL_PASSWORD'] = 'zrtysgulbxcuxdxz'

mail = Mail(app)



class data_access(Resource):

    def get(self):

        data = all_db_data()
        return make_response(jsonify({"allData" : data}))


class BookAdd(Resource):

    def post(self):

        book_name = request.json['bookName']
        bookAuthor = request.json['bookAuthor']
        bookPrice = request.json['bookPrice']
        book_type_Name = request.json['bookTypeName']
        token = request.headers['token']

        tokenDecord = jwt.decode(token,app.config['SECRET_KEY'],algorithms=['HS256'])

        userId = Session.query(Signup).filter(Signup.email == tokenDecord['email'] , Signup.contact == tokenDecord['contact']).first()

        book_add = book_add_function( book_type_Name , book_name , userId.id,bookAuthor,bookPrice)

        return make_response(jsonify({"Response": book_add}))

class BookTypeAdd(Resource):

    def post(self):

        book_type = request.json['bookTypeName']
        type_add = create_new_type(book_type)

        return make_response(jsonify({"Type Added Succesfully" : type_add}))

# # class LibraryAdd(Resource):
# #
# #     def post(self):
# #
# #         library_name = request.json['libraryName']
# #         library_add = library_new_create(library_name)
# #
# #         return make_response(jsonify({"Response" : library_add }))
#
# # class DonnerAddForNewLib(Resource):
# #
# #     def post(self,donner_name,library_name):
# #
# #         donner_add = new_donner_lib(donner_name,library_name)
# #
# #         return "Created Donner And Library"
# #
# # class DonnerAddForExistsLib(Resource):
# #
# #     def post(self,donner_name,library_id):
# #
# #         donner_add = new_donner(donner_name,library_id)
# #
# #         return "Created Donner In Exits Library"
#
class data_issue(Resource):

    def post(self):

        token = request.headers['token']
        book_name = request.json['bookName']
        book_id = request.json['bookId']

        tokenDecord = jwt.decode(token,app.config['SECRET_KEY'],algorithms=['HS256'])

        data = book_issue(book_name,book_id,tokenDecord['name'],tokenDecord['email'],tokenDecord['contact'])

        return make_response(jsonify({"Responce" : {data : {"bookName" : book_name,"bookId" :book_id ,"issuerName" : tokenDecord['name'] , "contact" : tokenDecord['contact']}}}))


class data_return(Resource):

    def post(self):

        book_name = request.json['bookName']
        book_id = request.json['bookId']
        token = request.headers['token']

        tokenDecord = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])

        data = book_return(book_name,book_id,tokenDecord['email'])

        return make_response(jsonify(({"Response": {data: {"bookName" : book_name,"bookId" :book_id ,}}})))


class file_Add(Resource):

    def dat(self,file_Name):

        return "done"

class allInfo(Resource):

    def get(self):

        return make_response(jsonify({"Data" : information()}))

class bookAvailable(Resource):

    def get(self):

        data =availableInfo()

        return make_response(jsonify(data))

class bookIssueList(Resource):

    def get(self):

        data =bookissuelist()

        return make_response(jsonify(data))

class bookList(Resource):

    def get(self):

        data =booklist()

        return make_response(jsonify(data))
        
class bookTypeList(Resource):

    def get(self):

        data =booktypelist()

        return make_response(jsonify(data))


api.add_resource(data_access,'/')
api.add_resource(allInfo,'/Info')
api.add_resource(BookAdd,'/book_add')
api.add_resource(BookTypeAdd,'/book_type_add')
api.add_resource(data_issue,'/bookissue')
api.add_resource(data_return,'/returnbook')
api.add_resource(file_Add,'/fileAdd/<file_Name>')
api.add_resource(bookAvailable,'/availableBooklist')
api.add_resource(bookIssueList,'/bookissuelist')
api.add_resource(bookList,'/booklist')
api.add_resource(bookTypeList,'/booktypelist')

from loginLogoutApi import *



if __name__ == '__main__':
    app.run(host= '192.168.1.148',port='3000',debug=True)
    # app.run(debug=True)