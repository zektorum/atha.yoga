printf "\n---------------------------\nInstall git hooks\n"
pre-commit install
pre-commit install --hook-type commit-msg
printf "Ok"