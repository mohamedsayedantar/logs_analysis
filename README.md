# logs_analysis
shows you the most popular three articles in an articles website, and the most 
popular article authors of all time, eventually it provides the percentage of the responses errors for each day.


## The virtual machine
  This project makes use of the same Linux-based virtual machine (VM) to install the virtual machine:-
  1. Install VirtualBox from https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
  2. Install Vagrant from https://www.vagrantup.com/downloads.html
  3. Download the VM configuration from https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip
  4. use your terminal and go to the directory called vagrant using "cd"
  5. Start the virtual machine using "vagrant up" command
  6. you can run "vagrant ssh" to log in to your newly installed Linux VM
  7. then you need to Download the data from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
  8. To load the data, "cd" into the vagrant directory and use the command "psql -d news -f newsdata.sql"
  9. put the news.py file inside the vagrant file and the run "python news.py" in your terminal
