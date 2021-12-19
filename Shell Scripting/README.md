
# Assignment-1: Bash Scripting
I am writing README first time. If anything is wrong, please consider
## Installation

Use the ubuntu latest version for [Bash](https://ubuntu.com/#download) to install ubuntu 20.04 lts.

```bash
sudo apt install build-essential
```

## All commit done
I am using Vim Editor


## Software System Development

#### Answer1
[du](https://www.commandlinux.com/man-page/man1/du.1.html) is basically used for estimating file size, options -s for display only a total for each argument and -h for human readable in size(K,M,G,B). Pipes help combine two or more commands and are used as input/output concepts in a command.
sort -hr command used for sorting the input in reverse order(descending). Here awk is used for rearranging the output column. column -t command for column alignment of output. And here sed is just removing the slash after directory name.

#### Answer2
[grep](https://linuxhint.com/grep_command_linux/) is searching a specific pattern in a input file. options -w for word and -i for case insensitive, pipe doing samething. awk is converting input into lower case. In Linux, “tr” is a built-in tool that can “translate, squeeze, and/or delete characters from standard input, writing to standard output” (from man page), but here it is adding a new line after each word.

#### Answer3
Here I am first sorting the given word and matching with each linux command (that will be sorted also) using [compgen -c](https://linux.die.net/man/1/compgen) which shows all the command .for loop and if statement is used in this script.


#### Answer4
This problem already has been solved by me in Cpp language. I just changed the syntax and only access I have done is checking the number of input and what type input it is whether string or integer by [this](https://ss64.com/bash/) command.

#### Answer5
First make a directory by [mkdir](https://ss64.com/bash/) command and then change terminal directory by [cd](https://ss64.com/bash/) .Then created 50 txt files by [touch temp{1..50}.txt](https://ss64.com/bash/), after that changing the extension of first 25 txt files into md extension with help of for loop and [mv](https://ss64.com/bash/) command.
Now it was the difficult part for me that changing the file name only not the extension which is again solved by [mv](https://ss64.com/bash/) command with some manipulation .Last part is zipping those txt files that is done with help of [zip](https://ss64.com/bash/) command.

## Acknowledgement
There is a issue with my second script , command is showing two times for some word.

[Read More](https://ss64.com/bash/)

