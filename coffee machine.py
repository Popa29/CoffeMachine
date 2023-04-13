from json import dumps
import tkinter
import customtkinter
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")
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
    "water": 1200,
    "milk": 800,
    "coffee": 550,
    'stash' : 0
} 
root_tk = customtkinter.CTk()  # create CTk window like the Tk window
root_tk.geometry("800x500")
root_tk.resizable(0, 0)
root_tk.title('Coffee Machine ')
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

def adminmode():
    submitbutton.configure(state="normal")
    password.configure(state="normal")
#################################################
def window_specs():
    secondary_window = customtkinter.CTkToplevel()
    secondary_window.geometry("800x250")
    secondary_window.resizable(0, 0)
    secondary_window.title("Admin Panel")
    secondary_window.configure(width=300, height=200)
    def report():
        x = dumps(resources)
        result = x[1:-1] 
        report.configure(text=result)     
    reportbtn = customtkinter.CTkButton(secondary_window,  text='Report', command = report)
    reportbtn.place(x=25, y=50)  
    submitbutton.configure(state="disabled")
    adminbutton.configure(state="disabled") 
      
    report = customtkinter.CTkLabel(secondary_window, text="", font=("Sitka", 20))
    report.place(x = 200, y = 50)


def open_secondary_window():
    password_attempt = password.get()
    if  password_attempt == 'secretpassword':
        window_specs()
        
quarter = customtkinter.CTkButton(root_tk, text= "Quarters", command =add_quarter)
quarter.place(x=600, y=75)
text = customtkinter.CTkLabel(root_tk, text=" 0", font=("Sitka", 20))
text.place(x = 268, y = 100)
def compare_coffee(output_label, balance_label, coffee_type):
    # get the cost of the coffee from the menu dictionary
    coffee_cost = MENU[coffee_type]['cost']
    
    # convert the balance label text to a float
    balance = float(balance_label.cget('text'))
    
    
    if MENU[coffee_type]['ingredients']['water'] > resources['water'] or  MENU[coffee_type]['ingredients']['milk'] > resources['milk'] or MENU[coffee_type]['ingredients']['coffee'] > resources['coffee']:
        output_label.configure(text="Not sufficient products, money refunded")
    
    elif balance == coffee_cost:
        # update the balance label
        new_balance = balance - coffee_cost
        resources['water'] -= MENU[coffee_type]['ingredients']['water']
        resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
        resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
        resources['stash'] += MENU[coffee_type]['cost']
        balance_label.configure(text="{:.2f}".format(new_balance))
        
        # update the output label
        output_label.configure(text="Here's your {}! Enjoy!".format(coffee_type))

    elif  balance > coffee_cost:
        # update the balance label
        resources['water'] -= MENU[coffee_type]['ingredients']['water']
        resources['milk'] -= MENU[coffee_type]['ingredients']['milk']
        resources['coffee'] -= MENU[coffee_type]['ingredients']['coffee']
        resources['stash'] += MENU[coffee_type]['cost']
        new_balance = balance - coffee_cost
        balance_label.configure(text="{:.2f}".format(new_balance))
        rounded_bal = round(new_balance, 2)
        output_label.configure(text=f"Enjoy your {coffee_type}! Your change is: \n {rounded_bal}".format(coffee_type))
    else:
        output_label.configure(text="Sorry, you don't have enough money \n for a {}.".format(coffee_type))
    dimes.configure(state="normal")
    quarter.configure(state="normal")
    nickles.configure(state="normal")
    pennies.configure(state="normal")


OutputL = customtkinter.CTkLabel(root_tk, text="", font=("Sitka", 20))
OutputL.place(x = 120, y = 434)
label = customtkinter.CTkLabel(root_tk, text=" Your current balance is:", font=("Sitka", 20))
label.place(x = 50, y = 100)

dimes = customtkinter.CTkButton(root_tk, text= "Dimes", command = add_dime)
dimes.place(x=600, y=175)

nickles = customtkinter.CTkButton(root_tk, text= "Nickles", command = add_nickel)
nickles.place(x=600, y=275)

pennies = customtkinter.CTkButton(root_tk, text= "Pennies", command = add_pennie)
pennies.place(x=600, y=375)

finish = customtkinter.CTkButton(root_tk, text= "Finish", command = doDisable)
finish.place(x=500, y=450)

latte = customtkinter.CTkButton(root_tk, text= "latte", command=lambda: compare_coffee(OutputL, text, "latte"))
latte.place(x=50, y=215, )
latte["state"] = 'disabled'
cappuccino = customtkinter.CTkButton(root_tk, text= "cappuccino", command=lambda: compare_coffee(OutputL, text, "cappuccino"))
cappuccino.place(x=200, y=320)
cappuccino["state"] = 'disabled'
espresso = customtkinter.CTkButton(root_tk, text= "espresso", command=lambda: compare_coffee(OutputL, text, "espresso"))
espresso.place(x=200, y=215)
espresso["state"] = 'disabled'

label = customtkinter.CTkLabel(root_tk, text=" Please choose your drink:", font=("Sitka", 20))
label.place(x = 50, y = 165)

label = customtkinter.CTkLabel(root_tk, text=" Output:", font=("Sitka", 20 ) )
label.place(x = 50, y = 430)

adminbutton = customtkinter.CTkButton(root_tk, text= "Admin mode", command = adminmode, font=("Sitka", 10 ))
adminbutton.place(x=50, y=320)
password = customtkinter.CTkEntry(root_tk, width = 175, state="disabled", font=('bold', 15)) 
password.place(x=50, y=375)
submitbutton = customtkinter.CTkButton(root_tk, text= "Submit", state="disabled",command = open_secondary_window, font=("Sitka", 15 ))
submitbutton.place(x=265, y=375)


exit_button = customtkinter.CTkButton(root_tk, text="Exit", command=root_tk.destroy)
exit_button.place(x=650, y=450)

root_tk.mainloop()