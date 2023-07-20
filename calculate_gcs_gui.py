import tkinter as tk
from tkinter import messagebox

def calculate_gcs():
    try:
        # Get user input for eye response, verbal response, and motor response
        eye_response = int(eye_response_entry.get())
        verbal_response = int(verbal_response_entry.get())
        motor_response = int(motor_response_entry.get())

        # Validate input scores
        if not (1 <= eye_response <= 4) or not (1 <= verbal_response <= 5) or not (1 <= motor_response <= 6):
            raise ValueError("Invalid input scores. Scores should be in the range 1-4 for Eye Response, 1-5 for Verbal Response, and 1-6 for Motor Response.")

        # Calculate GCS score
        gcs_score = eye_response + verbal_response + motor_response

        # Determine GCS category
        if 13 <= gcs_score <= 15:
            gcs_category = "Mild"
        elif 9 <= gcs_score <= 12:
            gcs_category = "Moderate"
        elif 3 <= gcs_score <= 8:
            gcs_category = "Severe"
        else:
            gcs_category = "Undefined"

        # Show the results in a message box
        result_text = "Glasgow Coma Scale (GCS) Calculation:\n\n"
        result_text += "Eye Response: {}\n".format(eye_response)
        result_text += "Verbal Response: {}\n".format(verbal_response)
        result_text += "Motor Response: {}\n".format(motor_response)
        result_text += "GCS Score: {}\n".format(gcs_score)
        result_text += "GCS Category: {}".format(gcs_category)
        messagebox.showinfo("GCS Calculation Result", result_text)

    except ValueError as e:
        messagebox.showerror("Error", str(e))

# Create the main window
window = tk.Tk()
window.title("Glasgow Coma Scale (GCS) Calculator")

# Create labels and entry fields for eye response, verbal response, and motor response
eye_response_label = tk.Label(window, text="Eye Response (1-4):")
eye_response_label.pack()
eye_response_entry = tk.Entry(window)
eye_response_entry.pack()

verbal_response_label = tk.Label(window, text="Verbal Response (1-5):")
verbal_response_label.pack()
verbal_response_entry = tk.Entry(window)
verbal_response_entry.pack()

motor_response_label = tk.Label(window, text="Motor Response (1-6):")
motor_response_label.pack()
motor_response_entry = tk.Entry(window)
motor_response_entry.pack()

# Create a button to calculate the GCS score
calculate_button = tk.Button(window, text="Calculate", command=calculate_gcs)
calculate_button.pack()

# Run the GUI event loop
window.mainloop()
