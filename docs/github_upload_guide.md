# GitHub Upload Guide (GitHub-il Upload Seiyum Murai)

This step-by-step guide explains how to upload the **Student Management System** to your GitHub account.

---

## Method 1: Using the 1-Click Automated Script (Most Recommended)

We have created an automated script [`upload_to_github.bat`](../upload_to_github.bat) inside the project folder.

### Steps:
1. Open your browser and create a new repository on GitHub:
   - Go to: **[https://github.com/new](https://github.com/new)**
   - **Repository Name**: `student-management-system`
   - **Public / Private**: Choose Public (for college submission)
   - **Important**: **DO NOT** check *"Add a README file"*, *"Add .gitignore"*, or *"Choose a license"*. Leave them unchecked because the project already contains them!
   - Click **Create repository**.
   - Copy the repository URL (e.g., `https://github.com/YourUsername/student-management-system.git`).
2. Open the project folder in File Explorer:
   ```
   C:\Users\BALAJI\.gemini\antigravity-ide\scratch\student_management_system
   ```
3. Double-click on **`upload_to_github.bat`**.
4. When prompted, paste your GitHub repository URL and press **Enter**.
5. It will automatically stage all files, commit them with a clean message, configure the `main` branch, and push everything to GitHub!

---

## Method 2: Manual Terminal Commands (PowerShell / Command Prompt)

If you prefer to run commands manually in your terminal, follow these steps:

### Step 1: Open PowerShell in the project directory
```powershell
cd C:\Users\BALAJI\.gemini\antigravity-ide\scratch\student_management_system
```

### Step 2: Initialize Git
```powershell
git init
```

### Step 3: Configure Git User Info (if running for the first time)
```powershell
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
```

### Step 4: Stage All Files
```powershell
git add .
```
*(The `.gitignore` automatically prevents `venv/`, `__pycache__/`, and temporary files from being staged).*

### Step 5: Commit Your Code
```powershell
git commit -m "Complete Student Management System full-stack web application"
```

### Step 6: Rename the Default Branch to `main`
```powershell
git branch -M main
```

### Step 7: Link Your GitHub Repository
Replace `<YOUR_GITHUB_URL>` with your actual repository URL from GitHub:
```powershell
git remote add origin <YOUR_GITHUB_URL>
```
*Example:*
```powershell
git remote add origin https://github.com/balaji/student-management-system.git
```

### Step 8: Push Code to GitHub
```powershell
git push -u origin main
```

---

## Tamil Guide / தமிழில் எளிய விளக்கம்:

1. **GitHub-ல் New Repository உருவாக்குங்கள்**:
   - [https://github.com/new](https://github.com/new) லிங்கிற்கு செல்லவும்.
   - Repository name: `student-management-system` என்று கொடுக்கவும்.
   - README மற்றும் .gitignore ஆப்ஷன்களை tick செய்ய வேண்டாம் (Already project-ல் உள்ளது).
   - "Create repository" பட்டனை கிளிக் செய்யவும்.
   - வரக்கூடிய GitHub URL-ஐ copy செய்து கொள்ளவும் (எ.கா: `https://github.com/username/student-management-system.git`).

2. **Upload செய்ய 2 வழிகள்**:
   - **எளிய வழி (1-Click)**: ப்ராஜெக்ட் ஃபோல்டரில் உள்ள **`upload_to_github.bat`** ஃபைலை double-click செய்து திறக்கவும். அங்கே உங்கள் GitHub URL-ஐ paste செய்து Enter கொடுத்தால் தானாகவே upload ஆகிவிடும்!
   - **Terminal வழி**: PowerShell-ல் மேலே கொடுக்கப்பட்டுள்ள command-களை ஒவ்வொன்றாக ரன் செய்யவும்.

3. **GitHub Password / Authentication கேட்டால்**:
   - GitHub-ல் வழக்கமான Password ஏற்கப்படாது.
   - **Personal Access Token (PAT)** பயன்படுத்த வேண்டும்:
     - GitHub Settings &rarr; Developer Settings &rarr; Personal Access Tokens &rarr; Tokens (classic).
     - "Generate new token" கிளிக் செய்து, `repo` பாக்ஸை tick செய்து token-ஐ copy செய்து Password இடத்தில் paste செய்யவும்.
