

# 简介

ARM具有两种运行模式，ARM模式和Thumb模式。Thumb指令可以是2或4个字节的

ARM与x86指令结构的不同之处

- ARM架构在ARMv3之前是小端序的，在那之后，ARM处理器提供一个配置项，可以通过配置在大端和小端之间切换。
- 在ARM中大多数指令可以用于分支跳转的条件判断。

ARM的不同版本之间的差别也不小



当你编写了后缀为“.s”的汇编文件，你可以使用as将它汇编，最后使用ld链接



# 数据类型与寄存器

## 数据类型

数据类型有四种，可按字节/半长/全长+是否有符号区分，相应的

![image-20200913212459395](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200913212459395.png) 



# ARM寄存器

除了基于ARMv6-M和ARMv7-M的处理器，其它的ARM处理器都有30个32 bit的通用寄存器。前17个寄存器是在**用户模式**下可访问的，其它的寄存器只有在特定的运行模式下才可以访问，此篇教程关注那些可以在任何运行模式下被访问的寄存器：r0~r15还有CPSR。这16个又被分为两组：用寄存器和专用寄存器。



![image-20200913213204286](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200913213204286.png) 



后来的ARM是流水线的，所以PC寄存器的值可能往后跳



当前程序状态寄存器CPSR，它里面有很多标志位thumb、fast、interrupt、overflow、carry、zero和negative

![image-20200913215603534](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200913215603534.png)  



![image-20200913215928995](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200913215928995.png) 

假设我们用cmp指令来比较1和2，结果将为负，Negative标志位被置1。 





# ARM和Thumb

不同的ARM版本，支持的Thumb指令集并不相同。

编写ARM shellcode时，需要使用16 bit的Thumb指令代替32 bit的ARM指令，从而避免在指令中出现’\0’截断。

