import time
import sqlite3 as sql
import turtle
import random


#lists
greetlist= ["Hey", "Hi", "Hello", "Nice to meet you","Greetings and salutations!"]
functions= ['1.Feed Mood','2.Count Mood','3.Mental Health Questionnaire','4.Draw Mood','5.Deep Breathing']
moods    = ['1.Great','2.Good','3.Okay','4.Bad','5.Awful']
mood     = ['Great','Good','Okay','Bad','Awful']
activity = ['work','relax','hangout','sport','entertainment','travel']
category = ['1.self care','2.stress','3.entertainment']
positive = ['good','great','nice','amazing','fun','not hard']
negative = ['hard','messed','bad','awful','lots of work','stress']
draw     = ["1.Happy","2.Sad","3.Angry"]


#mood boosting tips
#selfcare
def sc():
  print("  Have a well-balanced diet")
  print("  Go out with friends")
  print("  Go for a breif walk")
  print("  Do exercise")
  print("  Get enough sleep")


#stress
def st():
  print("  Plan out your week")
  print("  Ask for help if things are stressing you out")
  print("  Download a breathing app")
  print("  Go for a walk and breathe to calm down")
  print("  Contact a therepist")

#entertainment
def ent():
  print("  Read a book")
  print("  Watch a movie")
  print("  Listen to music")
  print("  Join a club")
  print("  Pick up a hobby")
  print("  Go on a trip")
  print("  Hang out with friends")


#function for random greeting
def BotGreeting():
  for x in greetlist:
    print("-"+ random.choice(greetlist))
    break
  entry = input(">>")
  print("\n")


#function to execute exit
def goodbye():
  
    time.sleep(0.5)
    print("\n-See you next time ,bye!")


   
#function to perform any of the functions ones again    
def help():
  
    print("\n")
    time.sleep(0.5)
    print("\n-Need anything else?")
    yes_no2=input(">>")
    
    while True:
      if yes_no2=="yes":
        recursive1()
        break
       
      if yes_no2=="no":
        goodbye()
        break
        
      else:
        print("-ERROR")
        break
      break  



#to select a category of tips
def moodboost():
  
    print("-Please select a category")

    for c in category:
        print(c)

    print("\n")
    ch3=input(">>")

    while True:
        if ch3=="1":
            sc()
            help()
            break
        if ch3=="2":
            st()
            help()
            break
        if ch3=="3":
            ent()
            help()
            break
        else:
            moodboost()
            help()
        break





#to have a small talk
def inquiremood():
  
    ch2=int(input(">>"))
    if ch2<6:
        print("-I see you are feeling", str(mood[ch2-1]) ,"today .")
    else:
        print("-ERROR")
        inquiremood()
          
     
    print("\n")
    insert()
    print("\n-What have you been up to?\n")

    for a in activity:
      print(a)

    print("\n")
    ans=input(">>")
    print("-Im always here to hear more from you. Please tell me more")
    ans2=input(">>")
    
    list=ans2.split()
    
    for l in list:
      if l in positive:
        print("-Well that's great, I'm glad you had a nice day!")
        break
            
      elif l in negative:
        print("-I'm sorry to hear that, things will surely work out.\n")
        break
        
      else:
        break
          
       
    print("\n-Would you like to have some mood boosters?")
    yes_no=input(">>")

    while True:
        if yes_no=="yes":
            moodboost()
            break
        if yes_no=="no":
            help()
            break
        else:
            print("-ERROR")
            help()
        break




#to feed current mood
def feedmood():
  
    print("_____FEED MOOD_____")
    print("-How are you feeling today (1-5)?")

    for m in moods:
        print(m)

    print("\n")
    inquiremood()





#intro to bot / main body
def getuser():

    BotGreeting()
    time.sleep(0.5)
    print("-What is your name?")

    name=input(">>")
    print("\n")
    time.sleep(0.5)
    print("-Nice to meet you, " + name)
    time.sleep(0.5)
    print("-I am Mo'bot !")
    print("-Your personal mood friendly chatbot")
    time.sleep(0.5)
    recursive1()

