import tkinter as tk
# Source: Class Notes
# This brings in tkinter so I can build the app window and GUI.

from tkinter import messagebox
# Source: Class Notes
# This lets me show pop-up messages like warnings and confirmations.

root = tk.Tk()
# Source: Class Notes
# This creates the main app window.

root.title("Gym Progress Tracker")
root.geometry("650x750")
root.config(bg="black")
# Source: My Own Code (GUI design)
# This sets up how my app looks, like the title, size, and background color.

workout_count = 0
weekly_goal = 5
workouts = []
workout_data = []
# Source: Class Notes
# These are variables and lists used to store workout information in the program.

title_label = tk.Label(
    root,
    text="Gym Progress Tracker",
    font=("Arial", 18, "bold"),
    bg="black",
    fg="white"
)
title_label.pack(pady=10)
# Source: My Own Code (GUI design)
# This makes the big title at the top of the app.

goal_label = tk.Label(
    root,
    text="Weekly Goal: 5 workouts",
    font=("Arial", 12, "bold"),
    bg="black",
    fg="white"
)
goal_label.pack()
# Source: My Own Code (GUI design)
# This shows the weekly goal on the screen.

exercise_label = tk.Label(root, text="Workout / Exercise:", bg="black", fg="white", font=("Arial", 12))
exercise_label.pack()

exercise_entry = tk.Entry(root, width=35, font=("Arial", 12))
exercise_entry.pack(pady=5)
# Source: My Own Code (GUI design)
# This adds the label and box where the user types the exercise name.

sets_label = tk.Label(root, text="Sets:", bg="black", fg="white", font=("Arial", 12))
sets_label.pack()

sets_entry = tk.Entry(root, width=35, font=("Arial", 12))
sets_entry.pack(pady=5)
# Source: My Own Code (GUI design)
# This adds the label and box for the number of sets.

reps_label = tk.Label(root, text="Reps:", bg="black", fg="white", font=("Arial", 12))
reps_label.pack()

reps_entry = tk.Entry(root, width=35, font=("Arial", 12))
reps_entry.pack(pady=5)
# Source: My Own Code (GUI design)
# This adds the label and box for reps.

weight_label = tk.Label(root, text="Weight (lbs):", bg="black", fg="white", font=("Arial", 12))
weight_label.pack()

weight_entry = tk.Entry(root, width=35, font=("Arial", 12))
weight_entry.pack(pady=5)
# Source: My Own Code (GUI design)
# This adds the label and box for weight.

rest_label = tk.Label(root, text="Rest Time (seconds):", bg="black", fg="white", font=("Arial", 12))
rest_label.pack()

rest_entry = tk.Entry(root, width=35, font=("Arial", 12))
rest_entry.pack(pady=5)
# Source: My Own Code (GUI design)
# This adds the label and box for rest time.

count_label = tk.Label(
    root,
    text="Total Workouts Logged: 0",
    font=("Arial", 12, "bold"),
    bg="black",
    fg="white"
)
count_label.pack(pady=10)
# Source: My Own Code (Workout tracking system)
# This shows how many workouts have been added.

progress_label = tk.Label(
    root,
    text="Progress to Goal: 0/5",
    font=("Arial", 12, "bold"),
    bg="black",
    fg="white"
)
progress_label.pack(pady=5)
# Source: My Own Code (Weekly goal tracking)
# This shows progress toward the weekly goal.

suggestion_label = tk.Label(
    root,
    text="Suggestion: None yet",
    font=("Arial", 11, "bold"),
    bg="black",
    fg="yellow"
)
suggestion_label.pack(pady=5)
# Source: My Own Code (Suggestion system)
# This shows a suggestion after a workout is added.

comparison_label = tk.Label(
    root,
    text="Comparison: None yet",
    font=("Arial", 11, "bold"),
    bg="black",
    fg="lightblue",
    wraplength=600,
    justify="left"
)
comparison_label.pack(pady=5)
# Source: My Own Code (Comparison logic)
# This shows a comparison between the current workout and a past one.

workout_listbox = tk.Listbox(root, width=75, height=15, font=("Arial", 11), bg="white", fg="black")
workout_listbox.pack(pady=10)
# Source: My Own Code (Workout tracking system)
# This box displays all saved workouts in a list.

def update_progress():
    progress_label.config(text=f"Progress to Goal: {workout_count}/{weekly_goal}")
    if workout_count >= weekly_goal:
        messagebox.showinfo("Goal Reached", "Nice job! You hit your weekly workout goal!")
# Source: My Own Code (Weekly goal tracking)
# This function updates the progress label and checks if the user hit the weekly goal.

def get_progress_suggestion(exercise, reps, weight):
    for item in reversed(workout_data):
        if item["exercise"].lower() == exercise.lower():
            if weight > item["weight"]:
                return "Increase weight next time!"
            elif weight == item["weight"] and reps > item["reps"]:
                return "Good job! Try increasing weight."
            elif weight == item["weight"] and reps == item["reps"]:
                return "You matched your last workout. Try 1 more rep next time."
            else:
                return "Stay consistent or reduce weight."
    return "First time doing this exercise."
