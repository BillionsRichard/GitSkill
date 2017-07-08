#-*-coding:utf-8-*-
print 'hello'

#edited on github

#edited on working tree
#
edited on github again
#this is modified in working tree.
＃测试远端仓库有更新，本地也更新了同一个文件时，如果本地的更新添加到缓存区，ｇit pull的行为如何？
#本地文件添加到缓存区（git add）还不够，pull时依然会报冲突，必须git stash或者git commit(edited on working tree)。
#测试本地修改如果缓存了，git pull会获取远端最新代码到本地工作区
