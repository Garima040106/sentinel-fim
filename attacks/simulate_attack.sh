#!/bin/bash

TARGET=~/fim_test

echo "[*] Simulating attacker activity..."

# create files
for i in {1..5}
do
    echo "malicious content" > $TARGET/file_$i.txt
done

sleep 1

# modify rapidly (ransomware-like)
for i in {1..10}
do
    echo "encrypted_data_$RANDOM" >> $TARGET/file_1.txt
done

sleep 1

# delete evidence
rm -f $TARGET/file_*.txt

echo "[✓] Attack simulation complete"
