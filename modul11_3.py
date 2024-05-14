# Program penghitung distribusi jam dimana ada email masuk
def distribusi(data):
    count = dict()
    for line in data:
        line = line.strip()
        if line.startswith("From "):
            lineFrom = line.split()
            jam = lineFrom[5].split(":")[0]
            if jam not in count:
                count[jam] = 1
            else:
                count[jam] += 1
    for key, value in sorted(count.items()):
        print(key, value)

file = open("mbox-short.txt", "r")
distribusi(file)

