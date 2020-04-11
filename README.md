<p align="center">
  <img alt="habbo" src="https://conteudo.imguol.com.br/blogs/311/files/2019/10/habbo_abre-615x300.jpg" width="250px" float="center"/>
</p>

<h1 align="center">🏨 Habbo Hotel CLI - Automate Auto Click 🏨</h1>

<p align="center">
  <strong>Python CLI to create an auto-click for Habbo Hotel</strong>
</p>

<p align="center">
  <a href="https://github.com/lpmatos/habbo-auto-click">
    <img alt="Open Source" src="https://badges.frapsoft.com/os/v1/open-source.svg?v=102">
  </a>

  <a href="https://github.com/lpmatos/habbo-auto-click/graphs/contributors">
    <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/lpmatos/habbo-auto-click">
  </a>

  <a href="https://github.com/lpmatos/habbo-auto-click">
    <img alt="GitHub Language Count" src="https://img.shields.io/github/languages/count/lpmatos/habbo-auto-click">
  </a>

  <a href="https://github.com/lpmatos/habbo-auto-click">
    <img alt="GitHub Top Language" src="https://img.shields.io/github/languages/top/lpmatos/habbo-auto-click">
  </a>

  <a href="https://github.com/lpmatos/habbo-auto-click/stargazers">
    <img alt="GitHub Stars" src="https://img.shields.io/github/stars/lpmatos/habbo-auto-click?style=social">
  </a>

  <a href="https://github.com/lpmatos/habbo-auto-click/commits/master">
    <img alt="GitHub Last Commit" src="https://img.shields.io/github/last-commit/lpmatos/habbo-auto-click">
  </a>

  <a href="https://github.com/lpmatos/habbo-auto-click">
    <img alt="Repository Size" src="https://img.shields.io/github/repo-size/lpmatos/habbo-auto-click">
  </a>

  <a href="https://github.com/lpmatos/habbo-auto-click/issues">
    <img alt="Repository Issues" src="https://img.shields.io/github/issues/lpmatos/habbo-auto-click">
  </a>

  <a href="https://github.com/lpmatos/habbo-auto-click/blob/master/LICENSE">
    <img alt="MIT License" src="https://img.shields.io/github/license/lpmatos/habbo-auto-click">
  </a>
</p>

<p align="center">
  <a href="#-how-to-contribute">How to contribute</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-license">License</a>
</p>

## ▶️ Getting Started

To use this repository you need to make a **git clone**:

```bash
git clone --depth 1 https://github.com/lpmatos/habbo-auto-click.git -b master
```

Pull requests are welcome. If you'd like to support the work and buy me a ☕, I greatly appreciate it!

<a href="https://www.buymeacoffee.com/EatdMck" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 100px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

## Description

This is a simple Python script that perform a auto-click in your screen. Basically we perform this task in an infinite loop, until there is some intervention.

![Alt text](docs/images/CODE.PNG?raw=true "Code")

When the application is started you receive a toast notifying.

![Alt text](docs/images/TOAST.PNG?raw=true "Toast")

## Running pip

The **pip** is a command line program. When you install **pip**, a **pip** command is added to your system, which can be run from the command prompt as follows:

```bash
$ pip <pip arguments>
```

If you cannot run the pip command directly (possibly because the location where it was installed isn't on your operating systems **PATH**) then you can run **pip** via the **Python** interpreter:

```bash
$ python -m pip <pip arguments>
```

On **Windows**, the py launcher can be used:

```bash
$ py -m pip <pip arguments>
```

## Installing Packages

### Pip

The **pip** supports installing from **PyPI**, version control, local projects, and directly from distribution files.

The most common scenario is to install from **PyPI** using Requirement specifiers.

```bash
$ pip install SomePackage            # latest version
$ pip install SomePackage==1.0.4     # specific version
$ pip install somePackage>=1.0.4     # minimum version
```

### Pipenv

**Pipenv** is a tool that aims to bring the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.) to the **Python** world. **Windows** is a firsts-class citizen, in our world.

