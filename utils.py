import requests
import urllib.request
import os
def url_checker(url):
    try:
        # Get Url
        get = requests.get(url)
        # if the request succeeds
        if get.status_code == 200:
            print(f"{url}: is reachable")
            return True
        else:
            print(f"{url}: is Not reachable, status_code: {get.status_code}")
            return False

    # Exception
    except requests.exceptions.RequestException as e:
        # print URL with Errs
        raise SystemExit(f"{url}: is Not reachable \nErr: {e}")

def download(txt_file):
    with open(txt_file, "r") as f:
        links = f.readlines()
        for link in links:
            link = link.strip()
            print("Downloading " + link)
            # check if temp dir exists
            if not os.path.exists("temp"):
                os.mkdir("temp")
            # download the file in the the temp folder
            urllib.request.urlretrieve(link, "temp/" + link.split("/")[-1])

def merge(filename):
    # check operating system
    if os.name == "nt":
        # windows
        os.system("copy /b temp\\*.ts " + filename + ".ts")
        # delete temp folder
        os.system("rmdir /s /q temp")
        print("Done merging")
    else:
        # linux
        os.system("cat temp/*.ts > " + filename + ".ts")
        # delete temp folder
        os.system("rm -rf temp")
        print("Done merging")

def convert(filename):
    # check operating system
    if os.name == "nt":
        # windows
        os.system("ffmpeg -i " + filename + ".ts -c:v libx264 -c:a aac -strict -2 " + filename + ".mp4")
        print("Done converting")
    else:
        # linux
        os.system("ffmpeg -i " + filename + ".ts -vcodec libx265 -acodec copy " + filename + ".mp4")
        print("Done converting")
