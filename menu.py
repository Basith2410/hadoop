import os 
print( '''Select the option you want to run :
	1.To open namenode hdfs configuration file
	2.To open namenode core configuration file        
	3.Start namenode in hadoop
	4.To run jps command        
	5.To open report
        6.Check hadoop list
	7.Create a file
	8.Upload a file in hadoop
	9.Delete a file in hadoop
	10.Exit''' )

while True:
	print(" Please enter your choice :")
	x=input()
	if (x=="1"):
	    os.system("vim /etc/hadoop/hdfs-site.xml")
	if (x=="2"):
	    os.system("vim /etc/hadoop/core-site.xml")
	if (x=="3"):
	    os.system("hadoop-daemon.sh start namenode")
	if (x=="4"):
	    os.system("jps")	
	if (x=="5"):
	    os.system("hadoop dfsadmin -report")
	if (x=="6"):
	    os.system("ls /") and os.system("hadoop")
	if (x=="7"):
	    print("Create new file")
	    y=input()
	    os.system("hadoop fs -touchz /{}".format(y))
	if (x=="8"):
	    print("Enter the file name to upload:")
	    z=input()
	    os.system("hadoop fs -put {} //".format(z))
	if (x=="9"):
	    print("Enter the filename to delete:")
	    k=input()
	    os.system("hadoop fs -rm /{}".format(k))
	if (x=="10"):
	    print("This program is ending") 	    
	    exit()
	
