.section .data

n:
 .long 5

.section .text

.globl _start
_start:

pushl n

call fact

addl $4, %esp


movl $1, %eax
int $0x080

fact:

pushl %ebp
movl %esp, %ebp

movl 8(%ebp),%ebx
movl n,%ecx
decl %ecx

beginloop:
cmpl $0, %ecx
je done

imull %ecx,%ebx
decl %ecx
jmp beginloop

done:

movl %ebp,%esp
popl %ebp
ret
