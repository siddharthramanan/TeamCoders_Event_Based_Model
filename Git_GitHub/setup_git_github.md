
# Work with Git

- This document introduces some basic usage of [Git](https://git-scm.com/), a distributed versioning system for tracking and managing source code changes during software development.

- [IDEAS](https://github.com/HealthBioscienceIDEAS/TeamCoders_Event_Based_Model) and [GitHub](https://github.com/) are two project hosting services. The [TeamCoders_Event_Based_Model repository](https://github.com/HealthBioscienceIDEAS/TeamCoders_Event_Based_Model) is hosted on the former, while you will submit your work to your GitHub Team repository.
- For more information and tutorial, have a look at the book/documentation [*Pro Git*](https://git-scm.com/book/en/v2)

- [IDEAS](http:///) and [GitHub](https://github.com/) are two project hosting services. The [TeamCoders_Event_Based_Model repository](https://github.com/HealthBioscienceIDEAS/TeamCoders_Event_Based_Model) is hosted on the former, while you will submit your coursework to the latter.
- For more information and tutorial, have a look at the book/documentation [*Pro Git*](https://git-scm.com/book/en/v2)

## Clone the module repository on IDEAS lab

Make a local copy of the entire repository hosted on the remote WEISSLab, e.g. remote repository -> local repository.

``` bash
git clone https://
```

Change the current directory to the repository folder, then update to the latest code.

``` bash
cd #event base model
git pull
```

## Complete the challenge work  on GitHub

### Set up a GitHub account

If you do not have one, sign up for a GitHub account at [github.com](https://github.com/).

### Create a repository

[Create a repo](https://docs.github.com/en/free-pro-team@latest/articles/create-a-repo) with name `teamcoders-challenge`

### Record you progress

Git supports complex workflows for large professional software development projects. A (over-)simplified single-user project may only need a few steps/commands.

- Make changes to your code on your local repository.
- Add the changes (or new files) to Git, so they become tracked.
- Commit these changes with a commit message.
- Push the commits to the remote repository.

```bash
git add file_you_with_to _change_from_your_local_directory
git commit -m "a brief message summarise the committed changes"
git push origin main
```

For those wish team-coding, the workflow is likely to be more complex and [branching and merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging) will become handy.
