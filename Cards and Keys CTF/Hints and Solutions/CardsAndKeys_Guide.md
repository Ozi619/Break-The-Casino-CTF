### Cards and Keys Guide ###


#### Linux Debian based Guide ####

'expect' is required to interact **keycard_scanner.bin**
`sudo apt-get install expect`

Run the supplied shell script **Win.sh** in the parent folder of **/Cards**.
**WARNING THE SCRIPT DOES CLEAR YOUR /TMP/ files**
*Inspect the Win.Sh script for further details*

Check **success_log.txt** for the winning combinations.
You should see the following
 - SUCCESS: KC_206_Pete.nfc accepted password 44693522
 - SUCCESS: KC_374_Bruce.nfc accepted password 76544567
 
Then use **keycard_scanner.bin** normally.
Enter the found file name and password.
Enter `2` too see the users **balance**.
*Note: check personal details with* `1` *to see Bruce's card is expired.*
*pete's card is still vaild and hence his balance is the flag*
