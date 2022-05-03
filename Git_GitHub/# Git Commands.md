# Git Commands 
You should have already completed the setup instructions for this workshop and have Git installed. Launch a command-line environment (in Windows launch “Bash” from the Start Menu, on Linux or Mac, start a new Terminal from the Terminal application). We will use this command line interface throughout these materials. We prefer this for educational reasons because the command-line is a common environment for all the operating systems.

You must provide some extra information before it is ready to interact with Git.
The information is related to the person who uses Git, and it gives the user's identity in any project which you might work on your computer. In collaborative projects, this is used to distinguish who has made what changes. You only need to perform the above commands once when you install Git on each individual computer.

```bash
 git config --global user.name "FIRST_NAME LAST_NAME"   # Use the name that you wish to be identified 
 git config --global user.email "email@example.com"  # Use your email that is linked with your GitHub 
 ```

 ## Creating a Repository 
  Now the Git is ready, and we will use it in a new project.
In Git terminology, a project is called a repository (frequently shortened to repo). 
Let's start a project withing your directories called cooking
\Users\mary\cooking 

Within cooking we create (with mkdir) other directories, recipes, tools, videos. We go to the directory recipes and we create pizza.md and cake.md files. There we write and instructions
```bash 
pwd 
```
Output
```bash 
 \Users\mary\
 ```
 ```bash
mkdir cooking 
cd cooking
```
```bash 
pwd 
```
Output
```bash 
 \Users\mary\cooking
 ```
 ```bash
mkdir recipes tools videos
ls
```
Output
```bash
recipies	tools		videos
```
Create pizza.md and cake.md

```bash
touch pizza.md cake.md
ls
```
To start using Git with our recipes we need to create a repository for it. Make sure the current working directory for your terminal is recipies and run:

```bash
git init
```
Output

```bash
Initialized empty Git repository in /Users/mary/cooking/recipes/.git/
``` 

