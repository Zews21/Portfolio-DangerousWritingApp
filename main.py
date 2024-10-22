import tkinter as tk


class DangerousWritingApp:
    def __init__(self, root):
        root.title("Dangerous Writing App")
        root.geometry("600x400")

        # Creates the text widget
        self.text_area = tk.Text(root, font=("Arial", 14), wrap="word")
        self.text_area.pack(expand=True, fill='both')

        # Creates the timer label
        self.timer_label = tk.Label(root, text="Time left: 5 seconds", font=("Arial", 12))
        self.timer_label.pack()

        # Time limit in seconds
        self.time_limit = 5
        self.remaining_time = self.time_limit
        self.timer = None

        # Binds any key press to reset timer
        self.text_area.bind("<KeyPress>", self.reset_timer)

        # Start the timer
        self.reset_timer()

    def reset_timer(self, event=None):
        """Reset the countdown timer whenever a key is pressed."""
        if self.timer:
            self.text_area.after_cancel(self.timer)  # Cancel the previous timer

        # Reset the remaining time and start a new countdown
        self.remaining_time = self.time_limit
        self.update_timer()

    def update_timer(self):
        """Update the timer countdown every second."""
        if self.remaining_time > 0:
            self.timer_label.config(text=f"Time left: {self.remaining_time} seconds")
            self.remaining_time -= 1
            self.timer = self.text_area.after(1000, self.update_timer)  # Call this method again after 1 second
        else:
            self.delete_text()

    def delete_text(self):
        """Delete all text if time limit exceeded without typing."""
        self.text_area.delete(1.0, tk.END)
        self.timer_label.config(text="Time's up! All text deleted.")


if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()
