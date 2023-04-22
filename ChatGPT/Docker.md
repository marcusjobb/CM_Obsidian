# ChatGPT through Docker

## Activate HyperV
### Windows 11 Pro
Activate Hyper-V from Features

or

```
Get-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V
```
### Windows 11 Home
Source: https://www.ubackup.com/enterprise-backup/windows-11-hyper-v-not-showing.html

Create file install HyperV.cmd
```
pushd "%~dp0"

dir /b %SystemRoot%\servicing\Packages\*Hyper-V*.mum >hyper-v.txt

for /f %%i in ('findstr /i . hyper-v.txt 2^>nul') do dism /online /norestart /add-package:"%SystemRoot%\servicing\Packages\%%i"

del hyper-v.txt

Dism /online /enable-feature /featurename:Microsoft-Hyper-V -All /LimitAccess /ALL

pause
```
Run the file and reboot

Open this 
```
https://apps.microsoft.com/store/detail/ubuntu-on-windows/9NBLGGH4MSV6?hl=sv-se&gl=se&rtc=1
```
install it

open Admin Console
```
wsl --update
wsl -l -v 
```

### VsCode Addin
https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl
Just for the fun

## Install Docker
https://download.docker.com/win/edge/Docker%20Desktop%20Installer.exe

### Download image
From terminal
```
docker pull deepaiorg/gpt2
docker run --rm -it -e MODE=http -p 5000:5000 deepaiorg/gpt2
```

