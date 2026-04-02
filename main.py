import os

def make_folder(source):
    while True:
        Folder_name = input("Enter the name of the folder that you want your organized file in : ")
        destination = os.path.join(source, Folder_name)
        try:
            os.mkdir(destination)
            return destination
        except:
            print("The folder already exists with this name select a different name")

def file_organizer(source):
    destination = make_folder(source)

    files = os.listdir(source)
    

def main():
    while True:
        source = input("Enter the path of your messey folder: ")

        if os.path.isdir(source):
            file_organizer(source)
            break
        else:
            print("Enther a valid path")


if __name__ == "__main__":
    main()
