
import random

f=open("Menu.csv")
content=f.readline();
print(content)
product_info={}
product_ids=[]
i=1
content=f.readline().replace("\n","")
while content !="":
    print(content)
    a,b,c =[int(x) for x in content.split(',')]
    product_info[a]=[b,c]
    product_ids.append(a)
    content=f.readline().replace("\n","")
    # print(content, end="")
f.close() 


order_info={}
print('''Enter your order in given format: item_id, half/full, quantity
And make sure you are entering available item_id
When you finished your order, type -1 :''')
order=input("")
while order!="-1":
    a,b,c=[x for x in order.split(',')]
    a=int(a)
    c=int(c)
    if order_info.get(a):
        if order_info.get(a).get(b) :
            order_info[a][b]+=c
        else:
            order_info[a][b]=c
    else:
        order_info[a]={b:c}
    order=input("")


total_amount=0
for id in order_info:
    for plate in order_info[id]:
        if plate=="half":
            total_amount+=(product_info[id][0]*order_info[id][plate])
        else:
            total_amount+=(product_info[id][1]*order_info[id][plate])



tip=int(input('''Please enter tips you want to give, in given format: 
1)enter 0 for 0%
2)enter 10 for 10%
3)enter 20 for 20% :\n'''))

tip_amount=(total_amount*tip)/100
total_amount+=tip_amount

print("Toatl amount you have to pay including tip : ",total_amount)

people=int(input("Enter the number of people wants pay bill equally: "))

split_amount=total_amount/people
print("Spliting amount is: ",round(split_amount,2))

print("*****************************************TEST YOUR LUCK EVENT**********************************************\n")
print('''1)There’s a 5% chance to get a 50% discount off the total bill
2) 10% chance to get 25% discount
3) 15% chance to get 10% discount
4) 20% chance to get no discount
5) 50% chance that the total amount increases by 20%\n''')
isPlay=input("Do you want to participate (yes/no): ")
discount=0;
if isPlay=="yes":
    randno=random.randint(1,20)
    if randno==1:
        discount=-(total_amount*50)/100
    elif randno>=2 and randno<=3:
        discount=-(total_amount*25)/100
    elif randno>=4 and randno<=6:
        discount=-(total_amount*10)/100
    elif randno>=7 and randno<=10:
        discount=0
    else: 
        discount=(total_amount*50)/100


    if discount<=0:
        print("Total discount is : ",-discount)
    else:
        print("Total increase is: ",discount)


    if discount<0 :       
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


for id in order_info:
    for plate in order_info[id]:
        if plate=="half":
            print(f'Item {id}[{plate}][{order_info[id][plate]}]= {product_info[id][0] * order_info[id][plate]}')
        else:
            print(f'Item {id}[{plate}][{order_info[id][plate]}]= {product_info[id][0] * order_info[id][plate]}')

total_final=total_amount+discount
print("Total = ",total_amount-tip_amount)
print("Tip percentage = "+str(tip)+"%")
print("Discount/Increase = ",discount)
print("Final total = ",total_final)

print(f'The new updated share or splitted amount of {people} people is = {round(total_final/people,2)}')