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

def image_organization(file , source , destination):
    image_folder = os.path.join(destination, "Image")
    if os.path.exists(image_folder):
        orginal_path = os.path.join(source , file)
        filename = os.path.basename(orginal_path)
        os.replace(orginal_path , os.path.join(image_folder , filename))
    else:
        os.mkdir(image_folder)
        image_organization(file , source , destination)

def file_organizer(source):
    destination = make_folder(source)
    files = os.listdir(source)
    images_ext = ("jpeg" , "png" , "jpg" , "webp")
    for file in files:
        if file.endswith(tuple(images_ext)):
            image_organization(file , source , destination)
    
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
