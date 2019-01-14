# One strategy of collaborating on a shared git repo

*Douglas Strodtman - SaMo*

## Most Important

You'll need to have a current version of the repo cloned on your computer before you start working. I'm all about not having a million forks to have to track, and instead using branches.

What this means is that each time you want to start editing, you should:

```
git checkout master
git pull
```

Then you should checkout a **new** branch (call it your first name):

```
git checkout -b douglas
```

By always pulling before creating a **new** branch before you start editing, we should be able to avoid merge conflicts.

Do your edits, whatever they are, and then **only add the files you changed**. 

```
git add ./changed_lesson_repo
git commit -m 'groomed and pushed a lesson for week X on some thing'
```

If you just type

```
git push
```

you'll get a message that tells you:

```
fatal: The current branch douglas has no upstream branch.
To push the current branch and set the remote as upstream, use

    git push --set-upstream origin douglas
```

Thanks for the useful message, git! Let's do that:

```
git push --set-upstream origin douglas
```

This creates a new branch that should be able to merge with the master branch. This is where I come back to this repo and confirm my merge.

Here's the overview of this process:

1. Find your branch.
2. Check that there are no merge conflicts.
3. Create a pull request.
4. Merge this pull request.
5. DELETE YOUR BRANCH.

By deleting your branch each time you merge, you'll avoid ever getting ahead or behind the master branch. After you've merge and deleted your branch, on your local machine:

```
git checkout master
git pull
git branch -d douglas
```

This will put you back on the master branch, pull the most recent version of the repo, and then delete your local version of the branch. Deleting your local branch ensures that when you use

```
git checkout -b douglas
```

before you start editing again, your local branch will be up-to-date with the master branch.