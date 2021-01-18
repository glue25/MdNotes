find:
https://www.cnblogs.com/wanqieddy/archive/2011/06/09/2076785.html
https://www.runoob.com/linux/linux-comm-find.html


find+grep:
https://www.jianshu.com/p/b30a8aa4d1f1
https://www.cnblogs.com/skynet/archive/2010/12/25/1916873.html





# find

find的参数后面加不加""有什么区别我还没太找出规律，示例中都是加了""的。但有时候不加反而
能得到期望的语义
-not给我感觉不好用，用的时候还需要摸索
-a -o应该按顺序走就好
要利用文件夹中的字符串筛选时，可以使用 | grep (-v) 的方法，还是挺快的
实际上很多功能也可以用 | grep解决



## find -name

使用的RE其实这不是标准的RE，而且只能针对文件名，路径中的信息检测不到。目前测试来看，{}不能发挥以往的用处,\S也用不了

|  符号  |                       解释                       |
| :----: | :----------------------------------------------: |
|   *    |           代表任意字符（可以没有字符）           |
|   ?    |                 代表任意单个字符                 |
|   []   | 代表括号内的任意字符，[abc]可以匹配a\b\c某个字符 |
| [a-z]  |              可以匹配a-z的某个字母               |
| [A-Z]  |              可以匹配A-Z的某个字符               |
| [0-9]  |              可以匹配0-9的某个数字               |
|   ^    |        用在[]内的前缀表示不匹配[]中的字符        |
| [^a-z] |             表示不匹配a-z的某个字符              |





## find -regex

是将文件的输出结果进行匹配而不是文件名，使用-regex时必须使用正规的RE，以下为简单的RE使用

（或许有更多可用的符号，但是\d，$还是用不了）

| 是好用，但是需要前面加\

| 符号  |                       解释                       |
| :---: | :----------------------------------------------: |
|  []   | 代表括号内的任意字符，[abc]可以匹配a\b\c某个字符 |
| [a-z] |              可以匹配a-z的某个字母               |
| [A-Z] |              可以匹配A-Z的某个字符               |
| [0-9] |              可以匹配0-9的某个数字               |
|   .   |                 表示任意单个字符                 |
|   ?   |           表示前面的字符出现一次或零次           |
|   +   |            表示前面的字符至少出现一次            |
|   *   |           表示前面的字符出现零次或多次           |
|  ()   |              将字符括起来后面跟量词              |
|  \|   |             逻辑或，可以搜索两个条件             |











# grep

https://www.runoob.com/linux/linux-comm-grep.html

| options | 解释                                   |
| :------ | :------------------------------------- |
| -i      | 不区分大 小写(只适用于单字符)          |
| -r      | 遍历匹配                               |
| -v      | 显示不包含匹配文本的所有行             |
| -s      | 不显示不存在或无匹配文本的错误信息     |
| -E      | 可用于同时匹配多关键词                 |
| -w      | 整字匹配                               |
| -l      | 查询多文件时只输出包含匹配字符的文件名 |
| -c      | 只输出匹配行的计数                     |
| -n      | 显示匹配行及行号                       |
| -h      | 查询多文件时不显示文件名               |





## grep正则表达式

（和前文说的一样，有些需要转义）

| 符号  |                         解释                          |
| :---: | :---------------------------------------------------: |
|   <   |                      单词的开始                       |
|   >   |                      单词的结束                       |
|   ^   | 行的开始，^ 用在 [ ] 内表示不匹配其中的字符，注意区别 |
|   $   |                       行的结束                        |
|  {n}  |                 表示前面的字符匹配n次                 |
| {n,m} |                表示前面的字符匹配n-m次                |
| {,m}  |              表示前面的字符至多匹配的m次              |
| {n,}  |               表示前面的字符至少匹配n次               |
|   \   |          忽略正则表达式中特殊字符的原有含义           |
|   .   |                                                       |
|   *   |                                                       |



## 例子

- 忽略大小写搜索

  ```
    grep -i "androiD"  logcat.txt   //从logcat.txt文件中，搜索包含android的文本行，不区分大小写
  ```

- 遍历搜索，且不显示无匹配信息

  ```
    grep -rs "android" .   //从当前目录下，遍历所有的文件，搜索包含android的文本行
  ```

- 整字匹配搜索

  ```
    grep -w "android" logcat.txt  //从logcat.txt文件中，搜索包含单词android的文本行
    grep -w "android | ios" logcat.txt  //从logcat.txt文件中，搜索包含单词android或者ios的文本行
  ```

- 只列出文件名

  ```
    grep -l "android" .
  ```

