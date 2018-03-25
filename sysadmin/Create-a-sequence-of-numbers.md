- Date : 2018-03-25
- Tags : #sysadmin #string

## Create a sequence of numbers

In the past, every time I want to create a sequence of numbers. I have to use something like MS EXCEL, then copy it and paste to text editor. It's tricky way and slow !

Now, I can use the handy tool `seq` to achieve that

`man seq`

```
SEQ(1)                                          User Commands                                         SEQ(1)            

NAME                          
       seq - print a sequence of numbers                    

SYNOPSIS                      
       seq [OPTION]... LAST   
       seq [OPTION]... FIRST LAST                           
       seq [OPTION]... FIRST INCREMENT LAST                 

DESCRIPTION                   
       Print numbers from FIRST to LAST, in steps of INCREMENT.                                                         

       Mandatory arguments to long options are mandatory for short options too.                                         

       -f, --format=FORMAT    
              use printf style floating-point FORMAT        

       -s, --separator=STRING 
              use STRING to separate numbers (default: \n)  

       -w, --equal-width      
              equalize width by padding with leading zeroes
```

So we have 3 main arguments (same as for loop) :

- FIRST
- INCREMENT
- LAST

And 3 options :

- format : you can use string format like `This is number %g`
- separetor : default is new line
- equal width : padding with leading zeroes

Example :

```bash
$ seq -f"This is number %g" 3 4 20
This is number 3              
This is number 7              
This is number 11             
This is number 15             
This is number 19
```

```bash
$ seq -w -s", " 10
01, 02, 03, 04, 05, 06, 07, 08, 09, 10
```
