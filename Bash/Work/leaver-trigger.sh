#!/bin/bash
echo $0
echo $1

$SHELL

expect -c '
 log_user 0
 spawn /usr/bin/sudo su - someuser
 expect "*: "
 send ${1}
 interact
'