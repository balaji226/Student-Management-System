@echo off
setlocal enabledelayedexpansion

echo =======================================================
echo   STUDENT MANAGEMENT SYSTEM - GITHUB UPLOADER
echo =======================================================
echo.

:: 1. Check if git is available
where git >nul 2>nul
if %errorlevel% neq 0 (
    echo [!] Git command not found in current PATH.
    if exist "C:\Program Files\Git\cmd\git.exe" (
        set "PATH=C:\Program Files\Git\cmd;!PATH!"
        echo [+] Added C:\Program Files\Git\cmd to temporary PATH.
    ) else (
        echo [ERROR] Git is not installed. Please install Git from https://git-scm.com/
        pause
        exit /b 1
    )
)

echo [+] Git detected:
git --version
echo.

:: 2. Initialize Git repo if not present
if not exist ".git" (
    echo [+] Initializing new Git repository...
    git init
) else (
    echo [*] Existing Git repository found.
)

:: 3. Configure local Git identity if not set
git config user.name >nul 2>nul
if %errorlevel% neq 0 (
    set /p GIT_USER="Enter your GitHub username or name: "
    git config user.name "!GIT_USER!"
)

git config user.email >nul 2>nul
if %errorlevel% neq 0 (
    set /p GIT_EMAIL="Enter your GitHub email address: "
    git config user.email "!GIT_EMAIL!"
)

:: 4. Stage and commit files
echo.
echo [+] Staging files (excluding venv, pycache, etc. via .gitignore)...
git add .

echo [+] Committing project files...
git commit -m "Complete Student Management System full-stack web application" 2>nul
if %errorlevel% neq 0 (
    echo [*] No new changes to commit or already up to date.
) else (
    echo [+] Commit created successfully!
)

:: 5. Set default branch to main
git branch -M main

:: 6. Prompt for GitHub repository URL
echo.
echo -------------------------------------------------------
echo   GitHub Repository Connection
echo -------------------------------------------------------
echo 1. Go to https://github.com/new in your browser
echo 2. Create a repository named "student-management-system"
echo    (DO NOT check "Add a README file" or ".gitignore")
echo 3. Copy the repository URL (e.g. https://github.com/YourUsername/student-management-system.git)
echo.
set /p REPO_URL="Paste your GitHub Repository URL here: "

if "!REPO_URL!"=="" (
    echo [!] No URL provided. Aborting remote upload.
    pause
    exit /b 1
)

:: Remove existing origin if present
git remote remove origin 2>nul
git remote add origin !REPO_URL!
echo [+] Remote 'origin' configured to: !REPO_URL!

:: 7. Push to GitHub
echo.
echo [+] Pushing code to GitHub (main branch)...
git push -u origin main

if %errorlevel% equ 0 (
    echo.
    echo =======================================================
    echo   SUCCESS! Your project is uploaded to GitHub!
    echo =======================================================
    echo View your repository online at: !REPO_URL!
) else (
    echo.
    echo [!] Push failed or authentication needed.
    echo If GitHub asked for credentials:
    echo   - Username: your GitHub username
    echo   - Password: Use a Personal Access Token (PAT) from:
    echo     https://github.com/settings/tokens (with 'repo' scope enabled)
)

echo.
pause
