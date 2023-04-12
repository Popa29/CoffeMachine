MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {  
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    'stash' : 0
}
import tkinter 
top = tkinter.Tk()
top.geometry("800x500")
top.resizable(0, 0)

top.title('Coffee Machine ')

def add_quarter():
    # get the current value of the label and convert it to a float
    current_value = float(text.cget("text"))
    new_value = current_value + 0.25
    # update the label text to the new value
    text.configure(text="{:.2f}".format(new_value))
def add_dime():
    # get the current value of the label and convert it to a float
    current_value = float(text.cget("text"))
    new_value = current_value + 0.1
    # update the label text to the new value
    text.configure(text="{:.2f}".format(new_value))
def add_nickel():
    # get the current value of the label and convert it to a float
    current_value = float(text.cget("text"))
    new_value = current_value + 0.05
    # update the label text to the new value
    text.configure(text="{:.2f}".format(new_value))

def add_pennie():
    # get the current value of the label and convert it to a float
    current_value = float(text.cget("text"))
    new_value = current_value + 0.01
    # update the label text to the new value
    text.configure(text="{:.2f}".format(new_value))

def doDisable():
    dimes.configure(state="disabled")
    quarter.configure(state="disabled")
    nickles.configure(state="disabled")
    pennies.configure(state="disabled")
    latte.configure(state="normal")
    espresso.configure(state="normal")
    cappuccino.configure(state="normal")

from json import dumps


def adminmode():
    submitbutton.configure(state="normal")
    password.configure(state="normal")
#################################################
def window_specs():
    secondary_window = tkinter.Toplevel()
    secondary_window.geometry("350x400")
    secondary_window.title("Admin Panel")
    secondary_window.config(width=300, height=200)
    def report():
        x = dumps(resources)

        result = x[1:-1] 
        report.configure(text=result)     
    reportbtn = tkinter.Button(secondary_window, height=3, width=10,  text='Report', command = report)
    reportbtn.place(x=25, y=50)  
    submitbutton.configure(state="disabled")
    adminbutton.configure(state="disabled") 
      
    report = tkinter.Label(secondary_window, text="", font=("Times New Roman", 15))
    report.place(x = 150, y = 68)


def open_secondary_window():
    password_attempt = password.get()
    if  password_attempt == 'secretpassword':
        window_specs()
        
quarter = tkinter.Button(top, text= "Quarters",height=4, width=17, command =add_quarter)
quarter.place(x=600, y=75)
text = tkinter.Label(top, text=" 0", font=("Times New Roman", 15))
text.place(x = 268, y = 100)
def compare_coffee(output_label, balance_label, coffee_type):
    # get the cost of the coffee from the menu dictionary
    coffee_cost = MENU[coffee_type]['cost']
    
    # convert the balance label text to a float
    balance = float(balance_label.cget('text'))
    
    
    if MENU[coffee_type]['ingredients']['water'] > resources['water'] or  MENU[coffee_type]['ingredients']['milk'] > resources['milk'] or MENU[coffee_type]['ingredients']['coffee'] > resources['coffee']:
        output_label.config(text="Not sufficient products, money refunded")
    
    elif balance == coffee_cost:
        # update the balance label
        new_balance = balance - coffee_cost
        resources['water'] -= MENU[coffee_type]['ingredients']['water']
        resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
        resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
        resources['stash'] += MENU[coffee_type]['cost']
        balance_label.config(text="{:.2f}".format(new_balance))
        
        # update the output label
        output_label.config(text="Here's your {}! Enjoy!".format(coffee_type))

    elif  balance > coffee_cost:
        # update the balance label
        resources['water'] -= MENU[coffee_type]['ingredients']['water']
        resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
        resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
        resources['stash'] += MENU[coffee_type]['cost']
        new_balance = balance - coffee_cost
        balance_label.config(text="{:.2f}".format(new_balance))
        rounded_bal = round(new_balance, 2)
        output_label.config(text=f"Enjoy your {coffee_type}! Your change is: \n {rounded_bal}".format(coffee_type))
    else:
        output_label.config(text="Sorry, you don't have enough money \n for a {}.".format(coffee_type))
    dimes.configure(state="normal")
    quarter.configure(state="normal")
    nickles.configure(state="normal")
    pennies.configure(state="normal")


OutputL = tkinter.Label(top, text="", font=("Times New Roman", 15))
OutputL.place(x = 120, y = 430)
label = tkinter.Label(top, text=" Your current balance is:", font=("Times New Roman", 15))
label.place(x = 50, y = 100)

dimes = tkinter.Button(top, text= "Dimes",height=4, width=17, command = add_dime)
dimes.place(x=600, y=175)

nickles = tkinter.Button(top, text= "Nickles",height=4, width=17, command = add_nickel)
nickles.place(x=600, y=275)

pennies = tkinter.Button(top, text= "Pennies",height=4, width=17, command = add_pennie)
pennies.place(x=600, y=375)

finish = tkinter.Button(top, text= "Finish",height=2, width=20, command = doDisable)
finish.place(x=550, y=450)

latte = tkinter.Button(top, text= "latte",height=5, width=10, command=lambda: compare_coffee(OutputL, text, "latte"))
latte.place(x=50, y=215)
latte["state"] = 'disabled'
cappuccino = tkinter.Button(top, text= "cappuccino",height=5, width=10, command=lambda: compare_coffee(OutputL, text, "cappuccino"))
cappuccino.place(x=50, y=320)
cappuccino["state"] = 'disabled'
espresso = tkinter.Button(top, text= "espresso",height=5, width=10, command=lambda: compare_coffee(OutputL, text, "espresso"))
espresso.place(x=155, y=215)
espresso["state"] = 'disabled'

label = tkinter.Label(top, text=" Please choose your drink:", font=("Times New Roman", 15))
label.place(x = 50, y = 165)

label = tkinter.Label(top, text=" Output:", font=("Times New Roman", 15))
label.place(x = 50, y = 430)

adminbutton = tkinter.Button(top, text= "Admin \n mode",height=2, width=5, command = adminmode, font=("Times New Roman", 10 ))
adminbutton.place(x=150, y=320)
password = tkinter.Entry(width = 13, state="disabled", font=('bold', 11)) 
password.place(x=150, y=375)
submitbutton = tkinter.Button(top, text= "Submit",height=1, width=4, state="disabled",command = open_secondary_window, font=("Times New Roman", 8 ))
submitbutton.place(x=265, y=375)


exit_button = tkinter.Button(top, text="Exit", command=top.destroy)
exit_button.place(x=725, y=460)

top.mainloop()