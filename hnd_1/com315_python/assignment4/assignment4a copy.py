import tkinter as tk

root = tk.Tk()
root.title('Travel Sales Man Problem')
root.geometry('500x500')



current_city_name = tk.StringVar()
first_city_distance = tk.IntVar()
second_city_distance = tk.IntVar()
third_city_distance = tk.IntVar()
fourth_city_distance = tk.IntVar()
hours = [1,2,3,4,5,6,7,8,9]

tk.Label(root, text="Travelling Salesman Problem", font=(24)).pack(fill='both', padx=50, pady=10)

tk.Label(root, text="Name of Current City").place(x=10, y=40, height=20)
current_city = tk.Entry(root, textvariable=current_city_name).place(x=170, y=40, height=20)
# Distance from current city to others
tk.Label(root, text="Distance to first City").place(x=10, y=70, height=20)
tk.OptionMenu(root, first_city_distance, *hours).place(x=170, y=70, height=20)


tk.Label(root, text="Distance to second City").place(x=10, y=100, height=20)
tk.OptionMenu(root, second_city_distance, *hours).place(x=170, y=100, height=20)

tk.Label(root, text="Distance to third City").place(x=10, y=130, height=20)
tk.OptionMenu(root, third_city_distance, *hours).place(x=170, y=130, height=20)

tk.Label(root, text="Distance to fourth City").place(x=10, y=160, height=20)
tk.OptionMenu(root, fourth_city_distance, *hours).place(x=170, y=160, height=20)


all_distances = [int(first_city_distance.get()), int(second_city_distance.get()), int(third_city_distance.get()), int(fourth_city_distance.get())]
all_city_names = ["First City", "Second City", "Third City", "Fourth City"]
all_city_names_by_mini = []
all_distances_by_min = []

def calculate():
    for i in range(len(all_distances)):
        minimum_val = min(all_distances)
        minimum_id = all_distances.index(minimum_val)
        all_distances.pop(minimum_id)
        all_distances_by_min.append(minimum_val)
        all_city_names_by_mini.append(all_city_names[minimum_id])
        all_city_names.pop(minimum_id)
    
    movement_plan()

def movement_plan():
    tk.Label(root, text="Suggested Travel Plan:").place(x=10, y=200)
    for i in range(len(all_city_names_by_mini)):
        if i == 0:
            tk.Label(root, text=all_city_names_by_mini[i]).place(x=30, y=220, height=20)
        elif i == 1:
            tk.Label(root, text=all_city_names_by_mini[i]).place(x=30, y=250, height=20)
        elif i == 2:
            tk.Label(root, text=all_city_names_by_mini[i]).place(x=30, y=280, height=20)
        elif i == 3:
            tk.Label(root, text=all_city_names_by_mini[i]).place(x=30, y=310, height=20)



tk.Button(root, text='Calculate', command=calculate).place(x=200, y=190, height=20)


root.mainloop()
