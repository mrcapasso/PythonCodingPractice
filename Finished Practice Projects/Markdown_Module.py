#Author: Matteo Capasso
#Email: matteo@capasso.dev
#Purpose: This module was created to simplify common markdown formatting processes. 
    #Note: Run this .py file for a print() demo of contained functions.
#Module: This contains the following...
    #createMDStatusBar() - Creates an Unicode status bar graphic with adjustable width and optional text.
    #createMDTable() - Creates a markdown table with headers and rows.

def createMDStatusBar(percentDone: int, width: int = 12, numText: bool = True) -> str: #Finished
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
    #(width-2) because of '[' and ']' concatenation
    statusBar = (
        '[' + str(fillChar*fillWidth) \
            + str(emptyChar*emptyWidth) + '] ' \
            + str(percentDone) + '%'
    )
    return statusBar


def createMDTable(rows: int, *headers: str) -> str: #Finished
    """Creates a markdown table with headers and rows.
    
    Args:
       rows (int): The number of non-header rows desired in table. 
       *headers (str): The table's desired text headers.
    Returns:
        str: A string containing the full markdown table
            template with headers
    Example: 
        createMDTable(5, 'Date', 'Client', 'Service')
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

def paragraphOutline(): #WIP
    pass

def fenceCodeBlock(): #WIP
    pass

def orderList(*listitems): #WIP
    pass

if __name__ == "__main__":
    import os
    os.system('cls')
    print(''
        + 'MD Status Bar Demo:' + "\n" 
        + createMDStatusBar(66) + "\n"*2
        + 'Create MD Table Demo:' + "\n" 
        + createMDTable(3, 'Date','Store','Item','Price') + "\n"
    )
    
