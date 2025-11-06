## File Permissions
### ls -l
- D or - : File Type (Directory or file)
- Permissions (9 characters - 3 groups of 3):
	- Owner - User who created file
	- Group - Users in the file's primary group
	- Other - Everyone else

	- R  - Read
	- W - Write
	- X - Execute
- No Letter ( - ): Lack of permission
### chmod {Owner/Group/Other}
- Read = 4
- Write = 2
-  Execute = 1
i.e:
- Owner (rwx) = 4 + 2 + 1 = 7
- Group (r-x) = 4 + 0 + 1 = 5
- Other (r--) = 4 + 0 + 0 = 4
chmod 754 {FileName}
## Variables

- Declaring - {VARIABLENAME} = {Data}
- Accessing - ${VARIABLENAME}

- Variable from input - read -p {InputPrompt} VARIABLENAME

```sh
#!/bin/bash

read -p "What are you having for tea?: " FOOD
echo "$USER, you are having $FOOD for tea"
```


# FLOSS (Free/Libre Open Source Software)
- Free Software (FSM) - Focuses on the user's Four Essential Freedoms. An ideological, ethical position.
	- Freedom 0 - To run the program for any purpose
	- Freedom 1 - To study + change it to fit the user
	- Freedom 2 - To redistribute copies to help a neighbour
	- Freedom 3 - To distribute copies of the modified versions
	- 