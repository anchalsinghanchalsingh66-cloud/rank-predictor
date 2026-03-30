from tkinter import *
from tkinter import messagebox


# Function to calculate percentile and rank
def predict_rank():
    try:
        # Get user inputs
        total = int(total_entry.get())
        marks = float(marks_entry.get())
        max_marks = float(max_entry.get())

        # Validate inputs
        if total <= 0 or max_marks <= 0:
            messagebox.showerror("Input Error", "Values must be greater than 0")
            return
        if marks < 0 or marks > max_marks:
            messagebox.showerror("Input Error", "Marks must be between 0 and maximum marks")
            return

        # Calculate percentage
        percentage = (marks / max_marks) * 100

        # Estimate percentile (simple assumption)
        percentile = round(percentage, 2)

        # Estimate rank using a simple scale
        rank = int(((100 - percentage) / 100) * total)
        if rank < 1:
            rank = 1

        # Display results
        result_label.config(
            text=(
                f"Percentage: {percentage:.2f}%\n"
                f"Estimated Percentile: {percentile:.2f}\n"
                f"Predicted Rank (out of {total}): {rank}"
            )
        )

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values")

# -------------------- GUI DESIGN --------------------
root = Tk()
root.title("Rank Predictor")
root.geometry("420x380")
root.resizable(True, True)
root.configure(bg="#f3f4f6")

# Heading
Label(
    root,
    text="🎯 Rank Predictor",
    font=("Arial", 18, "bold"),
    bg="#f3f4f6",
    fg="#1e40af"
).pack(pady=15)

# Frame for input fields
frame = Frame(root, bg="#f3f4f6")
frame.pack(pady=10)

# Labels and Entry Boxes
Label(frame, text="Total Participants:", font=("Arial", 11), bg="#f3f4f6").grid(row=0, column=0, padx=8, pady=6, sticky=W)
Label(frame, text="Marks Obtained:", font=("Arial", 11), bg="#f3f4f6").grid(row=1, column=0, padx=8, pady=6, sticky=W)
Label(frame, text="Maximum Marks:", font=("Arial", 11), bg="#f3f4f6").grid(row=2, column=0, padx=8, pady=6, sticky=W)

total_entry = Entry(frame, width=22, font=("Arial", 11))
marks_entry = Entry(frame, width=22, font=("Arial", 11))
max_entry = Entry(frame, width=22, font=("Arial", 11))

total_entry.grid(row=0, column=1, padx=8, pady=6)
marks_entry.grid(row=1, column=1, padx=8, pady=6)
max_entry.grid(row=2, column=1, padx=8, pady=6)

# Button
Button(
    root,
    text="Predict Rank",
    command=predict_rank,
    bg="#60a5fa",
    fg="white",
    font=("Arial", 12, "bold"),
    width=18,
    pady=5,
    relief=RAISED
).pack(pady=15)

# Result label
result_label = Label(
    root,
    text="Enter the values and click 'Predict Rank'",
    font=("Arial", 11),
    bg="#f3f4f6",
    fg="#111827",
    justify=LEFT
)
result_label.pack(pady=10)

# Footer
Label(
    root,
    text="Created by Anchal | Python Project",
    font=("Arial", 9),
    bg="#f3f4f6",
    fg="#6b7280"
).pack(side=BOTTOM, pady=8)

root.mainloop()