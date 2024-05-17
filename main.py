from PIL import Image
import numpy
from tkinter import Tk, END, LEFT, Listbox, Label, Button, filedialog

class Apsas:
    def __init__(self, langas):
        self.langas = langas
        self.file_name = ""
        # self.sarasas = Listbox(self.langas)
        self.sarasas = Label(self.langas)

        self.langas.geometry("1000x600")
        button = Button(self.langas, text="Select a picture", command=self.on_button_click)
        button.pack()
        self.sarasas.config(width=900, font="courier", height=500)
        self.sarasas.pack(side=LEFT)


    def grey(self, pav):
        pav = Image.open(pav)
        data = pav.getdata()
        new_data = []

        for pixel in data:
            average = int(numpy.average(pixel))
            new_pixel = (average, average, average)
            new_data.append(new_pixel)
        pav.putdata(new_data)
        pav.save('nespalvotas.jpg')


    def shades(self, pav, n):
        pav = Image.open(pav)
        ilgis = pav.width
        aukstis = pav.height
        listas = []
        m = int((aukstis / ilgis) * n / 2.5)
        for j in range(0, m):
            eil = ""
            for i in range(0, n):
                sector = pav.crop((int(i * ilgis / n), int(j * aukstis / m), int((i + 1) * ilgis / n), int((j + 1) * aukstis / m)))
                rez = numpy.average(sector.getdata())
                if rez < 50:
                    eil += "█"
                elif rez < 101 and rez >= 50:
                    eil += "▓"
                elif rez < 151 and rez >= 100:
                    eil += "▒"
                elif rez < 201 and rez >= 150:
                    eil += "░"
                else:
                    eil += "_"

            listas.append(eil)
        return listas

    def blocks(self, pav, n, rysk=127):
        pav = Image.open(pav)
        ilgis = pav.width
        aukstis = pav.height

        listas = []

        m = int((aukstis / ilgis) * n / 2.5)
        for j in range(0, m):
            eil = ""
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
                eil += simb[simb_indx]

            listas.append(eil)
        return listas

    def on_button_click(self):
        self.file_name = filedialog.askopenfilename()
        listas = self.shades(self.file_name, 200)
        # self.sarasas.insert(END, *listas)
        text = ""
        for eil in listas:
            text = text + eil + "\n"
        self.sarasas.config(text=text)


langas = Tk()
app = Apsas(langas)
langas.mainloop()