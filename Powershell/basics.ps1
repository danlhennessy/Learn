# User input + variable
$var = Read-Host "Enter a number"
echo $var

# Consecutive commands
Write-Output "command 1"; Write-Output "command 2"

#Escaping a semi-colon
Write-Output hello-world `; pwd

# Pipe output of $string to Get-Member
$string = 'tewst'
$string | Get-Member

#Using EndsWith method on $string
$string.EndsWith("t")

