# 一些关于跳转指令的规律

跳转涉及的指令：B系列、RET

### 跳转到原来的位置

大部分情况下IDA中不把这种情况当做跳转点。不是很懂这是出于什么目的，或许是和哈弗结构相关吧。但为什么没有`b`跳到当前指令的？

```
0x144:	bl	#0x144
```

```
0xf0:	bl	#0xf0
```



### 条件执行

记录到了0x2b8，0x2bc两个tag

```
0x2ac:	cmp	x9, x0
0x2b0:	cset	w10, eq
0x2b4:	tbnz	w10, #0, #0x2bc
0x2b8:	b	#0x314
0x2bc:	orr	w8, wzr, #4
0x2c0:	str	w8, [sp, #4]
0x2c4:	bl	#0x2c4
```



### 连续两个`b`

两个`b`相连，按照前面经验，或许会区分出3个tag，但是实际上IDA获得的tag是两个：0x3c0，0x3c4

```
0x3bc:	b	#0x330
0x3c0:	b	#0x280
```



### 没有被IDA识别的`bl`

除了跳转到指令自身位置，也存在`bl`不被识别的案例。没有被识别的原因大概是IDA把tag标记在了子函数的位置上。

0x14有一个`bl`调用，被调用额0x8c处也的确是一个函数的第一个指令位置，这个跳转应该是存在的。

```
x0:	stp	x22, x21, [sp, #-0x30]!
0x4:	orr	w0, wzr, #0x40
0x8:	stp	x20, x19, [sp, #0x10]
0xc:	stp	x29, x30, [sp, #0x20]
0x10:	add	x29, sp, #0x20
0x14:	bl	#0x8c
0x18:	mov	x19, x0
0x1c:	cbz	x19, #0x78

0x88:	ret	
0x8c:	str	x19, [sp, #-0x20]!
0x90:	stp	x29, x30, [sp, #0x10]
0x94:	add	x29, sp, #0x10
0x98:	mov	x19, x0
0x9c:	bl	#0x470
0xa0:	tbz	w0, #0, #0xb4
0xa4:	ldp	x29, x30, [sp, #0x10]
0xa8:	mov	x0, xzr
0xac:	ldr	x19, [sp], #0x20
0xb0:	ret	

tag: 0x8c
```



看起来在调用库文件时候`bl`才会触发tag。

**但是这存在一个问题，如果`bl`指令被包含在basic block中，且按照之前论文中的数据预处理方法（立即数清零），使用NLP处理时，不同的`bl`指令的特征是不同的，但是显然如果`bl`指向的函数功能不同，这个包含`bl`指令的basic block语义是不同的**







### 栈顶指针常常预示着函数



```
sub	sp, sp, #0x50
```





########################################################3

O0



cbz也会跳

有bl自跳

自跳常在头部tag前？

头部tag常在b中出现



看来头要更隐蔽，下面这样的很难发现

if XXX:

xxxxxx

```
0x214:	ldr	w0, [x0, #0x11b0]
0x218:	cmp	w19, w0
0x21c:	b.ge	#0x25c
0x220:	add	x21, x25, #0x20, lsl #12		tag!!!
0x224:	add	x26, x29, #0x68
0x228:	sxtw	x0, w19		tag!!!
0x22c:	ldr	x2, [x21, #0x11b8]
0x230:	add	x1, x2, x0, lsl #3
0x234:	ldr	x0, [x2, x0, lsl #3]
0x238:	cbz	x0, #0x24c
0x23c:	mov	x0, x26		tag!!!
0x240:	blr	x20
0x244:	cbnz	w0, #0x25c
0x248:	str	w19, [x22]		tag!!!
0x24c:	add	w19, w19, #1		tag!!!
0x250:	ldr	w0, [x21, #0x11b0]
0x254:	cmp	w0, w19
0x258:	b.gt	#0x228
0x25c:	ldr	w19, [x29, #0x7c]		tag!!!
0x260:	subs	w19, w19, #1
```

if对应的条件执行语句是容易发现的，但是问题在于有多少代码是条件执行

#条件

#满足条件则跳转至AD 1

#代码

#...

#代码

#AD 1



```
5,"PUSHQ~RBP
PUSHQ~R15
PUSHQ~R14
PUSHQ~RBX
SUBQ~RSP,0
MOVQ~R14,RCX
MOVL~EBP,ESI
MOVQ~RBX,RDI
MOVQ~R15,RSP
MOVQ~RDI,R15
MOVQ~RSI,RDX
MOVQ~RDX,R8
CALLQ~FOO
MOVQ~RDI,RBX
MOVL~ESI,EBP
MOVQ~RDX,R14
MOVQ~RCX,R15
CALLQ~FOO
ADDQ~RSP,0
POPQ~RBX
POPQ~R14
POPQ~R15
POPQ~RBP
RETQ","LSL~R0,R11,0
ASR~R0,R0,0
CMP~R0,0
BGE~<TAG>",0
```





被调用函数的语义如何考虑？



O1



跳自己的变少了





看不懂

b	#0xfffffffffffffff4



b.XX跳转，会与两个BLOCK HEAD相关





RET，B   这种大幅度不可能返回的函数后面肯定有跳转





被控制流与函数边界切碎的一两条指令构成的block，这种碎片block只能靠切头/尾的方式来找

0x160:	cmp	w0, #0		tag!!!
0x164:	cset	w0, eq
0x168:	b	#0x154
0x16c:	movz	w0, #0x1		tag!!!
0x170:	ret	



if切的变多了





w系列寄存器是做什么的？



O2

0x10c

```

0x104:	ldp	x23, x24, [x29, #0x30]
0x108:	ldp	x25, x26, [x29, #0x40]
0x10c:	movz	w21, #0x1		tag!!!
0x110:	mov	w0, w21
0x114:	ldp	x21, x22, [sp, #0x20]
0x118:	ldp	x29, x30, [sp], #0x120
0x11c:	ret	

```

movz	w21会跳，不知是不是巧合。而且都是在高级优化中出现的。但是O3中这个指令不是开头





tbnz





rule-based找block head

条件跳转指令（cbz,tbz，b.XX，...）一般可以找到两个，分别是跳转地址和下一条

无条件跳转可以找到1~2个，如b,re;如果b的目标地址在代码段，可认为找到两个

根据观察，当优化程度高的时候（O2，O3），nop很可能是block head，不过这个现象只在gcc用高级优化编译得到的文件中才有。clang中没有（也可能是我看的少？只看了约20个文件，查找约5000行）

压栈



