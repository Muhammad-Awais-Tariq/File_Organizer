import os

def make_folder(source):
    while True:
        Folder_name = input("Enter the name of the folder that you want your organized file in : ")
        destination = os.path.join(source, Folder_name)
        try:
            os.mkdir(destination)
            return Folder_name , destination
        except:
            print("The folder already exists with this name select a different name")

def folder_maker(file , source , destination , name):
    sub_folder = os.path.join(destination, name)
    if os.path.exists(sub_folder):
        orginal_path = os.path.join(source , file)
        filename = os.path.basename(orginal_path)
        os.replace(orginal_path , os.path.join(sub_folder , filename))
    else:
        os.mkdir(sub_folder)
        folder_maker(file , source , destination , name)


def delete(files,source):
    try: 
        allfiles = set()
        for file in files:
            file_name = file.rsplit(".",1)[0]
            if "- Copy" in file_name:
                while True:
                    choice = input(f"Following file : {file} is detected as duplicate do you wish delete it (Y/N) : ").lower()
                    if choice in ["y" , "n"]:
                        break                
                if choice == "y":        
                    os.remove(os.path.join(source,file))
                else:
                    allfiles.add(file)   
            else:
                allfiles.add(file)
        
        return allfiles
    except FileNotFoundError:
        pass

def cleanfiles(files,source):
    delete_files = delete(files,source)
    return delete_files

        
def file_organizer(source):
    foldername , destination = make_folder(source)
    raw_files = os.listdir(source)
    files = cleanfiles(raw_files,source)
    extension = {
        "Images" : (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".tiff"),
        "Videos" : (".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm"),
        "Documents" : (".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".md"),
        "Spreadsheets" : (".xls", ".xlsx", ".csv", ".ods"),
        "Presentations" : (".ppt", ".pptx", ".odp"),
        "Audio" : (".mp3", ".wav", ".aac", ".flac", ".m4a", ".ogg"),
        "Archives" : (".zip", ".rar", ".7z", ".tar", ".gz"),
        "Source Code" : (".py", ".cpp", ".c", ".java", ".js", ".ts", ".html", ".css", ".php", ".rb", ".go"),
        "Configurations" : (".json", ".xml", ".yaml", ".yml", ".ini", ".cfg", ".env", ".toml"),
        "Ebooks" : (".epub", ".mobi", ".azw", ".djvu"),
        "Fonts" : (".ttf", ".otf", ".woff", ".woff2"),
        "Installers" : (".exe", ".msi", ".apk", ".dmg", ".deb", ".rpm"),
        "Disk Images" : (".iso", ".img"),
        "Design Files" : (".psd", ".ai", ".xd", ".fig"),
        "Logs" : (".log"),
    }

    for file in files:
        if os.path.isfile(os.path.join(source , file)):
            for k , v in extension.items():
                if file.endswith(tuple(v)):
                    folder_maker(file , source , destination , k)
                    break
        elif file != foldername and os.path.isdir(os.path.join(source , file)):
            folder_maker(file , source , destination , "Folders")
        else:
            folder_maker(file , source , destination , "Miscellaneous")
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
