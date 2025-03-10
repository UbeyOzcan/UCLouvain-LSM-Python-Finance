# How to setup a Python Project using `uv`

This a very simply guide that will help you to create a Python Project from scratch. This guide can be reuse everytime you start a project.

---

## 1. Understanding Dependencies
A dependency is an external package or module required for a Python project to function correctly. Dependency management ensures that the correct versions of these packages are installed and maintained.

---

## 2. Installing `uv` (to do one time only in your laptop)
`uv` is a fast, Rust-based package manager for Python that works as a replacement for `pip` and `virtualenv`.

### Installation for macOS
```sh
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### Installation for Windows (PowerShell)
```powershell
irm https://astral.sh/uv/install.ps1 | iex
```

After installation, verify the installation with:
```sh
uv --version
```

---

## 3. Virtual Environments with `uv` (to do at every project)
`uv` provides an efficient way to manage virtual environments without relying on `venv`.

### Creating a Virtual Environment
```sh
uv venv .venv
```
This creates an isolated environment inside the `.venv` folder.

### Activating the Virtual Environment
- **macOS/Linux:**
  ```sh
  source my_env/bin/activate
  ```
- **Windows:**
  ```powershell
  my_env\Scripts\activate
  ```

### Deactivating the Virtual Environment
```sh
deactivate
```

---

## 4. Managing Dependencies with `uv`

### Installing Packages
```sh
uv pip install numpy pandas matplotlib
```

### Checking Installed Packages
```sh
uv pip list
```

### Freezing Dependencies
To save installed packages to a file:
```sh
uv pip freeze > requirements.txt
```
This creates a `requirements.txt` file listing all dependencies.

### Installing Dependencies from a File
```sh
uv pip install -r requirements.txt
```

---

## 5. Dependency Management with `uv sync`
`uv sync` offers an alternative to `pip` for managing dependencies efficiently.

### Creating a `requirements.txt` file
Manually create a `requirements.txt` file containing package names and versions:
```
numpy==1.21.2
pandas==1.3.3
matplotlib==3.4.3
```

### Installing Dependencies
```sh
uv sync
```
This command reads from `requirements.txt` and installs the correct versions.

### Updating Dependencies
To upgrade all dependencies:
```sh
uv pip install --upgrade -r requirements.txt
```

---

## 6. Best Practices for Dependency Management with `uv`
- Always use a virtual environment to isolate dependencies.
- Keep a `requirements.txt` file to ensure consistency.
- Use version pinning (`numpy==1.21.2`) to prevent unexpected updates.
- Regularly update dependencies (`uv pip install --upgrade -r requirements.txt`).
- Use `uv sync` for efficient dependency installation.

---

By following these principles and using `uv`, you can efficiently manage dependencies and avoid conflicts in Python projects.
