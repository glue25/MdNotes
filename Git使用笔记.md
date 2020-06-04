# Git使用笔记

## 个人理解

我认为目前git可以给我带来的好处有

1. 自己写代码时进行版本控制
2. 多终端灵活共享代码
3. 更灵活使用网络代码
4. 日后与人共同开发

前三者为目前需求，所以目前掌握便捷的基本操作就好。

## 命令行使用Git

本部分以Git命令行内容为主，有部分基础的GitHub网站操作。

1. 创建版本库

   进入目标文件夹后

   `git init`

2. 添加到暂存区

   `git add filename`

3. 提交到版本库

   `git commit -m "注释与说明"`

   将暂存区的修改放进版本库

4. 查看提交的日志

   `git log`

   可查看由近到远的提交日志

   `git log --pretty=oneline`

   后面附加的这个参数可以使输出看起来比较简洁

   <u>*值得注意的是输出的每项的数字是SHA1算出的版本号（commit id）*</u>

5. 版本回退

   下面是几种常用的指令

   `git reset --hard HEAD^ #回到上一个版本`
   `git reset --hard HEAD^^ #回到上两个版本`
   `git reset --hard HEAD~10 #回到上10个版本`
   `git reset --hard HEAD~版本号的前几位 #回到指定版本`
   
6. 查看命令历史

   `git reflog`

   可以用来查看命令历史，查看曾经的版本号（哪怕常规方法已经找不到了）

7. 查看状态

   `git status`

8. 比较工作区和版本库的最新版本（HEAD指向？先这么理解）的区别

   `git diff HEAD -- filename`

9. 撤销工作区修改

   `git checkout -- filename`

   丢弃工作区修改，恢复到暂存区或版本库的状态（总之是比较新的状态）。

10. 撤销暂存区修改

    `git reset HEAD filename`

    这个语句可以把暂存区的内容修改回退到工作区。如果想继续清理到最新版本库，可以再次使用9.

11.  





