# Source: My Own Code (Suggestion system) + Python Reflex App
# This function checks older workout data and gives the user a suggestion.
# The suggestion idea is my own.
# reversed() came from the Python Reflex app source.

def get_comparison_message(exercise, reps, weight):
    for item in reversed(workout_data):
        if item["exercise"].lower() == exercise.lower():
            return f"Last {exercise}: {item['weight']} lbs x {item['reps']} reps | Now: {weight} lbs x {reps} reps"
    return f"No earlier workout found for {exercise}."
# Source: My Own Code (Comparison logic) + Python Reflex App
# This function compares the user's current workout to the last saved workout for the same exercise.
# The comparison idea is my own.
# reversed() came from the Python Reflex app source.

def add_workout():
    global workout_count

    exercise = exercise_entry.get()
    sets = sets_entry.get()
    reps = reps_entry.get()
    weight = weight_entry.get()
    rest = rest_entry.get()
    # Source: Class Notes
    # This gets what the user typed into the boxes.

    if exercise == "" or sets == "" or reps == "" or weight == "" or rest == "":
        messagebox.showwarning("Missing Info", "Please fill in all boxes.")
        return
    # Source: Class Notes
    # This checks if the user left any box empty.

    try:
        reps_val = int(reps)
        weight_val = float(weight)
    except:
        messagebox.showwarning("Error", "Enter valid numbers.")
        return
    # Source: ChatGPT
    # ChatGPT helped me understand this error handling part.
    # It makes sure reps and weight are real numbers before the program runs.

    suggestion = get_progress_suggestion(exercise, reps_val, weight_val)
    comparison_message = get_comparison_message(exercise, reps_val, weight_val)
    # Source: My Own Code
    # This calls my own suggestion and comparison functions.

    workout_text = f"{exercise} | {sets} sets x {reps} reps @ {weight} lbs | Rest: {rest} sec"
    # Source: My Own Code (Workout tracking system)
    # This turns the workout into one line of text to display and save.

    workouts.append(workout_text)
    workout_listbox.insert(tk.END, workout_text)
    # Source: Class Notes
    # This saves the workout into a list and shows it in the listbox.

    workout_data.append({
        "exercise": exercise,
        "reps": reps_val,
        "weight": weight_val
    })
    # Source: Class Notes
    # This stores workout details in a structured way so the app can compare workouts later.

    suggestion_label.config(text=f"Suggestion: {suggestion}")
    comparison_label.config(text=f"Comparison: {comparison_message}")
    # Source: My Own Code
    # This updates the suggestion and comparison labels on the screen.

    workout_count += 1
    count_label.config(text=f"Total Workouts Logged: {workout_count}")
    # Source: My Own Code (Workout tracking system)
    # This adds 1 to the workout count and updates the total label.

    update_progress()
    # Source: My Own Code (Weekly goal tracking)
    # This updates the weekly goal progress after adding a workout.

    exercise_entry.delete(0, tk.END)
    sets_entry.delete(0, tk.END)
    reps_entry.delete(0, tk.END)
    weight_entry.delete(0, tk.END)
    rest_entry.delete(0, tk.END)
    # Source: Class Notes
    # This clears the entry boxes so the user can type a new workout.

    messagebox.showinfo("Saved", "Workout added successfully!")
# Source: My Own Code (Workout tracking system)
# This is the main function that runs most of the workout app.
# It collects input, checks it, saves it, compares it, gives a suggestion, and updates the screen.

def show_last_workout():
    if len(workouts) > 0:
        messagebox.showinfo("Last Workout", workouts[-1])
    else:
        messagebox.showwarning("No Data", "No workouts logged yet.")
# Source: My Own Code (Workout tracking system)
# This shows the most recent workout if one exists.

def save_workouts():
    if len(workouts) == 0:
        messagebox.showwarning("No Data", "There are no workouts to save.")
        return

    file = open("workouts.txt", "w")
    for workout in workouts:
        file.write(workout + "\n")
    file.close()

    messagebox.showinfo("Saved File", "Your workouts were saved")
# Source: Python Reflex App
# This saves the workout list into a text file.
# The file handling part came from the Python Reflex app source.

def clear_workouts():
    global workout_count
    workout_listbox.delete(0, tk.END)
    workouts.clear()

    workout_data.clear()
    suggestion_label.config(text="Suggestion: None yet")
    comparison_label.config(text="Comparison: None yet")

    workout_count = 0
    count_label.config(text="Total Workouts Logged: 0")
    progress_label.config(text="Progress to Goal: 0/5")

    messagebox.showinfo("Cleared", "All workouts removed.")
# Source: My Own Code (Workout tracking system + Weekly goal tracking)
# This clears all saved workouts and resets the tracker back to the beginning.

add_button = tk.Button(root, text="Add Workout", command=add_workout)
add_button.pack(pady=5)

last_button = tk.Button(root, text="Show Last Workout", command=show_last_workout)
last_button.pack(pady=5)

save_button = tk.Button(root, text="Save Workouts", command=save_workouts)
save_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear Workouts", command=clear_workouts)
clear_button.pack(pady=5)
# Source: Class Notes
# These lines create the buttons and connect each one to a function.

root.mainloop()
# Source: Class Notes
# This keeps the app running so the window stays open.
