"""
Joanne Kwon
PIC 16
Professor Cai
February 19, 2019
"""

'''
HOMEWORK 5
The function knights_tour(n) launches a nxn knight's tour puzzle game, which checks
if a user's click is valid or not. Previously visited positions are highlighted in blue,
while the knight's current position is highlighted in orange. The knight is unable
to go back to the position that it has previously visited. Function code partially derived from TA.
'''

import tkinter as Tk

class RectangleGUI:
    def __init__(self,canvas,n):
        #self.master = master
        self.window=canvas #sets canvas to window
        self.position=1 #starting position on chessboard (0,0)

def mouse_click(ev,vals):
    moves=[]
    att=[] #knight attempted position
    cur=[] #knight current position
    
    for i in vals[5]:
        #if rectangle position number equivalent (position/current) append attempt for x and y
        if i[2]==ev.widget.find_withtag('current')[0]:
            att.append(i[0])
            att.append(i[1])
        #if rectangle position number equivalent GUI instance at current position for x and y
        elif i[2]==vals[4].position:
            cur.append(i[0])
            cur.append(i[1])  
    #valid knight positions location (1 to 2 or 2 to 1)
    positions=[[cur[0]+1,cur[1]+2],[cur[0]+1,cur[1]-2],[cur[0]-1,cur[1]+2],[cur[0]-1,cur[1]-2],[cur[0]+2,cur[1]+1],[cur[0]+2,cur[1]-1],[cur[0]-2,cur[1]+1],[cur[0]-2,cur[1]-1]]
    for j in positions:
        moves.append(j)   
    #fill rectangle accordingly (current and previous knight position)
    for k in moves:
        if k==att:
            #new knight position orange
            vals[4].window.create_rectangle(vals[1],vals[2],vals[1]+100,vals[2]+100,fill='orange')
            #old knight position blue
            vals[4].window.create_rectangle(cur[0]*100,cur[1]*100,(cur[0]+1)*100,(cur[1]+1)*100,fill='blue')
            vals[4].position=ev.widget.find_withtag('current')[0]
                
def knights_tour(n):
    d=100 #side length of rectangle
    recta=[] #rectangle identification
    root=Tk.Tk()
    #create canvas fit to size
    canvas=Tk.Canvas(root,width=n*d,height=n*d)
    gui=RectangleGUI(canvas,n)
    
    #chessboard according to n
    for i in range(n):
        for j in range(n):
            if i==0 and j==0:
                canvas.create_rectangle(i*d,j*d,i*d+d,j*d+d,fill='orange') #initial starting position (orange at 0,0)
            else:
                recta.append([canvas.create_rectangle(i*d,j*d,i*d+d,j*d+d,fill='white'),0,i*d,j*d,d]) #white chessboard   
    #chessboard plots
    board=[[i,j,0] for i in range(n) for j in range(n)]
    for k in range(n*n):
        board[k][2]=k+1
    #upon left click call class RectangleGUI mouse_click helper function
    canvas.pack()
    for l in recta:
        canvas.tag_bind(l[0],'<ButtonPress-1>',lambda ev,vals=[l[1],l[2],l[3],l[4],gui,board]:mouse_click(ev,vals))
    root.mainloop()
    
n=5 #test case
knights_tour(n)


'''
import tkinter as Tk

class RectangleGUI:
    def __init__(self,master,n):
        self.d=100 #length of side of square
        self.master = master 
        #canvas fit to size
        self.canvas=Tk.Canvas(root,width=n*self.d,height=n*self.d)
        
        #multiple rectangles to form chessboard
        for i in range(n):
            for j in range(n):
                self.canvas.create_rectangle(i*self.d,j*self.d,i*self.d+self.d,j*self.d+self.d, fill="white")
        #knight's first location (upper left)
        self.canvas.create_rectangle(0,0,self.d,self.d,fill="orange")
        self.canvas.pack()
        self.canvas.bind('<Button-1>',self.mouse_click) #move when left clicked
        
    def mouse_click(self,ev):
        correct_x=(ev.x/self.d)*self.d
        correct_y=(ev.y/self.d)*self.d
        self.draw_rec(correct_x,correct_y,fill="blue")
        
    def draw_rec(self,x,y,fill):
        self.canvas.create_rectangle(x,y,x+self.d,y+self.d,fill="orange")

n=5
root=Tk.Tk()
gui=RectangleGUI(root,n)
root.mainloop()
'''