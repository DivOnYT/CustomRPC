from tkinter import filedialog
from tkinter.font import BOLD
from pypresence import Presence
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import time

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.titre = "Discord Personnalisated Rich Presence - Made By Div_YT"
        self.title(self.titre)
        
        x=400
        y=350
        self.resizable(height=False, width=False)
        self.geometry(f"{x}x{y}")

        menubar = Menu(self)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Credits", font=("DS-Digital bold", 15), command= self.credits)
        filemenu.add_command(label="Save Parameters", font=("DS-Digital", 15), command=self.save)
        filemenu.add_command(label="Open Parameters", font=("DS-Digital", 15), command=self.open)
        filemenu.add_command(label="Quit", font=("DS-Digital bold", 15), command=self.destroy)

        menubar.add_cascade(label="Options", menu=filemenu)
        self.config(menu=menubar)

        self.frame_text = Frame(self)
        Label(self.frame_text, text="Discord RPC - Free", font=("DS-Digital bold", 20)).grid()
        self.frame_text.grid(row=0, column=0)

        self.framePrincipal = Frame(self)

        Label(self.framePrincipal, text="Client ID : ", font=("DS-Digital", 15)).grid(row=0, column=0)
        self.client_id = Entry(self.framePrincipal, foreground="black", relief=FLAT, highlightbackground = "black", highlightcolor= "blue", highlightthickness=2)
        self.client_id.grid(row=0, column=1)

        Label(self.framePrincipal, text="Details : ", font=("DS-Digital", 15)).grid(row=1, column=0)
        self.details = Entry(self.framePrincipal, foreground="black", relief=FLAT, highlightbackground = "black", highlightcolor= "blue", highlightthickness=2)
        self.details.grid(row=1, column=1)

        Label(self.framePrincipal, text="Name Of the Large Image : ", font=("DS-Digital", 15)).grid(row=2, column=0)
        self.large_image = Entry(self.framePrincipal, foreground="black", relief=FLAT, highlightbackground = "black", highlightcolor= "blue", highlightthickness=2)
        self.large_image.grid(row=2, column=1)

        Label(self.framePrincipal, text="Name of the Small Image : ", font=("DS-Digital", 15)).grid(row=3, column=0)
        self.small_image = Entry(self.framePrincipal, foreground="black", relief=FLAT, highlightbackground = "black", highlightcolor= "blue", highlightthickness=2)
        self.small_image.grid(row=3, column=1)

        Label(self.framePrincipal, text="Large Text : ", font=("DS-Digital", 15)).grid(row=4, column=0)
        self.large_text = Entry(self.framePrincipal, foreground="black", relief=FLAT, highlightbackground = "black", highlightcolor= "blue", highlightthickness=2)
        self.large_text.grid(row=4, column=1)

        Label(self.framePrincipal, text="Buttons : ", font=("DS-Digital bold", 15)).grid(row=5, column=0)

        Label(self.framePrincipal, text="Text First Button : ", font=("DS-Digital", 15)).grid(row=6, column=0)
        self.text_first = Entry(self.framePrincipal, foreground="black", relief=FLAT, highlightbackground = "black", highlightcolor= "blue", highlightthickness=2)
        self.text_first.grid(row=6, column=1)

        Label(self.framePrincipal, text="URL of the first: ", font=("DS-Digital", 15)).grid(row=7, column=0)
        self.url_first = Entry(self.framePrincipal, foreground="black", relief=FLAT, highlightbackground = "black", highlightcolor= "blue", highlightthickness=2)
        self.url_first.grid(row=7, column=1)

        Label(self.framePrincipal, text="Text Second Button : ", font=("DS-Digital", 15)).grid(row=8, column=0)
        self.text_second = Entry(self.framePrincipal, foreground="black", relief=FLAT, highlightbackground = "black", highlightcolor= "blue", highlightthickness=2)
        self.text_second.grid(row=8, column=1)

        Label(self.framePrincipal, text="URL of the second: ", font=("DS-Digital", 15)).grid(row=9, column=0)
        self.url_second = Entry(self.framePrincipal, foreground="black", relief=FLAT, highlightbackground = "black", highlightcolor= "blue", highlightthickness=2)
        self.url_second.grid(row=9, column=1)

        self.start = Button(self.framePrincipal, text="Launch", font=("DS-Digital bold", 15), command=self.launch)
        self.start.grid(row=11, column=1)

        self.credits = Button(self.framePrincipal, text="Credits", font=("DS-Digital bold", 15), command=self.credits)
        self.credits.grid(row=11, column=0)
    

        self.framePrincipal.grid(row=1, column=0)
    
    def launch(self):
        details=self.details.get()
        large_image=self.large_image.get()
        small_image = self.small_image.get()
        large_text= self.large_text.get()
        text_first=self.text_first.get()
        url_first=self.url_first.get()
        text_second=self.text_second.get()
        url_second=self.url_second.get()

        liste = [details, large_text, text_first, text_second]
        urls =   [url_first, url_second]
        

        for mots in liste:
            if mots == details and mots == "" or mots == 0:
                details = "Discord RPC Made By Div_YT"

        for url in urls:
            if url == url_first and url == "" or url == 0:
                url_first = "https://www.google.com"
            elif url == url_second and url == "" or url == 0:
                url_second = "https://www.google.com"

        buttons = [text_first, url_first, text_second, url_second]
        text_lab1 = f"""'label': '{text_first}'"""
        text_url1 = f"""'url': '{url_first}'"""
        text_lab2 = f"""'label': '{text_second}'"""
        text_url2 = f"""'url': '{url_second}'"""
        text_bas = ""

        to_append = []
        text = [text_first, text_second]

        for texts in text:
            if texts == "":
                pass
            else:
                index = text.index(texts)
                if (url_first != 0 and index == 0) or (url_first != "" and index == 0):
                    liste = {'label': text_first, 'url': url_first}
                    to_append.append(liste)
                    """to_append.append("{"+text_lab1)
                    to_append.append(text_url1+"}")"""
                elif (url_second != 0 and index == 1) or (url_second != "" and index == 1):
                    liste = {'label': text_second, 'url': url_second}
                    to_append.append(liste)
                    """to_append.append("{"+text_lab2)
                    to_append.append(text_url2+"}")"""
                    
                """elif url_second == 0 or url_second == "" or url_first == 0 or url_first == "":
                    if len(to_append) > 2 or len(to_append) == 2:
                        pass
                    elif int(index)== 0:
                        to_append.append("{"+text_lab1+"}")
                    elif int(index) == 1:
                        to_append.append("{"+text_lab2+"}")"""

        text_bas = to_append
        """if to_append != []:
            text_bas = ", ".join(to_append)
              # ------ > buttons etc..
        text_bas = list(text_bas)
        text_bas.insert(0, "[")
        text_bas.insert(len(text_bas) + 1, "]")
        text_bas = "".join(text_bas)"""


        liste_dico = ["details", "large_image", "small_image", "large_text", "buttons", "start"]
        liste_for_rpc = [str(details), str(large_image), str(small_image), str(large_text), list(text_bas), time.time()]
        config = {}

        for mot in liste_for_rpc:
            index = liste_for_rpc.index(mot)
            if mot != 0 and mot != "" and mot != []:
                config[liste_dico[index]] = mot

    
        """if len(config) > 1:
            config = ", ".join(config)
        else:
            pass"""
        

        RPC = Presence(self.client_id.get())

        RPC.connect()
        
        RPC.update(**config)
                #details=details,
                #large_image=large_image,
                #small_image=small_image,
                #large_text=large_text,
                #buttons=[{"label": text_first, "url": url_first}, {"label": text_second, "url": url_second}],
                #start=time.time()
            

        print("<----- RPC Online ----->")
        while 1:
            a = input(">>> Quit  (Q) ---> ")
            if a == "Q" or a == "q":
                RPC.clear()
                self.destroy()
                self.quit()
                input("Exiting ...")
            time.sleep(10)
        """except:
            askyesno(f"{self.titre}", "An Error as occured. Maybe you don't have discord installed or running on your PC. You don't probably correctly completed the labels.")
        """


    def credits(self):
        askokcancel(f"{self.titre}", "This Program has Been Created By Python3 on CodeSources or Div_YT or DivOnYT(Diversité infinie) on Youtube, Thanks for your support !! \nDiv_YT")
    
    def save(self):
        filename = asksaveasfilename(title="Save Parameters", filetypes=[("Discord Custom RPC File", ".rpc")])
        id = self.client_id.get()
        details=self.details.get()
        large_image=self.large_image.get()
        small_image = self.small_image.get()
        large_text= self.large_text.get()
        text_first=self.text_first.get()
        url_first=self.url_first.get()
        text_second=self.text_second.get()
        url_second=self.url_second.get()
        message = f"""{id}\n{details}\n{large_image}\n{small_image}\n{large_text}\n{text_first}\n{url_first}\n{text_second}\n{url_second}"""
        f = open(filename + ".rpc", "w+", encoding="Utf-8")
        f.write(message)
        f.close()
        print(f"File Saved at :'{filename}'")

    def open(self):
        id = self.client_id
        details=self.details
        large_image=self.large_image
        small_image = self.small_image
        large_text= self.large_text
        text_first=self.text_first
        url_first=self.url_first
        text_second=self.text_second
        url_second=self.url_second
        filename = askopenfilename(title="Open Parameters", filetypes=[("Discord Custom RPC File", ".rpc")])
        f = open(filename, "r+", encoding="Utf-8")
        read = f.read()
        f.close()

        read = read.split("\n")
        liste = [id, details, large_image, small_image, large_text, text_first, url_first, text_second, url_second]
        self.appliqued_parameters(read, liste)


    def appliqued_parameters(self, parameters, liste):
        for value in liste:
            index = liste.index(value)
            value.delete(0, END)
            value.insert(0, parameters[index])
        print("Parameters Appliqued")


if __name__ == "__main__":
    MainApp().mainloop()