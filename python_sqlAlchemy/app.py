from enum import unique
from flask import Flask, request, json, session
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sk:9735@localhost/ssd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secretkey'
app.config["SESSION_TYPE"] = 'filesystem'
db = SQLAlchemy(app)


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20), nullable=False, unique=True)
    user_pass = db.Column(db.String(20), nullable=False)
    user_type = db.Column(db.String(30), nullable=False)

    def __init__(self, user_name, user_pass, user_type):
        self.user_name = user_name
        self.user_pass = user_pass
        self.user_type = user_type


class Menu(db.Model):
    item_id = db.Column(db.Integer, primary_key=True)
    item_half = db.Column(db.Float, nullable=False)
    item_full = db.Column(db.Float, nullable=False)

    def __init__(self, id, half, full):
        self.item_id = id
        self.item_half = half
        self.item_full = full

########### let's add some menu #################


def menu_function():
    obj = Menu.query.all()
    if not obj:
        f = open("Menu.csv")
        content = f.readline()
        content = f.readline().replace("\n", "")
        while content != "":
            a, b, c = [int(x) for x in content.split(',')]
            menu = Menu(a, b, c)
            db.session.add(menu)
            db.session.commit()
            content = f.readline().replace("\n", "")
            # print(content, end="")
        f.close()


'''
Item 1[Quantity]: total_price
Item 2[Quantity]: total_price
Total: value
Tip Percentage: value
Discount/Increase: value
Final Total: value
'''


class Transaction(db.Model):
    transaction_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    order_info = db.Column(db.String(1024), nullable=False)
    #date = db.Column(db.DateTime, default=db.func.now())

    def __init__(self, user_id, order_info):
        self.user_id = user_id
        self.order_info = order_info


class Signup(Resource):
    def post(self):
        data = request.get_json()
        user_name = data['user_name']
        user_pass = data['user_pass']
        user_type = data['user_type']

        inp = User.query.filter_by(user_name=user_name).first()
        if inp is not None:
            return 'User Already exist.'

        else:
            obj = User(user_name=user_name,
                       user_pass=user_pass, user_type=user_type)
            db.session.add(obj)
            db.session.commit()
            return 'User Registered successfully.'


class Signin(Resource):
    def post(self):
        data = request.get_json()
        user_name = data['user_name']
        user_pass = data['user_pass']

        inp = User.query.filter_by(user_name=user_name).first()
        if inp is not None:
            if user_pass == inp.user_pass:
                session['user'] = inp.user_id
                menu_function()
                return 'Login Successfull'
            else:
                return 'Wrong Password! please enter correct password'
        else:
            return 'user name does not exist! please enter correct user name'


class Logout(Resource):
    def post(self):
        if 'user' in session:
            session.pop('user', None)
            return "Logged out Done."
        else:
            return "You are not logged in yet."


class Showmenu(Resource):
    def post(self):
        if 'user' in session:
            obj = Menu.query.all()
            # result = "Item No\t"+"Half plate price\t"+"Full Plate price\n"
            menu_dict = dict()
            for item in obj:
                menu_dict[item.item_id] = dict()
                menu_dict[item.item_id]['half'] = item.item_half
                menu_dict[item.item_id]['full'] = item.item_full
            return menu_dict
        else:
            return "You are not logged in yet."


class Addmenu(Resource):
    def post(self):
        if 'user' in session:
            check = User.query.filter_by(user_id=session['user']).first()
            if check.user_type == 'chef':
                data = request.get_json()
                item_id = int(data['item_id'])
                item_half = float(data['item_half'])
                item_full = float(data['item_full'])
                inp = Menu.query.filter_by(item_id=item_id).first()
                if inp is not None:
                    return 'Item is already in menu.'
                else:
                    new_menu = Menu(item_id, item_half, item_full)
                    db.session.add(new_menu)
                    db.session.commit()
                    return 'New Item added successfully.'
            else:
                return 'You are not chef.'
        else:
            return 'You are not logged in yet.'


class Transactionhistory(Resource):
    def post(self):
        if 'user' in session:
            data = request.get_json()
            order_info = data['order_info']
            user_id = session['user']
            tr = Transaction(user_id=user_id, order_info=order_info)
            db.session.add(tr)
            db.session.commit()
            return "Your new transaction has been added"
        else:
            return 'You are not logged in yet.'


class Showtransaction(Resource):
    def post(self):
        if 'user' in session:
            obj = Transaction.query.filter_by(user_id=session['user']).all()
            myd = {}
            for tr in obj:
                myd[tr.transaction_id] = tr.order_info
            return myd
        else:
            return 'You are not logged in yet.'


################### API ##########################
api.add_resource(Signin, '/signin')
api.add_resource(Signup, '/signup')
api.add_resource(Logout, '/logout')
api.add_resource(Showmenu, '/showmenu')
api.add_resource(Addmenu, '/addmenu')
api.add_resource(Transactionhistory, '/transactionhistory')
api.add_resource(Showtransaction, '/showtransaction')

if __name__ == '__main__':
    db.create_all()
    app.run(port=8000, debug=True)
