#!/bin/bash
# Recursive function
recursion() {
  local n=$1
  if [ "$n" -le 0 ]; then
    return
  fi

  # Pre-recursion
  echo "Before: $n"

  # Recursive call
  recursion $((n - 1))

  # Post-recursion
  echo "After: $n"
}

# Start recursion with a number
recursion 5
