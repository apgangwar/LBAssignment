class Folder:
    def __init__(self, id, name):
        # creating a folder with data folder and reference folder which is pointing to Null
        self.id = id
        self.name = name
        self.nextDict = {}

class DirectoryTree:
    def __init__(self):
        self.root = None


    def print_DT(self):

        if self.root is not None:
            import queue
            queue = []
            queue.append(self.root)
            while queue:
                s = queue.pop(0)
                print(s.name)
                for values in s.nextDict.values():
                    queue.append(values)
        else:
            print("No directory to print")

    def add_at_path(self, path, id, name):
        new_folder = Folder(id, name)
        # Case: Check if the path is none or the path first argument is empty
        if path == None or path == "":
            self.root = new_folder
        else:
            path_split = path.split("/")
            #     dt.add_at_path("root", "f1", "f5", "f4")

            # Case: Check is self root exists
            if self.root != None:
                d = self.root.nextDict
                for i in range(len(path_split)):
                    if i == 0:
                        continue
                    else:
                        # check if there is key in dictionary
                        if path_split[i] in d:
                            d = d[path_split[i]].nextDict
                        else:
                            print("Error: " + str(path_split[i]) + " is not present in actual directory")

                d[id] = new_folder
            else:
                print("Error: No root folder is there")

    def remove(self, path):
        # Case: Check if the path is none or the path first argument is empty
        if path == None or path == "":
            print("No folder to remove")
        else:
            path_split = path.split("/")
            #     dt.add_at_path("root", "f1", "f5", "f4")

            # Case: Check is self root exists
            if self.root != None:
                if path == self.root.id:
                    self.root = None
                    return

                d = self.root.nextDict
                for i in range(len(path_split)-1):
                    if i == 0:
                        continue
                    else:
                        # check if there is key in dictionary
                        if path_split[i] in d:
                            d = d[path_split[i]].nextDict
                        else:
                            print("Error: " + str(path_split[i]) + " is not present in actual directory")
                del d[path_split[-1]]
            else:
                print("No root folder is there")


    def fetch(self):
        pass


    def update(self, path, newName):
        if path == None or path == "":
            print("No folder to update")
        else:
            path_split = path.split("/")
            #     dt.add_at_path("root", "f1", "f5", "f4")

            # Case: Check is self root exists
            if self.root != None:
                if path == self.root.id:
                    self.root.name = newName
                    return

                d = self.root.nextDict
                for i in range(len(path_split) - 1):
                    if i == 0:
                        continue
                    else:
                        # check if there is key in dictionary
                        if path_split[i] in d:
                            d = d[path_split[i]].nextDict
                        else:
                            print("Error: " + str(path_split[i]) + " is not present in actual directory")
                d[path_split[-1]].name = newName
            else:
                print("No root folder is there, no update required")


def testDT1():
    dt = DirectoryTree()
    dt.add_at_path("", "root", "root")
    dt.add_at_path("root", "f1", "f1")
    dt.add_at_path("root", "f2", "f2")
    dt.add_at_path("root", "f3", "f3")
    dt.add_at_path("root/f1", "f4", "f4")
    dt.add_at_path("root/f1", "f5", "f5")
    dt.add_at_path("root/f3", "f6", "f6")
    #dt.remove("root/f3", "f4")
    dt.print_DT()

def testDT2():
    dt = DirectoryTree()
    dt.add_at_path("", "root", "root")
    dt.add_at_path("root", "f1", "f1")
    dt.add_at_path("root", "f2", "f2")
    dt.add_at_path("root", "f3", "f3")
    dt.add_at_path("root/f1", "f4", "f4")
    dt.add_at_path("root/f1", "f5", "f5")
    dt.add_at_path("root/f3", "f6", "f6")
    dt.print_DT()
    dt.remove("root/f3")
    print("----")
    dt.print_DT()
    dt.update("root/f1/f4", "new name")
    print("----")
    dt.print_DT()
    print("----")
    dt.remove("root")
    dt.print_DT()

testDT2()

