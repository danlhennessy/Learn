## Create Module
go mod init module-name

## Run Module
go run module-name
or
go run module-directory

## Compile to executable and run
go build (From module directory)
./module-name

## Check install path and add to shell path
go list -f '{{.Target}}'
add path to PATH: export PATH=$PATH:/path/to/your/install/directory , or add to zshrc

## Install
go install (from module directory)

## Run application from anywhere
module-name

## Uninstall
rm install-path>/module-name