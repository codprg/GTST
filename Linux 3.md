## Further on Linux
### Linux file hierarchy
* File system is a directory str that the OS 
* system file are file used by the system software 
* the Linux file system in the root(/) section 
1. /(root)
* every single file and directory starts from the root directory. 
2. bin (Binary executable)
* essential commands binaries that need to be available in single user mode for all users.
3. boot (boot loader files)
* kernel intird. vmlinux, grub files are located under/boot
4. /dev (essential device files)
* these include terminal devices usb or any device attachde to the system.
5. /etc (et cetera)
* contains conf files required by all programs.this also contains startup and shutdown shell script
6. /home (home directory)
* for all users to store their personal files. 
7. /lib (libraries essential for the binaries in /bin & /sbin).
8. /media (mount point) removable media such as CD-ROMs.
9. /mnt (temporarily mounted file) whwre sysadmin can mount filesystem.
10. /opt (optional application software packages)
* contains add-on applications from individual vendors.
11. /sbin (essential system binaries) just like /bin, sbin, also contain binary excitable. 
12. /tmp (temporary file)
* directory that contain temporary file
13. /usr (User utilities)
* contains binary, libraries, documentation and source code for second level program. 
### command line text editor
* vim its a powerful, but at the same time it cryptic, its hard to learn, specially for windows users. to use vim first (i) insert mood than text anything to save (: w) than to out (: q) and to force out (:wq!) than enter and so (: u) undo (:%!) to write command
* nano its a text editor 
1. Ctrl+S-save
2. Alt+U-Undo
3. Alt+E-Redo
4. Ctrl+X-Exit
5. Ctrl-shift+C-copy
#### sudo (superuser do)
### creating users 
* there are 2 ways the first one is
1. Useradd its just normal sudo useradd chalew 
2. Adduser to add user sudo adduser chalew it have detail thing 
* the user file location /etc/passwd
* the user password location the password is decripted /etc/shadow/
[[Linux 4]]
