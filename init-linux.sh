#!/bin/bash

# Set the Edition of CEnv
edition="CEnv CE"

# Ask Which Files CEnv Want to Delete and the Language
while true;
do
    clear
    echo
    read -p " [+] LANGUAGE [en, es]: " lang
    if [[ "$lang" == "en" || "$lang" == "es" ]];
    then
        break
    fi
done

while true;
do
    clear
    if [[ "$lang" == "en" ]];
    then
        read -p " [?] Do You Want to Remove the Update Log File? | CHANGELOG.md | [y, n]: " changelog
    elif [[ "$lang" == "es" ]];
        then
        read -p " [?] ¿Desea Eliminar el Archivo del Registro de las Actualizaciones? | CHANGELOG.md | [y, n]: " changelog
    fi
    if [[ "$changelog" == "y" || "$changelog" == "n" ]];
    then
        break
    fi
done

while true;
do
    clear
    if [[ "$lang" == "en" ]];
    then
        read -p " [?] Do You Want to Remove the Document File? | DOCS.md | [y, n]: " docs
    elif [[ "$lang" == "es" ]];
        then
        read -p " [?] ¿Desea Eliminar el Archivo de la Documentación? | DOCS.md | [y, n]: " docs
    fi
    if [[ "$docs" == "y" || "$docs" == "n" ]];
    then
        break
    fi
done

while true;
do
    clear
    if [[ "$lang" == "en" ]];
    then
        echo " [*] We're Almost Done!!"
        echo
        read -p " [?] Do You Want to Install the Necessary Python Modules? [y, n]: " requirements
    elif [[ "$lang" == "es" ]];
        then
        echo " [*] ¡Ya Casí Acabamos!"
        echo
        read -p " [?] ¿Quiere Instalar los Modulos de Python Necesarios? [y, n]: " requirements
    fi
    if [[ "$requirements" == "y" || "$requirements" == "n" ]];
    then
        break
    fi
done

clear
if [[ "$requirements" == "y" ]];
then
    echo
    if [[ "$lang" == "en" ]];
    then
        echo " [*] We'll Install This:"
    elif [[ "$lang" == "es" ]];
        then
        echo " [*] Instalaremos Esto:"
    fi

    while IFS= read -r line;
    do
        echo "     - Python3-$line"
    done < "./requirements.txt"
fi

echo
echo " [*] $edition Files:"
echo "     - cenv.py"
echo "     - config.json"
echo "     - envs.json"
echo "     - README.md"
echo "     - LICENSE.md"
[[ "$changelog" == "y" ]] && echo "     - CHANGELOG.md"
[[ "$docs" == "y" ]] && echo "     - DOCS.md"
read -n 1 -s -r -p ""

# Install the Necessary Python Modules
clear
echo
if [[ "$requirements" == "y" ]];
then
    if ! pip3 install -r ./requirements.txt;
    then
        if [[ "$lang" == "en" ]];
        then
            echo " [!] Error installing Python modules."
        elif [[ "$lang" == "es" ]];
        then
            echo " [!] Error al instalar los módulos de Python."
        fi
        read -n 1 -s -r -p ""
    fi
    rm -f ./requirements.txt
else
    echo " After | Despues"
    echo " [!] pip3 install -r ~/CEnv/$edition/requirements.txt"
    mv ./requirements.txt ~/CEnv/$edition/requirements.txt
    read -n 1 -s -r -p ""
fi

# Delete the ./init-windows.bat File and ./img Directory
rm -f ./init-windows.bat
rm -rf ./img

# Create Directories in /usr/bin
mkdir -p /usr/bin/CEnv
mkdir -p /usr/bin/CEnv/"$edition"

# Move the CEnv Files to /usr/bin
mv -f ./cenv.py /usr/bin/CEnv/"$edition"/ 2>/dev/null
mv -f ./config.json /usr/bin/CEnv/"$edition"/ 2>/dev/null
mv -f ./envs.json /usr/bin/CEnv/"$edition"/ 2>/dev/null
mv -f ./README.md /usr/bin/CEnv/"$edition"/ 2>/dev/null
mv -f ./LICENSE.md /usr/bin/CEnv/"$edition"/ 2>/dev/null
[[ "$changelog" == "y" ]] && mv -f ./CHANGELOG.md /usr/bin/CEnv/"$edition"/ 2>/dev/null
[[ "$docs" == "y" ]] && mv -f ./DOCS.md /usr/bin/CEnv/"$edition"/ 2>/dev/null

# Delete this File and CEnv Folder, and Enjoy CEnv
clear
echo
echo " [+] Use: cenv ..."
rm -f ./init-linux.sh
rm -rf ./"$edition"
