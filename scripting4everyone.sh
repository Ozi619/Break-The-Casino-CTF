obfuscate_output() {
    echo " "
    echo "Welcome to the High Stakes Casino Challenge!"
    echo "Your goal is to find the secret underground casino's location."
    echo " "
    echo "But beware, not everything is as it seems..."
    echo " "
    sleep 5
    echo " "
    echo "Scanning underground gambling networks..."
    echo " "
    sleep 5
}

fake_output() {
    echo "Alert: Casino security detected unauthorized access!"
    echo "Scrambling GPS signals..."
    sleep 2
    echo "Access denied. Try again later."
    exit 1
}

encrypted="Tif{eDvcsflievTSU"  

decode_location() {
    echo "$encrypted" | tr 'A-Za-z' 'N-ZA-Mn-za-m'  
}


if [ "$1" == "--cheat" ]; then
    echo "SECRET OVERRIDE: High-roller coordinates -> $(decode_location)"
    exit 0
fi

sleep 2
obfuscate_output

read -p "Press Enter to reveal the high-stakes casino coordinates: "


echo "🎰 Jackpot! The underground casino is located at: $(decode_location)"
echo " "
