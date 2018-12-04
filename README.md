File: Readme.md

Name: Alexander Karbo (Karbo)

Date: 9/3/18

Desc: Instructions for setting up autoemail.sh and associated python files. 
This guide will likely not give you sufficient information to make substantial 
edits to how the code works, but it should be enough for ou to get the code 
working and if you want to make changes the comments + google should prevent 
that from being too difficult.

------------------------------------------------------------------------------

This is the README for autoemail.sh (and its subsidiary code). If you're
reading this then you have found the code, which is good. This Readme should
be in a folder named "autoemail" along with four peices of code: autoemail.sh,
FOHemail-week.py, FOHemail-day.py, TOemail-week.py and TOemail-day.py. autoemail.sh is the 
primary bash script which in turn runs the four python codes (which in turn write and 
run more bash script). For the code to work you need to do three things: 
create the correct file structure, update the code for you and your employees, 
and setup the code to run automatically. The following sections will discuss 
these steps in more detail, but if all else fails you can reach out to 
Alexander Karbo at alexanderkarbo@gmail.com.

1. FILE ARCHITECTURE

This code uses hard pathing to make it more stable. You will need to change
part of the pathing in step 2 anyway, so if you're comfortable with terminal
you can skip this step and just configure your pathing as needed. It is,
however, promabably simplest to just use this file structure:

/Users/*yourusername*/autoemail/

aka your home folder: 

~/autoemail/

If you're not familiar with Terminal then the simplest thing is probably just
to move the folder "autoemail" into your home folder. If you search for your
username it will bring up your home folder (this folder probably has a house
as its icon). If you don't have the folder then you can create one with the
name "autoemail" verbatim. As long as it has the three peices of code in it
and is located in your home folder you're done!

If you don't have all of the three peices of code (your predecessor really 
should have given them to you via email or thumbdrive or something) there are
a few things you can try to fix that.

The simplest fix would be if the backup site Karbo created is still there. Try
this command in Terminal:

cp -r /backup/autoemail/ ~/

This will try to copy the autoemail folder (and recursively all of the files it
contains) to your home folder. If this works then you're done with step 1!

If this does not work then the either your syntax is wrong (check your spelling
because every letter and capitalization matters) or the backup is no longer
there. If this doesn't work, fret not! The files are on github.

Ok so if you haven't used github before I don't think I can explain everything
about it here.. but the short version is that the files are stored online. Head
to this link: https://github.com/Karbobawitz/autoemail and download the files.
Once downloaded make sure you have all of the code in a folder named 
"autoemail" in your home folder.   

2. CODE CHANGES

There are three changes that you need to make: updating the signupsheet urls,
changing the emails, and correcting the pathing. The following sections will go
into more detail.

     2a) UPDATING SIGNUP SHEET URLS

     First of all you should know that this code is configured to work with a
     google signup sheet. If you want to use a different system you'll need to
     know enough about coding to help the code find whatever system you are
     using.

     The code expects the following format from the FOH signup:

              | SHOW 1 | SHOW 2 | SHOW 3 | etc.
--------------|--------|--------|--------|-------
Date          |        |        |        |
--------------|--------|--------|--------|-------
Call Time     |        |        |        |
--------------|--------|--------|--------|-------
Show Time     |        |        |        |
--------------|--------|--------|--------|-------
Number Needed |        |        |        |
--------------|--------|--------|--------|-------
NAME 1        |        |        |        |
--------------|--------|--------|--------|-------
NAME 2        |        |        |        |
--------------|--------|--------|--------|-------
NAME 3        |        |        |        |
--------------|--------|--------|--------|-------
etc.          |        |        |        |

     And the following format for the TO signup:

              | SHOW 1 | SHOW 2 | SHOW 3 | etc.
--------------|--------|--------|--------|-------
Date	      |	       |	|	 |
--------------|--------|--------|--------|-------
Show Time     |	       |	|	 |
--------------|--------|--------|--------|-------
Call Time     |        |        |        |
--------------|--------|--------|--------|-------
Venue         |	       |	|	 |
--------------|--------|--------|--------|-------
Number Needed |	       |	|	 |
--------------|--------|--------|--------|-------
NAME 1	      |	       |	|	 |
--------------|--------|--------|--------|-------
NAME 2	      |	       |	|	 |
--------------|--------|--------|--------|-------
NAME 3	      |	       |	|	 |
--------------|--------|--------|--------|-------
etc.	      |        |	|	 |

     If this formatting is correct, next setup your signups to publish: 

     File > Publish to the web...

     Publish only your current sheet and make sure it is in a .csv format. Once
     this is done you can copy the url it provides and paste that into the 
     appropriate place in autoemail.sh. Be sure to do this for both the FOH and
     TO signups!

     2b) CHANGING EMAILS

     At the beginning of each of the python files there is a list of emails.
     All you need to do is replace the emails there with the emails for your
     workers. The emails should appear in the same order as they do in the
     singup sheet. You should copy the syntax of the emails which are already
     there:
     
     emails.append("*emailaddress*")

     You should also change the code in the python files to email you instead
     of your predecessor. Find the line where the comment says it is adding
     the manager and change the email address to your own.

     2c) CORRECTING PATHING

     As previously mentioned, the pathing in this code is absolute. Basically, 
     whenever the code references a file it looks for it in your home folder. 
     My username is "alkarbo" so for me this path looks like:

     /Users/alkarbo/autoemail/

     What you need to do is go through all of the code and change this to
     work with your username. Any time you see the above /Users/... syntax you
     need to change the second field to your username. So, the above would become:

     /Users/*yourusername*/autoemail/

     There are 10 uses of this syntax in automeial.sh and 5 uses in each of the
     python files (the same 5 uses because the python files all have the same
     format). You must change all of them, but if you miss one the code should
     produce an error saying that the file does not exist and telling you
     where the incorrect pathing is.  

3. CRONJOB

The code is now fully configured to run correctly! You could manually run it
every day but i'd recommend just setting up a cronjob to do it. From Terminal 
first use this command:

crontab -e

Then press fn + i

Then paste in the following line:

00 09 * * * ~/autoemail/autoemail.sh > ~/autoemail/log.txt

Then press Esc

Then Type: 

:wq!

And finally press return.

That's it! What you just did is tell your system to run a cronjob at 9:00am
every day. The cronjob will run autoemail.sh and record the output of the code
to a log file in the autoemail folder.

Ok, that should be everything! If the code isn't running make sure your computer
isn't asleep or off (because then crontab won't be running). There is a lot of 
online support for the different aspects of this code, but if you need
assistence specific to this program you can reach out to Karbo at 
alexanderkarbo@gmail.com.

I hope you enjoy being the Ticket Office Fellow!