from tkinter import *
from datetime import datetime
import pyttsx3
import webbrowser
import os
import csv

# Window / engine
root = Tk()
bot_pc = pyttsx3.init()
bot_pc.setProperty('rate', 123)
root.title("TiBot v1.0-beta.1")
root.resizable(width=FALSE, height=FALSE)



# Global Variables
face_book = ' '
name_of_birth = 'No one'
new_year = '0101'
christmas = '2512'


# Variables date
day = datetime.now()
day = day.strftime('%A')
month = datetime.now()
month = month.strftime("%B")
year = datetime.now()
year = year.strftime('%Y')
full_date = day + " " + month + " " + year  # Full date (Monday July 2020)

# Birthday check
check_now = datetime.now()
format_date = "%d%m"
flag_date = int(check_now.strftime(format_date))

# Userprofile
userprofile = os.getlogin()


# Function
def greeting(birthday):
    birthday = f"today it's {birthday}'s birthday"
    if flag_date == int(new_year):
        bot_pc.say(f"Today's date is {full_date}, It's the new year of {year}, welcome {userprofile} and happy new year,  {birthday}, let begin.")
        bot_pc.runAndWait()
    elif flag_date == int(christmas):
        bot_pc.say(f"Today's date is {full_date}, welcome {userprofile}, it's christmas, {birthday}, let begin.")
        bot_pc.runAndWait()
    else:
        bot_pc.say(f"Today's date is {full_date}, welcome {userprofile},  {birthday}, let begin.")
        bot_pc.runAndWait()


def open_csv():
    global face_book
    global name_of_birth
    with open("Birthdays.csv", "r") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=",")

        for birthday in reader:
            birth_ = int(birthday['Birthday'])
            if birth_ == flag_date:
                face_book = birthday['Facebook']
                name_of_birth = birthday['Name']
                return name_of_birth


def help_command():
    top = Toplevel()
    top.resizable(width=FALSE, height=FALSE)
    bot_pc.say("Here are the commands i can execute.")
    bot_pc.runAndWait()
    Label(top, text="Commands : ").pack()
    command_box = Text(top, width=40, height=15)
    command_box.pack(padx=10, pady=5)

    with open('Command.txt', 'r') as command_file:
        reader = command_file.read()
        for text in reader:
            command_box.insert(END, text)


def facebook_profile():
    webbrowser.open(face_book)


def open_youtube(genre):
    webbrowser.open(f'https://www.youtube.com/results?search_query={genre}')
    


def music():
    music_root = Toplevel()
    music_root.resizable(width=FALSE, height=FALSE)
    # GUI
    frame_music = LabelFrame(music_root, padx=5, pady=5)
    frame_music.pack(padx=5, pady=5)

    bot_pc.say('Type the genre you like to listen.')
    bot_pc.runAndWait()

    genre = Label(frame_music, text='Enter genre : ')
    genre.pack()

    genre_entry = Entry(frame_music, borderwidth=2, width=20)
    genre_entry.pack()

    genre_button = Button(music_root, text='Enter', command=lambda: open_youtube(genre_entry.get()))
    genre_button.pack(padx=5, pady=5)



def start_bot(user_command):
    if user_command.lower() == 'help':
        help_command()
    if user_command.lower() == "facebook":
        bot_pc.say(f"Am going to open the profile facebook of {name_of_birth}.")
        bot_pc.runAndWait()
        facebook_profile()
    if user_command.lower() == 'music':
        music()


# Start of bot
today_birthday_is = open_csv()  # Check for birthdays
greeting(today_birthday_is)

# GUI start

# Frame
frame_input = LabelFrame(root, padx=5, pady=5)
frame_input.grid(row=3, column=3, columnspan=3, padx=20, pady=10)
frame_birthday = LabelFrame(root, padx=5, pady=5)
frame_birthday.grid(row=4, column=6, padx=2, pady=2)

# Label
title = Label(root, font=('Helvetica', 14), text="What do you want to start?", justify=CENTER)
title.grid(row=1, column=3, columnspan=6)

user_input = Label(frame_input, text="Enter task: ")
user_input.grid(row=3, column=4)

instruction = Label(root, text=f"Type 'help' to see the list of command\nYou can operate with me.")
instruction.grid(row=3, column=6, padx=10)

birth_labe = Label(frame_birthday,text=f"Today it's {name_of_birth} birthday")
birth_labe.grid(row=4, column=6)
# Entry
user_entry = Entry(frame_input, borderwidth=2, width=25)
user_entry.grid(row=3, column=5)
# Button
enter = Button(root, text='Enter Command', command=lambda: start_bot(user_entry.get()))
enter.grid(row=4, column=3, pady=5)

bts_exit = Button(root, text='Enter Command', command=root.quit)
bts_exit.grid(row=4, column=4, pady=5)

mainloop()
