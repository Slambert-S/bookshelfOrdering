# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import Node
import json


def addBook(bookList):
    newAuthor = input("Name of the author :")
    newSerie = ""
    newVolume = ""
    newTitle = ""
    isBiger = ""
    newSpecific = ""
    partOfSeries = input("Is the book part of a series Y/N :")
    if (partOfSeries == "Y"):
        newSerie = input("Enter the name of the serie : ")
        newVolume = input("What is the volume of the serie : ")

    elif (partOfSeries == "N"):
        newSerie = "nada"
        newVolume = "1"
    newTitle = input("Title of the book : ")
    isBiger = input("Is the book in a large version Y/N :")
    if (isBiger == "Y"):
        newSpecific = "big"
    else:
        newSpecific = "pocket"
    newBook = {
        "author": newAuthor,
        "series": newSerie,
        "volume": newVolume,
        "title": newTitle,
        "special": newSpecific
    }
    bookList["list"].append(newBook)


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dictionary = {
        "list": []

    }

    json_object = ""
    with open('list.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)
    print(json_object)
    index = 0
    root = ""
    loopValue = 0
    menuValue = ""
    while (loopValue == 0):
        print("What do you want to do:")
        print("1 : Add a new book")
        print("2 : Show the order list of book")
        print("3 : Update the  order list in the document")
        menuValue = input("Option selected :")

        if (menuValue == "1"):
            addBook(json_object)
            with open("list.json", "w") as outfile:
                json.dump(json_object, outfile)
        elif (menuValue == "2"):
            root = ""
            index = 0
            for x in json_object["list"]:
                if index == 0:
                    root = Node.Node(x)
                    index += 1
                else:
                    root.insertBasic(x)
            root.PrintTree()

        elif (menuValue == "3"):
            root.updateOrderdFile(dictionary)
            with open("orderdList.json", "w") as outfile:
                json.dump(dictionary, outfile)


    test = {"author": "F", "series": "naruto", "title": "byakugan eyes"}
    json_object["list"].append(test)
    for x in json_object["list"]:
        if index == 0:
            root = Node.Node(x)
            index += 1
        else:
            root.insertBasic(x)
        # print(x)

    root.PrintTree(dictionary)
    """
    root=Node.Node({"author": "A","series": "trone de fer","title": "danganrompa"})
    root.insertBasic({"author": "A","series": "nada", "title": "danganrompa"})
    root.insertBasic({"author": "B","series": "nada", "title": "danganrompa"})
    root.insertBasic({"author": "D","series": "narnia", "title": "danganrompa"})
    root.insertBasic({"author": "E","series": "nada", "title": "danganrompa"})
    root.insertBasic({"author": "A","series": "apex", "title": "danganrompa"})
    root.insertBasic({"author": "C","series": "nada", "title": "danganrompa"})
    root.insertBasic({"author": "A", "series": "nada", "title": "Academioa"})
    root.insertBasic({"author": "A", "series": "trone de cuivre", "title": "danganrompa"})
    root.PrintTree(dictionary)

    with open("list.json", "w") as outfile:
        json.dump(dictionary, outfile)
    """
    {
        "author": "",
        "series": "nada",
        "volume": "1",
        "title": "",
        "special": "big"
    }

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
