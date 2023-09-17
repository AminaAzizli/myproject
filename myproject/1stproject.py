import datetime
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from PIL import Image, ImageTk
from datetime import date
import time
from time import strftime



window = tk.Tk()
window.config(bg='white')
window.geometry('1360x1000')

Heading = tk.LabelFrame(window, bd=2, relief='groove', bg='white')
Heading.place(x=0, y=0, width=1380, height=70)
name = tk.Label(Heading, text='The Online shop', font='Arial 18 bold', bg='white', fg='black')
name.grid(row=0, column=1)
photo_lozunf = tk.PhotoImage(file='icons8-spacex-starship-64 (1).png', height=64, width=64)

lozung =tk.Label(Heading,image=photo_lozunf, font='Cursive 16', bg='white', fg='black')
lozung.grid(column=3, row=0)
lab_sp = tk.Label(Heading, text='SpaceX', font='Arial 30 bold', bg='white', fg='black')
lab_sp.grid(row=0, column=5, padx=280)

produc = tk.LabelFrame(window, bd=2, relief='groove', bg='white')
produc.place(x=310, y=66, width=600, height=620)
Rate_frame = tk.LabelFrame(window, height=530, width=400)
Rate_frame.place(x=910, y=66)
ff = tk.Frame(window, height=385, width=150)
ff.place(x=1215, y=87)




#
#



notebook = ttk.Notebook(produc, height=650, width=1040)
notebook.grid(row=1, column=0)
frame1 = tk.Frame(notebook, width=500, height=600,bg='black')
frame2 = tk.Frame(notebook, width=500, height=600, bg='black')
frame3 = tk.Frame(notebook, width=500, height=600, bg='black')
frame1.grid(column=1, row=1)
frame2.grid(column=2, row=1)
frame3.grid(column=3, row=1)
notebook.add(frame1, text='WOMEN')
notebook.add(frame2, text='MEN')
notebook.add(frame3, text='ACCESSORIES')

img1 = tk.PhotoImage(file='women1.png', width=1600, height=700)
img1 = img1.subsample(3, 3)
labelforimg = tk.Label(frame1, image=img1)
labelforimg.place(x=8, y=20)

img2 = tk.PhotoImage(file='women22.png', width=1600, height=700)
img2 = img2.subsample(3, 3)
labelforimgw = tk.Label(frame1, image=img2)
labelforimgw.place(x=8, y=300)
#men
img3 = tk.PhotoImage(file='men11.png', width=1600, height=700)
img3 = img3.subsample(3, 3)
labelforimgm = tk.Label(frame2, image=img3)
labelforimgm.place(x=8, y=20)

img4 = tk.PhotoImage(file='men22.png', width=1600, height=700)
img4 = img4.subsample(3, 3)
labelforimgmm = tk.Label(frame2, image=img4)
labelforimgmm.place(x=8, y=300)
#accessories
img5 = tk.PhotoImage(file='accessorie11.png', width=1600, height=700)
img5 = img5.subsample(3, 3)
labelforimga = tk.Label(frame3, image=img5)
labelforimga.place(x=8, y=20)

img6 = tk.PhotoImage(file='accessories22.png', width=1600, height=700)
img6 = img6.subsample(3, 3)
labelforimgaa = tk.Label(frame3, image=img6)
labelforimgaa.place(x=8, y=300)


imgsp = tk.PhotoImage(file='11231.png', width=880, height=1900)
imgsp = imgsp.subsample(3, 3)
labbb = tk.Label(window, image=imgsp)
labbb.place(x=10,y=65)
#
size = ['XS', 'S', 'M', 'L', 'XL']
f1 = tk.StringVar()
f1.set('size')
size_select = ttk.Combobox(frame1, textvariable=f1, width=4)
size_select['values']=('XS', 'S', 'M', 'L', 'XL')
size_select.place(x=140, y=225)
size_select.current()

f2 = tk.StringVar()
f2.set('size')
size2 = ttk.Combobox(frame1, textvariable=f2, width=4)
size2['values']=('XS', 'S', 'M', 'L', 'XL')
size2.place(x=310, y=225)
size2.current()

