"""
import datetime

now = datetime.datetime.now()
print("Поточна дата і час:", now)



date = input("Введіть дату (дд.мм.рррр): ")

try:
    d = datetime.datetime.strptime(date, "%d.%m.%Y")
    print("Дата правильна")
except:
    print("Дата неправильна")



def age(birth):
    today = datetime.datetime.now()
    years = today.year - birth.year
    return years

date = input("Введіть дату народження: ")
birth = datetime.datetime.strptime(date, "%d.%m.%Y")

print("Ваш вік:", age(birth))


d1 = input("Введіть першу дату: ")
d2 = input("Введіть другу дату: ")

date1 = datetime.datetime.strptime(d1, "%d.%m.%Y")
date2 = datetime.datetime.strptime(d2, "%d.%m.%Y")

difference = date2 - date1
print("Різниця в днях:", difference.days)


"""



import tkinter as tk
from tkinter import PhotoImage

root = tk.Tk()
root.title("ICONS FOR COMPANY")

root.geometry("640x480")
root.resizable(True, True)
root.minsize(320, 240)
root.maxsize(1920, 1080)


img1 = tk.PhotoImage(file="pngtree-illustration-of-garuda-with-indonesian-flag-emblem-png-image_13550572.png")
label_img1 = tk.Label(master=root,
                     image=img1,
                     )
label_img1.pack()

img2 = tk.PhotoImage(file="images.png")
label_img2 = tk.Label(master=root,
                     image=img2,
                     )
label_img2.pack()

img3 = tk.PhotoImage(file="images (1).png")
label_img3 = tk.Label(master=root,
                     image=img3,
                     )
label_img3.pack()

root.mainloop()