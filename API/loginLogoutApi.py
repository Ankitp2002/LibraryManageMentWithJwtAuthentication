import time
from flask_api_data import app ,session , make_response , request ,current_app , mail ,Message,jsonify
import jwt
from sqlalchemy_db import *
from datetime import datetime , timedelta
from functools import wraps


@app.route('/home',methods=['GET'])
def home():

    return "Login Signup Page"

@app.route('/signup', methods=['POST'])
def signUpUser():

    name = request.json['name']
    contact = request.json['contact']
    email = request.json['email']
    password = request.json['password']

    userAdd = Signup (name = name ,  contact = int(contact),email = email , password=password)
    Session.add(userAdd)
    Session.commit()

    return make_response(jsonify({"Response" : "successfully signup"}))

@app.route('/login',methods = ['POST'])
def loginUser():

    # name = request.json['name']
    email = request.json['email']
    password = request.json['password']

    availableUserData = Session.query(Signup)

    data = [(data.password,data.email) for data in availableUserData]


    if (password,email) in data:

        userData = Session.query(Signup).filter(Signup.email == email).first()

        exp_time = int((datetime.now() + timedelta(minutes=30)).timestamp())

        payload = {

            "name": userData.name,
            "email" : email,
            "contact" :userData.contact,
            "expTime": exp_time

        }

        token = jwt.encode(payload, app.config['SECRET_KEY'] , algorithm="HS256")

        # session['sessiontoken'] = token

        # if 'sessiontoken' in session:

        data = make_response(jsonify({"Response" : "Login successfully", "token" : token , "userName" :userData.name }))

            # data.headers['token'] = token

        return data

    else:

        return make_response(jsonify({"Response":"check your credential"}))


@app.route('/profile',methods=['POST'])
def profile():

    token = request.headers['token']

    tokendecode = jwt.decode(token, app.config['SECRET_KEY'],algorithms=['HS256'])

    profileData = Session.query(Signup).filter(Signup.email == tokendecode['email']).first()

    userData = {'userName':profileData.name, "contactNumber" : profileData.contact, "email" : profileData.email}

    return make_response(jsonify({"profile" : userData}))


@app.route('/userissuebook',methods=['GET'])
def userIssueData():

    token = request.headers['token']

    tokendecode = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])

    issueData = Session.query(issue_book).filter(issue_book.issuer_email == tokendecode['email'],
                                                 issue_book.issuer_contact == tokendecode['contact'])
    time.sleep(1)
    try:

        userIssueBook = [{"bookName": data.book_name, "bookId": data.book_id ,"bookAuthor": data.bookAuthor, "bookPrice": data.bookPrice,"typeName" : data.typeName} for data in issueData]

        return make_response(userIssueBook)

    except AttributeError :

        return make_response(jsonify("No any Book Issue"))

@ app.route('/pswwchange', methods=['POST'])
def passwork():

    email = request.json['email']
    oldPassword = request.json['oldPassword']
    newPassword = request.json['newPassword']

    old_psw = Session.query(Signup).filter(Signup.password == oldPassword,Signup.email == email).first()

    if oldPassword == old_psw.password and email == old_psw.email:

        old_psw.password = newPassword
        Session.commit()

        return make_response(jsonify({"status":"successfully"}))
    else:
        return "please chack your credential"

@app.route('/forgotpsw',methods=['POST'])
def forgotPssword():

    email = request.json['email']
    # contact = request.json['contact']

    if email == "":

        return make_response(jsonify("enter email id !!!!"))

    else:

        old_psw = Session.query(Signup).filter(Signup.email == email).first()

        if old_psw is not None:
            
            if old_psw.email == email:

                exp = int((datetime.now() + timedelta(minutes=5)).timestamp())

                payload = {

                    "name": old_psw.name,
                    "email": old_psw.email,
                    "exp": exp

                }
                token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm="HS256")

                msg = Message('Password Reset Request', sender='ankitprajapati1205@gmail.com', recipients=[email])
                # msg.body = f"To reset your password, please click the following link: token : {token}"

                msg.body = f"To reset your password, please click the following link: token :  http://192.168.1.142:3000/reset/{token}"
                mail.send(msg)

                return make_response(jsonify("Reset Link Send On Your Mail Address"))

        else:

            return make_response(jsonify("check your credential"))

@app.route('/reset_password/<string:token>',methods=['POST'])
def resetpsw(token):

    # token = request.json['token']

    data = jwt.decode(token,app.config['SECRET_KEY'],algorithms=['HS256'])

    db = Session.query(Signup).filter(Signup.email == data['email'] , Signup.name ==  data['name']).first()

    password = request.json['newPassword']
    db.password = password

    Session.commit()

    return make_response(jsonify({"message":"Password reset successful."}))



