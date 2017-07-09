#-*-coding:utf-8-*-
print 'hello'

#edited on github

#edited on working tree
#
edited on github again
#this is modified in working tree.
＃测试远端仓库有更新，本地也更新了同一个文件时，如果本地的更新添加到缓存区，ｇit pull的行为如何？
#本地文件添加到缓存区（git add）还不够，pull时依然会报冲突，必须git stash或者git commit(edited on working tree)。
#测试本地修改如果提交或者stash了，git pull才会获取远端最新代码到本地工作区，否则会提示冲突。（modified on github）
#通过TortoiseGit-->add to ignore list--->recurse可以将文件夹及其内容添加到忽略列表中.
