x=10
y=20
a=80
b=25
c=80
d=25
recx2=(600/2)-40
recy2=-1
verx=1
very=1
alta=20
larga=20
recx=(600/2)-40
recy=400-25
xcer=x
ycer=(y+(larga/2))
punt1=0
punt2=0

def setup():
            size(600,400)

def draw():
    global x,y,verx,very,larga,alta,a,b,recx,recy,xcer,ycer,recx2,recy2,c,d,punt1,punt2
    background(100,100,0)
    x= x+2*(verx)
    y= y+2*(very)
    rect(recx,recy,a,b)
    rect(recx2,recy2,c,d)
    ellipse(x,y,alta,larga)
    text("point",10,50)
    text("point",10,350)
    text(punt1,60,50)
    text(punt2,60,350)
    if x<=0:
        verx =1
        fill(random(255),random(255),random(255))

    if y<=0:
        very =1
        fill(random(255),random(255),random(255))
  
    if x>=width:
        verx =-1
        fill(random(255),random(255),random(255))

    if y>=height:
        very =-1
        fill(random(255),random(255),random(255))
    
    if  x+alta/2>recx and x-alta/2<recx+a and y+alta/2>=recy:
        very=-1
        
    if  x+alta/2>recx2 and x-alta/2<recx2+c and y-alta/2<=recy2+d:
        very=+1
    
    if y-alta/2==0:
        punt1+=1
        
    if y+alta/2==height:
        punt2+=1
    
        
def keyPressed():
    global recx,recy,recx2,recy2
    if keyCode==RIGHT and recx<(width-a):
        recx+=15
    
    if keyCode==LEFT and recx>0:
        recx-=15
        
    if key=="d" and recx2<(width-c):
        recx2+=15
        
    if key=="a" and recx2>0:
        recx2-=15
    
    
   
    
    
    

        
  
    
