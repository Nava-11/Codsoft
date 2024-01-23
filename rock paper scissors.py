import random
option=int(input("enter 1 to start"))
while(option):
  option=int(input("if continue then 1 or to stop press 0 "))
  if(option==1):
    user=input("enter your choice ")
    choice=["rock","paper","scissors"]
    cc = random.randint(0, 2)
    print(choices[cc])
    if (choice[cc] == 'rock' and user == 'paper'):
        print("you won")
    elif (choice[cc]== 'paper' and user == 'scissors'):
      print('computer won')
    elif(choice[cc]=='scissors' and user=='paper'):
      print('computer won')
    elif(choice[cc]=='scissors' and user=='rock'):
      print('you won')
    elif(choice[cc]=='rock' and  user=='scissors'):
      print('computer won')
    elif(choice[cc]=='paper' and  user=='rock'):
      print("you won")
else:
  print('end of the game')
