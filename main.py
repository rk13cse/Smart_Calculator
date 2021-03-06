# Project on calculator
responses=["Welcome to SMART CALCULATOR!","My name is Star","Thanks","Sorry, this is beyond my ability"]
def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return (l)
def lcm(a,b):
    L=a if a>b else b
    while L<=a*b:
        if L%a==0 and L%b==0:
            return L
        L+=1
def hcf(a,b):
    H=a if a<b else b
    while H>=1:
        if a%H==0 and b%H==0:
            return H
        H-=1
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multiply(a,b):
    return a*b
def division(a,b):
    return (a/b)
def end():
    print(responses[2])
    input("Please enter key to exit")
    exit()
def myname():
    print(responses[1])
def sorry():
    print(responses[3])
operations={"PLUS":add,"SUM":add,"ADD":add,"ADDITION":add,"MINUS":sub,"SUBTRACT":sub,"SUBTRACTION":sub,"DIFFERENCE":sub,
            "MULTIPLY":multiply,"MULTIPLICATION":multiply,"PRODUCT":multiply,"DIVIDE":division,
            "LCM":lcm,"HCF":hcf}
commands={"NAME":myname,"END":end,"EXIT":end,"CLOSE":end}
print(responses[0])
print(responses[1])
while True:
    text=input("Enter the values and operation: ")
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l=extract_numbers_from_text(text)
                r=operations[word.upper()](l[0],l[1])
                print(r)
            except:
                print("Something is wrong, please enter valid inputs")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()