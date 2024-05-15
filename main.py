import tkinter as tk
import random
from animate_img import SimpleApp
balance = 1000
selected_color = None
bet = 0
window = tk.Tk()
def rand_number():
    global balance, selected_color, bet
    if selected_color:
        number  =  random.randint(0, 36, )
        label["text"] = f"Выпал: {("black", "red")[number % 2]}"
        if f"Выпал: {selected_color}" == label["text"]:
            balance += bet * 2 
            label["text"] += "\n WIN" 

        # else:
        #     balance -= bet
        balance_label['text'] = f'Ваш баланс: {balance}'
        bet =  0 
        bet_label['text'] = f"Ваша ствка: {bet}"
def change_color():
    global selected_color
    color_label["text"] = f"Ваш цвет: {selected_color}"
    color_label["fg"] = selected_color
def black():
    global selected_color
    selected_color = "black"
    change_color()
def red():
    global selected_color
    selected_color = "red"
    change_color()
def bet_change(number):
    global bet, balance
    if balance - number >= 0:
        balance -= number
        balance_label['text'] = f'Ваш баланс: {balance}'
        bet += number
        bet_label['text'] = f"Ваша ствка {bet}"
chips = (1, 5, 10, 25, 100)
bet_button_list = []
img_list = []
for i in range(5):
    bet_img = tk.PhotoImage(file = f"img/chip{chips[i]}.png")
    img_list.append(bet_img)
    button = tk.Button(window, command = lambda param = chips[i]: bet_change(param), image = bet_img)
    bet_button_list.append(button)
    bet_button_list[i].place(x = 150 * i + 50, y = 150)
window.geometry("1200x710")
casino_background_img = tk.PhotoImage(file="img/background.png")
window.configure(bg= "#2D572C")
# background_lable = tk.Label(window, image= casino_background_img)
# background_lable.place(x = 0, y = 0)
start_button = tk.Button(window, text = "start", command = rand_number, bg= "#ffdf33", width = 15, height= 5, font=("Arial", 15))
start_button.place(x = 555, y = 0)
label = tk.Label(window, text = "Нажмите старт", bg= "#2D572C", font= ("Arial", 15))
label.place(x  =250, y = 0)
balance_label = tk.Label(window, text = f'Ваш баланс: {balance}', bg = "#2D572C", font = ('arial', 15))
balance_label.pack(anchor='nw')
casino_wheel = tk.PhotoImage(file= "img/wheel.png")
casino_wheel.configure
# wheel_lable = tk.Label(window,  image= casino_wheel, bg= "#2D572C")
# wheel_lable.place(x = 152, y = 235)
casino_table = tk.PhotoImage(file= "img/table.png")
table_label = tk.Label(window, image= casino_table, bg= "#2D572C")
table_label.place(x  = 800, y = 15)
button_red = tk.Button(window, bg = "#ff0000", command = red)
button_red.place(x = 825, y = 310)
button_black = tk.Button(window, bg = "#000000", command = black)
button_black.place(x = 825, y = 400)
bet_label = tk.Label(window, text = f"Ваша ствка: {bet}", bg = "#2D572C", font = ('arial', 15))
bet_label.pack(anchor='nw')
color_label = tk.Label(window, text = "Ввыберите цвет", font = ('arial', 15), bg = "#2D572C")
color_label.pack(anchor='nw')
app = SimpleApp(window, "img/wheel.png")
window.title("CASINO")
window.mainloop()
