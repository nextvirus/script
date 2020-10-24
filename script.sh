a=$(cat app_logs | grep Refund | awk '{print $7}')
for i in $a
do 
 echo $i | ./uc-refund.sh
done
