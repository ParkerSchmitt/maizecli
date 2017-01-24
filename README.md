# maizecli
CLI for Maize


# Installation

## Windows

1) Download and install python

* [32 bit](https://www.python.org/ftp/python/2.7.12/python-2.7.12.amd64.msi)
* [64 bit](https://www.python.org/ftp/python/2.7.12/python-2.7.12.msi)

2) Download the .zip of maizecli

[Download link here](https://github.com/ParkerSchmitt/maizecli/archive/master.zip)

3) Extract the .zip
  
  Go to the download location, right click on the master.zip,  and press extract
  
4) Open the folder

5) Double click on maize.py, or press shift+right click, press "open command-window here", and type in "python maize.py"

## Linux

1) Download and install python

> sudo apt-get update

> sudo-apt-get install python

2) Download .zip or clone the repo

[Download link here](https://github.com/ParkerSchmitt/maizecli/archive/master.zip)

3) Extract the .zip

4) Open the folder

5) Open the terminal, and type in "python maize.py"


# Usage

## Setup

When you first open the program, it will ask you for your username. Enter it (ex 190000193) and press enter. Then it will ask you for your password. Type in your normal login password for blackboard (it won't display on the screen for your privacy), and press enter

## Commands

### check

parameters:

* (--grades) | shows grades for all of your classes.
* (--submitted) | shows what you have not submitted so far. option argument (weeks) will check what you have due, x-number days ahead. example usage:

> python maize.py check --submitted --weeks =1
will check your blackboard account for work submitted, that is due within 1 day.

