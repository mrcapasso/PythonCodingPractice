#Author: Matteo Capasso
#Email: matteo@capasso.dev
#Purpose: This module was created to simplify common markdown formatting processes and syntax. 
#Demo: Run this .py file as is for a print() demo of contained functions.
#Function List:
    #* See invidual function documentation for further details. 
    ## createMDStatusBar() - Creates a unicode status bar graphic.
    ## createMDTable() - Creates a markdown table with variable rows user defined headers.
#Notes: 
    #* These types of formatting are best used with monospaced typeface.
    #* GitHub has its on Markdown syntax called GFM
    #* GFM Syntax: https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf
#Question: How to document *arg for preferred type

def createMDStatusBar(percentDone: int, width: int = 12, numLabel: bool = True) -> str:
    """Creates a unicode status bar graphic with adjustable width.
    
    Args:
        percentDone (int): Percent complete of project.
        width (int): The character width of the desired status bar.
        numLabel (bool): Enable or disable percent number at end of bar.
    Returns:
        str: A unicode status bar graphic with optional percent number.

    Examples:
        print(generateStatusBar(66))

    """
    fillChar = '█'
    emptyChar = '░'
    fillWidth = round((percentDone/100)*(width-2))
    emptyWidth = (width-2) - fillWidth
    #(width-2) because of '[' and ']' concatenation
    numLabelText = str(percentDone) + '% '
    statusBar = (
        '[' + str(fillChar*fillWidth)
            + str(emptyChar*emptyWidth) + '] '
            + numLabel*numLabelText
    )
    return statusBar

def createMDTable(rows: int, *headers: str) -> str:
    """Creates a markdown table with variable rows and user defined headers.
    
    Args:
       rows (int): The number of non-header rows desired in table. 
       *headers (str): The table's desired text headers.
    Returns:
        str: A string containing the full markdown table
            template with headers
    Example: 
        print(createMDTable(5, 'Date', 'Client', 'Service'))
    """
    #Creating Table's Header String
    oldMaxHeadLen = 0
    headerLineString = ' | '.join(headers)
    for head in headers:
        currentHeadLength = len(head)
        if currentHeadLength > oldMaxHeadLen: 
            oldMaxHeadLen = currentHeadLength
    #Creating Tabel's Line Break and Body Strings
    (a, b) = ([], [])
    for i in enumerate(headers):
        a.append('-' * oldMaxHeadLen)
        b.append('#' * oldMaxHeadLen)
    lineBreakString = ' | '.join(a)
    iterFillerString = ' | '.join(b)
    table = (
            headerLineString + 
            "\n" + lineBreakString +
            ("\n" + iterFillerString)*rows
    )
    return table

def createMDNumList(*listItems, startNum:int = 1) -> str:
    """Creates a markdown numeric list string.
    Args:
       *listItems (str): Individual lines of the list.
       startNum (int): What number the list should start with.
    Returns:
        str: A string containing a markdown formatted numeric list.
    Example:
        print(createMDNumList('Go Run', 'Go Eat', 'Go Home'))
    """
    numListString = ''
    for i in enumerate(listItems, start=startNum):
        lineString = (''
            + str(i[0]) + ') '
            + str(i[1]) + "\n"
            )
        numListString = numListString + lineString
    return numListString

def createMDTaskList(*listItems:str, checked:bool = False) -> str:
    """Creates a markdown task list string.

    Args:
       *listItems (str): Individual lines of the list.
       checked (bool): Enable or disable to have all lines checked.
    Returns:
        str: A string containing a markdown formatted task list.
    Example:
        print(createMDTaskList('Eat','Drink','Sleep','Code'))
    """
    taskListString = ''
    for item in listItems: 
        lineList = (''
        + r'- ['
        + (r'X'*checked) 
        + r'] ' 
        + str(item) 
        + '\n'
        )
        taskListString = taskListString + lineList
    return taskListString

if __name__ == "__main__":
    import os
    os.system('cls')
    print(''
        + 'createMDStatusBar() Demo:' + "\n" 
        + createMDStatusBar(66) + "\n"*2

        + 'createMDTable() Demo:' + "\n" 
        + createMDTable(3, 'Date','Store','Item','Price') + "\n"*2

        + 'createMDNumList() Demo:' + "\n"
        + createMDNumList('Go Outside','Think about food','Go back inside','Take a nap') + "\n"
        
        + 'createMDTaskList() Demo:' + "\n"
        + createMDTaskList('Eat','Drink','Sleep','Code', checked=True)
    )
    os.system('pause')
