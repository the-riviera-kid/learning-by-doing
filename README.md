# Learning By Doing

This is the main repository for our Learning By Doing sessions (a.k.a. The Dojo Of Doom). You'll be working in your own forks, and pulling updates from this repository.

## How to start

1. Get thee to thy terminal! 
2. `cd` to a nice directory, "documents", "projects", something like that.
3. Type the following:
```bash
git clone https://github.com/the-riviera-kid/dojo-of-panic.git
```
  * This will create a new folder, containing everything in this repository.

## How to build a Virtual Environment

This is a one-time setup.

1. In the terminal, ensure you are at the top level of this repository.
2. Run the following:
```bash
virtualenv -p python3 venv
```

## How to activate your Virtual Environment

This must be done __every time__ you want to run your programs.

1. In the terminal, ensure you are at the top level of this repository.
2. Run the following:
```bash
. venv/bin/activate
```
  * Your terminal prompt should now start with `venv`, to show you it is active.
