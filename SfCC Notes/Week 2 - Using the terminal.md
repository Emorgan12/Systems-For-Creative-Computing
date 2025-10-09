```Bash

pwd - Print Working (Current) Directory
	- -L -Logical
	- -P - Physical
ls - List contents
	- -l - Long (More info)
cd {FolderName}/ - Go inside folder
cd .. - Go back
cd ~ - Go home
cd ~/{FolderName} - Go to Folder from home
mkdir {DirectoryName} - Make Directory
touch {FileName}.{File Extension} - Create File
cp {FileName}  {CopyName} - Copy File
rm {FileName} - Remove File
	- -rf * - Recursively Remove all by force
mv {FileName} {DirectoryName/NewName} - Move/Rename File
open {FileName} - Open file in default app
cat {FileName} - Output file content
echo '{Message}' - Output Message
man {Command} - Output command manual (Q to quit)
nano {FileName} - Edit File (Text only)
| (Pipe) - Sends output of previous command to next
	- i.e. cat file1.txt | wc --> {Lines} {Words} {Characters}
wc {Text} - Word Count
date - Output (Long) Date + Time
{Text} >> {FileName} - Append Text to File
chmod {Permission} {FileName} - Change Mode
	- +x - Executable
./{FileName} - Run executable
```


```Bash
#!/bin/bash

# This is a Script to create a folder and populate it

mkdir library_project
cd library_project
touch library.txt
date >> library.txt
echo 'All finished!'
```