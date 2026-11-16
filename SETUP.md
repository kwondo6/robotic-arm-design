# Setup on Windows (Week 1)

About an hour in total. Run every command in **PowerShell**: open Start, type "Terminal" and press Enter. After installing anything, close the terminal and open a new one so it picks up the new commands.

## 0. See what you already have

```powershell
python --version
git --version
code --version
```

Each one prints a version number if that tool is installed. If `python` opens the Microsoft Store instead, Python isn't installed (that is a Windows shortcut). Skip any step below for a tool you already have, except Python: do step 1 anyway, to get a current version through the install manager.

## 1. Python

Python on Windows now installs through the **Python Install Manager**, which installs Python versions and keeps them updated.

1. If an older Python is installed, open Settings > Apps > Installed apps and uninstall only **Python Launcher**, if it is listed. The new manager uses the same `py` command. Older Python versions can stay.
2. Open the Microsoft Store, search for **Python Install Manager** and click Get. (Or download it from [python.org/downloads](https://www.python.org/downloads/).)
3. In a new terminal, run the following. Say yes if it asks to add Python to your PATH.

```powershell
py install 3.15
py list
python --version
```

`python --version` should print `Python 3.15.x`. If it shows an older version, use `py -V:3.15` instead of `python` in step 5 to create the environment. Once the environment is active, plain `python` is the right one.

## 2. Git

```powershell
winget install --id Git.Git -e --source winget
```

Open a new terminal, then tell Git who you are:

```powershell
git --version
git config --global user.name "Daniel Kwon"
git config --global user.email "the-email-you-use-on-github@example.com"
git config --global init.defaultBranch main
```

To keep your email off public commits, use GitHub's private no-reply address instead (GitHub > Settings > Emails).

## 3. GitHub account

- Sign up at [github.com](https://github.com) with a **personal** email, so you keep the account after uni.
- Choose a professional username. It becomes part of your portfolio address (`username.github.io`) in Week 12.

## 4. VS Code and the Python extension

If `code --version` worked in step 0, VS Code is already installed. If not, run `winget install -e --id Microsoft.VisualStudioCode`. Then add Microsoft's Python extension:

```powershell
code --install-extension ms-python.python
```

## 5. Open the project and create its Python environment

```powershell
cd C:\Personal\Projects\summer-portfolio-2026\robotic-arm-design
code .
```

In VS Code, open a terminal (Ctrl + `) and run:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

- If activation fails with "running scripts is disabled on this system", run `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` once, then try again.
- When the environment is active, the prompt starts with `(.venv)`.
- Press Ctrl + Shift + P, run **Python: Select Interpreter** and pick the one in `.venv`. New VS Code terminals then activate it automatically.

The `.venv` folder holds this project's packages. It is listed in `.gitignore`, so it never goes to GitHub.

## 6. Run the starter script

```powershell
python python\arm_2link_pose.py
```

You should see:

```
Elbow at      x =   88.4 mm, z =   88.4 mm
Tool point at x =  209.1 mm, z =   56.0 mm
Shoulder to tool point: 216.5 mm
```

A plot window also opens, and the plot is saved to `media\week1_arm_pose.png`. Then work through the "Try this" exercises at the bottom of the script.

## 7. First commit and push to GitHub

```powershell
git init
git add .
git commit -m "Set up repo structure and Week 1 starter"
```

On github.com, click **+ > New repository**. Name it `robotic-arm-design`, make it **Public**, and leave "Add a README", .gitignore and licence **unticked**, because the repo already has them. Click Create, then run:

```powershell
git remote add origin https://github.com/YOUR-USERNAME/robotic-arm-design.git
git push -u origin main
```

The first push opens a browser window so you can sign in to GitHub. After that, `git push` on its own is enough.

## 8. Accounts for the CAD and MATLAB work

- [Fusion education licence](https://www.autodesk.com/education/edu-software/fusion): sign in with your university email and check the licence is active (it renews yearly).
- MATLAB and Simulink through the university licence. Check that Control System Toolbox, Simulink Control Design and Simscape Multibody are included.
- A MathWorks account on your university email, so your Onramp certificates appear in your course list (Project 2).

## Every work session

```powershell
cd C:\Personal\Projects\summer-portfolio-2026\robotic-arm-design
code .
# ...work...
git add .
git commit -m "Short description of what changed"
git push
```

At the end of each week, add one line to the README progress log.

## If something goes wrong

| Problem | Fix |
| --- | --- |
| `python` opens the Microsoft Store | Finish step 1, then open a new terminal |
| `git` or `py` is "not recognized" | Close and reopen the terminal (and VS Code) after installing |
| `pip install` tries to build numpy from source | You're on the wrong Python: check `python --version` inside the activated `.venv` |
| No plot window, but the script finishes | The PNG is still saved in `media\`; check that the right interpreter is selected in VS Code |
| Stuck for more than 2 hours | Stop, ask (MATLAB Answers, a classmate, or Claude), and move on to another task while you wait |
