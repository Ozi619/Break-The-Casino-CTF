#!/usr/bin/env bash

# Create a new combinations file
tempfile="combinations.txt"
success_log="success_log.txt"
> "$tempfile"
> "$success_log"

# Generate combinations: Each line = "filename<TAB>passwordA<TAB>passwordB<TAB>passwordC"
for file in *.nfc; do
    paste -d '\t' - - - < Passcodes.txt | sed "s/^/$file\t/" >> "$tempfile"
done

# Function to attempt unlocking the keycard
try_combination() {
    file="$1"
    passwordA="$2"
    passwordB="$3"
    passwordC="$4"

    expect <<EOF
        send "\r"
        spawn python3 keycard_scanner.py

        expect "Enter the file name:" { send "$file\r" }
        expect "Please enter your pass-code:" { send "$passwordA\r" }
        send "hello"
        expect {
            "Card and Pass accepted" {
                send "3\r"
                expect "Press Enter to close the program" { send "\r" }
                puts "SUCCESS: $file accepted password $passwordA"
                echo "SUCCESS: $file accepted password $passwordA" >> "$success_log"
                exit 0
            }
            "Error: Keycard and pass-code do not match" {
                send "$passwordB\r"
                expect {
                    "Card and Pass accepted" {
                        send "3\r"
                        expect "Press Enter to close the program" { send "\r" }
                        puts "SUCCESS: $file accepted password $passwordB"
                        echo "SUCCESS: $file accepted password $passwordB" >> "$success_log"
                        exit 0
                    }
                    "Error: Keycard and pass-code do not match" {
                        send "$passwordC\r"
                        expect {
                            "Card and Pass accepted" {
                                send "3\r"
                                expect "Press Enter to close the program" { send "\r" }
                                puts "SUCCESS: $file accepted password $passwordC"
                                echo "SUCCESS: $file accepted password $passwordC" >> "$success_log"
                                exit 0
                            }
                	expect "Press Enter to close the program" { send "\r" }
                	exit 1
                        }
                     expect "Press Enter to close the program" { send "\r" }
                     exit 1
                    }
                expect "Press Enter to close the program" { send "\r" }
                exit 1
                }
            }
        }
EOF
    return $?
}

export -f try_combination

echo "Testing combinations sequentially..."

# Read and execute each combination one at a time, ensuring sequential execution
while IFS=$'\t' read -r arg1 arg2 arg3 arg4; do
    echo start
    try_combination "$arg1" "$arg2" "$arg3" "$arg4"
    echo done
done < "$tempfile"

echo "All attempts completed."

