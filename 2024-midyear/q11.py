def CheckFile(filename: str) -> bool:
    linecount: int = 0
    try:
        with open(filename, "rt") as file:
            for line in file:
                if line.strip() == "":
                    pass
                else:
                    linecount += 1
                if linecount >= 10:
                    break
    except FileNotFoundError:
        print("Get lost!")
    return linecount >= 10
    #implicitly close file