f3 = tk.StringVar()
f3.set('size')
size3 = ttk.Combobox(frame1, textvariable=f3, width=4)
size3['values']=('XS', 'S', 'M', 'L', 'XL')
size3.place(x=480, y=225)
size3.current()

f4 = tk.StringVar()
f4.set('size')
size4 = ttk.Combobox(frame1, textvariable=f4, width=4)
size4['values']=('XS', 'S', 'M', 'L', 'XL')
size4.place(x=140, y=510)
size4.current()

f5 = tk.StringVar()
f5.set('size')
size5 = ttk.Combobox(frame1, textvariable=f5, width=4)
size5['values']=('XS', 'S', 'M', 'L', 'XL')
size5.place(x=310, y=510)
size5.current()

f6 = tk.StringVar()
f6.set('size')
size6 = ttk.Combobox(frame1, textvariable=f6, width=4)
size6['values']=('XS', 'S', 'M', 'L', 'XL')
size6.place(x=480, y=510)
size6.current()
##########
f7 = tk.StringVar()
f7.set('size')
size7 = ttk.Combobox(frame2, textvariable=f7, width=4)
size7['values']=('XS', 'S', 'M', 'L', 'XL')
size7.place(x=140, y=225)
size7.current()

f8 = tk.StringVar()
f8.set('size')
size8 = ttk.Combobox(frame2, textvariable=f8, width=4)
size8['values']=('XS', 'S', 'M', 'L', 'XL')
size8.place(x=310, y=225)
size8.current()

f9 = tk.StringVar()
f9.set('size')
size9 = ttk.Combobox(frame2, textvariable=f9, width=4)
size9['values']=('XS', 'S', 'M', 'L', 'XL')
size9.place(x=480, y=225)
size9.current()

f10 = tk.StringVar()
f10.set('size')
size10 = ttk.Combobox(frame2, textvariable=f10, width=4)
size10['values']=('XS', 'S', 'M', 'L', 'XL')
size10.place(x=140, y=510)
size10.current()

f11 = tk.StringVar()
f11.set('size')
size11 = ttk.Combobox(frame2, textvariable=f11, width=4)
size11['values']=('XS', 'S', 'M', 'L', 'XL')
size11.place(x=310, y=510)
size11.current()

f12 = tk.StringVar()
f12.set('size')
size12 = ttk.Combobox(frame2, textvariable=f12, width=4)
size12['values']=('XS', 'S', 'M', 'L', 'XL')
size12.place(x=480, y=510)
size12.current()
# ######

#
f16 = tk.StringVar()
f16.set('size')
size16 = ttk.Combobox(frame3, textvariable=f16, width=4)
size16['values']=('XS', 'S', 'M', 'L', 'XL')
size16.place(x=140, y=510)
size16.current()
#

texlab = tk.Label(Rate_frame,
text='Product                                             Size                 Price',
                  font='Times 10 bold')
texlab.grid()
###add item
tot =[]
prodnames = []
imenaproductov = []

def ad1():

    item = 'Womens Bomber Jacket'

    price = 140.00
    tot.append(price)
    imenaproductov.append(item)
    prodnames.append(1)
    l1 = tk.Label(Rate_frame, text=f'{item}                   {size_select.get()}                  ${price}      ',
                  font='Times 10  ', foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold', bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()





def ad2():

    item = 'Unisex Starship Pullover Hoodie'
    imenaproductov.append(item)
    price = 65.00
    tot.append(price)
    prodnames.append(1)
    l1 = tk.Label(Rate_frame, text=f'{item}     {size2.get()}                  ${price}         ',
                  font='Times 10 ', foreground='black', background='white')
    l1.grid()

    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold', bg='black', fg='white', height=0, width=20,
                     command=lambda: [l1.destroy(), rem1.destroy(), remove()])
    rem1.grid()
