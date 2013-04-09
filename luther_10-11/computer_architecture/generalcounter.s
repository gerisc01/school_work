.section .data
items:
   .long 6,22,4,8,9,1,22,22

counter:
   .long 0

.section .text

.globl _start

_start:

movl $1,%esi
movl items(,%esi,4),%ebx
movl $0,%esi
movl items(,%esi,4),%eax
movl $8,%edx
loopbegin:
cmpl %esi,%eax
je done
movl items(%edx,%esi,4),%ecx
cmpl %ecx,%ebx
jne increment
addl $1,counter
increment:
incl %esi
jmp loopbegin
done:
movl counter,%ebx
movl $1,%eax
int $0x080
