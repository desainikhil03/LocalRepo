import tkinter as tk
from tkinter import filedialog, ttk, messagebox
from PIL import Image, ImageTk

class EBSDApp:
    def __init__(self, root):
        self.root = root
        self.root.title("EBSD Microstructure Analysis")
        self.root.geometry("800x500")
        self.root.configure(bg="#f0f0f0")

        # Sidebar Menu Frame (Top-Left)
        self.sidebar = tk.Frame(root, bg="#333", width=180, height=500)
        self.sidebar.pack(side="left", fill="y")

        self.menu_label = tk.Label(self.sidebar, text="☰ Menu", fg="white", bg="#333", font=("Arial", 14, "bold"))
        self.menu_label.pack(pady=10)

        self.menu_buttons = [
            ("EBSD Deep Clean", self.open_deep_clean),
            ("Future Option 1", None),
            ("Future Option 2", None),
            ("Future Option 3", None)
        ]

        for text, command in self.menu_buttons:
            btn = tk.Button(self.sidebar, text=text, font=("Arial", 12), width=18, bg="#444", fg="white",
                            relief="flat", command=command)
            btn.pack(pady=5)

        # Welcome Section
        self.main_frame = tk.Frame(root, bg="#f0f0f0")
        self.main_frame.pack(side="right", expand=True, fill="both")

        self.welcome_label = tk.Label(self.main_frame, text="Welcome to EBSD Microstructure", 
                                      font=("Arial", 16, "bold"), fg="#333", bg="#f0f0f0")
        self.welcome_label.pack(pady=30)

        self.subtitle_label = tk.Label(self.main_frame, text="AI-Based Analysis of Microstructure",
                                       font=("Arial", 12), fg="#666", bg="#f0f0f0")
        self.subtitle_label.pack()

    def open_deep_clean(self):
        # New window for EBSD Deep Clean
        deep_clean_window = tk.Toplevel(self.root)
        deep_clean_window.title("EBSD Deep Clean")
        deep_clean_window.geometry("700x550")
        deep_clean_window.configure(bg="#fff")

        tk.Label(deep_clean_window, text="EBSD Deep Clean", font=("Arial", 16, "bold"), fg="#333", bg="#fff").pack(pady=10)

        # Upload Button
        upload_button = tk.Button(deep_clean_window, text="Upload File", font=("Arial", 12), bg="#0078D7", fg="white",
                                  command=self.upload_file, width=15)
        upload_button.pack(pady=10)

        self.file_label = tk.Label(deep_clean_window, text="Upload your .ang or .ctf file here", font=("Arial", 10),
                                   fg="#666", bg="#fff")
        self.file_label.pack()

        # Placeholder for Image
        self.image_label = tk.Label(deep_clean_window, text="[Image Placeholder]", bg="gray", width=50, height=10)
        self.image_label.pack(pady=10)

        # Slider Frame
        self.slider_frame = tk.Frame(deep_clean_window, bg="#fff")
        self.slider_frame.pack()

        # Clean Button
        clean_button = tk.Button(deep_clean_window, text="CLEAN", font=("Arial", 12), bg="#28a745", fg="white",
                                 command=self.clean_image, width=15)
        clean_button.pack(pady=10)

        # Download Button
        download_button = tk.Button(deep_clean_window, text="Download Cleaned File", font=("Arial", 12), bg="#dc3545",
                                    fg="white", width=20)
        download_button.pack(pady=10)

    def upload_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("EBSD Files", "*.ang *.ctf")])
        if file_path:
            self.file_label.config(text=f"Uploaded: {file_path}")
            if file_path.endswith(".ang"):
                self.display_ang_options()
            elif file_path.endswith(".ctf"):
                self.display_ctf_options()

    def display_ang_options(self):
        for widget in self.slider_frame.winfo_children():
            widget.destroy()
        
        tk.Label(self.slider_frame, text="CI (0 to 1)", font=("Arial", 10), bg="#fff").pack()
        tk.Scale(self.slider_frame, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL).pack()

        tk.Label(self.slider_frame, text="FIT (0 to max FIT)", font=("Arial", 10), bg="#fff").pack()
        tk.Scale(self.slider_frame, from_=0, to=100, resolution=1, orient=tk.HORIZONTAL).pack()

    def display_ctf_options(self):
        for widget in self.slider_frame.winfo_children():
            widget.destroy()
        
        tk.Label(self.slider_frame, text="Band Ratio (0 to 1)", font=("Arial", 10), bg="#fff").pack()
        tk.Scale(self.slider_frame, from_=0, to=1, resolution=0.01, orient=tk.HORIZONTAL).pack()

        tk.Label(self.slider_frame, text="MAD (0 to max MAD)", font=("Arial", 10), bg="#fff").pack()
        tk.Scale(self.slider_frame, from_=0, to=100, resolution=1, orient=tk.HORIZONTAL).pack()

    def clean_image(self):
        messagebox.showinfo("Processing", "Cleaning process simulated (backend not implemented).")

if __name__ == "__main__":
    root = tk.Tk()
    app = EBSDApp(root)
    root.mainloop()
