#File: FOHemail-week.py

#Name: Alexander Karbo (Karbo)

#Date: 7/27/18

#Desc: This is FOHemail-week.py, a script written to parse the .csv files generated
#by autoemail.sh and return the values needed for mailsmp to send the emails. 
#You will need to customize this document with the emails of your workstudy 
#students. See README.txt for full instructions or is all else fails contact 
#the creator of this script: Alexander Karbo at alexanderkarbo@gmail.com.

#Usage: autoemail.sh runs this code to parse the FOH signup sheet. Besides 
#changing the emails and pathing you don't really need to do anything with it.

#---------------------------------------

#ENTER EMAILS HERE in the same order as they appear on the signupsheet

emails = []
emails.append("almcatee@davidson.edu")
emails.append("anclaire@davidson.edu")
emails.append("cagschwind@davidson.edu")
emails.append("eslherisson@davidson.edu")
emails.append("haseligmann@davidson.edu")
emails.append("lupereira@davidson.edu")
emails.append("mirummage@davidson.edu")
emails.append("sogonzalezleal@davidson.edu")

#---------------------------------------

import csv #this helps parse the csv file
import datetime #this gets today's date and does date arithmetic

nextweek = datetime.date.today() + datetime.timedelta(days=7) #next week is 7 days after today
nextweek = "{:%-m/%-d/%Y}".format(nextweek) #change the format to match the csv file

print "\nCode initialized on %s\n" % datetime.date.today()

print "\nChecking For FOH Shows On %s\n" % nextweek

with open('/Users/alkarbo/autoemail/FOHsignup.csv', 'rb') as f: #open the csv file
    data = list(csv.reader(f)) #make a list out of the csv file contents
    ncols = len(data[0]) #count the columns
    nrows = len(data) #count the rows
    allinfo = [] #make a list to store all the show information
    for i in range(ncols): #for every column
        showinfo = [] #make a list to store show info
        if nextweek == str(data[1][i]): #if the date of a show is next week
            a = i #store which column we are on
            for j in range(ncols): #try a maximum number of times equal to the number of columns
                if str(data[0][a]) == "": #if there is no show title
                    a = a-1 #look at the column to the left of this one and try again
                else: #if there is a show name
                    showinfo.append(str(data[0][a])) #store the show name
                    break #stop looking for a show name
            for j in range(4 + len(emails)): #for the four rows of other information plus the email rows
                showinfo.append(str(data[j+1][i])) #store the info
            allinfo.append(showinfo) #add this show's info to the list of all info
print "FOH Show Info Saved. Shows Found: %s\n" % [i[0] for i in allinfo]

for i in range(len(allinfo)): #for each show
    for j in range(len(emails)): #for each student
        if allinfo[i][j+5] != "": #if a student has signed up in their row
            allinfo[i][j+5] = emails[j] #store their email address from the list of emails
    allinfo[i] = filter(None, allinfo[i]) #filter out the students who did not sign up
    allinfo[i].remove(str(allinfo[i][4])) #remove the "number needed" row
print "FOH Email Info Tabulated:\n"
print allinfo

with open('/Users/alkarbo/autoemail/FOHemail.sh', 'a+') as f: #open a file to write some bash code
    for i in range(len(allinfo)): #for each show
        f.write("mail -s 'You Have a Show Next Week! (On %s)' " % allinfo[i][1]) #begin the mail command and specify the subject
        for j in range(len(allinfo[i])-4): #for each email
            f.write("{0}, ".format(allinfo[i][j+4])) #add them as a recipient
        f.write("alkarbo@davidson.edu") #then add the manager
        f.write(" < /Users/alkarbo/autoemail/FOHemail{0}.txt\n".format(i)) #specify the content of the email to be a text file
        f.write("echo 'FOH Emails Sent'\n")
        f.write("rm /Users/alkarbo/autoemail/FOHemail{0}.txt\n".format(i)) #make the bash code delete the .txt files

        with open('/Users/alkarbo/autoemail/FOHemail{0}.txt'.format(i), "w+") as e: #create a text file for the body of the email
            e.write("\nYou have the show {0} at {1}. The call time is {2}.\n".format(allinfo[i][0], allinfo[i][3], allinfo[i][2])) #put int he show info
            e.write("\nIf you cannot attend this show you must find someone to cover for you and let Karbo know asap.\n") #write some things in the message
            e.write("\nThis is an automated message, reply at your peril.\n") #more message
            e.write("\nSincerely,\n\nKarbo's Robot\n") #message
        
print "\nFOH Email Script Written\n"
print "\n-------------------------------------\n"
