# MIT License
# -*- coding: utf-8 -*-
import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno, showinfo, showwarning
import dictionary


class App(tk.Tk):

    def __init__(self):
        super().__init__()

        # main properties of the app
        self.title('Word Finder')
        self.iconbitmap('./word_finder/icons/dict.ico')
        self.iconbitmap()
        self.size(350,300)
        self.main_screen()


    def size(self,window_width,window_height):
        # get the screen dimension
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # find the center point
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2 - 100)

        # set the position of the window to the center of the screen
        self.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
        self.resizable(False, False)


    def main_screen(self):
        # special placement features
        self.special_padd1 = {'padx': 5, 'pady': 2.5}
        self.special_padd2 = {'padx': 5, 'pady': 5}

        # image used in the start button
        self.str_image = tk.PhotoImage(file='./word_finder/images/start.png')

        # features of main page contents 
        self.main_frame = tk.Frame(self,bg="Lavender")
        self.title_frame = tk.Frame(self.main_frame,bg="Lavender")
        self.main_title = tk.Label(self.title_frame, text="Welcome to the Word Finder Game!", bg="indigo", fg="Lavender", anchor=tk.CENTER, font=("Helvetica", 12))
        self.main_title.pack(expand=True,fill=tk.BOTH)

        self.msg_frame = tk.Frame(self.main_frame,bg="Lavender")
        self.main_msg = tk.Label(self.msg_frame, text="You must guess the word correctly\n\nto win the game.\n\nLet's start guessing.",bg="darkblue",fg="Lavender",font=("Helvetica", 12))
        self.main_msg.pack(expand=True,fill=tk.BOTH)

        self.btn_frame = tk.Frame(self.main_frame,bg="darkgreen")
        self.emp = tk.Label(self.btn_frame,font=("Helvetica", 1),bg="darkgreen")
        self.emp.pack()
        self.btn_msg = tk.Label(self.btn_frame, text="Please press the button to start.",bg="darkgreen",fg="Lavender",font=("Helvetica", 12))
        self.btn_msg.pack(expand=True,fill=tk.BOTH)

        # features of the start button 
        self.str_btn = tk.Button(self.btn_frame,image=self.str_image,bg="Lavender",command=self.start,activebackground="Thistle",cursor="hand2")
        self.str_btn.pack(expand=True,fill=tk.BOTH,padx=100,pady=5)
        
        # placement settings of begin and quit buttons
        self.title_frame.pack(expand=True,fill=tk.BOTH,**self.special_padd1)
        self.msg_frame.pack(expand=True,fill=tk.BOTH,**self.special_padd1)
        self.btn_frame.pack(expand=True,fill=tk.BOTH,**self.special_padd1)
        self.main_frame.pack(expand=True,fill=tk.BOTH)


    def start(self):
        # resizing for app screen
        self.size(380,280)

        # describing guess rights
        self.guess_right = 6
        self.line = 0
    
        # destroying main screen contents
        self.main_frame.destroy()
        self.title_frame.destroy()
        self.msg_frame.destroy()
        self.btn_frame.destroy()

        # features of app page frame 
        self.app_frame = tk.Frame(self,bg="Lavender")

        # calling essential functions
        self.rand_kelime()

        self.top_frame_func()

        self.bottom_frame_func()
        
        # placement settings of app frame
        self.app_frame.pack(fill=tk.BOTH,expand=True)

        
    def rand_kelime(self):
        # choice the word and meaning from dictionary database randomly
        self.word, self.mean = random.choice(list(dictionary.my_dict.items()))
        

    def top_frame_func(self):
        # features of the top frames
        self.top_frame = tk.Frame(self.app_frame,bg="SteelBlue")
        self.topleft_frame = tk.Frame(self.top_frame,bg="SteelBlue")
        self.toplefttop_frame = tk.Frame(self.topleft_frame,bg="SteelBlue")
        self.topleftcenter_frame = tk.Frame(self.topleft_frame,bg="SteelBlue")
        self.topleftbottom_frame = tk.Frame(self.topleft_frame,bg="SteelBlue")
        self.topright_frame= tk.Frame(self.top_frame,bg="SteelBlue")

        # features of the text message
        self.guess_msg = tk.Label(self.toplefttop_frame, text="Please enter the word\nyou would guess.",bg="SteelBlue",fg="Lavender",font=("Helvetica", 15))
        self.guess_msg.pack(fill=tk.BOTH,expand=True)

        # entering the number to guess
        self.guess_text = tk.Text(self.topleftcenter_frame,width=5,height=1,font=("Helvetica", 20),fg="SteelBlue",bg="Lavender")
        self.guess_text.pack(fill=tk.X,expand=True,side=tk.LEFT,padx=10)

        # features of the guess button
        self.guess_image = tk.PhotoImage(file='./mystery_number/images/guess.png')
        self.guess_btn = tk.Button(self.topleftcenter_frame,image=self.guess_image,bg="SteelBlue",activebackground="SteelBlue",bd=0,cursor="hand2",command=self.guess)
        self.guess_btn.pack(expand=True,side=tk.LEFT)

        # showing the remaining guess right text
        self.guess_msg = tk.Label(self.topleftbottom_frame, text="You have "+str(self.guess_right)+ " guess rights!",bg="SteelBlue",fg="Lavender",font=("Helvetica", 15))
        self.guess_msg.pack(fill=tk.BOTH,expand=True)


        # features of the textbox 
        self.guess_textbx = tk.Text(self.topright_frame,height=5,width=5,font=("Helvetica", 25),bg="Lavender",fg="red")
        self.guess_textbx.pack(fill=tk.BOTH,expand=True,**self.special_padd1)

        # placement of the top frames
        self.top_frame.pack(fill=tk.BOTH,side=tk.TOP,**self.special_padd1,expand=True)
        self.topleft_frame.pack(fill=tk.BOTH,side=tk.LEFT)
        self.toplefttop_frame.pack(fill=tk.BOTH,side=tk.TOP,expand=True)
        self.topleftcenter_frame.pack(fill=tk.BOTH,side=tk.TOP,expand=True)
        self.topleftbottom_frame.pack(fill=tk.BOTH,side=tk.BOTTOM,expand=True)
        self.topright_frame.pack(fill=tk.BOTH,side=tk.RIGHT,expand=True)

    
    def bottom_frame_func(self):
        # features of the buttom frame
        self.bottom_frame= tk.Frame(self.app_frame,bg="Teal")
        self.bottomtop_frame = tk.Frame(self.bottom_frame,bg="Teal")

        # special placement features
        self.special_font1 = {'fg': "Teal",'bg':"Lavender",'justify':tk.CENTER,"highlightbackground":"Lavender"}

        # features of the numbers in the guess number 
        self.first_num = tk.Entry(self.bottomtop_frame,width=1,font=("Helvetica", 30), **self.special_font1)
        self.first_num.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,**self.special_padd2)
        self.second_num = tk.Entry(self.bottomtop_frame,width=1,font=("Helvetica", 30), **self.special_font1)
        self.second_num.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,**self.special_padd2)
        self.third_num = tk.Entry(self.bottomtop_frame,width=1,font=("Helvetica", 30), **self.special_font1)
        self.third_num.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,**self.special_padd2)
        self.forth_num = tk.Entry(self.bottomtop_frame,width=1,font=("Helvetica", 30), **self.special_font1)
        self.forth_num.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,**self.special_padd2)
        self.fifth_num = tk.Entry(self.bottomtop_frame,width=1,font=("Helvetica", 30), **self.special_font1)
        self.fifth_num.pack(fill=tk.BOTH,side=tk.LEFT,expand=True,**self.special_padd2)

        # placement of the buttom frames
        self.bottomtop_frame.pack(fill=tk.BOTH,expand=True)
        self.bottom_frame.pack(fill=tk.BOTH,side=tk.TOP,expand=True,**self.special_padd1)

    
    def guess(self):
        # calling essential functions
        self.ret()

        self.main()


    def ret(self):
        # deleting contents inside the guess letters
        self.first_num.delete(0,tk.END)
        self.second_num.delete(0,tk.END)
        self.third_num.delete(0,tk.END)
        self.forth_num.delete(0,tk.END)
        self.fifth_num.delete(0,tk.END)

        # painting red the guess letters background
        self.first_num.configure(bg="red")
        self.second_num.configure(bg="red")
        self.third_num.configure(bg="red")
        self.forth_num.configure(bg="red")
        self.fifth_num.configure(bg="red")


    def main(self):
        # creating the empty array for guess word
        self.guess_arr = []
        
        # inserting the letters in the guess word to array
        for i in self.guess_text.get("1.0",tk.END):
            self.guess_arr.append(i)   

        # when there is no any guess word
        if len(self.guess_text.get("1.0",tk.END).strip()) == 0:
            showwarning(
                title='Warning',
                message='Please guess any word!')
            self.guess_text.delete("1.0",tk.END)
            return False
        
        # when the guess word does not have five letters
        elif len(self.guess_text.get("1.0",tk.END).strip()) != 5:
            showwarning(
                title='Warning',
                message="Please guess a five digit word!")
            self.guess_text.delete("1.0",tk.END)
            return False
        
        # when the guess number is not alphabetic
        elif self.guess_text.get("1.0",tk.END).strip().isalpha() == 0:
            showwarning(
                title='Warning',
                message='Please guess any word!')
            self.guess_text.delete("1.0",tk.END)
            return False

        # when the word does not make sense 
        elif self.guess_text.get("1.0",tk.END).strip() not in list(dictionary.my_dict.keys()):
            showwarning(
                title='Warning',
                message='Please guess a word found in the dictionary!')
            self.guess_text.delete("1.0",tk.END)
            return False
        
        # when the word does not have big letter 
        elif self.guess_text.get("1.0",tk.END).strip().isupper() == 0:
            showwarning(
                title='Warning',
                message='Please use capital letters!')
            self.guess_text.delete("1.0",tk.END)
            return False
        
        else:
            # when the guess word already exists in the textbox
            if(self.guess_text.get("1.0",tk.END) in self.guess_textbx.get("1.0",tk.END)):
                showinfo(
                    title='Warning',
                    message='You guessed this word before!')
                self.guess_text.delete("1.0",tk.END)
                return False
            else:
                # calling the essential function
                self.paint_letter()
                
                # emptying the guess word input 
                self.guess_text.delete("1.0",tk.END)
                
                # inserting the letters of the guess word into the entry boxes
                self.first_num.insert(tk.END,self.guess_arr[0])
                self.second_num.insert(tk.END,self.guess_arr[1])
                self.third_num.insert(tk.END,self.guess_arr[2])
                self.forth_num.insert(tk.END,self.guess_arr[3])
                self.fifth_num.insert(tk.END,self.guess_arr[4])  
            
            # calling the essential function
            self.paint()


    def paint_letter(self):
        # creating the empty array for the letters of the guess word
        self.txt_arr = []

        # determining the lines in textbox
        self.line +=1

        # adding the letters of the guess word to empty array
        for i in self.guess_text.get('1.0',tk.END):
            self.txt_arr.append(i)

        # inserting the guess word to the textbox
        self.guess_textbx.insert(tk.END, self.guess_text.get('1.0',tk.END))
        
        for i in range(len(self.word)):
            self.count2 = 0
            for j in range(len(self.word)):
                if self.word[j] == self.txt_arr[j]:
                    self.count2 += 1

                # painting blue when the guess letters are not equal but has to the random word in the textbox
                if self.txt_arr[j] in self.word[i] and self.txt_arr[i] != self.word[i] and self.word[j] != self.txt_arr[j]:
                    self.count2 += 1
                    self.guess_textbx.tag_add("blue1", str(self.line) + "." + str(self.txt_arr.index(self.txt_arr[j],j,len(self.word))), str(self.line) + "." + str(self.txt_arr.index(self.txt_arr[j],j,len(self.word))+1))
                    self.guess_textbx.tag_config("blue1",foreground="blue")
                
                # painting red when the guess letters already have in the random word in the textbox
                if self.count2 > self.word.count(self.word[i]) and self.txt_arr.count(self.txt_arr[j])>self.word.count(self.txt_arr[j]):
                    self.guess_textbx.tag_add("red1", str(self.line) + "." + str(self.txt_arr.index(self.txt_arr[j],j,len(self.word))), str(self.line) + "." + str(self.txt_arr.index(self.txt_arr[j],j,len(self.word))+1))
                    self.guess_textbx.tag_config("red1",foreground="red")                    

        for i in range(len(self.word)):
            # painting darkgreen when the guess letters equal to the random word letters in the textbox
            if self.word[i] == self.guess_arr[i]:
                self.guess_textbx.tag_add("darkgreen", str(self.line) + "."+ str(self.txt_arr.index(self.txt_arr[i],i,len(self.word))), str(self.line) + "." + str(self.txt_arr.index(self.txt_arr[i],i,len(self.word))+1))
                self.guess_textbx.tag_config("darkgreen",foreground="darkgreen")  
     

    def paint(self):
        # subtracting one from guess right
        self.guess_right -= 1
        for i in range(len(self.word)):
            self.count = 0
            for j in range(len(self.word)):
                if self.word[j] == self.guess_arr[j]:
                    self.count += 1

                # painting blue when the guess letters are not equal but has to the random word
                if self.guess_arr[j] in self.word[i] and self.guess_arr[i] != self.word[i] and self.word[j] != self.guess_arr[j]:
                    self.count += 1
                    if j == 0:
                        self.first_num.configure(bg="blue")
                    
                    if j == 1:
                        self.second_num.configure(bg="blue")
                    
                    if j == 2:
                        self.third_num.configure(bg="blue")

                    if j == 3:
                        self.forth_num.configure(bg="blue")
                    
                    if j == 4:
                        self.fifth_num.configure(bg="blue")
                
                # painting red when the guess letters already have in the random word
                if self.count > self.word.count(self.word[i]) and self.guess_arr.count(self.guess_arr[j])>self.word.count(self.guess_arr[j]):
                    if j == 0:
                        self.first_num.configure(bg="red")
                    
                    if j == 1:
                        self.second_num.configure(bg="red")
                    
                    if j == 2:
                        self.third_num.configure(bg="red")

                    if j == 3:
                        self.forth_num.configure(bg="red")
                    
                    if j == 4:
                        self.fifth_num.configure(bg="red")

        for i in range(len(self.word)):
            # painting darkgreen when the guess letters equal to the random word letters 
            if self.word[i] == self.guess_arr[i]:
                if i == 0:
                    self.first_num.configure(bg="darkgreen")
                    
                if i == 1:
                    self.second_num.configure(bg="darkgreen")
                    
                if i == 2:
                    self.third_num.configure(bg="darkgreen")

                if i == 3:
                    self.forth_num.configure(bg="darkgreen")
                    
                if i == 4:
                    self.fifth_num.configure(bg="darkgreen")

        # when the guess word is equal to the random word
        if self.word[0] == self.guess_arr[0] and self.word[1] == self.guess_arr[1] and self.word[2] == self.guess_arr[2] and self.word[3] == self.guess_arr[3] and self.word[4] == self.guess_arr[4]:
            showinfo(
                title='Congratulations',
                message='You have won the "Word Finder" game.')
            
            answer = askyesno(title='Proposal',
                message='Do you want to play again?')
            if answer:
                # want to play again
                self.guess_right = 6
                self.line = 0
                self.app_frame.destroy()
                self.size(350,300)
                self.main_screen()
            else:
                # closing the game 
                showinfo(
                    title='GoodBye',
                    message='See you later!')
                self.quit()

        # when there is no guess right
        elif  self.guess_right == 0:
            showinfo(
                title='Game Over!!',
                message="The number was \""+self.word+"\"\n\nUnfortunately you don't have any guess rights!.")
            
            answer = askyesno(title='Congratulations',
                message='Do you want to play again?')
            if answer:
                # want to play again
                self.guess_right = 6
                self.line = 0
                self.app_frame.destroy()
                self.size(350,300)
                self.main_screen()
            else:
                # closing the game 
                showinfo(
                    title='GoodBye',
                    message='See you later!')
                self.quit()
        
        else:
            # when three guess rights left
            if self.guess_right == 3:
                self.guess_msg.configure(text="You have "+str(self.guess_right)+ " guess rights!")

                showinfo(
                    title='Guess Right!',
                    message="You have three guesses left!")

                answer = askyesno(title='Congratulations',
                    message='Do you want a hint?')
                if answer:
                    self.top_frame.pack(expand=False)
                    self.bottom_frame.pack(expand=False)
                    # resizing for the app screen
                    self.size(380,400)
                    # adding the frame for the text area contains the word meaning  
                    self.bottombottom_frame = tk.Frame(self.app_frame,bg="SlateBlue")
                    
                    # features of the word meaning text 
                    self.text_mean = tk.Text(self.bottombottom_frame,height=5,bg="Lavender",fg="SlateBlue",highlightbackground="Lavender",wrap="word")
                    self.text_mean.pack(fill=tk.BOTH,expand=True,**self.special_padd2)
                    self.text_mean.insert('1.0', self.mean)
                    
                    # pleacement of the frame 
                    self.bottombottom_frame.pack(fill=tk.BOTH,side=tk.TOP,expand=True,**self.special_padd1)
                    
                else:
                    self.guess_msg.configure(text="You have "+str(self.guess_right)+ " guess rights!")

            elif self.guess_right == 1:
                self.guess_msg.configure(text="You have " +str(self.guess_right)+" guess right!")
                
            else:
                self.guess_msg.configure(text="You have "+str(self.guess_right)+ " guess rights!")


if __name__ == "__main__":
    root = App()
    root.mainloop()
