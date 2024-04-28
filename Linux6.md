# it is the end of Linux class
                   Script Installation 
==some hacking tools are developed by some people and those people make it open source that means we can those script Programs from GitHub==
          ==let me see an example: git clone <link of the script from GitHub>==

          Script modules
 ==are made with scripting languages (programming) like python, bash, go, ruby==
 ==so when we use these programming languages to do tasks their is something==
 ==called modules/library's these are needed to run the script as the dependencies==

   example 1. python to install modules we use > pip install <module name>
   example 2. Go there are 2 Installation method 
   a, old * go github.com: capotej/groupcache-db-experiment.git *
   b, New * downloading the package go install github.com/Ic/gau/..../.git

                   errors you may encounter

                   don't close apt while Installation
                   repository errors, if this happened u can fix it using [sudo apt edit-sources]
                   and more
                   for those kinds of errors what you have to do is google/YouTube


                         if u need help on Linux about commands
                         u can use 
                         .man (manual) this will give u the whole manual and instruction of a tool or commands
                         example man <your-command>
                         .q to quite or to out of them 
                         .help some commands have help
                         to use help option <your-command> -h
                                            <your-command> -help
                                            <your-command> - -help
                        

                        Linux processes and services

                        - as we interact with Linux we crate numbered instances of running Programs
ps 
ps -a
ps -u username
                        . to stop processes
                        
                        _ kill[option]
                        _more on kill 
                        .kill-19pid > to stop the processes
                        .kill-18pid > to resume the processes we stopped
                        .kill-9pid > to stop a processes immediately

                        -background run method tools
                        .use this method (&) let me see an example nano takme.txt$
                        .to re-back use this method (fg) 


                        Null device
                        .dev/null/ -redirect output to nowhere
                        .if u want to ignore output, u can send it to the null device, del/null
                        .the null device is a special file that throws away whatever is fed to it

                        -symbolic linking
                        is same as windows shortcut
                        is a processes of creating a linked shortcut from of file from of file to some pre-existed
                        file or folder

                        .syntax > ln -s source_file-path my-filename