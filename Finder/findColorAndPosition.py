import tkinter as tk
import pyautogui as root
import keyboard as key
from PIL import ImageTk, Image
import os
from pathlib import Path


class MainPage(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
    
        self.title("Нахождение позиции и цвета")
        self.geometry("500x600+100+100")
        self.minsize(500, 600)
        self.maxsize(500, 600)
        self.config(bg='black')

        thisdir = os.path.dirname(__file__)
        iconFile = os.path.join(thisdir, 'icon.png')
        backGroundFile = os.path.join(thisdir, 'BackGround.jpg')
        
        self.iconphoto(False, tk.PhotoImage(file = iconFile))
        canvas = tk.Canvas(self, width= 500, height= 600)
        image = ImageTk.PhotoImage(Image.open(backGroundFile))
        canvas.create_image(0, 0, anchor = tk.NW, image = image)
        canvas.pack()
        



        #Labels
        self.textPosition = tk.Label(self,
                            text = ' ',
                            bg= 'dark grey',
                            height= 3,
                            width= 25
                            )
        self.textColor =    tk.Label(self, 
                            text = ' ',
                            bg= 'dark grey',
                            height= 3,
                            width= 25
                            )

        #Buttons
        self.checkPositionButton = tk.Button(self,
                                    text='Позиция курсора',
                                    command= self.findPositionAndColorCursor,
                                    bg= 'grey',
                                    activebackground= 'light blue',
                                    height= 2,
                                    width= 16
                                    )

        self.confirmButton =       tk.Button(self,
                                    text='Подтвердить',
                                    command= self.confirmFunction,
                                    bg= 'grey',
                                    activebackground= 'light blue',
                                    height= 1,
                                    width= 12
                                    )

        self.rebootButton =        tk.Button(self,
                                    text='↻',
                                    command= self.rebootFunction,
                                    bg= 'grey',
                                    activebackground= 'light blue',
                                    height= 1,
                                    width= 3
                                    )

        #Entrydata
        self.chooseKey = tk.Entry(self,
                        width= 8,
                        bd= 2,
                        state= tk.NORMAL
                        )

        #Labels
        self.textPosition.pack()
        self.textPosition.place(x= 0, y= 81)
        self.textColor.pack()
        self.textColor.place(x= 0, y= 150)

        #Buttons
        self.checkPositionButton.pack()
        self.checkPositionButton.place(x= 0, y= 26)
        self.confirmButton.pack()
        self.confirmButton.place(x= 136, y= 25)
        self.rebootButton.pack()
        self.rebootButton.place(x= 206, y= 60)

        #EntryData
        self.chooseKey.pack()
        self.chooseKey.place(x= 135, y= 55)

        self.mainloop()

    #Functions
    def findPositionAndColorCursor(self):
        while (True):
            if (key.is_pressed(self.selectedButton)):
                x, y = root.position()
                self.textPosition.config(text = str(root.position()))
                self.textColor.config(text = str(root.pixel(x, y)))
                break

    def confirmFunction(self):
        self.selectedButton = self.chooseKey.get()
        self.chooseKey['state'] = tk.DISABLED


    def rebootFunction(self):
        self.chooseKey['state'] = tk.NORMAL

def main():
    mw = MainPage()
    mw.mainloop()


if __name__ == "__main__":
    main()