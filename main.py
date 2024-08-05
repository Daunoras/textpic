from PIL import Image
import numpy
from tkinter import Tk, END, Label, Button, filedialog, Checkbutton, Entry, Text, DISABLED, NORMAL

class Apsas:
    def __init__(self, langas):
        self.langas = langas
        self.file_name = None
        self.sarasas = Text(self.langas)
        self.switch = False
        self.langas.geometry("1000x600")

        open_button = Button(self.langas, text="Select a picture", command=self.open_file)
        open_button.grid(row=0, column=0)

        self.pavadinimas = Label(self.langas, text="No file selected")
        self.pavadinimas.grid(row=0, column=1)

        check = Checkbutton(self.langas, text="Blocks", command=self.swichas)
        check.grid(row=1, column=0)

        kiek = Label(self.langas, text="Number of symbols in a row: ")
        kiek.grid(row=2, column=0)

        self.laukas = Entry(self.langas)
        self.laukas.grid(row=2, column=1, sticky='w')

        generate_button = Button(self.langas, text="Generate", command=self.generate)
        generate_button.grid(row=3, column=0)

        self.sarasas.config(width=900, font="courier", height=500, state=DISABLED)
        self.sarasas.grid(row=4, column=0, columnspan=3)

        self.langas.grid_columnconfigure(0, weight=0)
        self.langas.grid_columnconfigure(1, weight=0)
        self.langas.grid_columnconfigure(2, weight=1)
        self.langas.grid_rowconfigure(4, weight=1)

    def swichas(self):
        self.switch = not self.switch

    def shades(self, pav, n):
        pav = Image.open(pav)
        ilgis = pav.width
        aukstis = pav.height
        listas = []
        m = int((aukstis / ilgis) * n / 2.5)
        for j in range(0, m):
            row = []
            for i in range(0, n):
                sector = pav.crop((int(i * ilgis / n), int(j * aukstis / m), int((i + 1) * ilgis / n), int((j + 1) * aukstis / m)))
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
            listas.append(row_str)
        return listas

    def blocks(self, pav, n, rysk=127):
        pav = Image.open(pav)
        ilgis = pav.width
        aukstis = pav.height

        listas = []
        rysk = numpy.average(pav.getdata())
        m = int((aukstis / ilgis) * n / 2.5)
        for j in range(0, m):
            row = []
            for i in range(0, n):
                sector = pav.crop((int(i * ilgis / n), int(j * aukstis / m), int((i + 1) * ilgis / n), int((j + 1) * aukstis / m)))
                vk = sector.crop((0, 0, int(sector.width / 2), int(sector.height / 2),))
                rez_vk = numpy.average(vk.getdata())
                vd = sector.crop((int(sector.width / 2), 0, sector.width, int(sector.height / 2),))
                rez_vd = numpy.average(vd.getdata())
                ak = sector.crop((0, int(sector.height / 2), int(sector.width / 2), sector.height,))
                rez_ak = numpy.average(ak.getdata())
                ad = sector.crop((int(sector.width / 2), int(sector.height / 2), sector.width, sector.height,))
                rez_ad = numpy.average(ad.getdata())

                simb = "█▛▜▀▙▌▚▘▟▞▐▝▄▖▗_"
                simb_indx = 0
                if rez_ad > rysk:
                    simb_indx += 1
                if rez_ak > rysk:
                    simb_indx += 2
                if rez_vd > rysk:
                    simb_indx += 4
                if rez_vk > rysk:
                    simb_indx += 8
                row.append(simb[simb_indx])
            row_str = "".join(row)
            listas.append(row_str)
        return listas

    def open_file(self):
        self.file_name = filedialog.askopenfilename()
        self.pavadinimas.config(text=self.file_name)

    def generate(self):
        if self.file_name:
            try:
                n = int(self.laukas.get())
            except ValueError:
                n = 50
            if self.switch == False:
                listas = self.shades(self.file_name, n)
            else:
                listas = self.blocks(self.file_name, n)
            text = ""
            for eil in listas:
                text = text + eil + "\n"
            self.sarasas.config(state=NORMAL)
            self.sarasas.delete(1.0, END)
            self.sarasas.insert(END, text)
            self.sarasas.config(state=DISABLED)


langas = Tk()
app = Apsas(langas)
langas.mainloop()