#Author: Matteo Capasso
#Goal: Create a collection of functions to easily generate markdown formats and graphics.
#Source: Original ideas.

def createStatusBar(percentDone: int, width: int = 12, numText: bool = True) -> str:
    """Creates an Unicode status bar graphic with adjustable width and optional text.
    
    Args:
        percentDone (int): Percent complete of project.
        width (int): The character width of the desired status bar.
        numText (bool): Enable or disable percent number at end of bar.
    Returns:
        str: A unicode status bar graphic with optional percent number.

    Examples:
        print(generateStatusBar(66))

    """
    fillChar = '█'
    emptyChar = '░'
    fillWidth = round((percentDone/100)*(width-2))
    emptyWidth = (width-2) - fillWidth
    statusBar = (
        '[' + str(fillChar*fillWidth) \
            + str(emptyChar*emptyWidth) + '] ' \
            + str(percentDone) + '%'
    )
    return statusBar


def generateTable(*headers, rows): #WIP
    pass

def fenceCodeBlock(): #WIP
    pass

def orderList(*listitems): #WIP
    pass

if __name__ == "__main__":
    import os, sys
    print(createStatusBar(66))
    os.system('pause')
    os.system('cls')
