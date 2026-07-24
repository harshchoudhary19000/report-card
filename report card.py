sum=0
hindi=0
english=0
math=0
science=0
sst=0
a=input("student Name")
b=input("father Name")
c=input("DOB")
h= "hindi"
def marks():
    global hindi
    hindi = int(input("Marks Obtain hindi"))
    if hindi>100:
        marks()
marks()        
if hindi<=100:
    if hindi<=100:
        if hindi>=85:
            h="A"
        elif hindi>70:
            h="B"
        elif hindi>50:
            h="C"
        elif hindi>=33:
            h="D"
        else:
            h="Fail"
        
en="english"
def marks2():
    global english
    english=int(input("Marks Obtain english"))
    if english>100:
        marks2()
marks2()

if english<=100:
    if english>85:
        en="A"
    elif english>70:
        en="B"
    elif english>50:
        en="C"
    elif english>=33:
        en="D"
    else:
        en="Fail"
                
m="math"
def marks3():
    global math       
    math=int(input("Marks Obtain maths"))
    if math >100:
        marks3()
marks3()
if math<=100:
    if math>85:
        m="A"
    elif math>70:
        m="B"
    elif math>50:
        m="C"
    elif math>=33:
        m="D"
    else:
        m="Fail"   
                 
s="science"
def marks4():
    global science         
    science=int(input("Marks Obtain science"))
    if science >100:
        marks4()
marks4()
if science<=100:
    if science>85:
        s="A"
    elif science>70:
        s="B"
    elif science>50:
        s="C"
    elif science>=33:
        s="D"
    else:
        s="Fail"
                
ss="sst"
def marks5():
    global sst            
    sst=int(input("Marks Obtain sst"))
    if sst>100:
        marks5()
marks5()
if sst<=100:
    if sst>85:
        ss="A"
    elif sst>70:
        ss="B"
    elif sst>50:
        ss="C"
    elif sst>=33:
        ss="D"
    else:
        ss="Fail"             
        
sum=(hindi+english+math+science+sst)
percentage=sum/5 
if hindi < 33 or english < 33 or math < 33 or science < 33 or sst < 33 or percentage < 33:
    result="Fail"
else:
    result="Pass"
        
        
              















 
print("                 ")
print("                 ")
print(f"student Name:{a}")
print(f"father Name :{b}")
print(f"DOB         :{c}")
print("                 ")
print("SrNo  Subject    M.M   MO     Grade")
print(f" 1    Hindi      100   {hindi}      {h}")
print(f" 2    English    100   {english}      {en}")
print(f" 3    Maths      100   {math}      {m}")
print(f" 4    science    100   {science}      {s}")
print(f" 5    sst        100   {sst}      {ss}")
print("                 ")
print(f"Total Marks: {sum}")
print(f"Pass/Fail:   {result}")
print(f"percentage:  {percentage}")
print("                 ")
