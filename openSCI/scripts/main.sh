echo 'Starting auto-deploy'
echo

# NODE_VERSION=$(nodes -v 2>&1)

# HAS_NODE=1
# if [[ $NODE_VERSION =~ 'command not found' ]];
# then
#     HAS_NODE=0
# fi

# if [[ $HAS_NODE == 0 ]];
# then
#     echo 'Installing node'
#     echo
#     sh utils/node_installer.sh
# fi

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
# echo "$PROJECT_PATH"
echo

# HAS_PACKAGE=$(sh utils/package.sh)

# if [[ $HAS_PACKAGE == 0 ]];
# then
#     exit 1
# fi

case $1 in
    angular) sh angular/main.sh $PROJECT_PATH;;
    react) sh react/main.sh $PROJECT_PATH;;
    *)
        echo 'Select a available framework to be deployed'
        echo
        exit 1
    ;;
esac

echo 'Ending auto-deploy'
echo
