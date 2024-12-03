
REM Init Batch Program Language
@echo off

REM Set the Edition of CEnv
set "edition=CEnv CE"

REM Ask Which Files CEnv Want to Delete and the Language
:while_idiom
if 1 == 1 (
    cls
    echo.
    set /p "lang= [+] LANGUAJE [en, es]: "
    if "%lang%" neq "en" if "%lang%" neq "es" (
        goto :while_idiom
    ) else (
        goto :while_changelog
    )
)
:while_changelog
if 1 == 1 (
    cls
    echo.
    if "%lang%"=="en" (
        set /p "changelog= [?] Do You Want to Remove the Update Log File? | CHANGELOG.md | [y, n]: "
    ) else if "%lang%"=="es" (
        set /p "changelog= [?] ¿Desea Eliminar el Archivo del Registro de las Actualizaciones? | CHANGELOG.md | [y, n]: " 
    )
    if "%changelog%" neq "y" if "%changelog%" neq "n" (
        goto :while_changelog
    ) else (
        goto :while_docs
    )
)
:while_docs
if 1 == 1 (
    cls
    echo.
    if "%lang%"=="en" (
        set /p "docs= [?] Do You Want to Remove the Document File? | DOCS.md | [y, n]: "
    ) else if "%lang%"=="es" (
        set /p "docs= [?] ¿Desea Eliminar el Archivo de la Documentación? | DOCS.md | [y, n]: " 
    )
    if "%docs%" neq "y" if "%docs%" neq "n" (
        goto :while_docs
    ) else (
        goto :while_requirements
    )
)
:while_requirements
if 1 == 1 (
    cls
    echo.
    if "%lang%"=="en" (
        echo " [*] We're Almost Done!! "
        echo.
        set /p "requirements= [?] Do You Want to Install the Necessary Python Modules? [y, n]: "
    ) else if "%lang%"=="es" (
        echo " [*] ¡Ya Casí Acabamos! "
        echo.
        set /p "requirements= [?] ¿Quiere Instalar los Modulos de Python Necesarios? [y, n]: " 
    )
    if "%requirements%" neq "y" if "%requirements%" neq "n" (
        goto :while_requirements
    ) else (
        goto :install
    )
)
:install
cls
if "%requirements%"=="y" (
    echo.
    if "%lang%"=="en" (
        echo " [*] We'll Install This: "
    ) else if "%lang%"=="es" (
        echo " [*] Instalaremos Esto: "
    )
    for /f "tokens=*" %%i in ("%cd%\requirements.txt") do (
        echo "     - Python3-%%i"
    )
)
echo.
echo " [*] %edition% Files: "
echo "     - cenv.py "
echo "     - config.json "
echo "     - envs.json "
echo "     - README.md "
echo "     - LICENSE.md "
if %changelog%=="y" echo "     - CHANGELOG.md"
if %docs%=="y" echo "     - DOCS.md"
pause > nul

REM Install the Necessary Python Modules
cls
echo.
if "%requirements%"=="y" (
    pip.exe install -r "%cd%\requirements.txt" || (
        if "%lang%"=="en" (
            echo " [!] Error installing Python modules."
        ) else (
            echo " [!] Error al instalar los módulos de Python."
        )
        pause
    )
    if exist "%cd%\requirements.txt" del /f /q "%cd%\requirements.txt"
) else (
    echo " After | Despues"
    echo " [!] pip install -r %USERPROFILE%\AppData\Local\Programs\CEnv\%edition%\requirements.txt"
    if exist "%cd%\requirements.txt" move "%cd%\requirements.txt" "%USERPROFILE%\AppData\Local\Programs\CEnv\%edition%\requirements.txt"
    pause > nul
)
cls

REM Delete the .\init-linux.sh File and .\img Directory
del /f /q "%cd%\init-linux.sh"
rmdir /s /q "%cd%\img"

REM Create Directories in AppData\Local\Programs
mkdir "%USERPROFILE%\AppData\Local\Programs\CEnv"
mkdir "%USERPROFILE%\AppData\Local\Programs\CEnv\%edition%"

REM Move the CEnv Files to AppData\Local\Programs\CEnv\EDITION\cenv.py
if exist "%cd%\cenv.py" move "%cd%\cenv.py" "%USERPROFILE%\AppData\Local\Programs\CEnv\%edition%"
if exist "%cd%\config.json" move "%cd%\config.json" "%USERPROFILE%\AppData\Local\Programs\CEnv\%edition%"
if exist "%cd%\envs.json" move "%cd%\envs.json" "%USERPROFILE%\AppData\Local\Programs\CEnv\%edition%"
if exist "%cd%\README.md" move "%cd%\README.md" "%USERPROFILE%\AppData\Local\Programs\CEnv\%edition%"
if exist "%cd%\LICENSE.md" move "%cd%\LICENSE.md" "%USERPROFILE%\AppData\Local\Programs\CEnv\%edition%"
if "%changelog%"=="y" if exist "%cd%\CHANGELOG.md" move "%cd%\CHANGELOG.md" "%USERPROFILE%\AppData\Local\Programs\CEnv\%edition%"
if "%docs%"=="y" if exist "%cd%\DOCS.md" move "%cd%\DOCS.md" "%USERPROFILE%\AppData\Local\Programs\CEnv\%edition%"

REM Set a new Path Site for CEnv
echo %PATH% | findstr /i /c:"%USERPROFILE%\AppData\Local\Programs\CEnv\%edition%" > nul
if errorlevel 1 (
    setx Path "%Path%;%USERPROFILE%\AppData\Local\Programs\CEnv\%edition%"
)

REM Delete this File and CEnv Folder, and Enjoy CEnv
cls
echo.
echo " [+] Use: | cenv |... "
if exist "%cd%\init-windows.bat" move "%cd%\init-windows.bat" "%cd%\..\init-windows.bat"
if exist "%edition%" rmdir /s /q "%edition%"
if exist "%cd%\init-windows.bat" del /f /q "..\init-windows.bat"
