"""
import datetime

date_time = datetime.datetime(2026,
                              3,
                              7,
                              hour=16,
                              minute=17,
                              second=34,
                              microsecond=584)
print(f"object datetime:\n\t{date_time}")
print(f"method datetime:\n\t{date_time.date()}")
print(f"type (date_time):\n\t{type(date_time)}")
print(f"method time:\n\t{date_time.time()}")
print(f"type(time):\n\t{type(date_time.time())}")

print()

date_1 = datetime.date(2026, 3, 7)
time_1 = datetime.time(16, 30, 45)
print(f"date: {date_1}, \ntype time: {type(date_1)}")
print(f"time: {time_1}, \ntype time: {type(time_1)}")


date_time_2 = datetime.datetime.combine(date_1, time_1)
print(f"date: {date_time_2}, \ntype time: {type(date_time_2)}")

print(f"new date: {date_time_2.replace(2020, 10, 25)}")
print(f"date_time_2: {date_time_2}")  #!!!!

x = date_time_2.replace(2020, 10, 25)
print(f"x: {x}")

date_now = datetime.datetime.now()
print(f"date_now: {date_now}")

date_today = datetime.date.today()
print(f"date_today: {date_today}")

date_date_today = datetime.date.today()
print(f"date_date_today: {date_date_today}")

print(f"time now: {date_now.time()}")

print(f"weekday(): {date_now.weekday()}")
print(f"isoweekday(): {date_now.isoweekday()}")

date_now = datetime.datetime.now()
time_stamp = date_now.timestamp()
print(f"time_stamp: {time_stamp}")
print(f"fromtimestamp(): {date_now.fromtimestamp(time_stamp)}")


date_now = datetime.datetime.now()
print(f"date_time to str: {date_now.strftime('%d/%m/%Y %H:%M:%S')}")
print(f"date to str: {date_now.strftime('%d/%m/%Y %A %B')}")
print(f"date to str: {date_now.strftime('%H:%M:%S')}")

date_now = datetime.datetime.now()
print(f"date_now: {date_now}")
delta = datetime.timedelta(days = 20,
                           hours = 16,
                           weeks = 5)
print(f"delta: {delta}")
date_future = date_now + delta
print(date_future)
print(f"day week: {date_future.strftime('%A')}")
"""





import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("GUI tkinter")
#root.iconbitmap("image.ico")
root.geometry("640x480")
root.resizable(True, True)
root.minsize(320, 240)
root.maxsize(1920, 1080)

label_title = tk.Label(root, text="Hello students!",
                       font=("Arial", 18, "bold italic"),
                       fg='#980B25',
                       bg='#FABDC8',
                       width=20,
                       height=3,
                       anchor="center",# n.e.s.w ne.nw.se.sw...
                       relief="solid", #solid,raised,sunken,flat,ridge,groove
                       bd=2,
                       justify="center", #CENTER.TOP.LEFT.RIGHT.BOTTOM
                       )
label_title.pack()

button_play = tk.Button(master=root,
                        text="Click Me!",
                        font=("Arial", 18, "bold italic"),
                        fg='#752380',
                        bg='#EBC7F0',
                        width=20,
                        height=3,
                        anchor="center",
                        relief="solid",
                        bd=2,
                        justify="center")
button_play.pack()

img = tk.PhotoImage(file="c7fabcfab6ac48be82906ac67ca3b623.png")
label_img = tk.Label(master=root,
                     image=img,
                     )
label_img.pack()

root.mainloop()





