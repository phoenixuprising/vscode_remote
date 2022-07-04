#!/bin/bash

function code-curl() {
    ip=$1
    port=$2
    path_to_open=$(realpath $3)
    is_file=0
    if [[ -f $path_to_open ]]; then
      is_file=1
    fi
    curl -X POST "http://${ip}:${port}/open-vscode" \
        -H 'Content-Type: application/json' \
        -d "{\"path\":\"${path_to_open}\", \"is_file\":${is_file}}"
}

export CODE_CLIENT_IP="192.168.0.28"
export CODE_CLIENT_PORT="8080"
alias code="code-curl ${CODE_CLIENT_IP} ${CODE_CLIENT_PORT} $1"