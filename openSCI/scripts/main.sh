#!/bin/bash
echo 'Starting auto-deploy'
echo

PROJECT_PATH=0
for arg in "$@"
do
    case $arg in
        -p=*|--path=*)
            PROJECT_PATH="${arg#*=}"
        ;;
    esac
done

if [[ $PROJECT_PATH == 0 ]];
then
    echo 'Set project path'
    exit 1
fi

echo
echo

case $1 in
    angular) sh $(dirname ${BASH_SOURCE[0]})/angular/main.sh $PROJECT_PATH;;
    react) sh $(dirname ${BASH_SOURCE[0]})/react/main.sh $PROJECT_PATH;;
    *)
        echo 'Select a available framework to be deployed'
        echo
        exit 1
    ;;
esac

echo 'Ending auto-deploy'
echo
