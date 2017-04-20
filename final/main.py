import sys
import os
import getopt
import re
import urllib
import shutil
import random

links = {
    "f": {
        "b": ["f-b1-hello_caller", "f-b2-lady_at"],
        "e": ["f-e1-she_will_get_back_to_you", "f-e2-thanks_for_calling"],
        "r": ["f-r0.2-she_is_busy", "f-r1-ingesting_old_spice", "f-r2-listening_to_reading", "f-r3-lobster_dinner", "f-r4-moon_kiss", "f-r5-riding_a_horse"]
    },
    "m": {
        "b":["m-b1-hello", "m-b2-have_dialed"],
        "e": ["m-e1-horse", "m-e2-jingle", "m-e3-on_phone", "m-e4-swan_dive", "m-e5-voicemail"],
        "r": ["m-r1-building", "m-r2-cracking_walnuts", "m-r3-polishing_monocole", "m-r4-ripping_weights"]
    }
}

def clean_number(num): #Formats
    num = re.sub('[^0-9]','', num)
    for i in num:
        if int(i) < 0 or int(i) > 9:
            raise ValueError("Bad Number")
    return num

def set_reasons(gender, reasons): #Get Links
    out = []
    for i in reasons:
        if int(i) < 0 or int(i) > 5 or (int(i) == 5 and gender == "m"):
            raise ValueError("Bad Reason")
        out.append(int(i))
    return out
logFile = open("logFile.txt", "wb")

def get_mp3(extension, file): #Wrapper for Url lib
    urllib.urlretrieve("http://www-bcf.usc.edu/~chiso/itp125/project_version_1/" + extension + ".mp3", file + ".mp3")
    logFile.write(file + ".mp3 ")

def combine_mp3(mp1, dest): # Attaches url to end of base
    shutil.copyfileobj(open(mp1+".mp3"), dest)

def make_number(number, dest): # Handles the number and stuff
    for i in number:
        get_mp3(i,i)
    for i in number:
        combine_mp3(i, dest)
    for i in number:
        try:
            os.remove(i+".mp3")
        except:
            pass
        
def make_reasons(gender, reasons, dest): # Handles the reasons
    urls = []
    for i in reasons:
        urls.append(links[gender]["r"][i-1])
    for i in urls:
        get_mp3(i,i)
    for i in urls:
        combine_mp3(i, dest)
    for i in urls:
        os.remove(i+".mp3")

def get_end(gender, ending, dest): # Handles the ending
    link = links[gender]["e"][ending-1]
    get_mp3(link, link)
    combine_mp3(link,dest)
    os.remove(link+".mp3")

def get_open(gender, dest): # Handles the opener
    link = links[gender]["b"][random.randint(0,1)]
    get_mp3(link, link)
    combine_mp3(link,dest)
    os.remove(link+".mp3")

def make_mp3(gender, number, reasons, end, out): # Main MP3 Generator
    dest = open(out, "wb")
    get_open(gender, dest)
    make_number(number, dest)
    make_reasons(gender, reasons, dest)
    get_end(gender, end, dest)

def main(argv): # Its main you know
    gender, number, reasons, ending, out = "", "", [], "", ""
    opts, args = getopt.getopt(argv, "g:n:r:e:o:")
    if len(opts) > 0:
        try:
            for opt, arg in opts:
                if opt == "-g":
                    if arg != "m" and arg != "f":
                        raise ValueError("Non Gender")
                    gender = arg
                if opt == "-n":
                    number = clean_number(arg)
                if opt == "-r":
                    reasons = set_reasons(gender, arg)
                if opt == "-e":
                    if int(arg) < 0 or int(arg) > 2:
                        raise ValueError("Bad Ending")
                    ending = int(arg)
                if opt == "-o":
                    out = arg
            if gender == "" or number == "" or reasons == [] or ending == "" or out == "":
                raise ValueError("Missing Inputs")
            make_mp3(gender, number, reasons, ending, out)
        except ValueError as err:
            print "Invalid Input: " + err.args[0]
    else:
        try:
            gender = raw_input("m for Male, f for female: ")
            if gender != "m" and gender != "f":
                raise ValueError("Non Gender")
            number = clean_number(raw_input("Enter your number"))
            for i in range(0, len(links[gender]["r"])):
                print str(i+1) + " " + links[gender]["r"][i]
            reasons = set_reasons(gender, raw_input("Enter number for reasons in 1 line: "))
            for i in range(0, len(links[gender]["e"])):
                print str(i+1) + " " + links[gender]["e"][i]
            ending = int(raw_input("Pick 1 ending: "))
            if ending < 0 or ending > 2:
                raise ValueError("Bad Ending")
            print "You Picked:"
            print "Gender: " + str(gender)
            print "Number: " + str(number)
            print "Reasons: " + str(reasons).strip("[]")
            print "Ending: " + str(ending)
            if raw_input("Press y to confirm") != "y":
                return
            out = raw_input("Output file name: ")
            make_mp3(gender, number, reasons, ending, out)
        except ValueError as err:
            print "Invalid Input: " + err.args[0]

if __name__ == "__main__": # Just python things
    main(sys.argv[1:])

