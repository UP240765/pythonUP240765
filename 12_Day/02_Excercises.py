import random as rd
import string as st

#Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array
def list_of_hexa_colors(n):
    char = st.ascii_letters[:6] + st.digits
    listHex = []
    hx = '#'
    for i in range(n):
        for x in range(6):
            num = rd.randint(0,len(char)-1)
            hx += char[num]
        listHex.append(hx)
        hx = '#'
    return listHex

#Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(n):
    rgbList = []
    for i in range(n):
        r = rd.randint(0,255)
        g = rd.randint(0,255)
        b = rd.randint(0,255)
        rgb = f'rgb({r},{g},{b})'
        rgbList.append(rgb)
    return rgbList

#Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(colorType,n):
    if colorType.upper() == "HEX":
        hx = list_of_hexa_colors(n)
        return hx

    elif colorType.upper() == "RGB":
        rgb = list_of_rgb_colors(n)
        return rgb

    else:
        print(f"Color type no valid")

