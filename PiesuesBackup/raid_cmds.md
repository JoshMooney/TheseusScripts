
#Prints out data about the RAID
sudo mdadm --examine /dev/md0

# Check which drives are available
ll /dev/sd*

# Note
If one or more of the drives are not appearing then this could be a boot mount issue. If so a
quick fix for this is to remove all the drives reboot the pi and then after the pi is fully
rebooted insert the drives again. Then run the start script and bobs your uncle.

# Rebuilds RAID Cache (without data loss)
sudo mdadm --assemble --verbose --run --force /dev/md0 /dev/sdd1 /dev/sde1 /dev/sdf1 /dev/sdg1
