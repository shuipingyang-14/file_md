# 1 git init命令
把本地创建目录变成git可管理的仓库

# 2 git add命令
```buildoutcfg
git add readme.txt
```
把readme.txt添加到暂存区

# 3 git commit命令
```buildoutcfg
git commit -m "注释"
```
把文件提交到仓库

# 4 git status
查看文件状态

# 5 git diff命令
查看文件修改内容

# 6 git log命令
查看历史记录
```buildoutcfg
git log –pretty=oneline 
```
日志内容显示为一行

# 7 git reset命令
```buildoutcfg
git reset --hard HEAD^
```
把当前版本回退到上一版本

```buildoutcfg
git reset --hard HEAD^^
```
把当前版本回退到上上一版本

```buildoutcfg
git reset --hard HEAD~100
```
把当前版本回退到前一百个版本

```buildoutcfg
git reset --hard 版本号
```
把当前版本回退到指定版本

# 8 git reflog命令
查看版本号

# 9 git checkout命令
```buildoutcfg
git checkout -- 文件名称
```
撤销本次修改的文件

```buildoutcfg
git checkout 分支名称
```
切换分支

```buildoutcfg
git checkout -b 分支名称
```
创建并且切换分支

# 10 git stash命令
新增文件，执行stash不会被存储

```buildoutcfg
git stash "save message"
```
存储时，添加备注

```buildoutcfg
git stasg list
```
查看stash了哪些存储

```buildoutcfg
git stasg show
```
显示做了什么改动，默认show显示第一个存储，如果要显示其他存储，后面加上stash@{num},比如第二个git stash show stash@{1}

```buildoutcfg
git stasg show -p
```
显示第一个存储的改动，如果想显示其他存储，命令：git stash show stash @{num} -p，比如第二个：git stash show stash@{1} -p

```buildoutcfg
git stasg apply
```
应用某个存储,但不会把存储从存储列表中删除，默认使用第一个存储,即stash@{0}，如果要使用其他个，git stash apply stash@{$num} ， 比如第二个：git stash apply stash@{1} 

```buildoutcfg
git stasg pop
``` 
恢复之前缓存的工作目录，将缓存堆栈中的对应stash删除，并将对应修改应用到当前的工作目录下,默认为第一个stash,即stash@{0}，如果要应用并删除其他stash，命令：git stash pop stash@{$num} ，比如应用并删除第二个：git stash pop stash@{1}

```buildoutcfg
git stash drop stash@{$num}
```
丢弃stash@{$num}存储，从列表中删除这个存储

```buildoutcfg
git stash clear
```
删除所有缓存的stash