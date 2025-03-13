#!/usr/bin/env bash

tempfile="combinations.txt"
> "$tempfile"

# Each line will contain "filename<TAB>password<TAB>password<TAB>password"
for file in *.nfc; do
    paste -d '\t' - - - < Passcodes2.txt | sed "s/^/$file\t/" >> "$tempfile"
done

try_combination() {
    file="$1"
    passwordA="$2"
    passwordB="$3"
    passwordC="$4"
    expect <<EOF
        set timeout 1
        spawn python3 keycard_scanner.py

        expect "Enter the file name:" { send "$file\r" }
        expect "Please enter your pass-code:" { send "$passwordA\r" }

        expect {
            "Card and Pass accepted" {
                send "3\r"
                expect "Press Enter to close the program" { send "\r" }
                echo "SUCCESS: $file accepted password $passwordA" >> "$tempfile"
                echo "SUCCESS: $file accepted password $passwordA"
                exit 0
            }
            "Error: Keycard and pass-code do not match" {
                send "$passwordB\r"
                expect {
                    "Card and Pass accepted" {
                        send "3\r"
                        expect "Press Enter to close the program" { send "\r" }
                        echo "SUCCESS: $file accepted password $passwordB" >> "$tempfile"
                        echo "SUCCESS: $file accepted password $passwordB"
                        exit 0
                    }
                    "Error: Keycard and pass-code do not match" {
                        send "$passwordC\r"
                        expect {
                            "Card and Pass accepted" {
                                send "3\r"
                                expect "Press Enter to close the program" { send "\r" }
                                echo "SUCCESS: $file accepted password $passwordC" >> "$tempfile"
                                echo "SUCCESS: $file accepted password $passwordC"
                                exit 0
                            }
                        }
                    }
                }
            }
        }

        expect "Press Enter to close the program" { send "\r" }
        exit 1
EOF
    return $?
}

export -f try_combination

echo "Testing combinations concurrently..."

parallel -j 2 --colsep '\t' 'try_combination {1} {2} {3} {4} && echo "SUCCESS: {1} accepted password {2} {3} {4}"' :::: "$tempfile"
