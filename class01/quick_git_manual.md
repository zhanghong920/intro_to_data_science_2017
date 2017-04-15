# Why is version control useful?
* **Backup** 
* **Collaborate** 

# Git basics
### Get an existing repo
`git clone <url goes here>`
### Create a new repo
`git init <project name goes here>`

## When you’re ready to push code

### 1. See what’s changed since the last commit
`git status` shows files that have changed or are untracked
`git diff [optional: filename]` shows the changes themselves

### 2. “Stage” the things you want to include in your commit
This includes both files that have changed and new files you want to add.

`git add <file or directory>`

### 3. Commit your changes and add a useful message

`git commit -m ‘message goes here’`

### 4. (optional) Pull from the origin repo

`git pull`

If any other changes were made since you last pulled, this will attempt to merge them with yours. If you don’t do this and you need to, the remote repo will tell you.

### 5. Push to the origin repo

`git push`

## Additional useful commands
### `git log`
See the history of commits present in your copy of the repo.
### `git checkout <revision #, or branch name> <optional filename>`
If you give a revision number, this changes your files to how they were when that commit was the latest. Think of this like a time machine for going to old commits, without changing/losing anything in the present repo.

**WARNING:** if you specify a file, using `git checkout` without committing your latest changes will wipe them out.

If you give a branch name, `git checkout` will switch you to the most recent commit in that named branch and make that branch the active one (so new commits will be added to that branch)
### `git rm`
Remove a file from the repo
### `git mv`
Rename/move a file in the repo
### `git stash`
Save your changes to a “stash”, but don’t commit them. Useful if you might want to come back to things later, but want to wipe your changes clean right now.

# Do the following
1. Navigate to the folder you want to put this repo through command line.
2. Clone the repo
```
git clone https://github.com/Tian-Su/intro_to_data_science_2017.git
```
3. Check your current branch
```
git branch
```
4. make a branch




## Git Cheatsheet
[PDF](https://training.github.com/kit/downloads/github-git-cheat-sheet.pdf)
