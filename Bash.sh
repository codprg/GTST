#!/bin/bash



#echo hello world this is bash course" 

#date 

#rm -rf //home/codprg/Pictures/* 

#pwd

#day 10 course its all about Bash 
# what is Bash 
# -use of bash for hackers
# -output
# -variables and data type


# bash - bourne again shell
# -it is a shell thst used to interact with your kernel 

# what is script
# - is a file that contains shell commands in simple clear algorithm.
# - the original is sh - bourne shell


# uses of Bash 
# - script development 
# - automating tasks
# - simplifying your linux ablity



# - bash files can have sh extension but you can have it without .sh too
# - the file have to have executable permissions.


# - to crate a bash file follow this steps 
# -  touch main.sh, nano text.sh and so ............


# to display the output use this method 
# - to star every bash script use shebang, #!/bin/bash, #!/bin/sh


echo "this is bash scribting tutorial day 10 course started on"
date 
echo

fname="Codprg"
lname="chalew"

echo "Your Name is $fname and your father name is $lname"

# to call the var use this $ sign and ${} this option
# the are difference ${} in this method the difference is In this method ${} to colaborate the text.

set natan mintesnot jr_Malik hamza joel

echo $1 $2 $3 $4

num=10
echo "this is day${num}class"

echo $BASH
echo $BASH_VERSION
echo $PWD
echo $HOME
echo $PATH  # they are system variables
echo $USER # it shows the owner of the maction

# variables and Data types
# - Arrays are lists or tuples on python

var=("joel" "at_10" "emebet" "samuel")

echo ${var[0]}

echo ${var[@]} # to display all var

echo ${!var[@]} #to show the index number

echo ${#var[@]} # to show the length of your var

var[6]="chalew" # to add the element  

echo ${!var[@]}

unset var[2] # to delet the remove

echo ${var[@]}

# Bash read 

echo "[?] GTST COMPANY LOGIN."

read -p "[+] Enter Username: " NAME

read -sp "[+] Enter Password: " PASS

echo

echo "Your Username is $NAME"

echo

echo "Your Password is $PASS"

# bash sleep 

# - sleep option

echo "chalew"

sleep 23s

echo "codprg"















