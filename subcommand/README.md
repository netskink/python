Found this subcommand module and I am trying to learn how to use it.

https://github.com/anandology/subcommand/blob/master/Readme.md

Testing on mac

```
$ python3 -m venv testy
$ source testy/bin/activate
$ python3 -m pip install subcommand
```

Hmm. It appears that the code is for python2.  Skip using 
a module.  Rewrite the code and use python3 syntax.

```
$ python3 example.py --verbose checkout  --username=john --password=pw --revision=1.2 arg1 arg2
$ python3 example.py --verbose co  --username=john --password=pw --revision=1.2 arg1 arg2
```




