import tkinter
import getcsvindex
from time import sleep
"""make a 1000x1000 pixel art canvas that is made up of 10px by 10px squares and any pixel can be replaced with another color by right clicking."""
zerozero,ofset,lmao = ([0,0],[5,5]),[0,0],[0,0]
main = tkinter.Tk()
main.title("Replace")
main.geometry("2000x2000")
canvas = tkinter.Canvas(main, width=2000, height=2000)
scrollheld = False
meowy = tkinter.Label(main, text="Loading...")
meowy.pack(pady=1)
fily = tkinter.Label(main, text="Loading...")
fily.pack(pady=0.5)
canvas.pack()
def updatelmao():
    global ofset
    ofset = [lmao[0] * zerozero[1][0], lmao[1] * zerozero[1][1]]
def replace(event):
    """replace the color of the pixel that is clicked with the color of the color picker."""
    x = (event.x - (event.x % zerozero[1][0]))
    y = (event.y - (event.y % zerozero[1][1]))
    colorr = "black"
    canvas.create_rectangle(x, y, x + zerozero[1][0], y + zerozero[1][0], fill=colorr, outline="", tag="cube")
    canvas.update()
def placeatcordsoncanvas(xx, yy, color):
    """place the color picker at the x and y cordinates on the canvas."""
    """apply dragoffset to the x and y cordinates."""
    x, y = (ofset[0] + (xx * zerozero[1][0])) - ((xx * zerozero[1][0]) % zerozero[1][0]),(ofset[1] + (yy * zerozero[1][1])) - ((yy * zerozero[1][1]) % zerozero[1][1])
    if canvas.itemcget(canvas.find_closest(x,y), "fill") != color:
        canvas.create_rectangle(x, y, x + zerozero[1][0], y + zerozero[1][0], fill=color, outline="",tag="cube")
        canvas.update()
def placeatcordsextended(x1,x2,y1,y2,color):
    x1,x2,y1,y2 = (ofset[0] + (x1 * zerozero[1][0])) - ((x1 * zerozero[1][0]) % zerozero[1][0]),(ofset[1] + (x2 * zerozero[1][1])) - ((x2 * zerozero[1][1]) % zerozero[1][1]),(ofset[0] + (y1 * zerozero[1][0])) - ((y1 * zerozero[1][0]) % zerozero[1][0]),(ofset[1] + (y2 * zerozero[1][1])) - ((y2 * zerozero[1][1]) % zerozero[1][1])
    canvas.create_rectangle(x1 + zerozero[1][0], y1 + zerozero[1][0], x2 + zerozero[1][0], y2 + zerozero[1][0], fill=color, outline="",tag="cube")
    canvas.update()
placeatcordsextended(-2,2002,-2,2002,"black")
placeatcordsextended(-1,2001,-1,2001,"white")
def applyoffset(x,y):
    xx, yy = x * zerozero[1][0], y * zerozero[1][1]
    canvas.move("cube", xx, yy)
def keychange(event):
    yeo = event.keysym
    if event.type == "2":
        if yeo == "Up":
            lmao[1] = lmao[1] + 10
            applyoffset(0,10)
        if yeo == "Down":
            lmao[1] = lmao[1] - 10
            applyoffset(0,-10)
        if yeo == "Left":
            lmao[0] = lmao[0] + 10
            applyoffset(10,0)
        if yeo == "Right":
            lmao[0] = lmao[0] - 10
            applyoffset(-10,0)
        updatelmao()
"""make a function that drag the canvas around by clicking and dragging the scroll wheel button."""
def zoom(event):
    if event.delta > 0:
        canvas.scale("cube",0, 0,1.1, 1.1)
        zerozero[1][0] = zerozero[1][0] * 1.1
        zerozero[1][1] = zerozero[1][1] * 1.1
    else:
        canvas.scale("cube",0,0, 0.9, 0.9)
        zerozero[1][0] = zerozero[1][0] * 0.9
        zerozero[1][1] = zerozero[1][1] * 0.9
    updatelmao()
filenumber = 1 # which file to load first 1-78
couny,caunt,number,lisy = False,0,0,[]
cvspath,oldsec,number,root,slep,caunt = f"{filenumber}.zip",0,0,[],0,0
while True:
    if couny == False:
        root = getcsvindex.getcsvindex("D:/Sorted files.zip","history.txt", cvspath)
        number = len(root) - 6
        print(f"{number}")
        couny = True
        print(f"loaded {filenumber}.zip")
        fily.config(text=f"loaded {filenumber}.zip")
    if caunt > number:
        caunt, couny = 0, False
        filenumber += 1
        print(f"new file loaded")
        cvspath = f"{filenumber}.zip"
        continue
    timestamp, user_id, colord, cords = root["timestamp"][caunt], root["user_id"][caunt], root["colord"][caunt], root["cords"][caunt]
    timestamp2, user_id2, colord2, cords2, = root["timestamp"][caunt + 1], root["user_id"][caunt + 1], root["colord"][caunt + 1], root["cords"][caunt + 1]
    tim1,tim2 = float(timestamp.replace(" UTC","").replace(" ","").replace(":","").replace("-","")),float(timestamp2.replace(" UTC","").replace(" ","").replace(":","").replace("-",""))
    meowy.config(text=f"{timestamp}\n{caunt}/{number}")
    slep = max(tim2,0) - max(tim1,0)
    if len(cords.split(",")) == 4:
        x1,y1,x2,y2 = int(colord.split(",")[0]),int(colord.split(",")[1]),int(colord.split(",")[2]),int(colord.split(",")[3])
        placeatcordsextended(x1,x2,y1,y2,colord)
        continue
    posi = [int(cords.split(",")[0]),int(cords.split(",")[1])]
    placeatcordsoncanvas(posi[0], posi[1], colord)
    canvas.bind("<MouseWheel>", zoom)
    main.bind("<KeyPress>", lambda event: keychange(event))
    main.bind("<KeyRelease>", lambda event: keychange(event))
    caunt += 1
