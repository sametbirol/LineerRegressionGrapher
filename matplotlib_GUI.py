import tkinter as tk
import tkinter.font as tkfont
from tkinter import filedialog
import ocr
import matplotlib_process


# def on_paste(event):
#     text = event.widget.get()
#     if text != "":
#         # Get the text from the clipboard
#         clipboard_text = root.clipboard_get()

#         # Check if the clipboard text is the same as the current input value
#         if clipboard_text.strip() == text.strip():
#             return

#         # Check if the input already ends with a comma
#         if text and not text.endswith(','):
#             event.widget.insert('end', ',')

def on_paste(event):
    text = event.widget.get()
    if text != "":
        # Get the text from the clipboard
        clipboard_text = root.clipboard_get()

        # Check if the clipboard text is the same as the current input value
        if clipboard_text.strip() == text.strip():
            # Add a comma at the end of the input value if it doesn't already end with one
            if not text.endswith(','):
                root.after(1, lambda: event.widget.insert('end', ','))
            return

        # Check if the input already ends with a comma
        if text and not text.endswith(','):
            event.widget.insert('end', ',')



def open_file_dialog():
    initialdirectory = ocr.get_initial_dir()
    filepath = filedialog.askopenfilename(
        initialdir=initialdirectory, title="Select image", filetypes=[("All files", "*.*")])
    text = ocr.img_to_text(filepath)
    img_to_text_input.delete(1.0, 'end')
    img_to_text_input.insert("1.0", text)
    img_to_text_input.grid(row=7, columnspan=2)


def calculate_plot():
    xval = value_x_input.get()
    yval = value_y_input.get()
    xlabel = label_x_input.get()
    ylabel = label_y_input.get()
    m, b = matplotlib_process.polyfit_process(xval, yval, xlabel, ylabel)
    plot_input.delete(1.0, 'end')
    plot_input.insert("1.0", f"{m}*x + {b}")
    plot_input.grid(row=10, columnspan=2)


root = tk.Tk()
root.title("Lineer regression")
global_font = tkfont.Font(family="Arial", size=13)
root.option_add("*Font", global_font)
root.option_add('*padX', 10)
root.option_add('*padY', 5)

label_x = tk.Label(root, text="Enter label of x axis:")
label_x_input = tk.Entry(root)


label_y = tk.Label(root, text="Enter label of y axis:")
label_y_input = tk.Entry(root)

divider = tk.Frame(root, height=5, bd=1, relief=tk.SUNKEN)


value_x = tk.Label(root, text="Enter x values seperated by comma:")
value_x_input = tk.Entry(root)


value_y = tk.Label(root, text="Enter y values seperated by comma:")
value_y_input = tk.Entry(root)

divider1 = tk.Frame(root, height=5, bd=1, relief=tk.SUNKEN)

label_image = tk.Label(root, text="Choose image to convert:")
# label_image_input = tk.Entry(root)


img_button = tk.Button(root, text="Convert", command=open_file_dialog)
plot_button = tk.Button(root, text="Plot", command=calculate_plot)
img_to_text_input = tk.Text(root, width=50, height=10)
plot_input = tk.Text(root, height=20)
label_x.grid(row=0, column=0)
label_x_input.grid(row=0, column=1)

label_y.grid(row=1, column=0)
label_y_input.grid(row=1, column=1)

divider.grid(row=2, columnspan=2)

value_x.grid(row=3, column=0)
value_x_input.grid(row=3, column=1)

value_y.grid(row=4, column=0)
value_y_input.grid(row=4, column=1)

divider1.grid(row=5, columnspan=2)

label_image.grid(row=6, column=0)
img_button.grid(row=6, column=1)

plot_button.grid(row=8, column=0)

label_x_input.insert(0, "Vin(V)")
label_y_input.insert(0, "Vout(V)")
value_x_input.insert(0, "0.930,0.810,0.735,0.634,0.536")
value_y_input.insert(0, "1.293,1.502,1.605,2.08,2.48")
value_x_input.bind('<<Paste>>', on_paste)
value_y_input.bind('<<Paste>>', on_paste)
root.mainloop()
