.text
	.globl main
	
main:	
	li $v0, 4		# print msg 1
	la $a0, msg1
	syscall
	
	li $v0, 5		# take input
	syscall
	move $t0, $v0		# input
	
	li $t1, 0		# sum
	li $t2, 1		# check
	move $t3, $t0		
	srl $t3, $t3, 1
	
loop:	add $t1, $t1, $t3
	srl $t3, $t3, 1
	beq $t3, $t2, exit
	j loop
	
exit:	addi $t1, $t1, 1
	li $v0, 1
	move $a0, $t1
	syscall
	
	li $v0, 10		# exit
	syscall
	
	.data
msg1:	.asciiz "Enter n: " 
