# Fable-Repository 2
 Fixed width Formatter



Created By:  Padraic Gilbert




Thanks for your interest in my formatter.  I created this tool to deal with large fixed width text files.  Large in this context is something +200K rows.  
It uses pandas to format the text file based on the layout file its provided.   


This requires to inputs:

1)  A Layout File.  This just needs to be a two columned file, in first column you need the column names for your fixed width file.  The second column should have the widths for Each Column
in your File.  

2) A save folder and name you want to save your excel or database file under.  

I added multiple options:

A) Provide a file name and this will save the file to your specified excel sheet


B) If you have a lot of files to load, this option lets you provide a file list.  It will read in each file, formatting it based on the provided layout file, 
and then store it to a local sql database located in save directory you provided.  By default, the database will be named YourFileNameHere.db

