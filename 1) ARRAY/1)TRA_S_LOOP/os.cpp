#!/bin/bash

echo "Parent Process ID: $$"

# Fork using background process (&)
echo "Creating Child Process..."

(
    echo ""
    echo "--- Child Process ---"
    echo "Child PID: $$"
    echo "Parent PID: $PPID"

    echo ""
    echo "Executing 'ps' command:"
    
    # exec replaces current shell with ps command
    exec ps
) &

# Store child PID
child_pid=$!

echo ""
echo "--- Parent Process ---"
echo "Parent is waiting for child process to finish..."

# wait for child process
wait $child_pid

echo "Child process finished."

