with open('words.txt', 'r') as file:
    track = file.readline()
    for cwords in track.split():
        if 'c' in cwords:
            print(cwords.strip(',.'))