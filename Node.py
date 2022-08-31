class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.author = data
        self.info =data

    def insertBasic(self, info):
        if self.info:
            innerValue = self.info["author"].lower()
            outerValue = info["author"].lower()

            if outerValue < innerValue:
                if self.left is None:
                    self.left = Node(info)
                else:
                    self.left.insertBasic(info)

            elif outerValue > innerValue:
                if self.right is None:
                    self.right = Node(info)
                else:
                    self.right.insertBasic(info)
            elif outerValue == innerValue:
                seriesInner = self.info["series"].lower()
                seriesOuter = info["series"].lower()

                if seriesOuter == "nada":
                    if self.left is None:
                        self.left = Node(info)
                    else:
                        self.left.insertBasic(info)
                else:
                    if seriesInner == "nada":
                        if self.right is None:
                            self.right = Node(info)
                        else:
                            self.right.insertBasic(info)
                    elif seriesOuter < seriesInner:
                        if self.left is None:
                            self.left = Node(info)
                        else:
                            self.left.insertBasic(info)
                    elif seriesOuter > seriesInner:
                        if self.right is None:
                            self.right = Node(info)
                        else:
                            self.right.insertBasic(info)
                    elif seriesOuter == seriesInner:
                        innerVolume = self.info["volume"].lower()
                        outerVolume = info["volume"].lower()

                        if outerVolume < innerVolume:
                            if self.left is None:
                                self.left = Node(info)
                            else:
                                self.left.insertBasic(info)

                        elif outerVolume > innerVolume:
                            if self.right is None:
                                self.right = Node(info)
                            else:
                                self.right.insertBasic(info)

        else:
            self.author = info

    def firstInsert(self,info):
        if info["special"] == "big":
            self.right.insertBasic(info)
        else:
            self.left.insertBasic(info)

    def insertSeries(self,info):
        if self.info:
            innerValue = self.info["series"].lower()
            outerValue = info["series"].lower()
            if outerValue == "nada":
                print("problem detected not in a series but called in insertSeries")
                return

            if outerValue < innerValue:
                if self.left is None:
                    self.left = Node(info)
                else:
                    self.left.insertBasic(info)

            elif outerValue > innerValue:
                if self.right is None:
                    self.right = Node(info)
                else:
                    self.right.insertBasic(info)
            elif outerValue == innerValue:

                seriesOuter = info["volume"].lower()

                if seriesOuter == "nada":
                    if self.right is None:
                        self.left = Node(info)
                    else:
                        self.left.insertOneShot(info)
                else:
                    if self.right is None:
                        self.left = Node(info)
                    else:
                        self.right.insertSeries(info)


        else:
            self.author = info

        print("Debug")

    def insertVolume (self,info):

        if self.info:
            innerValue = self.info["volume"].lower()
            outerValue = info["volume"].lower()

            if outerValue < innerValue:
                if self.left is None:
                    self.left = Node(info)
                else:
                    self.left.insertBasic(info)

            elif outerValue > innerValue:
                if self.right is None:
                    self.right = Node(info)
                else:
                    self.right.insertBasic(info)

        else:
            self.author = info



    def insertOneShot(self, info):
        if self.info:
            innerValue = self.info["title"].lower()
            outerValue = info["title"].lower()

            if outerValue < innerValue:
                if self.left is None:
                    self.left = Node(info)
                else:
                    self.left.insertBasic(info)

            elif outerValue > innerValue:
                if self.right is None:
                    self.right = Node(info)
                else:
                    self.right.insertBasic(info)

        else:
            self.author = info



        print("Debug")

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        #list["list"].append(self.info)
        print("Author: "+ self.info["author"]+"     Series: "+self.info["series"]+"     Volume: "+self.info["volume"]+"     Title: " +self.info["title"]+"      Special: "+self.info["special"])
        if self.right:
            self.right.PrintTree()

    def updateOrderdFile(self,list):
        if self.left:
            self.left.updateOrderdFile(list)
        list["list"].append(self.info)
        #print("Author:" + self.info["author"] + " Series: " + self.info["series"] + " Title: " + self.info["title"])
        if self.right:
            self.right.updateOrderdFile(list)
