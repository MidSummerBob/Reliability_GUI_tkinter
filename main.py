import tkinter as tk
import pandas as pd

WIDTH_SET_DEFAULT = 10
FONT_NAME = "Courier"

welcome_window = tk.Tk()
welcome_window.title("Reliability Software")
welcome_window.minsize(width=600, height=400)

welcome_label = tk.Label(welcome_window, text="Welcome to our software", font=(FONT_NAME, 24, "italic"))
welcome_label.pack()
intro_label = tk.Label(welcome_window, text="Instruction of using our software is: ..."
                                            "\n1. How to use it to calculate reliability?"
                                            "\n2. What is maintenance time distribution?"
                                            "\n3. What is the cost of maintenance?"
                                            "\n4...", font=(FONT_NAME, 12))
intro_label.pack()


def to_add_comp_window():
    def generate_data():
        for number, (ent1, ent2, ent3, ent4) in enumerate(all_entries):
            print(number, ent1.get(), ent2.get(), ent3.get(), ent4.get())
            component_data = {
                "Distribution": [ent1.get()],
                "Parameter1": [ent2.get()],
                "Parameter2": [ent3.get()],
                "Parameter3": [ent4.get()],
            }
            df = pd.DataFrame(component_data)
            df.to_csv("data.csv", mode="a", index=False, header=False)

    def add_component():
        frame = tk.Frame(add_comp_window)
        frame.pack()

        tk.Label(frame, text="Distribution").grid(row=0, column=0)

        ent1 = tk.Entry(frame, width=WIDTH_SET_DEFAULT)
        ent1.grid(row=1, column=0)

        tk.Label(frame, text="parameter1").grid(row=0, column=1)

        ent2 = tk.Entry(frame, width=WIDTH_SET_DEFAULT)
        ent2.grid(row=1, column=1)

        tk.Label(frame, text="parameter2").grid(row=0, column=2)

        ent3 = tk.Entry(frame, width=WIDTH_SET_DEFAULT)
        ent3.grid(row=1, column=2)

        tk.Label(frame, text="parameter3").grid(row=0, column=3)

        ent4 = tk.Entry(frame, width=WIDTH_SET_DEFAULT)
        ent4.grid(row=1, column=3)

        all_entries.append((ent1, ent2, ent3, ent4))

    add_comp_window = tk.Toplevel(welcome_window)
    add_comp_window.minsize(width=500, height=300)
    add_comp_window.title("Add Components")

    add_button = tk.Button(add_comp_window, text="+", command=add_component)
    add_button.pack()
    back_button_1 = tk.Button(add_comp_window, text="Back", command=add_comp_window.destroy)
    back_button_1.pack()
    show_data_button = tk.Button(add_comp_window, text="Generate data", command=generate_data)
    show_data_button.pack()


all_entries = []


def to_relib_cal_window():
    relib_cal_window = tk.Toplevel()
    relib_cal_window.minsize(width=500, height=300)
    relib_cal_window.title("Calculate Reliability")

    label_1 = tk.Label(relib_cal_window, text="This is the page of reliability calculation.")
    label_1.pack()

    back_button_2 = tk.Button(relib_cal_window, text="Back", command=relib_cal_window.destroy)
    back_button_2.pack()


def to_main_cal_window():
    main_cal_window = tk.Toplevel()
    main_cal_window.minsize(width=500, height=300)
    main_cal_window.title("Calculate Maintenance")

    label_1 = tk.Label(main_cal_window, text="This is the page of maintenance calculation.")
    label_1.pack()

    back_button_2 = tk.Button(main_cal_window, text="Back", command=main_cal_window.destroy)
    back_button_2.pack()


def to_cost_window():
    cost_cal_window = tk.Toplevel()
    cost_cal_window.minsize(width=500, height=300)
    cost_cal_window.title("Calculate Maintenance")

    label_1 = tk.Label(cost_cal_window, text="This is the page of cost calculation.")
    label_1.pack()

    back_button_2 = tk.Button(cost_cal_window, text="Back", command=cost_cal_window.destroy)
    back_button_2.pack()


# Button
add_comp_button = tk.Button(welcome_window, text="Add components", command=to_add_comp_window)
add_comp_button.place(x=50, y=350)
relib_cal_button = tk.Button(welcome_window, text="Reliability", command=to_relib_cal_window)
relib_cal_button.place(x=200, y=350)
main_cal_button = tk.Button(welcome_window, text="Maintenance", command=to_main_cal_window)
main_cal_button.place(x=320, y=350)
main_cost_button = tk.Button(welcome_window, text="Cost", command=to_cost_window)
main_cost_button.place(x=450, y=350)


welcome_window.mainloop()
