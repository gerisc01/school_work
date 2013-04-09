.section .data

inputstr:
.ascii "Please enter a number \0"

formatstr:
.ascii "%d\0"

formatstr1:
.ascii "%s\0"

outputstr:
.ascii "Is your number a prime number? %s\n\0"

outputstr1:
.ascii "%d\n\0"

n:
.long 0

true:
.ascii "true\0"

false:
.ascii "false\0"

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

pushl n
call prime
addl $4,%esp

pushl %ebx
pushl $outputstr
call printf
addl $8,%esp

movl n,%esi

findprimes:
cmpl $1,%esi
je halt
movl %esi,%ebx
decl %ebx

printloop:
cmpl $1,%ebx
je isprime

movl %esi,%eax
cdq
idivl %ebx
cmpl $0,%edx
je notprime
decl %ebx
jmp printloop

notprime:
decl %esi
jmp findprimes

isprime:
pushl %esi
pushl $outputstr1
call printf
addl $8,%esp
decl %esi
jmp findprimes

halt:
movl $1,%eax
movl $0,%ebx
int $0x080

prime:
pushl %ebp
movl %esp,%ebp

movl 8(%ebp),%ebx
cmpl $1,%ebx
jle donefalse

decl %ebx

beginloop:
cmpl $1,%ebx
je donetrue

movl n,%eax
cdq
idivl %ebx
cmpl $0,%edx
je donefalse

decl %ebx
jmp beginloop

donefalse:
movl $0,%ecx
movl $false,%ebx
movl %ebp,%esp
popl %ebp
ret

donetrue:
movl $true,%ebx
movl %ebp,%esp
popl %ebp
ret