#re-occuring function 
def recursive1():
  
    print("\n-What can I do for you ?")

    for f in functions:
        print(f)


    print("\n")
    ch1=input(">>")

    while True :
      if ch1=="1" :
        feedmood()
        break

      if ch1=="2" :
        countmood()
        break
        
      if ch1=="3":
        quest()
        help()  
        break
      
      if ch1=="4":
        drawmood()
        break
        
      if ch1=="5":
        breathe()
        break
        
      else :
        print("-ERROR")
        recursive1()
        break
      break

      
      
#to track previous moods      
def countmood():

    time.sleep(0.5)
    print("\n_____COUNT MOOD_____")  
    print("-Would you like to see previous moods?\n")
    yes_no3=input(">>")
    
    while True:
      if yes_no3=="yes":
        time.sleep(0.5)
        show()
        break
      
      if yes_no3=="no":
        help()
        break
        
      else:
        print("-ERROR")
        countmood()
        break 
      break  
        

        
#creating table into database (sql)
def create():
  
  con = sql.connect('hk.db')
  cur = con.cursor()

  c = cur.execute("CREATE TABLE IF NOT EXISTS y (date DATE (30) ,mood VARCHAR (5));")

  con.commit()

  con.close()
     
  
#insert user inputs into the table  
def insert():
  
  con = sql.connect('hk.db')
  cur = con.cursor()
  
  print("\n-Enter date (Y/M/D) into database:")
  date=input(">>")
  print("-Enter mood:")
  mood=input(">>")

  c = cur.execute('INSERT INTO y VALUES (?, ?);',(date,mood) )

  con.commit()

  con.close()

  
#displaying the values in the table   
def show():
  
  con = sql.connect('hk.db')
  cur = con.cursor()
  
  print("\n-Do you ant to see the track for")
  print("1.Specific day")
  print("2.Entire chart")
  print("3.Delete mood")
  
  print("\n")
  ans3=input(">>")
  while True:
    if ans3=="2":
      c = cur.execute('SELECT * FROM y ORDER BY date;')
  
      for row in cur:
        print('%s %s'  % row)
      break
    
    if ans3=="1":
      print("\n")
      c = cur.execute('SELECT date FROM y ORDER BY date ;')
  
      for row in cur:
        print('%s'  % row)
        
      print("\n-Enter date (Y/M/D) from database :")
      question=input(">>")
      c = cur.execute('SELECT mood FROM y WHERE date = ? ;',[question] )
      
      print("\n-Your mood on "+str(question)+" was")
      for row in cur:
        print('%s'  % row)
      break
        
        
    if ans3=="3":
      delmood()
      break
       
    else:
      print("-Data does not exist")
      show()
      break
    break  
  
  help()

  con.commit()
  con.close()
  


#deleting any specific value from the table  
def delmood():
  
  con = sql.connect('hk.db')
  cur = con.cursor()
  
  print("\n-Do you want to delete track?")
  yes_no4=input(">>")
  
  while True:
    if yes_no4=="yes":
      c = cur.execute('SELECT * FROM y ORDER BY date;')
  
      for row in cur:
        print('%s %s'  % row)
        
      print("\n-Enter date (Y/M/D) to delete :")
      date=input(">>")
      c = cur.execute('DELETE FROM y WHERE date = ? ;',[date] )
   
      for row in cur:
        print('%s %s'  % row)
      break
      
    if yes_no4=="no":
      help()
      break
        
    else:
      print("-ERROR")
      delmood()
      break
    break  
  
 

  con.commit()
  con.close()
      

  
#fun drawing of moods
def drawmood():
  
    print("\n_____DRAW MOOD_____")  
    print("-Select a mood to draw?\n")
    
    for d in draw:
      print(d)
    
    print("\n")
    ans4=input(">>")
    
    while True:
      if ans4=="1" or ans4=="happy":
        happy()
        help()
        break
      
      elif ans4=="2" or ans4=="sad":
        sad()
        help()
        break
        
      elif ans4=="3" or ans4=="angry":
        angry()
        help()
        break
        
      else:
        print("-ERROR")
        drawmood()
        break
      break

    
       
def happy():
  
