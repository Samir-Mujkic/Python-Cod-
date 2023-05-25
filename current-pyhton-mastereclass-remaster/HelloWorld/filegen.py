import os

root = "music"

for path, directiories, files in os.walk(root, topdown=True):
    if files:
        print(path)
        first_split = os.path.split(path)
        print(first_split)
        second_split = os.path.split(first_split[0])
        print(second_split)
        for f in files:
            song_details = f[:-5].split(" - ")
            print(song_details)
        print("*" * 40)
        #Nece mi music da se ubaci ali ovako se radi
        #Rezultat je:
        #music/1000manics/out time in eden
        #music/1000manicas out time in eden
        #music 1000 Maniacs
        #lista pjesmi da ne pisem 1,10,11,12,13,2,3,4,5,6,7,8,9