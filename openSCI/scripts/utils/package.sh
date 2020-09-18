#!/bin/bash
PROJECT_PATH=$1
FILE="$PROJECT_PATH/package.json"

echo 'looking package.json'
if [ -f "$FILE" ]; then
    echo "package.json file was found"
    return 1
else
    echo "package.json file was not found"
    return 0
fi