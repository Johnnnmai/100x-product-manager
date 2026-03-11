@echo off
setlocal
set "REPO_ROOT=%~dp0..\.."
for %%I in ("%REPO_ROOT%") do set "REPO_ROOT=%%~fI"
cd /d "%REPO_ROOT%"
set "PAPERCLIP_WORKSPACE_ROOT=%REPO_ROOT%"
where codex >nul 2>nul
if errorlevel 1 (
  echo [paperclip-wrapper] codex executable not found in PATH. 1>&2
  exit /b 1
)
call codex %*
exit /b %ERRORLEVEL%
