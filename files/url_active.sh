set -x 
file = "$1"
while IFS= read -r i; do
if nmap -sn "$i" | grep -q "Host is up"; then
echo "Ping successful, host active: $i"
echo "$i" >> "${file}_active"
else
echo "Ping unsuccessful: $i"
fi
done < "$file"