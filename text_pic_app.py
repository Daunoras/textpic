from PIL import Image
import numpy
from tkinter import Tk, END, Label, Button, filedialog, Checkbutton, Entry, Text, DISABLED, NORMAL

class TextPicApp:
    def __init__(self, window):
        self.window = window
        self.file_name = None
        self.final_text_picture = Text(self.window)
        self.switch = False
        self.window.geometry("1000x600")

        open_button = Button(self.window, text="Select a picture", command=self.open_file)
        open_button.grid(row=0, column=0)

        self.file_name_label = Label(self.window, text="No file selected")
        self.file_name_label.grid(row=0, column=1)

        check = Checkbutton(self.window, text="Blocks", command=self.togle_switch)
        check.grid(row=1, column=0)

        row_length = Label(self.window, text="Number of symbols in a row: ")
        row_length.grid(row=2, column=0)

        self.entry_field = Entry(self.window)
        self.entry_field.grid(row=2, column=1, sticky='w')

        generate_button = Button(self.window, text="Generate", command=self.generate)
        generate_button.grid(row=3, column=0)

        self.final_text_picture.config(width=900, font="courier", height=500, state=DISABLED)
        self.final_text_picture.grid(row=4, column=0, columnspan=3)

        self.window.grid_columnconfigure(0, weight=0)
        self.window.grid_columnconfigure(1, weight=0)
        self.window.grid_columnconfigure(2, weight=1)
        self.window.grid_rowconfigure(4, weight=1)

    def togle_switch(self):
        self.switch = not self.switch

    def shades(self, image_file, row_length):
        pic = Image.open(image_file)
        length = pic.width
        height = pic.height
        list_of_rows = []
        line_amount = int((height / length) * row_length / 2.5)
        for j in range(0, line_amount):
            row = []
            for i in range(0, row_length):
                sector = pic.crop(
                    (int(i * length / row_length),
                     int(j * height / line_amount),
                     int((i + 1) * length / row_length),
                     int((j + 1) * height / line_amount))
                )
                rez = numpy.average(sector.getdata())
                if rez < 50:
                    row.append("█")
                elif rez < 101 and rez >= 50:
                    row.append("▓")
                elif rez < 151 and rez >= 100:
                    row.append("▒")
                elif rez < 201 and rez >= 150:
                    row.append("░")
                else:
                    row.append("_")
            row_str = "".join(row)
            list_of_rows.append(row_str)
        return list_of_rows

    def blocks(self, image_file, row_length):
        pic = Image.open(image_file)
        length = pic.width
        height = pic.height

        list_of_rows = []
        darkness_threshold = numpy.average(pic.getdata())
        line_amount = int((height / length) * row_length / 2.5)
        for j in range(0, line_amount):
            row = []
            for i in range(0, row_length):
                sector = pic.crop(
                    (int(i * length / row_length),
                     int(j * height / line_amount),
                     int((i + 1) * length / row_length),
                     int((j + 1) * height / line_amount))
                )
                up_left = sector.crop((0, 0, int(sector.width / 2), int(sector.height / 2),))
                avrg_up_left = numpy.average(up_left.getdata())

                up_right = sector.crop((int(sector.width / 2), 0, sector.width, int(sector.height / 2),))
                avrg_up_right = numpy.average(up_right.getdata())

                down_left = sector.crop((0, int(sector.height / 2), int(sector.width / 2),sector.height,))
                avrg_down_left = numpy.average(down_left.getdata())

                down_right = sector.crop(
                     (int(sector.width / 2),
                     int(sector.height / 2),
                     sector.width,
                     sector.height,)
                )
                avrg_down_right = numpy.average(down_right.getdata())

                symbol_array = "█▛▜▀▙▌▚▘▟▞▐▝▄▖▗_"
                symbol_index = 0
                if avrg_down_right > darkness_threshold:
                    symbol_index += 1
                if avrg_down_left > darkness_threshold:
                    symbol_index += 2
                if avrg_up_right > darkness_threshold:
                    symbol_index += 4
                if avrg_up_left > darkness_threshold:
                    symbol_index += 8
                row.append(symbol_array[symbol_index])
            row_str = "".join(row)
            list_of_rows.append(row_str)
        return list_of_rows

    def open_file(self):
        self.file_name = filedialog.askopenfilename()
        self.file_name_label.config(text=self.file_name)

    def generate(self):
        if self.file_name:
            try:
                row_length = int(self.entry_field.get())
            except ValueError:
                row_length = 50
            if self.switch == False:
                list_of_rows = self.shades(self.file_name, row_length)
            else:
                list_of_rows = self.blocks(self.file_name, row_length)

            text = "\n".join(list_of_rows)

            self.final_text_picture.config(state=NORMAL)
            self.final_text_picture.delete(1.0, END)
            self.final_text_picture.insert(END, text)
            self.final_text_picture.config(state=DISABLED)


window = Tk()
app = TextPicApp(window)
window.mainloop()