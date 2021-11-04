# Python Programming

A group of friends ordered food for pickup from the menu items provided in csv. Write an interactive python code that accepts input and displays output via command line and calculates the total bill.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install python.
and then install some library by below command

```bash
pip install library_name
```

## How to run
type below command in terminal

```python
python bill.py
```

## Input
enter your order in given format, and each order is entered in a newline:  
item_id,full/half,item_quantity                                                                
before ordering any item, make sure that item is available and after ordering your item type -1 which indicates your order has been ordered.

```python
1,full,5
5,half,7
3,full,5
1,half,6
8,half,3
-1
```
Enter your tip, you want to give : (0/10/20) percent                                          
let's say 10% :

```python
10
```
Enter the number of people want to split the total bill :
let's say 11 people
```python
11
```
Enter yes/no , if you want to participate in the LUCKY DRAW event:

```python
yes
```

## Output
download my "python" folder and run it on your machine 
```python
Microsoft Windows [Version 10.0.19042.1288]
(c) Microsoft Corporation. All rights reserved.

E:\IIITH\OneDrive - International Institute of Information Technology\SSD(sem1)\assignment3A>python bill.py
Item no,Half Plate,Full Plate

1,20,30
2,210,400
3,460,600
4,500,650
5,400,800
6,450,600
7,320,400
8,360,450
9,220,400
Enter your order in given format: item_id, half/full, quantity
And make sure you are entering available item_id
When you finished your order, type -1 :
1,full,5
5,half,7
3,full,5
1,half,6
8,half,3
-1
Please enter tips you want to give, in given format:
1)enter 0 for 0%
2)enter 10 for 10%
3)enter 20 for 20% :
10
Toatl amount you have to pay including tip :  7865.0
Enter the number of people wants pay bill equally: 11
Spliting amount is:  715.0
*****************************************TEST YOUR LUCK EVENT**********************************************

1)There’s a 5% chance to get a 50% discount off the total bill
2) 10% chance to get 25% discount
3) 15% chance to get 10% discount
4) 20% chance to get no discount
5) 50% chance that the total amount increases by 20%

Do you want to participate (yes/no): yes
Total increase is:  3932.5
 ****
*    *
*    *
*    *
*    *
 ****
Item 1[full][5]= 100
Item 1[half][6]= 120
Item 5[half][7]= 2800
Item 3[full][5]= 2300
Item 8[half][3]= 1080
Total =  7150.0
Tip percentage = 10%
Discount/Increase =  3932.5
Final total =  11797.5
The new updated share or splitted amount of 11 people is = 1072.5

```

## GitHub Link
[Assignment3A](https://github.com/skabukhoyer/Softawre-System-Development/tree/main/python)
