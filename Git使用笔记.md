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

11. 从版本库中删除文件

    `git rm filename`

12. 用版本库的版本替换工作区的版本

    `git checkout`

13. 创建远程库

    在GitHub网站上直接创建

14. 关联远程库

    `git remote add origin git@github.com:githubname/name.git`

    网站上解释：

    添加后，远程库的名字就是`origin`，这是Git默认的叫法，也可以改成别的，但是`origin`这个名字一看就知道是远程库。

15. 把本地库内容推到远程

    `git push -u origin master`

    网站上解释：

    由于远程库是空的，我们第一次推送`master`分支时，加上了`-u`参数，Git不但会把本地的`master`分支内容推送的远程新的`master`分支，还会把本地的`master`分支和远程的`master`分支关联起来，在以后的推送或者拉取时就可以简化命令。

    在此之后，本地提交可以用如下命令。
    `git push origin master`

16. clone的命令（下载到终端，并建立独立的文件夹）

     `git clone git@github.com:githubname/name.git`

17. 

# 分支管理
1. 创建并切换到`dev`分支

    方法1：

    `$ git checkout -b dev`

    方法2：

    `$ git branch dev`
`$ git checkout dev`
    

    方法3：
  
    `$ git switch -c dev`


2. 查看分支

    `$ git branch`

    会列举所有分支，当前的分支前会有\*


  3. 切换分支

     方法1：

     如果想在某个分支工作，像上面那样用`git checkout`切换就行

     方法2：

     `$ git switch master`


  4. 合并分支

     例如，把`dev`分支的工作成果合并到`master`分支上：

     `$ git merge dev`

  5. 删除分支

     `git branch -d dev`

  6. 

# 解决冲突

1. 显示冲突的文件

   `git status`

2. 查看分支合并情况

   `git log --graph --pretty=oneline --abbrev-commit`

3. 

# 分支管理策略

如果禁用`Fast forward`模式，Git就会在merge时生成一个新的commit，使用的参数是`--no-ff`。

![image-20201004204424478](E:%5CMDNotes%5CGit%E4%BD%BF%E7%94%A8%E7%AC%94%E8%AE%B0.assets%5Cimage-20201004204424478.png)  

这样不用删dev，某种意义上说可以保存`dev`分支的信息



<u>平时不应该在`master`上干活，都在`dev`上干活。团队协作的时候大家都向`dev`提交</u>

























