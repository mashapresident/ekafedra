# PowerShell script to push project to GitHub

Write-Host "Initializing git repository..." -ForegroundColor Green
git init

Write-Host "`nAdding remote repository..." -ForegroundColor Green
git remote add origin https://github.com/mashapresident/ekafedra.git

Write-Host "`nAdding all files..." -ForegroundColor Green
git add .

Write-Host "`nCreating initial commit..." -ForegroundColor Green
git commit -m "Initial commit: eDepartment (єКафедра) - web guide for university applicants"

Write-Host "`nPushing to GitHub..." -ForegroundColor Green
git branch -M main
git push -u origin main

Write-Host "`nDone! Check your repository at https://github.com/mashapresident/ekafedra" -ForegroundColor Green
Read-Host "Press Enter to exit"

