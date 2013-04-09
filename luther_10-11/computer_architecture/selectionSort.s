.section .data

string:
.ascii "abdicators\n"

nl:
.ascii "\n"

.section .text

.global _start
_start:

movl $4,%eax
movl $1,%ebx
movl $string,%ecx
movl $11,%edx
int $0x080

movl $10,%ecx
movl $1,%edx

beginloop:
cmpl $1,%ecx
je done

movl $0,%eax

movl $1,%edx

compareloop:

movl %ecx,%esi
incl %esi

cmpl %edx,%esi 
je endcompareloop

movb string(,%edx,1),%bl
movb string(,%eax,1),%bh

cmp %bh,%bl
jng endif  

movl %edx,%eax

endif:
incl %edx
jmp compareloop

endcompareloop:
movb string(,%ecx,1),%bl 
movb string(,%eax,1),%bh       
movb %bh,string(,%ecx,1)   
movb %bl,string(,%eax,1)
decl %ecx
jmp beginloop

done:
movl $4,%eax
movl $1,%ebx
movl $string,%ecx
movl $12,%edx
int $0x080

movl $1,%eax
movl $0,%ebx
int $0x080
