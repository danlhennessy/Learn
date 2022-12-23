$var = Read-Host "Enter a number"
echo $var

Write-Output "command 1"; Write-Output "command 2"

$string = 'tewst'

# Pipe output of $string to Get-Member
$string | Get-Member

#Using EndsWith method on $string
$string.EndsWith("t")