#The following code is adapted from this example :
#https://stackoverflow.com/questions/26500332/how-to-make-a-smiley-face-in-turtle/26500432#26500432  
  smiles = turtle.Turtle() 
  
  smiles.penup()
  smiles.goto(-75,150)
  smiles.pendown()
  smiles.circle(10)       #eye one

  smiles.penup()
  smiles.goto(75,150)
  smiles.pendown()
  smiles.circle(10)       #eye two

  smiles.penup()
  smiles.goto(0,0)
  smiles.pendown()
  smiles.circle(100,90)   #right smile

  smiles.penup()           
  smiles.setheading(180)  #move West
  smiles.goto(0,0)
  smiles.pendown()
  smiles.circle(-100,90)
# This is the end of code adapted from this example  





def sad():
  
#The following code is adapted from this example :
#https://stackoverflow.com/questions/44493062/python-draw-a-angry-and-surprise-face  
  smiles = turtle.Turtle()
  
  smiles.penup()
  smiles.goto(-75,150)
  smiles.pendown()
  smiles.circle(10)        #eye one

  smiles.penup()
  smiles.goto(75,150)
  smiles.pendown()
  smiles.circle(10)        #eye two

  smiles.penup()
  smiles.goto(0,0)
  smiles.pendown()
  smiles.circle(-100,90)   #i changed the coordinates

  smiles.penup()
  smiles.setheading(180) 
  smiles.goto(0,0)
  smiles.pendown()
  smiles.circle(100,90)    #i changed the cordinates
  
# This is the end of code adapted from this example



def angry():
  
#The following code is adapted from this example : 
#https://stackoverflow.com/questions/44493062/python-draw-a-angry-and-surprise-face  
  smiles = turtle.Turtle()

  smiles.penup()
  smiles.goto(-105,155)
  smiles.pendown()
  smiles.goto(-45,115)

  smiles.penup()
  smiles.goto(-75,75)
  smiles.pendown()
  smiles.circle(10)

  smiles.penup()
  smiles.goto(105,155)      
  smiles.pendown()
  smiles.goto(45,115)

  smiles.penup()
  smiles.goto(75,75)
  smiles.pendown()
  smiles.circle(10)

  smiles.penup()
  smiles.goto(0,25)
  smiles.pendown()
  smiles.circle(-100,80)

  smiles.penup()
  smiles.setheading(180)
  smiles.goto(0,25)
  smiles.pendown()
  smiles.circle(100,80)

  turtle.done()
# This is the end of code adapted from this example



#function for breating exercise
def breathe():
 
  print("\n____DEEP BREATHING____\n")
  print("-Are you ready for a breathing exercise?")
  yes_no5=input(">>")
  print("\n")
  
  while True :
    if yes_no5=="yes" :
      print("-How many time do you want to repeat the exercise?")
      n=int(input(">>"))
      print("\n")
      
      for i in range(n):
        print("-1.INHALE")
        time.sleep(2)
        print("-Hold in your breath for 5 seconds")
        time.sleep(5)
        print("2.EXHALE\n")
        
      print("\n-Well done!")
      help()
      break
      
    elif yes_no5=="no":
      help()
      break
    
    else:
      print("-ERROR")
      breathe()
      break
    break  

    
    
    
def quest():
  
    print("\n____QUESTIONNAIRE____\n")
    print("-Are you ready to take the quiz?")
    yes_no6=input(">>")
    print("\n")
    
    while True:
      if yes_no6=="yes":
        
        if __name__ == '__main__':
          Mental.diagnose(user)
        
        break
                
      elif yes_no6=="no":
        help()
        break
      
      else:
        print("-ERROR")
        quest()
        break
      break  
      