[http://infocenter.arm.com/help/index.jsp](https://bbs.pediy.com/thread-220753.htm)

ARM状态下的所有指令都支持条件执行。某些ARM处理器版本允许使用IT指令在Thumb中进行条件执行。

32位ARM和Thumb指令：32位Thumb指令具有.w后缀。



# ARM指令简介



```
MNEMONIC{S}{condition} {Rd}, Operand1, Operand2
```



MNEMONIC   - 指令的助记符如ADD

{S}     - 可选的扩展位， \- 如果指令后加了S，将依据计算结果更新CPSR寄存器中相应的FLAG

{condition} - 执行条件，如果没有指定，默认为AL(无条件执行)，设置了执行条件的指令在执行指令前先校验CPSR寄存器中的标志位，只有标志位的组合匹配所设置的执行条件指令才会被执行。

{Rd}     - 目的寄存器，存储指令计算结果

Operand1   - 第一个操作数，可以是一个寄存器或一个立即数

Operand2   - 第二个(可变)操作数 \- 可以是一个<u>立即数</u>或<u>寄存器</u>甚至<u>带移位操作的寄存器</u>，

![image-20200914162617763](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914162617763.png) 



**总的来看，主要是{S} 与{condition}是新的，第二个操作数的模式比想象的要多**



## 常见的指令

| MOV  | 移动数据       | EOR     | 单比特异或             |
| ---- | -------------- | ------- | ---------------------- |
| MVN  | 取反码移动数据 | LDR     | 加载数据               |
| ADD  | 数据相加       | STR     | 存储数据               |
| SUB  | 数据相减       | LDM     | 多次加载               |
| MUL  | 数据相乘       | STM     | 多次存储               |
| LSL  | 逻辑左移       | PUSH    | 压栈                   |
| LSR  | 逻辑右移       | POP     | 出栈                   |
| ASR  | 算数右移       | B       | 分支                   |
| ROR  | 循环右移       | BL      | 带返回的分支           |
| CMP  | 比较操作       | BX      | 带状态切换的分支       |
| AND  | 单比特与       | BLX     | 带返回、状态切换的分支 |
| ORR  | 单比特或       | SWI/SVC | 系统调用               |





# 寻址

## 寄存器寻址

**寻址上，ARM指令支持立即数寻址，寄存器寻址，缩放（Scaled）寄存器寻址**



#### First basic example

对例如LDR的指令，第二个寄存器外是否有\[\]是不一样的，如果是个立即数（或者说label?），（下面的adr_var1），则存入的是这个数字，如果后面是有\[\]的寄存器，则存入的是<u>寄存器数值指向的地址的值</u>

![image-20200914165730941](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914165730941.png) 



pc相对寻址

![image-20200914170629946](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914170629946.png) 



\[pc, #12]的意思是pc寄存器的值加12，这是由于ARM采用的是哈佛指令结构，得到这个值是0x8074+4+4+12。运行到第一个ldr的时候pc指向了第三个ldr



### 1.偏移方式：立即数做偏置

![image-20200914172053773](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914172053773.png) 

立即数涉及三种写法，除了之前的写法，还有两种，一种叫做pre-indexed，另一种写法称作post-indexed。

```
str r2, [r1, #2]            @ address mode: offset. Store the value found in R2 (0x03) to the memory address found in R1 plus 2. Base register (R1) unmodified. 
str r2, [r1, #4]!           @ address mode: pre-indexed. Store the value found in R2 (0x03) to the memory address found in R1 plus 4. Base register (R1) modified: R1 = R1+4 
ldr r3, [r1], #4            @ address mode: post-indexed. Load the value at memory address found in R1 to register R3. Base register (R1) modified: R1 = R1+4 
```



第一种是常规的，r1不变，后两种里r1都发生了改变，区别在于r1变化发生在何时。



### 2.偏移方式：寄存器做偏置

![image-20200914173257618](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914173257618.png) 

具体的规则和立即数寻址里是一样的。

```
str r2, [r1, r2]            @ address mode: offset. Store the value found in R2 (0x03) to the memory address found in R1 with the offset R2 (0x03). Base register unmodified.   
str r2, [r1, r2]!           @ address mode: pre-indexed. Store value found in R2 (0x03) to the memory address found in R1 with the offset R2 (0x03). Base register modified: R1 = R1+R2. 
ldr r3, [r1], r2            @ address mode: post-indexed. Load value at memory address found in R1 to register R3. Then modify base register: R1 = R1+R2.
```



### 3.偏移方式：缩放（Scaled）寄存器寻址

![image-20200914174837586](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914174837586.png) 



```
str r2, [r1, r2, LSL#2]            @ address mode: offset. Store the value found in R2 (0x03) to the memory address found in R1 with the offset R2 left-shifted by 2. Base register (R1) unmodified.
str r2, [r1, r2, LSL#2]!           @ address mode: pre-indexed. Store the value found in R2 (0x03) to the memory address found in R1 with the offset R2 left-shifted by 2. Base register modified: R1 = R1 + R2<<2
ldr r3, [r1], r2, LSL#2            @ address mode: post-indexed. Load value at memory address found in R1 to the register R3. Then modifiy base register: R1 = R1 + R2<<2
```



**总结：**

![image-20200914175405576](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914175405576.png) 



## PC相对寻址

LDR不止可以从内存向寄存器加载数据，也存在这样的语法。

![image-20200914175747875](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914175747875.png) 

可以载入标签，十进制（默认），和十六进制（0x）。In the example above we use these pseudo-instructions to reference an offset to a function, and to move a 32-bit constant into a register in one instruction. The reason why we sometimes need to use this syntax to move a 32-bit constant into a register in one instruction is because ARM can only load a 8-bit value in one go.



## 在ARM上使用立即值



![image-20200914182323914](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914182323914.png) 

We know that each ARM instruction is 32bit long, and all instructions are conditional. There are 16 condition codes which we can use and one condition code takes up 4 bits of the instruction. Then we need 2 bits for the destination register. 2 bits for the first operand register, and 1 bit for the set-status flag, plus an assorted number of bits for other matters like the actual opcodes. The point here is, that after assigning bits to instruction-type, registers, and other fields, there are only 12 bits left for immediate values, which will only allow for 4096 different values.



**为什么说第一个操作数寄存器为2位？？没看明白**



这意味着ARM指令只能直接在MOV中使用有限范围的立即值。如果不能直接使用数字，则必须将其分成多个部分，然后将多个较小的数字拼凑在一起。

但是还有更多。不是将12位用于单个整数，而是将这12位拆分为一个8位数字（n），它可以加载0-255范围内的任何8位值，而4位旋转字段（r）为一个整数。在0到30之间以2的步长向右旋转。这意味着完整的立即值v由以下公式给出：v = n ror 2 * r。换句话说，唯一有效的立即数是旋转的字节（可以减少为以偶数旋转的字节的值）。



![image-20200914182604970](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914182604970.png) 

也就是说数字是8位数位移0,2,4,6，.......30



**结论**：在ARM使用是有很多限制的，因为给立即数的位置就12位。**但是为什么说2 bits for the first operand register我没看明白**。

**绕过这一限制的解决方案**：

![image-20200914183152448](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914183152448.png) 

例子：

![image-20200914183008683](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914183008683.png) 

mov指令会引发报错。



替代方案：

![image-20200914183325097](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914183325097.png) 

两种都是可行的

*<u>literal pool是什么？？？</u>*





# 多次加载/存储

LDM 

STM 

具体的指令涉及到ldm,stm,ldmia,stmia,ldmib,stmib,ldmda,ldmdb,stmda,stmdb这些指令的差别在与处理序列时的起始位置和处理方向不同 **The type of variation is defined by the suffix of the instruction. Suffixes used in the example are: -IA (increase after), -IB (increase before), -DA (decrease after), -DB (decrease before). **

![image-20200914185706718](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914185706718.png) 



*（有趣的是后三行的操作，记下了序列的起始地址）*





另外要注意的是ADR指令，大概是这么用，不难但是前面没有提到过。

```
adr r0, words+12             /* address of words[3] -> r0 */
```



**总结**：我认为这块涉及的道理不难



# PUSH AND POP

堆栈指针SP，正常情况下将始终指向an address wihin the Stack’s memory region（栈顶）。ARM里堆栈向下生长，

入栈时：

![image-20200914192854119](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914192854119.png) 

出栈时：

![image-20200914192944028](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914192944028.png) 



下面是汇编和反汇编的结果。可以看出<u>pop,push可以用stmdb之类的指令替代，有点像混淆的感觉</u>

![image-20200914193148807](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914193148807.png) 

![image-20200914193203136](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914193203136.png) 





# CONDITIONAL EXECUTION

这里是ARM架构的一个特色。cmp语句会触发CPSR寄存器进行修改，后面的 程序如果要用到cmp中的比较结果，直接看CPSR就好了（我是这么理解的）

![image-20200914194342049](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914194342049.png) 



```
.global main

main:
    mov     r0, #2     /* setting up initial variable */
    cmp     r0, #3     /* comparing r0 to number 3. Negative bit get's set to 1 */
    addlt   r0, r0, #1 /* increasing r0 IF it was determined that it is smaller (lower than) number 3 */
    cmp     r0, #3     /* comparing r0 to number 3 again. Zero bit gets set to 1. Negative bit is set to 0 */
    addlt   r0, r0, #1 /* increasing r0 IF it was determined that it is smaller (lower than) number 3 */
    bx      lr
```





# CONDITIONAL EXECUTION IN THUMB

某些ARM处理器版本支持“ IT”指令，该指令最多可在Thumb状态下有条件地执行4条指令。

语法：

```
IT{x{y{z}}} cond
```

![image-20200914195159884](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914195159884.png) 

![image-20200914195225418](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914195225418.png) 

注意这里的NE/EQ,GT/LE都是完全对立的逻辑，上面也提到了logical inverse

![image-20200914195236321](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914195236321.png) 

![image-20200914195520858](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914195520858.png) 



![image-20200914200816539](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914200816539.png) 



![image-20200914200831792](D:%5CPAPER%5CARM%E7%AC%94%E8%AE%B0.assets%5Cimage-20200914200831792.png) 

第一个例子没看懂，这个和LSB有什么关系？？可能要从指令对应的二进制码开始看。































