- 统计字符出现次数

  ```
    grep -c "android" .
  ```

- 显示字符出现所在行

  ```
    grep -n "android“ .
  ```

- 显示多条件匹配

  ```
    grep -E "android|linux“ .
  ```



## 实例

https://www.runoob.com/linux/linux-comm-grep.html

1. 在当前目录中，查找后缀有 file 字样的文件中包含 test 字符串的文件，并打印出该字符串的行。此时，可以使用如下命令：

   ```
   grep test *file 
   ```

2. 找指定目录/etc/acpi 及其子目录（如果存在子目录的话）下所有文件中包含字符串"update"的文件（==**这个比较实用，字符串和路径的顺序是要记住的**==）

   ```
   grep -r update /etc/acpi
   ```

    

3. 通过"-v"参数可以打印出不符合条件行的内容。查找文件名中包含 test 的文件中不包含test 的行

   ```
   grep -v test *test*
   ```

   





## egrep

egrep是grep的进化版，改进了许多grep中不方便之处如下，egrep使用RE符号 `+ ， ？ ， | （或） , {}` 时不用转义，如果要用其本身则需要转义，因此推荐使用egrep和RE配合使用



**例1：搜索精确匹配Dialer单词的行（形如DialerActivity则不会匹配）**
 `egrep –nr “\<Dialer\>”`
 **例2：当前目录搜索以private开始的行（private前可能有空格）**
 `egrep -nr "^.*private"`









# find与grep结合

先看一个例子



```bash
function jgrep()
{
    find . -name .repo -prune -o -name .git -prune -o   
    -name out -prune -o -type f -name "*\.java" -print0 | xargs -0 grep --color -n "$@"
}
```

这个是Android系统源码build/envsetup.sh中的jgrep函数，用于搜索java文件内容，使用jgrep搜索效率远胜于单单使用grep进行搜索，下面对这个函数进行分析
 **find**
 在当前目录搜索
 **-o**
 或，并列多个条件
 **-name .repo –prune**
 忽略.repo目录（git库相关）
 **-name .git –prune**
 忽略.git目录（git库相关）
 **-name out –prune**
 忽略out目录（编译生成的目录）
 **-type f**
 指定文件类型为普通文件
 **-name "\*.java"**
 指定匹配的文件名为.java文件
 **-print0 | xargs -0**
 忽略搜索中可能出现的错误信息，并将搜索到的文件作为结果向后传递并继续执行
 **grep --color –n**
 用grep在之前搜索到的文件中进行内容搜索，输出行号并标识颜色
 **"$@"**
 表示在使用jgrep函数时输入的参数，这里即为egrep搜索的内容

### 管道符号以及xargs的使用

上例中的`|`为管道符号，作用是将前一个命令的标准输出作为后一个命令的标准输入。

<u>如果仅使用`|`，那么前面的结果会作为输入直接传递到后面的命令中，而使用`xargs`，就可以使前面的结果作为参数传递到后面的命令中，而这个特性对于find和grep而言十分重要。</u>



**例1：在当前目录中搜索所有`AndroidManifest.xml`文件并在其中搜索`DialtactsActivity`**

```swift
find . –name AndroidManifest.xml | xargs grep –n –-color “DialtactsActivity”
```

*<u>该例是xargs最基本的用法，如果将xargs去掉，那么grep搜索的内容是find输出的结果内容而非结果文件中的内容*</u>





**例2：在当前目录搜索所有的`values-zh-rCN`文件目录并在其中搜索所有的`strings.xml`文件，然后在搜索到的`strings.xml`文件中搜索“通话”字符串**



```shell
find . –type d –name “values-zh-rCN” |   
xargs –i find {} –name “strings.xml” | xargs grep –n –-color 通话
```

*该例中xargs后使用了`-i`参数，该参数的作用是可以将后面命令中的 `{}`符号视为前面find搜索的结果文件。本例中连续使用了两次`xargs`进行结果的传递*

**例3：在当前目录中的所有mk文件中搜索ro.build.type**



```shell
find . –type f –name “*.mk” –print0 | xargs -0 grep –n –color “ro.build.type”
```

*本例中和之前提到的jgrep函数都使用了`–print0 | xargs -0`进行结果传递而非单纯使用`xargs`，这样做的好处是如果find搜索会忽略可能出现的错误，使最终输出的结果更清晰，因此在使用xargs时建议按照`–print0 | xargs -0方式`书写命令(**实际上运行不通**)*







# 编写搜索函数

（暂略）

https://www.jianshu.com/p/b30a8aa4d1f1





































