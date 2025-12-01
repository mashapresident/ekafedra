@echo off
echo Initializing git repository...
git init

echo.
echo Adding remote repository...
git remote add origin https://github.com/mashapresident/ekafedra.git

echo.
echo Adding all files...
git add .

echo.
echo Creating initial commit...
git commit -m "Initial commit: eDepartment (єКафедра) - web guide for university applicants"

echo.
echo Pushing to GitHub...
git branch -M main
git push -u origin main

echo.
echo Done! Check your repository at https://github.com/mashapresident/ekafedra
pause

