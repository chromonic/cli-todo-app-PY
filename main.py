dbFilePath = "appDB.txt"

print("Hello, please enter 'help' if you're stuck.")

def fileParser(dnFilePath):
    lTasks = []
    with open(dbFilePath, 'r') as file:
        lLines = file.readlines();
        for sLine in lLines:
            if sLine == "\n":
                continue
            task = []
            tags = sLine.split(", ")
            
            tasknum, taskTitle = tags[0].strip('"\n').split(": ") # -> is 'task1: "something"'
            _, taskdesc = tags[1].strip('"\n').split(": ")

            task.append(int(tasknum[4:]))
            task.append(taskTitle.strip('"'))
            task.append(taskdesc.strip('"'))

            lTasks.append(task)

    return lTasks


def comList(dbFilePath):
    with open(dbFilePath, 'r') as file:
        sContents = file.readlines();
        if (len(sContents) == 0):
            print("-- nothing to see here! --")
            return
        for sLine in sContents:
            if sLine == "\n":
                continue
            print(sLine, end='') # better mem management
    print()


def comAdd(dbFilePath):
    taskTitle = input("Task Title -> ")
    taskNumber = input("Task Number -> ")    
    taskDesc = input("Task Description ->")

    formattedString = f"task{taskNumber}: \"{taskTitle}\", description: \"{taskDesc}\"\n"

    with open(dbFilePath, 'a') as file:
        file.write(formattedString)
    print(formattedString)


def comDel(dbFilePath): 
    lTasks = fileParser(dbFilePath)
    if len(lTasks) == 0:
        print("-- Nothing to delete! --")
        return
    iTaskNumber = int(input("Task Number? -> "))
    for lTask in lTasks:
        if iTaskNumber != lTask[0]:
            continue

        sChoice = input(f"--Do you want to delete task {lTask[1]}? (y/n)--\n: ")
        if sChoice != "y":
            return

        with open(dbFilePath, 'r') as file:
            lLines = file.readlines()
            with open(dbFilePath, 'w') as writeFile:
                for sLine in lLines:
                    if sLine == "\n":
                        continue

                    taskname, _ = sLine.split(", ")
                    tasknum, _ = taskname.split(": ")
                    tasknum = int(tasknum[4:])

                    if tasknum != iTaskNumber:
                        writeFile.write(sLine)


    

dAvailableCommands = {
        'list' : comList,
        'add'  : comAdd,
        'del'  : comDel
        }

def getHelp(dAvailableCommands):
    print("--")
    for key in dAvailableCommands:
        print(key)
    print("help")
    print("exit")
    print("--")
    

bRunning = True
while bRunning:
    userInput = input("Command: ")

    if userInput == "exit":
        bRunning = False
    elif userInput == "help":
        getHelp(dAvailableCommands)
    else: 
        try:
            dAvailableCommands[userInput](dbFilePath)
        except KeyError as e:
            print("Invalid command")
            print(e)

