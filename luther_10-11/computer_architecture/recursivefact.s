.section .data

inputstr:
.ascii "Please enter a number \0"

formatstr:
.ascii "%d\0"

outputstr:
.ascii "The factorial is %d\n\0"

simpleoutput:
.ascii "%d\0"

n:
.long 0

.section .text

.globl _start
_start:

pushl $inputstr
call printf
addl $4,%esp

pushl $n
pushl $formatstr
call scanf
addl $8,%esp

movl $1,%eax

pushl n
call fact
addl $4,%esp

pushl %ebx
pushl $outputstr
call printf
addl $8,%esp

movl $1,%eax
int $0x080

fact:
pushl %ebp
movl %esp,%ebp

movl 8(%ebp),%ebx

cmpl $1,%ebx
je done

imull %ebx
decl n

pushl n
call fact
addl $4,%esp

done:

movl %eax,%ebx
movl %ebp,%esp
popl %ebp
ret

