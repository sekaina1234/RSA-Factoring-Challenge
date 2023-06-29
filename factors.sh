#!/bin/bash

factorize_number() {
  local number=$1
  local factors=()
  for ((i=2; i <= number / 2; i++)); do
    if ((number % i == 0)); then
      factors+=("$i $((number / i))")
    fi
  done
  printf "%s\n" "${factors[@]}"
}

factorize_file() {
  local file=$1
  while IFS= read -r line || [[ -n $line ]]; do
    number=$(echo "$line" | tr -d '\n')
    factors=$(factorize_number "$number")
    while IFS= read -r factor; do
      echo "$number=$factor"
    done <<< "$factors"
  done < "$file"
}

if [[ $# -ne 1 ]]; then
  echo "Usage: factors <file>"
else
  factorize_file "./$1"
fi
