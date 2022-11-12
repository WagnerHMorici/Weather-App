from tkinter import *
from main_funcs import GetData


root = Tk()
root.title("Weather App")
root.geometry("400x200")


def get_data():
    data = GetData(token.get(), city.get())
    Label(root, text=str(data)).place(x=10, y=100, width=200, height=40)   


Label(root, text="Enter your token:").place(x=10, y=10, width=100, height=20)

token = Entry(root)
token.place(x=110, y=10, width=250, height=20)


Label(root, text="Enter the city:").place(x=20, y=40, width=100, height=20)

city = Entry(root)
city.place(x=110, y=40, width=250, height=20)


btn_get = Button(root, text="Get Weather", command=get_data)
btn_get.place(x=245, y=65, width=100, height=20)


root.mainloop()






















