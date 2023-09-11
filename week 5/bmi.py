import tkinter as tk


def calculate_bmi():
    try:
        gewicht = float(gewicht_entry.get())
        lengte = float(lengte_entry.get()) / 100  
        bmi = gewicht / (lengte * lengte)
        bmi_label.config(text=f"BMI: {bmi:.2f}")

        if bmi < 18.5:
            result_label.config(text="Ondergewicht", bg="orange")
        elif 18.5 <= bmi < 24.9:
            result_label.config(text="Goed gewicht", bg="green")
        else:
            result_label.config(text="Overgewicht", bg="orange")

    except ValueError:
        bmi_label.config(text="Voer geldige getallen in")
        result_label.config(text="", bg="white")


root = tk.Tk()
root.title("BMI Calculator")


gewicht_label = tk.Label(root, text="Gewicht (kg)")
gewicht_label.pack()
gewicht_entry = tk.Entry(root)
gewicht_entry.pack()

lengte_label = tk.Label(root, text="Lengte (cm)")
lengte_label.pack()
lengte_entry = tk.Entry(root)
lengte_entry.pack()

bereken_button = tk.Button(root, text="Bereken BMI", command=calculate_bmi)
bereken_button.pack()

bmi_label = tk.Label(root, text="", font=("Helvetica", 16))
bmi_label.pack()

result_label = tk.Label(root, text="", font=("Helvetica", 16))
result_label.pack()


root.mainloop()
