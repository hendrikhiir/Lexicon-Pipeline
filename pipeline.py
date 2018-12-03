from os import walk, rename, listdir, getcwd, chdir, remove
import re

# C:\Users\Hendrik\Documents\lyx_õige\
path = input("Sisesta kausta asukoht: ")
f = []
d = []

# failide ja kaustade saamine path kataloogist
for (dirpath, dirnames, filenames) in walk(path):
    f.extend(filenames)
    d.extend(dirnames)
    break

# nimetab juurkataloogi (sisaldab: lyx files + klasside materjalide kaustad) kaustad õigesti ümber
for a in d:
    try:
        chdir(path)
        a1, a2 = a.split(".html")
        uusnimi = a1+"_materjalid"
        rename(a, uusnimi)
    except:
        pass

# Nimetab piltide nimed kõigis kaustades õigesti ümber
for i in d:
    for (dirpath, dirnames, filenames) in walk(i):
        #print(filenames)
        for file in filenames:
            #print(file)
            try:
                a1, a2 = file.split("lyx_img_")
                uusnimi = path + "\\" + i + "\\" + a2
                vananimi = path + "\\" + i + "\\" + file
                #print(uusnimi)
                rename(vananimi, uusnimi)
            except:
                pass

# Asendab html failides piltide nimed
# TODO
for i in d:
    for (dirpath, dirnames, filenames) in walk(i):
        print (filenames)
        for file in filenames:
            n = open(path + "\\" + i + "\\" + file, "r+")
            html_nimi = dirpath.split("_materjalid")[0]
            #print(html_nimi)
            if (html_nimi + ".html" == file):
                #print(file)
                with open(path + "\\" + i + "\\" + file, "r+") as f:
                    for line in f:
                        text = str(line)
                        text.strip()
                        #print(line)
                        #match = re.match("src=\"(\d(\d)?C(.)+).png", str(line))
                        #print(match)
                        #print(pilt)
                        if re.match("src=\"(\d(\d)?C(.)+).png", line):
                            #print(line)
                            p1, p2 = line.split("src=\"")
                            p3, p4 = p2.split("\" alt")
                            p5, p6 = p3.split("lyx_img_")
                            asendus = "src=\"" + p6 + "\" alt=\"PIC\""
                            print(text)
                            print(asendus)
                            line = line.replace(text, asendus)
                            n.write(line)
                        else:
                            n.write(line)

# Teeb klassi HTML faili tükkideks definitsioonide kaupa, uue definitsioon nimeks tuleb
# praeguse HTML faili nimi (nt 3_klass) ja _järjekorranumber (nt esimese definitsiooni nimi
# 3_klass_1).
# TODO
for i in d:
    for (dirpath, dirnames, filenames) in walk(i):
        for file in filenames:
            html_nimi = dirpath.split("_materjalid")[0]
            if (html_nimi + ".html" == file):
                with open(path + "\\" + i + "\\" + file, "r+") as f:
                    tykid = f.read().split("<h3")
                    tykid2 = tykid[1:]
                    tykid3 = []
                    for j in tykid2:
                        j = "<h3" + j
                        tykid3.append(j)
                    c = 1
                    for m in tykid3:
                        if html_nimi == "gymnaasium":
                            f2 = open(path + "\\" + i + "\\" + html_nimi.strip(".html") + "m_" + str(c) + ".html", "w")
                        else:
                            f2 = open(path + "\\" + i + "\\" + html_nimi.strip(".html")+"_"+str(c)+".html", "w")
                        f2.write(m)
                        c+=1
                remove(path + "\\" + i + "\\" + html_nimi+".html")

print(f)
print(d)