import requests
import random
#from flask import jsonify, json
import json
session = requests.Session()

product_info = dict()

###############  order function  #############################


def order_function():
    order_info = {}
    print('''\nEnter your order in given format: item_id, half/full, quantity
    And make sure you are entering available item_id
    When you finished your order, type -1 :\n''')
    order = input("")
    while order != "-1":
        a, b, c = [x for x in order.split(',')]
        a = int(a)
        c = int(c)
        if order_info.get(a):
            if order_info.get(a).get(b):
                order_info[a][b] += c
            else:
                order_info[a][b] = c
        else:
            order_info[a] = {b: c}
        order = input("")

    total_amount = 0
    for id in order_info:
        for plate in order_info[id]:
            if plate == "half":
                total_amount += (product_info[id][0]*order_info[id][plate])
            else:
                total_amount += (product_info[id][1]*order_info[id][plate])

    tip = int(input('''\n\nPlease enter tips you want to give, in given format: 
    1)enter 0 for 0%
    2)enter 10 for 10%
    3)enter 20 for 20% :\n'''))

    tip_amount = (total_amount*tip)/100
    total_amount += tip_amount
    #print("\nToatl amount you have to pay including tip : ",total_amount)
    people = int(
        input("\nEnter the number of people wants pay bill equally: "))
    split_amount = total_amount/people
    #print("\nSpliting amount is: ",round(split_amount,2))
    print("\n\n***************************  TEST YOUR LUCK EVENT  ***************************************\n")
    print('''1)There’s a 5% chance to get a 50% discount off the total bill
    2) 10% chance to get 25% discount
    3) 15% chance to get 10% discount
    4) 20% chance to get no discount
    5) 50% chance that the total amount increases by 20%\n''')
    isPlay = input("\nDo you want to participate (yes/no): ")
    discount = 0
    if isPlay == "yes":
        randno = random.randint(1, 20)
        if randno == 1:
            discount = -(total_amount*50)/100
        elif randno >= 2 and randno <= 3:
            discount = -(total_amount*25)/100
        elif randno >= 4 and randno <= 6:
            discount = -(total_amount*10)/100
        elif randno >= 7 and randno <= 10:
            discount = 0
        else:
            discount = (total_amount*50)/100

        # if discount<=0:
        #     print("\nTotal discount is : ",-discount)
        # else:
        #     print("\nTotal increase is: ",discount)
        if discount < 0:
            print(" "+"*"*4+"\t\t "+"*"*4)
            print("|    |\t\t|    |")
            print("|    |\t\t|    |")
            print("|    |\t\t|    |")
            print(" "+"*"*4+"\t\t "+"*"*4)
            print("\t  {}")
            print("    _____________")
        else:
            print(" "+"*"*4)
            print("*    *")
            print("*    *")
            print("*    *")
            print("*    *")
            print(" "+"*"*4)
    tran = ""
    for id in order_info:
        for plate in order_info[id]:
            if plate == "half":
                tran += f'Item {id}[{plate}][{order_info[id][plate]}]= {product_info[id][0] * order_info[id][plate]}' + '\n'
            else:
                tran += f'Item {id}[{plate}][{order_info[id][plate]}]= {product_info[id][0] * order_info[id][plate]}' + '\n'

    total_final = total_amount+discount
    tran += f'\nTotal = {total_amount-tip_amount }' + '\n'
    tran += f'\nTip percentage = {str(tip)}%' + '\n'
    tran += f'\nDiscount/Increase = {discount}' + '\n'
    tran += f'\nFinal total = {total_final}' + '\n'
    tran += f'\nThe new updated share or splitted amount of {people} people is = {round(total_final/people,2)}' + '\n'
    print(tran)
    resp = session.post(
        "http://127.0.0.1:8000/transactionhistory", json={'order_info': tran})
    message = resp.content.decode('ascii')
    print('\n Your order transaction: ')
    print(message)


############################   MAIN    ######################################
while(1):
    print('############### option available for you ###############')
    print('1. Sign In')
    print('2. Sign Up')
    print('3. Exit')
    sel = int(input("Enter your selection:  "))

    if sel == 1:
        user_name = input("Enter Your username: ")
        password = input("Enter Your password: ")
        response = session.post("http://127.0.0.1:8000/signin",
                                json={'user_name': user_name, 'user_pass': password})
        msg = response.content.decode('ascii')
        print(msg)
        if msg[1] == 'L':
            while(1):
                print('############### option available for you now ###############')
                print('1. See Menu')
                print('2. Order')
                print('3. Logout')
                print('4. Add menu')
                print('5. transaction history')
                choice = int(input("Enter your selection:  "))
                if choice == 1:
                    resp = session.post("http://127.0.0.1:8000/showmenu")
                    message = resp.content.decode('ascii')
                    mydict = json.loads(message)
                    print(
                        "\n\n######################### TODAY'S MENU ########################\n\n")
                    print("Item No   half plate price   full plate price ")
                    for item in mydict.keys():
                        a = int(item)
                        b = mydict[item]['half']
                        c = mydict[item]['full']
                        product_info[a] = [b, c]
                        print(f'{a}\t\t{b}\t\t{c}')
                    print(
                        '########################################################################\n')
                elif choice == 2:
                    order_function()
                elif choice == 3:
                    resp = session.post("http://127.0.0.1:8000/logout")
                    message = resp.content.decode('ascii')
                    print(message)
                    break
                elif choice == 4:
                    a, b, c = [str(s) for s in input(
                        "Please Enter item id, half plate and full plate price in comma separated: ").split(',')]
                    resp = session.post("http://127.0.0.1:8000/addmenu",
                                        json={'item_id': a, 'item_half': b, 'item_full': c})
                    message = resp.content.decode('ascii')
                    print(message)
                elif choice == 5:
                    resp = session.post(
                        "http://127.0.0.1:8000/showtransaction")
                    message = resp.content.decode('ascii')
                    var = json.loads(message)
                    if var:
                        print('\nYour transaction Id: ')
                        for i in var.keys():
                            print(i)
                        check = input(
                            "Please enter a transaction id to view: ")
                        print(var[check])
                    else:
                        print("No transaction is added as of now .")
                else:
                    print("Invalid choice!!!")

    elif sel == 2:
        user_name = input("Enter user name: ")
        user_pass = input("Enter password: ")
        user_type = input("Enter user type: ")
        response = session.post("http://127.0.0.1:8000/signup", json={
                                'user_name': user_name, 'user_pass': user_pass, 'user_type': user_type})
        msg = response.content.decode('ascii')
        print(msg)

    elif sel == 3:
        break
    else:
        print("Invalid selection!!")
