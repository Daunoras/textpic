from PIL import Image
import numpy

def grey(pav):
    pav = Image.open(pav)
    data = pav.getdata()
    new_data = []

    for pixel in data:
        average = int(numpy.average(pixel))
        new_pixel = (average, average, average)
        new_data.append(new_pixel)
    pav.putdata(new_data)
    pav.save('nespalvotas.jpg')


def shades(pav, n):
    pav = Image.open(pav)
    data = pav.getdata()
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
    for eil in listas:
        print(eil)
    print(n, m)

def blocks(pav, n):
    pav = Image.open(pav)
    data = pav.getdata()
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

            if rez_vk < 128:
                if rez_vd < 128:
                    if rez_ak < 128:
                        if rez_ad < 128:
                            simb = "█"
                        else:
                            simb = "▛"
                    else:
                        if rez_ad < 128:
                            simb = "▜"
                        else:
                            simb = "▀"
                else:
                    if rez_ak < 128:
                        if rez_ad < 128:
                            simb = "▙"
                        else:
                            simb = "▌"
                    else:
                        if rez_ad < 128:
                            simb = "▚"
                        else:
                            simb = "▘"
            else:
                if rez_vd < 128:
                    if rez_ak < 128:
                        if rez_ad < 128:
                            simb = "▟"
                        else:
                            simb = "▞"
                    else:
                        if rez_ad < 128:
                            simb = "▐"
                        else:
                            simb = "▝"
                else:
                    if rez_ak < 128:
                        if rez_ad < 128:
                            simb = "▄"
                        else:
                            simb = "▖"
                    else:
                        if rez_ad < 128:
                            simb = "▗"
                        else:
                            simb = "_"
            eil += simb

        listas.append(eil)
    for eil in listas:
        print(eil)
    print(n, m)


def kartu(img, n):
    shades(img, n)
    blocks(img, n)

kartu('img_2.png', 100)