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

def folder_maker(file , source , destination , name):
    sub_folder = os.path.join(destination, name)
    if os.path.exists(sub_folder):
        orginal_path = os.path.join(source , file)
        filename = os.path.basename(orginal_path)
        os.replace(orginal_path , os.path.join(sub_folder , filename))
    else:
        os.mkdir(sub_folder)
        folder_maker(file , source , destination , name)

def file_organizer(source):
    destination = make_folder(source)
    files = os.listdir(source)
    images_ext = (".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg", ".tiff")
    video_ext = (".mp4", ".mkv", ".mov", ".avi", ".wmv", ".flv", ".webm")
    for file in files:
        if file.endswith(tuple(images_ext)):
            folder_maker(file , source , destination , "Image")
        if file.endswith(tuple(video_ext)):
            folder_maker(file , source , destination , "Video")  
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

#to be done in the future
# documents → [".pdf", ".doc", ".docx", ".txt", ".rtf", ".odt", ".md"]
# spreadsheets → [".xls", ".xlsx", ".csv", ".ods"]
# presentations → [".ppt", ".pptx", ".odp"]
# audio → [".mp3", ".wav", ".aac", ".flac", ".m4a", ".ogg"]
# archives → [".zip", ".rar", ".7z", ".tar", ".gz"]
# code → [".py", ".cpp", ".c", ".java", ".js", ".ts", ".html", ".css", ".php", ".rb", ".go"]
# config → [".json", ".xml", ".yaml", ".yml", ".ini", ".cfg", ".env", ".toml"]
# ebooks → [".epub", ".mobi", ".azw", ".djvu"]
# fonts → [".ttf", ".otf", ".woff", ".woff2"]
# installers → [".exe", ".msi", ".apk", ".dmg", ".deb", ".rpm"]
# disk_images → [".iso", ".img"]
# design_files → [".psd", ".ai", ".xd", ".fig"]
# logs → [".log"]
#make a dictionary of all the values where key is the type and the value is tuple of the extensions
# Files with no extension
# Hidden files like dotfiles
# Duplicate files
# Very small temp files
# Incomplete downloads
# Mixed folders where one folder contains many different types
# Unknown file types that do not match any rule
# Nested folders so files are not only sorted in the top level