git add .
$commitMessage = Read-Host -Prompt "Enter your commit message"
git commit -m "$commitMessage"
git push -u origin main