class Mental:
  """This class stores methods that test the users mental health using their mood,age,sleep ..etc"""    

  def __init__(self):
    self.mood = 0
    self.duration = 0
    self.sleep = 0
    self.age = 0
    self.speech = 0
    self.interest = 0
    self.food = 0
  
  def preDepression(self):
    print("\n-Experiencing a low mood for more than 2 weeks can be linked to depression if found with other symptoms:\nLets find out\n")
    user.interest = int(input('\n-Please choose a number:\nDo you experience\n 1- Loss of interest\n 2- Over interest\n 3- Normal\n>>'))
    user.speech = int(input('\n-Please choose a number:\nAre you \n 1- Talkative \n 2- Quiet\n 3-Normal\n>> '))
    user.sleep = int(input( '\n-On average, How many hours do you sleep every day\n>>'))
    if user.interest >=1 and user.interest<=3 and user.speech>= 1 and user.speech<=3 and user.sleep>=1 and user.sleep<=24 and user.food>=1and user.food<=3:
      if user.interest == 1 and user.speech == 2 and user.sleep > 8 :
        Mental.depression(self)
      elif user.interest== 2 and user.speech == 1 and user.sleep < 8:
        Mental.bipolar(self)
      elif user.interest== 3 and user.speech == 3 and user.sleep == 8:
        Mental.normal(self)
    else: 
        print("-You've entered a wrong selection. Please try again:\n")
        Mental.preDepression(self)
    
  def depression(self):
    print("\n-Sleeping more..\nEating more..\nInteracting less..\nLoss of interest...\nWhen experienced for more than two weeks are linked to depression.\n")
  
  
  def mania(self):
    print("\n-Sleeping less..\nEating less..\nBeing interested in dangerous activities and sexual experiments..\nWhen experienced for more than two weeks are linked to mania\n")
    print("Go to this link for more information")
    print("https://www.verywellmind.com/symptoms-of-mania-380311\n")
                        
  def preBipolar(self):
    print("\n-High mood and flunctuations in mood are signs of bipolar. Lets proceed:\n")
    user.interest = int(input('\n-Please choose a number:\nDo you experience\n 1- Loss of interest\n 2- Over interest\n 3- Normal\n>>'))
    user.speech = int(input('\n-Please choose a number:\nAre you \n 1- Talkative \n 2- Quiet\n 3- Normal\n>>'))
    user.sleep = int(input( '\n-On average, How many hours do you sleep every day\n>>'))
    user.food = int(input('\n-Please choose a number:\n On average, do you eat\n 1- normal\n 2- less than normal\n 3- more than normal?\n>>'))
    if user.interest >=1 and user.interest<=3 and user.speech>= 1 and user.speech<=3 and user.sleep>=1 and user.sleep<=24 and user.food>=1and user.food<=3:
      if user.interest == 2 and user.speech == 1 and user.sleep < 8 and user.food == 2:
        Mental.bipolar(self)
      elif user.interest == 1 and user.speech == 2 and user.sleep > 8 and user.food ==3:
        Mental.depression(self)
      elif user.interest == 3 and user.speech == 3 and user.sleep == 8 and user.food ==1 :
        Mental.normal(self)
      else:
        Mental.mood_swings(self)
    else:
      print("-You've entered a wrong selection. Please try again:\n")
      Mental.preBipolar(self)
    
    
  def bipolar(self):
    print("\n-Sleeping less..\nEating less...\nBeing interested in dangerous activities and sexual experiments..\nWhen experienced for mor than two weeks are linked to bipolar\n")
    print("Go to this website for more information about bipolar.")
    print("https://www.healthline.com/health/could-it-be-bipolar-signs-to-look-for\n")
    
  def mood_swings(self):
    print("-Fluctuation in daily activities for less that 2 weeks are nothing but  mood swingng\n")
            
  def normal(self):
    print("-Your attributes are normal therefore, your mental health is on point\n")
    
    
  def sleep_lack(self):
    print("-You sleep less than normal. Adults must sleep about 7-8 hours everyday.\n")
    
  def diagnose(self):
    user = Mental()
    user.mood = int(input("\n-Please choose a number:\nDo you experience\n 1- High\n 2- Low mood\n 3- Normal mood\n>>"))
    user.duration = int(input('\n-How long does this last?\n 1- Less than 2 weeks\n 2- More than 2 weeks\n>>'))
    
    while True:
      if user.mood>=1 or user.mood <=3 or user.duration>=1 or user.duration<=3:
        if user.mood == 1 and user.duration == 2:
          Mental.preBipolar(user)
        elif user.mood == 2 and user.duration == 2:
          Mental.preDepression(user)
        elif user.mood == 3 and user.duration == 2:
          Mental.normal(user)
        elif user.mood == 3 and user.duration == 2:
          Mental.mood_swings(user)
        elif user.duration == 1:
          print("\n-Sometimes things things go wrong and you feel low. But if its been going on for less than two weeks then its not considered a mental issue.\n")
          break
     
      else:
        print("-You've entered a wrong selection, Please try again:\n")
        Mental.diagnose(self)
        break
      break
  
user= Mental()    
      
      
      
#calling functions to start the execution of code
create()
getuser()

