from twilio.rest import Client
import random
from tkinter import *
from tkinter import messagebox

class otp_verify(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("600x550")
        self.resizable(False, False)
        self.n = random.randint(100000,999999)
        #for privacy reasons some things are not displayed here
        self.client=Client("#your acccount sid","#your auth token") 
        self.client.messages.create(to =["+91 number need to send otp"],
                                    from_ = "twilio number",
                                    body=self.n)
    
    def Labels(self):
        self.c = Canvas(self,bg = "white", width = 400, height = 200)
        self.c.place(x=100,y=60)
        
        self.otp_title = Label(self,text="OTP Verification",font="bold, 20",bg="white")
        self.otp_title.place(x=210,y=90)
    
    def Entry(self):
        self.user_name = Text(self,borderwidth=2, wrap="word",width = 29, height = 2)
        self.user_name.place(x=190,y=160)
        
    def Buttons(self):
       button_frame = Frame(self)
       button_frame.pack(side=BOTTOM,fill=X)

       self.submitButton = Button(button_frame,text="Submit",font=("Arial", 20),command = self.checkOTP,width = 10, height = 2)
       self.submitButton.pack(side=LEFT,padx=10,pady=10)
        
       self.resendOTP = Button(button_frame,text="Resend",font=("Arial", 20),command = self.resendOTP,width = 10, height = 2)
       self.resendOTP.pack(side=RIGHT,padx=10, pady=10)
        
    def resendOTP(self):
        self.n = random.randint(100000,999999)
        #for privacy reasons some things are not displayed here
        self.client=Client("#your account sid","#your auth token ")
        self.client.messages.create(to =["+91number need to send"],
                                    from_ = "number twilio",
                                    body=self.n)
    
    def checkOTP(self):
            self.userInput = int(self.user_name.get(1.0,"end-1c"))
            if self.userInput == self.n:
                messagebox.showinfo("showinfo","OTP verified success")
                self.n="done"
            elif self.n == "done":
                messagebox.showinfo("showinfo","already Verified ")
            else:
                messagebox.showinfo("showinfo","OTP not verified")
       
    
if __name__ == "__main__":
    window = otp_verify()
    window.Labels()
    window.Entry()
    window.Buttons()
    window.mainloop()