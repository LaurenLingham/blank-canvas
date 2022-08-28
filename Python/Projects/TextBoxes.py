def PrintHorizontalLine():
    print("* * * * * * *")

def PrintVerticalLine():
    print("*           *")

numberOfSpaces = 11

def PrintText(text):
    textLength = len(text)
    spacesToType = numberOfSpaces - textLength
    textToPrint = "*" + text + " " * spacesToType + "*"
    print(textToPrint)

def PrintTextCentred(text):
    textLength = len(text)
    spacesToType = numberOfSpaces - textLength
    spacesForEachSide = spacesToType / 2
    spacesOnTheLeft = spacesForEachSide
    spacesOnTheRight = spacesForEachSide 
    
    if spacesForEachSide % 2 == 1:
        spacesOnTheLeft += 0.5
        spacesOnTheRight -= 0.5

    spacesOnTheLeft = int(spacesOnTheLeft)
    spacesOnTheRight = int(spacesOnTheRight)

    textToPrint = "*" + " " * spacesOnTheLeft + text + " " * spacesOnTheRight + "*"
    print(textToPrint)

PrintHorizontalLine()
PrintVerticalLine()
PrintText("hello")
PrintVerticalLine()
PrintHorizontalLine()

print()

PrintHorizontalLine()
PrintVerticalLine()
PrintTextCentred("goodbye")
PrintVerticalLine()
PrintHorizontalLine()