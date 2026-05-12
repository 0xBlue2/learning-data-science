# Convenient Commands

## Renaming Files
```powershell
ls | Rename-Item -NewName {$_.Name -replace 'worda', 'wordb'}
```
[https://vexx32.github.io/2019/03/20/PowerShell-Replace-Operator/](https://vexx32.github.io/2019/03/20/PowerShell-Replace-Operator/)