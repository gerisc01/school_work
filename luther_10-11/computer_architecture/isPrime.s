.section .data
n:
 .long 3

.section .text

.globl _start
_start:

pushl n
call prime

addl $4,%esp

movl $1,%eax
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
movl $0,%ebx
movl %ebp,%esp
popl %ebp
ret

donetrue:
movl $1,%ebx
movl %ebp,%esp
popl %ebp
ret
