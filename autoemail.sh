#This is autoemail.sh, a script written to email front of house and ticket office workers to remind them when they 
#have concerts to work. For setup instructions please read the provided README.txt. You will need to alter the script
#based upon the publishing address of your google spreadsheet and the number/names/emails of the students working for
#you. See the readme for further instructions on how to do that. If all else fails email the creator of this script: 
#Alexander Karbo (hi!) at alexanderkarbo@gmail.com.
#--------------------------------------------------
/usr/local/bin/wget -q -O /Users/alkarbo/autoemail/FOHsignup.csv 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRli1gZ_o1-oiurONRWY0D1nhlEA7pVHlTX5KfXctii2-vKus9yiFNcmKSsHEiVsMylqvBNTYDgUyOj/pub?gid=0&single=true&output=csv' #download FOH signup and save as FOHsignup.csv
/usr/local/bin/wget -q -O /Users/alkarbo/autoemail/TOsignup.csv 'https://docs.google.com/spreadsheets/d/e/2PACX-1vRAR6jqTmx2ybHnaOwbtOZYILsBQjScK8u8BFQMB-i-KGOTbNh8yvFSB98309ltkZ1dNDwdmHvADgnN/pub?gid=0&single=true&output=csv' #dowload TO signup and save as TOsignup.csv
echo "\nSchedules Downloaded"
python /Users/alkarbo/autoemail/FOHemail.py #run the FOH code
python /Users/alkarbo/autoemail/TOemail.py #run the TO code
python /Users/alkarbo/autoemail/TOemail2.py #run secondary TO code (they wanted a second reminder)
sh /Users/alkarbo/autoemail/FOHemail.sh #run the bash script written by FOHemail.py
sh /Users/alkarbo/autoemail/TOemail.sh #run the bash script written by TOemail.py
rm /Users/alkarbo/autoemail/FOHemail.sh && rm /Users/alkarbo/autoemail/TOemail.sh && rm /Users/alkarbo/autoemail/*.csv #clean temporary files
echo "Files Cleaned\n"