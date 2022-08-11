import telebot
import cv2

# Create bot
bot = telebot.TeleBot('5442120137:AAEVdN0KYzO39dQm5LjMpcWzUXn2Eos7OwY')

#Weepy Face \xF0\x9F\x98\x9E
#Group Id = '@cetkrauth'
#myid='607964025'
# Send message
def sendht(student_id,student_name):
    student_id = student_id.split('/')
    bot.send_message('@cetkrauth', "{} of {} 20{}th batch is having High Temperature\U0001F321.He/She is at the Gate rn Catch Him/HerFast".format(student_name,student_id[2],student_id[0]))

def sendnnm(student_id,student_name):
    student_id = student_id.split('/')
    bot.send_message('@cetkrauth', "I told {} of {} 20{}th batch to Put Mask Twice.He/She is Not Listening To Me \U0001F61E".format(student_name,student_id[2],student_id[0]))

def sendnostud(student_id):
        bot.send_message('@cetkrauth', "\U0001F632 Scanned Student Not Found in Database. ID={}".format(student_id))

def sendstudnomask(frame,student_name):
        success, encoded_image = cv2.imencode('.png', frame)
        frametemp = encoded_image.tobytes()
        bot.send_photo('@cetkrauth', photo = frametemp)
        bot.send_message('@cetkrauth', "Found a lad with No Mask Roaming the Campus. Name={}".format(student_name))