def ad3():
    item = 'Womens Starlink T-Shirt'
    imenaproductov.append(item)
    price = 30.00
    tot.append(price)
    prodnames.append(1)
    l1 = tk.Label(Rate_frame, text=f'{item}                {size3.get()}                     ${price}      ',
                  font='Times 10 ', foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold',  bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()
def ad4():
    item = 'Womens Starman T-Shirt'
    price = 30.00
    imenaproductov.append(item)
    tot.append(price)
    prodnames.append(1)
    l1 = tk.Label(Rate_frame, text=f'{item}              {size4.get()}                    ${price}      ',
                  font='Times 10 ', foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove',font='Times 7 bold', bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()
def ad5():
    item = 'Womens Crew Dragon T-Shirt'
    imenaproductov.append(item)
    price = 30.00
    tot.append(price)
    prodnames.append(1)
    l1 = tk.Label(Rate_frame, text=f'{item}        {size5.get()}                 ${price}        ',
                  font='Times 10 ', foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold', bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()
def ad6():
    item = 'Womens Occupy Mars T-Shirt'
    price = 30.00
    imenaproductov.append(item)
    prodnames.append(1)
    tot.append(price)
    l1 = tk.Label(Rate_frame, text=f'{item}        {size6.get()}                  ${price}        ',
                  font='Times 10 ', foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold', bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()
def ad7():
    item = 'Mens Starlink T-Shirt'
    price = 30.00
    imenaproductov.append(item)
    prodnames.append(1)
    tot.append(price)
    l1 = tk.Label(Rate_frame, text=f'{item}                  {size7.get()}                     ${price}     ',
                  font='Times 10 ', foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold', bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()
def ad8():
    item = 'Mens Nuke Mars T-Shirt'
    price = 30.00
    imenaproductov.append(item)
    prodnames.append(1)
    tot.append(price)
    l1 = tk.Label(Rate_frame, text=f'{item}                {size8.get()}                     ${price}       ',
                  font='Times 10 ', foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold', bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()
def ad9():
    item = 'Mens Falcon HeavyT-Shirt'
    price = 30.00
    imenaproductov.append(item)
    prodnames.append(1)
    tot.append(price)
    l1 = tk.Label(Rate_frame, text=f'{item}              {size9.get()}                 ${price}       ',
                  font='Times 10 ', foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold', bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()
def ad10():
    item = 'Mens Falcon 1 T-Shirt'
    price = 30.00
    imenaproductov.append(item)
    prodnames.append(1)
    tot.append(price)
    l1 = tk.Label(Rate_frame, text=f'{item}                 {size10.get()}                   ${price}',
                  font='Times 10 ', foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold', bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()
def ad11():
    item = 'Mens F9 T-Shirt'
    price = 30.00
    imenaproductov.append(item)
    prodnames.append(1)
    tot.append(price)
    l1 = tk.Label(Rate_frame, text=f'{item}                              {size11.get()}                ${price}',
                  font='Times 10 ', foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold', bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()
def ad12():
    item = 'Mens Dragon T-Shirt'
    price = 30.00
    imenaproductov.append(item)
    prodnames.append(1)
    tot.append(price)
    l1 = tk.Label(Rate_frame, text=f'{item}                    {size12.get()}                   ${price}',
                  font='Times 10 ', foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold', bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()
def ad13():
    item = 'SpaceX Journal'
    price = 30.00
    imenaproductov.append(item)
    prodnames.append(1)
    tot.append(price)
    l1 = tk.Label(Rate_frame, text=f'{item}                                                        ${price}',
                  font='Times 10 ', foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold', bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()
def ad14():
    item = 'SpaceX Water Bottle'
    price = 35.00
    imenaproductov.append(item)
    prodnames.append(1)
    tot.append(price)
    l1 = tk.Label(Rate_frame, text=f'{item}                                               ${price}',
                  font='Times 10 ', foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold', bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()
def ad15():
    item = 'Starship Poster Pack'
    price = 30.00
    imenaproductov.append(item)
    prodnames.append(1)
    tot.append(price)
    l1 = tk.Label(Rate_frame, text=f'{item}                                               ${price}',
                  font='Times 10 ', foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold', bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()
def ad16():
    item = 'F9 Cap'
    price = 25.00
    imenaproductov.append(item)
    prodnames.append(1)
    tot.append(price)
    l1 = tk.Label(Rate_frame, text=f'{item}                                            {size16.get()}                     ${price}',
                  font='Times 10 ', foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold', bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()
def ad17():
    item = 'Remove Before Flight Key Chains'
    price = 15.00
    imenaproductov.append(item)
    prodnames.append(1)
    tot.append(price)
    l1 = tk.Label(Rate_frame, text=f'{item}                           ${price}', font='Times 10 ',
                  foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold', bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()
def ad18():
    item = 'Remove Before Flight Key Chains'
    price = 15.00
    imenaproductov.append(item)
    prodnames.append(1)
    tot.append(price)
    l1 = tk.Label(Rate_frame, text=f'{item}                          ${price}', font='Times 10 ', foreground='black', background='white')
    l1.grid()
    def remove():
        tot.remove(price)
        prodnames.remove(1)
        imenaproductov.remove(item)

    rem1 = tk.Button(ff, text='Remove', font='Times 7 bold', bg='black', fg='white', height=0, width=20, command=lambda: [l1.destroy(),rem1.destroy(), remove()])
    rem1.grid()
anotherframe = tk.LabelFrame(window, height=30, width=90)
anotherframe.place(x=950, y=610)
def finish():
       onemoreframe =tk.Frame(window, height=20, width=42)
       onemoreframe.place(x=1200, y=613)
       labforfinish = tk.Label(onemoreframe, text=f'{sum(tot)     }',
                            font = 'Times 13 bold', foreground='black', background='white')
       labforfinish.place(x=0, y=0)


##








def new_frame():
    credit = tk.Frame(window, width=1355, height=660, background='light gray')
    credit.place(x=0, y=63)
    imgg = Image.open('fonepictureshipp (1).png')
    resize_image = imgg.resize((1600, 960))
    test = ImageTk.PhotoImage(resize_image)

    label1 = tk.Label(image=test)
    label1.image = test
    label1.place(x=0, y=63)

    accnametxt = tk.StringVar()
    label_name = tk.Label(window, text='Name:', font='Times 13 bold', fg='white', bg='black')
    label_name.place(x=15, y=70)
    accname = tk.Entry(window, textvariable=accnametxt, bg='white', width=30)
    accname.place(x=15, y=90)



    accsurntxt = tk.StringVar()
    label_surname = tk.Label(window, text='Surname:', font='Times 13 bold', fg='white', bg='black')
    label_surname.place(x=15, y=110)
    accsurn = tk.Entry(window, textvariable=accsurntxt, bg='white', width=30)
    accsurn.place(x=15, y=130)

    emaitxt = tk.StringVar()
    label_email = tk.Label(window, text='Email:', font='Times 13 bold', fg='white', bg='black')
    label_email.place(x=15, y=150)
    email = tk.Entry(window, textvariable=emaitxt, bg='white', width=35)
    email.place(x=15, y=175)
    #
    labpay = tk.Label(window, text='Payment', font='Cursive 15 bold', bg='black', fg='dark blue')
    labpay.place(x=30, y=200)
    #


    button_card = tk.Button(window, width=10, height=2)
    button_card.place(x=35, y=235)

    carimg = Image.open('cccard.png')
    resize_image = carimg.resize((45, 45))
    test = ImageTk.PhotoImage((resize_image))
    #button_card.config(image=test)
    label2 = tk.Label(image=test, height=35, width=45)
    label2.image = test
    label2.place(x=47, y=235)

    button_pp = tk.Button(window,bg='white', width=10, height=2)
    button_pp.place(x=125, y=235)
    ppimg = Image.open('PayPalCard-802x1024.png')
    resize_image = ppimg.resize((45, 45))
    test = ImageTk.PhotoImage((resize_image))
    # button_card.config(image=test)
    label3 = tk.Label(image=test, height=35, width=45)
    label3.image = test
    label3.place(x=130, y=235)



    lab_cnumber = tk.Label(window, text='Card Number (Secure & Encrypted)', font='Times 10 bold ', fg='white', bg='black')
    lab_cnumber.place(x=35, y=270)
    text = tk.StringVar()

    cardnum_entry = tk.Entry(window, textvariable=text, bg='white', width=35)
    cardnum_entry.place(x=35, y=290)
    #
    shipping = tk.Label(window, text='Shipping', font='Cursive 12 bold', bg='black', fg='white')
    shipping.place(x=25, y=320)
    #
    name = tk.StringVar()
    naame = tk.Label(window, text='Name', font='Cursive 10 bold', bg='black', fg='white')
    naame.place(x=25, y=349)

    enname = tk.Entry(window, textvariable=name, bg='white', width=30)
    enname.place(x=25, y=370)





    lab_location = tk.Label(window, text='Country/region:', font='Cursive 10 bold', bg='black', fg='white')
    lab_location.place(x=25, y=390)
    n = tk.StringVar()
    country_select = ttk.Combobox(window, textvariable=n, width=27)
    country_select['values']=('Azerbaijan', 'Canada', 'United Kingdom','Turkey','Germany', 'Albania', 'Angola',
                                 'Argentina','Australia', 'Austria', 'United States', 'Belarus', 'China')
    country_select.place(x=25, y=415)
    country_select.current()
    #
    settle_lab = tk.Label(window, text='Apartment, suite, etc(optional):', font='Cursive 10 bold', bg='black', fg='white')
    settle_lab.place(x=25, y=440)
    settle_text = tk.StringVar()
    settle_entry = tk.Entry(window, textvariable=settle_text, bg='white', width=32)
    settle_entry.place(x=25, y=460)
    # #
    code_name = tk.Label(window, text='Zip', font='Cursive 10 bold', bg='black', fg='white')
    code_name.place(x=25, y=480)
    code_text = tk.StringVar()
    code_entry = tk.Entry(window, textvariable=code_text, bg='white', width=32)
    code_entry.place(x=25, y=500)
    #

    labforfinish = tk.Label(window, text=f'Items                                                 {sum(prodnames)}             ',
                            font='Times 10 bold', bg='black', fg='white')
    labforfinish.place(x=600, y=90)
    labforfinishh = tk.Label(window, text=f'Total amount                                    {sum(tot)}      ',
                            font='Times 10 bold', bg='black', fg='white')
    labforfinishh.place(x=600, y=110)


    def oredered():
        if accname.get() == '':
            messagebox.showerror('Error', 'Please enter name')
        elif accsurn.get() == '':
            messagebox.showerror('Error', 'Please enter surname')
        elif cardnum_entry.get() == '':
            messagebox.showerror('Error', 'Please enter Card number')
        elif name.get() == '':
            messagebox.showerror('Error', 'Please enter name in shipping')
        elif country_select.get() == '':
            messagebox.showerror('Error', 'Please enter country/region')
        elif settle_entry.get() == '':
            messagebox.showerror('Error', 'Please enter apartment/suite')
        elif code_entry.get() == '':
            messagebox.showerror('Error', 'Please enter zip number')
        else:
            newwindow = tk.Toplevel(window, bg='light gray')
            newwindow.title('bill')
            newwindow.geometry('600x700')
            labelord = tk.Label(newwindow, text='Its ordered!', font='Times 16 bold', fg='black', bg='light gray')
            labelord.place(x=240, y=0)
            welclab = tk.Label(newwindow, text=f'Hi {accname.get()} - thanks for your order, we hope you enjoyed shopping with us ',
                           font='Times 10 bold',  fg='black', bg='light gray')
            welclab.place(x=170, y=40)
            where = tk.Label(newwindow, text='Where', font='Times 10 bold' , fg='black', bg='light gray')
            where.place(x=0, y=70)
            addr = tk.Label(newwindow, text=f'{country_select.get()}, \n{settle_entry.get()}', font='Times 10', fg='black', bg='light gray')
            addr.place(x=0, y=90)
            lbox = tk.Listbox(newwindow, height=10, width=50)
            lbox.place(x=0, y=150)

            for i in imenaproductov:
                 lbox.insert(0, i)
            lboxx = tk.Listbox(newwindow, height=10, width=60)
            lboxx.place(x=300, y=150)
            for i in tot:
                 lboxx.insert(0, i)

            subtot = tk.Label(newwindow, text=f'Subtotal: {sum(tot)} \n Delivery: 0.00 \n Discount: 0.00 \n\n Total: {sum(tot)}',
                              font='Times 10 bold', fg='black', bg='light gray')
            subtot.place(x=500, y=340)
            l1 = tk.Label(newwindow, font='Times 8 bold', fg='black', bg='light gray')
            l1.place(x=500, y=100)
            time = strftime('%H:%M:%S %p \n %x')
            l1.config(text=time)








    button_order = tk.Button(window, text='Order',font='Times 12 bold', command=oredered)
    button_order.place(x=100, y=600)

    but_back = tk.Button(Heading,text='Back',font='Times 13 bold', height=2, width=7, bg='black', fg='white', command=lambda:[credit.destroy(),
            label1.destroy(),label_name.destroy(),
            accname.destroy(), label_surname.destroy(), accsurn.destroy(), label_email.destroy(),
            email.destroy(), labpay.destroy(), button_card.destroy(), label2.destroy(),
            button_pp.destroy(), label3.destroy(),
            lab_cnumber.destroy(), cardnum_entry.destroy(), shipping.destroy(), naame.destroy(),
            enname.destroy(), lab_location.destroy(), country_select.destroy(),
            settle_lab.destroy(), settle_entry.destroy(), code_name.destroy(), code_entry.destroy(),
            labforfinish.destroy(), labforfinishh.destroy(), button_order.destroy(), but_back.destroy()
    ])  ###command
    # but_back.config(image=ph_back)
    but_back.place(x=1230, y=10)






ph_forbasketimage = tk.PhotoImage(file='shopping-bag.png')
ph_forbasketimage=ph_forbasketimage.subsample(18, 18)
but_basket = tk.Button(Heading, height=35, width=35, bg='white', command=new_frame)###command
but_basket.config(image=ph_forbasketimage)
but_basket.place(x=1250, y=15)



but1 = tk.Button(frame1, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad1)
but1.place(x=59, y=255)

but2 = tk.Button(frame1, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad2)
but2.place(x=240, y=255)

but3 = tk.Button(frame1, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad3)
but3.place(x=409, y=255)
#second part of women
but4 = tk.Button(frame1, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad4)
but4.place(x=59, y=537)

but5 = tk.Button(frame1, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad5)
but5.place(x=240, y=537)

but6 = tk.Button(frame1, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad6)
but6.place(x=409, y=537)
#men
but7 = tk.Button(frame2, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad7)
but7.place(x=59, y=255)

but8 = tk.Button(frame2, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad8)
but8.place(x=240, y=255)

but9 = tk.Button(frame2, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad9)
but9.place(x=409, y=255)
#second part of men
but10 = tk.Button(frame2, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad10)
but10.place(x=59, y=537)

but11 = tk.Button(frame2, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad11)
but11.place(x=240, y=537)

but12 = tk.Button(frame2, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad12)
but12.place(x=409, y=537)
#accessories
but13 = tk.Button(frame3, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad13)
but13.place(x=59, y=255)

but14 = tk.Button(frame3, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad14)
but14.place(x=240, y=255)

but15 = tk.Button(frame3, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad15)
but15.place(x=409, y=255)
#second part of women
but16 = tk.Button(frame3, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad16)
but16.place(x=59, y=537)

but17 = tk.Button(frame3, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad17)
but17.place(x=240, y=537)

but18 = tk.Button(frame3, text='ADD TO CART', font='Cursive 8 bold', fg='black', bg='white', command=ad18)
but18.place(x=409, y=537)

b = tk.Button(anotherframe, text='Total', font='Times 8 bold',fg='white', bg='black', width=15, command=finish)
b.place(x=0, y=0)












window.mainloop()
