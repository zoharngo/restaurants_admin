#!/bin/bash

# Activate virtual environment
. /appenv/bin/activate

# Wait until DB service is ready
wait_for_it (){
    wait_for_it.sh db:3306 -s -t 5
    return $?
}
 if [[ $(wait_for_it) -eq 0 ]]; then 
    exec $@
else
    exit $?
fi
exec $@