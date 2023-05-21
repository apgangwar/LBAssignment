'''
Assignment :
1. Come up with a config (Data Structure) and load a new directory tree from config.
2. Write a program that does flowing operations on a directory tree.
a. Add a new folder at a particular path in the directory tree.
b. Removed a folder from a particular path in thedirectory tree.
c. Fetch the path of the given folder.
d. Update name of the folder.
Note: For each folder we should have unique `id` and `name`.
Also upload the program on github and share the link with
README.
'''
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
        pass

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
                        # check if there is a key in dictionary
                        if path_split[i] in d:
                            d = d[path_split[i]].nextDict
                        else:
                            print("Error: " + str(path_split[i]) + " is not present in actual directory")

                d[id] = new_folder
            else:
                print("Error: No root folder is there")

    def Fetch(self):
        n = self.root
        while n is not None:
            print(n.id)
            print(n.name)
            # n become next folder with this
            # n -> n_next
            n = n.next

    def Update(self, pos, id, name):
        pass

def testDT1():
    dt = DirectoryTree()
    dt.add_at_path("", "root", "root")
    dt.add_at_path("root", "f2", "f2")
    dt.add_at_path("root", "f3", "f3")
    dt.add_at_path("root/f1", "f4", "f4")
    dt.add_at_path("root/f1", "f5", "f5")
    dt.add_at_path("root/f3", "f6", "f6")

    dt.print_DT()

testDT1()


