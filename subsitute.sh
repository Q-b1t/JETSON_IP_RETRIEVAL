#!/bin/bash
# initialize the scripts with ip and port adresses (i dont want to publish any address)

if [ $# -lt 3 ]; then
    echo "No file was specified"
    echo "Format: ./substitute.sh /<folder>/<script>.py <address> <port>"  
    exit 0
else
    target_file=$1
    address=$2
    port=$3
fi

echo "$target_file, $address, $port"

sed -i "s/INPUT_ADDRESS_CHANGE/$address/" $target_file
sed -i "s/INPUT_PORT_CHANGE/$port/" $target_file