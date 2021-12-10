from tkinter import *
import serial


def open_serial():
    l_ser = serial.Serial('COM5', 115200)
    if l_ser.isOpen():
        l_ser.close()
    l_ser.open()
    print(l_ser.isOpen())
    return l_ser


ser = open_serial()


def main():
    root = Tk()
    root.title("AquaLab v0.1")
    canvas = Canvas(root, width=300, height=300)
    lbl_name = Label(canvas, text="AquaLab v0.1")
    # lbl_name = Label(canvas, text="Longevia v0.1")

    frm_manual_buttons = LabelFrame(canvas, text="Manual control")
    frm_manual_buttons_row1 = Frame(frm_manual_buttons)
    frm_manual_buttons_row2 = Frame(frm_manual_buttons)
    frm_manual_buttons_row3 = Frame(frm_manual_buttons)
    frm_manual_buttons_row4 = Frame(frm_manual_buttons)
    frm_manual_buttons_row5 = Frame(frm_manual_buttons)
    frm_manual_buttons_row6 = Frame(frm_manual_buttons)

    frm_manual_buttons_row7 = Frame(frm_manual_buttons)
    frm_manual_buttons_row8 = Frame(frm_manual_buttons)
    frm_manual_buttons_row9 = Frame(frm_manual_buttons)
    frm_manual_buttons_row10 = Frame(frm_manual_buttons)
    frm_manual_buttons_row11 = Frame(frm_manual_buttons)
    frm_manual_buttons_row12 = Frame(frm_manual_buttons)
    frm_manual_buttons_row13 = Frame(frm_manual_buttons)
    frm_manual_buttons_row14 = Frame(frm_manual_buttons)
    frm_manual_buttons_row15 = Frame(frm_manual_buttons)

    frm_manual_buttons_row16 = Frame(frm_manual_buttons)
    frm_functions = LabelFrame(canvas, text="Pre-cooked programs")

    lbl_01 = Label(frm_manual_buttons_row1, text="Control shower out")  # 4rd
    lbl_02 = Label(frm_manual_buttons_row2, text="Test drug out")
    lbl_03 = Label(frm_manual_buttons_row3, text="Test shower out")
    lbl_04 = Label(frm_manual_buttons_row4, text="Control home out")  # 2nd
    lbl_05 = Label(frm_manual_buttons_row5, text="Control drug out")
    lbl_06 = Label(frm_manual_buttons_row6, text="Test home out")

    lbl_11 = Label(frm_manual_buttons_row7, text="Test home in")
    lbl_12 = Label(frm_manual_buttons_row8, text="Test drug in")
    lbl_13 = Label(frm_manual_buttons_row9, text="Control home in")  # 1st
    lbl_14 = Label(frm_manual_buttons_row10, text="Test shower in")
    lbl_15 = Label(frm_manual_buttons_row11, text="Control drug in")
    lbl_16 = Label(frm_manual_buttons_row12, text="Control feed")
    lbl_17 = Label(frm_manual_buttons_row13, text="Test feed")
    lbl_18 = Label(frm_manual_buttons_row14, text="Control shower in")  #3rd
    lbl_19 = Label(frm_manual_buttons_row15, text="Feeder mixing")

    lbl_50 = Label(frm_manual_buttons_row16, text="Add feed")

    # BIG PUMPS
    btn011 = Button(frm_manual_buttons_row1, text="off", command=lambda: ser.write("211".encode()))
    btn021 = Button(frm_manual_buttons_row2, text="off", command=lambda: ser.write("221".encode()))
    btn031 = Button(frm_manual_buttons_row3, text="off", command=lambda: ser.write("231".encode()))
    btn041 = Button(frm_manual_buttons_row4, text="off", command=lambda: ser.write("241".encode()))
    btn051 = Button(frm_manual_buttons_row5, text="off", command=lambda: ser.write("251".encode()))
    btn061 = Button(frm_manual_buttons_row6, text="off", command=lambda: ser.write("261".encode()))

    btn010 = Button(frm_manual_buttons_row1, text="on", command=lambda: ser.write("210".encode()))
    btn020 = Button(frm_manual_buttons_row2, text="on", command=lambda: ser.write("220".encode()))
    btn030 = Button(frm_manual_buttons_row3, text="on", command=lambda: ser.write("230".encode()))
    btn040 = Button(frm_manual_buttons_row4, text="on", command=lambda: ser.write("240".encode()))
    btn050 = Button(frm_manual_buttons_row5, text="on", command=lambda: ser.write("250".encode()))
    btn060 = Button(frm_manual_buttons_row6, text="on", command=lambda: ser.write("260".encode()))

    # MINI PUMPS
    btn111 = Button(frm_manual_buttons_row7, text="off", command=lambda: ser.write("111".encode()))
    btn121 = Button(frm_manual_buttons_row8, text="off", command=lambda: ser.write("121".encode()))
    btn131 = Button(frm_manual_buttons_row9, text="off", command=lambda: ser.write("131".encode()))
    btn141 = Button(frm_manual_buttons_row10, text="off", command=lambda: ser.write("141".encode()))
    btn151 = Button(frm_manual_buttons_row11, text="off", command=lambda: ser.write("151".encode()))
    btn161 = Button(frm_manual_buttons_row12, text="off", command=lambda: ser.write("161".encode()))
    btn171 = Button(frm_manual_buttons_row13, text="off", command=lambda: ser.write("171".encode()))
    btn181 = Button(frm_manual_buttons_row14, text="off", command=lambda: ser.write("181".encode()))
    btn191 = Button(frm_manual_buttons_row15, text="off", command=lambda: ser.write("191".encode()))

    btn110 = Button(frm_manual_buttons_row7, text="on", command=lambda: ser.write("110".encode()))
    btn120 = Button(frm_manual_buttons_row8, text="on", command=lambda: ser.write("120".encode()))
    btn130 = Button(frm_manual_buttons_row9, text="on", command=lambda: ser.write("130".encode()))
    btn140 = Button(frm_manual_buttons_row10, text="on", command=lambda: ser.write("140".encode()))
    btn150 = Button(frm_manual_buttons_row11, text="on", command=lambda: ser.write("150".encode()))
    btn160 = Button(frm_manual_buttons_row12, text="on", command=lambda: ser.write("160".encode()))
    btn170 = Button(frm_manual_buttons_row13, text="on", command=lambda: ser.write("170".encode()))
    btn180 = Button(frm_manual_buttons_row14, text="on", command=lambda: ser.write("180".encode()))
    btn190 = Button(frm_manual_buttons_row15, text="on", command=lambda: ser.write("190".encode()))


    btn500 = Button(frm_manual_buttons_row16, text="+", command=lambda: ser.write("500".encode()))
    btn901 = Button(frm_functions, text="Custom schedule #1", command=lambda: ser.write("901".encode()))
    btn999 = Button(frm_functions, text="Abort", command=lambda: ser.write("111".encode()))  # delete this

    canvas.pack(padx=70, pady=40)
    lbl_name.pack()
    lbl_01.pack(side=LEFT)
    lbl_02.pack(side=LEFT)
    lbl_03.pack(side=LEFT)
    lbl_04.pack(side=LEFT)
    lbl_05.pack(side=LEFT)
    lbl_06.pack(side=LEFT)
    lbl_11.pack(side=LEFT)
    lbl_12.pack(side=LEFT)
    lbl_13.pack(side=LEFT)
    lbl_14.pack(side=LEFT)
    lbl_15.pack(side=LEFT)
    lbl_16.pack(side=LEFT)
    lbl_17.pack(side=LEFT)
    lbl_18.pack(side=LEFT)
    lbl_19.pack(side=LEFT)
    lbl_50.pack(side=LEFT)


    btn011.pack(side=LEFT)
    btn021.pack(side=LEFT)
    btn031.pack(side=LEFT)
    btn041.pack(side=LEFT)
    btn051.pack(side=LEFT)
    btn061.pack(side=LEFT)
    btn111.pack(side=LEFT)
    btn121.pack(side=LEFT)
    btn131.pack(side=LEFT)
    btn141.pack(side=LEFT)
    btn151.pack(side=LEFT)
    btn161.pack(side=LEFT)
    btn171.pack(side=LEFT)
    btn181.pack(side=LEFT)
    btn191.pack(side=LEFT)

    btn010.pack(side=LEFT)
    btn020.pack(side=LEFT)
    btn030.pack(side=LEFT)
    btn040.pack(side=LEFT)
    btn050.pack(side=LEFT)
    btn060.pack(side=LEFT)
    btn110.pack(side=LEFT)
    btn120.pack(side=LEFT)
    btn130.pack(side=LEFT)
    btn140.pack(side=LEFT)
    btn150.pack(side=LEFT)
    btn160.pack(side=LEFT)
    btn170.pack(side=LEFT)
    btn180.pack(side=LEFT)
    btn190.pack(side=LEFT)

    btn500.pack()
    btn901.pack()
    btn999.pack()

    frm_manual_buttons.pack()
    frm_manual_buttons_row1.pack()
    frm_manual_buttons_row2.pack()
    frm_manual_buttons_row3.pack()
    frm_manual_buttons_row4.pack()
    frm_manual_buttons_row5.pack()
    frm_manual_buttons_row6.pack()

    frm_manual_buttons_row7.pack()
    frm_manual_buttons_row8.pack()
    frm_manual_buttons_row9.pack()
    frm_manual_buttons_row10.pack()
    frm_manual_buttons_row11.pack()
    frm_manual_buttons_row12.pack()
    frm_manual_buttons_row13.pack()
    frm_manual_buttons_row14.pack()
    frm_manual_buttons_row15.pack()
    frm_manual_buttons_row16.pack()

    frm_functions.pack()

    root.mainloop()


if __name__ == "__main__":
    main()
