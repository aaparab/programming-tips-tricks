## Random topics which don't belong to any particular category
---

- `bashrc` for `Git for Windows`
Using Git for Windows, I realized the `~/.bashrc` file is not being run when bash starts. 
I observe that during initialization, bash runs the `.bash_profile` file but not the `.bashrc` file. 
To correct this, I added 
```
if [ -f ~/.bashrc ]; then . ~/.bashrc; fi
```
to the `~/.bash_profile` and then the stuff I wanted to be initialized in the usual `~/.bashrc` file. 
