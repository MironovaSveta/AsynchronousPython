import time

def fetch_file():
    print("Starting to fetch file")
    time.sleep(1) # duration to fetch the file
    print("Fetching file completed")

def main():
    fetch_file()
    fetch_file()
    fetch_file()
    print("Main completed")

main()
