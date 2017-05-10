# Git forking
## 1st Forking exercise 
1. Product owner fork the repo from Tian's repo. This will be your team repo.
2. Create a new branch called 'fork_exercise'.
```
a quick example:
# the first time pushing a new local branch
Git branch test_branching
Git checkout test_branching (now you are in test_branching branch)
touch test.txt
Git add test.txt
Git commit -m “test.”
Git push origin test_branching (alternatively you can also push it to a different branch: git push origin develop, not recommend. Better do pull requests between branches)

# from the 2nd time
# create a file add to git
Git push (no need to specify branch if you want to push to the same branch)
```
2. Each team member fork the repo from your product owner.
3. Each team member add an empty file called 'test_forking.txt'.
4. Each team member pull request to fork_exercise branch.
5. Product owner merge the docs into the team repo fork_exercise branch.

## 2nd Forking exercise
1. Everybody finished the pandas exercise 
2. Pull request to your team repo branch 'fun_with_pandas'. 
2. Check each other's scripts. You may need to sync your fork with the team fork to do this.

## Some helpful information
### Git Fork
Click on Fork on the upper right corner of the repo. This will fork the repo to your account.

### Setup the upstream and sync
Please follow the instruction [here](https://help.github.com/articles/syncing-a-fork/).
### Create a pull request from web page
[Here](https://help.github.com/articles/creating-a-pull-request/) is the documentation from github.

