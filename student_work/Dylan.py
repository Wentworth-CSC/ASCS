Height = 0
while Height <= 0 and Height < 23:
    Height = int(input("Please enter the height you want!"))
constanthash: str = "#"
constantspace: str = " "
spacecount = Height
 
count = 2
for i in range(Height + 1):
    print(constantspace * spacecount, "#" * i, " ", "#" * i, sep="")
    spacecount = spacecount - 1