It automatically creates and manages a **virtualenv** for your projects, as well as adds/removes packages from your **Pipfile** as you install/uninstall packages. It also generates the ever-important **Pipfile.lock**, which is used to produce deterministic builds.

#### Installation

```bash
$ pip install pipenv
```

#### Create a TOML Spec Pipfile

You can build the **Pipfile** to specifying:

* Versions of a Package.
* Versions of **Python**.
* Basic configurations.

#### Pipenv Workflow

Clone/create project repository:

```bash
$ cd myproject
```

Install from **Pipfile**, if there is one:

```bash
$ pipenv install
```

Install from **Pipfile** dev:

```bash
$ pipenv install --dev
```

## Requirement File

**Requirement File** are files containing a list of items to be installed using **pip** install like so:

```bash
$ pip install -r requirements.txt
```

Logically, a **Requirement File** is just a list of **pip** install arguments placed in a file. Note that you should not rely on the items in the file being installed by **pip** in any particular order.

## Environment variables

**Name**  |  **Description**
:---:  |  :---:
**LOG_PATH**  |  Just the Log Path
**LOG_FILE**  |  Just the Log File
**LOG_LEVEL**  |  Just the Log Level
**LOGGER**  |  Just the Logger name
**DELAY**  |  Auto Click Delay

## Usage

<kbd>python ./main.py --help</kbd> - Helper

## Params

![Alt text](docs/images/USAGE.PNG?raw=true "Usage")

## Link Reference

* https://pyautogui.readthedocs.io/en/latest/
* https://github.com/jithurjacob/Windows-10-Toast-Notifications

## 🎒 How to contribute

1. Make a **Fork**.

2. Follow the project organization.

3. Add the file to the appropriate level folder - If the folder does not exist, create according to the standard.

4. Make the **Commit**.

5. Open a **Pull Request**.

6. Wait for your pull request to be accepted.. 🚀

Remember: There is no bad code, there are different views/versions of solving the same problem. 😊

## 🔔 Add to git and push

You must send the project to your GitHub after the modifications

```bash
git add -f .
git commit -m "Added - Fixing somethings"
git push origin master
```

## 📋 Versioning

- [CHANGELOG](CHANGELOG.md)

## 📜 License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.

## ☎️ Contacts

Hey!! If you like this project or if you find some bugs feel free to contact me in my channels:

* **Email**: luccapsm@gmail.com
* **Linkedin**: www.linkedin.com/in/lucca-pessoa-4abb71138/

[![Facebook](https://github.frapsoft.com/social/facebook.png)](https://www.facebook.com/lucca.pessoa.9)
[![Github](https://github.frapsoft.com/social/github.png)](https://github.com/lpmatos)

## ✨ Contributors

<table>
  <tr>
    <td align="center"><a href="https://github.com/lpmatos"><img src="https://avatars2.githubusercontent.com/u/58797390?s=400&v=4" width="100px;" alt=""/><br /><sub><b>Lucca Pessoa</b></sub></a><br /><a href="https://github.com/lpmatos/habbo-auto-click/commits?author=lpmatos" title="Code">💻</a></a></td>
  <tr>
</table>

## 🐯 Autor

<table>
  <tr>
    <td align="center"><a href="https://github.com/lpmatos"><img src="https://avatars2.githubusercontent.com/u/58797390?s=400&v=4" width="100px;" alt=""/><br /><sub><b>Lucca Pessoa</b></sub></a><br /><a href="https://github.com/lpmatos/habbo-auto-click/commits?author=lpmatos" title="Code">💻</a> <a href="#lpmatos" title="Design">🎨</a></td>
  <tr>
</table>

## Project Status

* 🔛 In production

---

<p align="center">Feito com ❤️ by <strong>Lucca Pessoa :wave:</p>
