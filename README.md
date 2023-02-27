# Undercover
🔎 Python CLI adapted from the [undercover](https://play.google.com/store/apps/details?id=com.yanstarstudio.joss.undercover&gl=US) game

```
├── app
│   ├── config.json
│   ├── data
│   │   ├── default.json
│   │   ├── games.json
│   │   ├── rules.json
│   │   └── words.json
│   ├── lang
│   │   ├── en.json
│   │   └── fr.json
│   ├── main.py
│   └── src
│       ├── components
│       │   ├── Menu.py
│       └── core
│           ├── Game.py
│           ├── Inspector.py
│           ├── Interactor.py
│           ├── Meta.py
│           ├── Service.py
│           └── Utils.py
├── Makefile
├── README.md
├── requirements.txt
├── scripts
│   ├── _constants.py
│   ├── _core.py
│   ├── make.py
│   ├── build.py
├── tests
│   ├── _menu.py
│   └── test_auto.py
└── venv
```

## Dependencies
- [python 3.10](https://docs.python.org/3.10/)

### Windows
Download and install it from [python.org](https://www.python.org/downloads/macos/) or run on terminal
```powershell
$ winget install -e --id Python.Python -v 3.10
```

### MacOS
Download and install it from [python.org](https://www.python.org/downloads/macos/) or run on terminal
```bash
$ brew install python
```

### Debian / Ubuntu
```bash
$ sudo apt update && sudo apt upgrade && sudo apt install python3.10
```

### ArchLinux / Manjaro
```bash
$ sudo pacman -Sy python
```

## Installation
### Windows
- Create virtual environment from this directory
```powershell
$ python -m venv venv
```

- Install python requirements from this directory
```powershell
$ pip install -r requirements.txt
```

- Generate development data
```powershell
$ python scripts/make.py
```

- Compile requirements
```powershell
$ pip freeze > requirements.txt
```

- Build your version
```powershell
$ python scripts/build.py -l [lang]
```

### Linux & MacOS
- Prepare environment
```bash
$ make init
```

- Compile environment
```bash
$ make env
```

- Build version
```bash
$ make build
```
