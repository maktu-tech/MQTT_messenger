import tkinter as tk
from tkinter.constants import LEFT, TOP

from tkscrolledframe import ScrolledFrame
# #functions
# def addcomp(c,txt,n):
#     btn = tk.Button(c,text = txt, width = 40,height = 20)
#     btn.pack()

# #driver code
# w = tk.Tk()
# width = 800
# height = 800
# w.title('First try')
# # c = tk.Canvas(w,width = width, height = height, bg = 'white')
# # c.pack()
# # c.create_line(width/2,0,width//2,height,width = 3)
# for i in range(20):
#     addcomp(w,"hello world",i)
# w.mainloop()
#01b0aa

bkcolor = '#e0f7fa'
bklight = '#ccff90'
secCol = '#263238'

secfont = '#ffffff'
whiteCol = '#ffffff'
col_msg = '#1a237e'

def createLbl(par,txt,anchor,color = '#ffffff'):
   lbl = tk.Label(par,text=txt, font=("Calibri",20 ),fg = '#006064',anchor=anchor,bg = bkcolor)
   return lbl

def tf(par,hint,passtf = False):

   flag = [True,passtf]

   def click(*args):
      if flag[0]:
         txte.delete(0, 'end')
         txte.config(fg = '#000000')
         if flag[1]:
                txte.config(show = '*')
         flag[0] = False

   txtf = tk.Frame(par, borderwidth=1, relief=tk.SUNKEN, bg = '#ffffff')
   txte = tk.Entry(txtf, borderwidth=10, relief=tk.FLAT,fg = '#a3a3a3',width = 300)
   txte.pack(side = tk.LEFT)

   txte.insert(0, hint)
   txte.bind("<Button-1>", click)
   return (txtf,txte)

# def button(par,txt,):
#    Button(frame0, text="Ok", command=lambda: check(text_name.get(), text_pass.get()) ,font=("", 12))

def scrframe(root):
       
   sf = ScrolledFrame(root, width=260, height=700,scrollbars = 'vertical')
   sf.pack(side=LEFT, fill="both")
   sf.bind_scroll_wheel(root)
   sf.bind_arrow_keys(root)
   inner_frame = sf.display_widget(tk.Frame)
   return inner_frame,sf

# def scrmsgfrm(root):
#    sf = ScrolledFrame(root, width=620, height=620,bg = b)
#    sf.pack(side=LEFT, fill="both")
#    # sf.bind_scroll_wheel(root)
#    # sf.bind_arrow_keys(root)
#    inner_frame = sf.display_widget(tk.Frame)
#    return inner_frame,sf


def scrButton(par,txt,command,row):
   butt = tk.Button(par, text=txt, command=command,borderwidth=0,bg = secCol,relief=tk.FLAT,fg = secfont ,font=('Ariel',15,'bold'),width=16,height=2)
   butt.grid(column=1,row=row,padx = 4,pady=2)
   return butt
   # butt.place(x=x, y=y, width=width, height=height)
   # ,width=width//100, height=height//100


def msgLbl(par,txt1,txt2):
   wd = 25
   frm = tk.Frame(par,height=50,width=wd)
   # frm.pack(side=TOP)
   frmpad = tk.Frame(frm,height=50,width=wd,bg = bklight)
   frmpad.grid(column=1,row=1,padx=10,pady=10)
   nameUser = tk.Label(frmpad,text = txt1,bg=bklight,justify=LEFT,fg = col_msg,font=("Times Roman",12),width=wd,anchor=tk.W)
   nameUser.grid(column=1,row=1,padx=10,pady=10)
   msg = tk.Label(frmpad,text=txt2,bg = bklight,justify=LEFT,font=("Times Roman",12),width=wd,anchor=tk.W)
   msg.grid(column=1,row=2,padx=10,pady=10)
   return frm,nameUser,msg