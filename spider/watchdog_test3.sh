#!/bin/bash

# watchdog test script

compute_ip="10.127.2.62"
network_ip="10.127.2.66"
FILE=$0
comp_cmd="./$FILE a"
net_cmd="./$FILE a b"

# 备注：由于停止 openvswitch 服务会断开当前连接，故此服务需要手工进行测试
service_base=(nova-api nova-scheduler nova-conductor nova-novncproxy nova-consoleauth ceilometer-collector httpd \
heat-engine heat-api heat-api-cfn haproxy memcached keepalived_haproxy keepalived_drs keepalived_vmha keepalived_zabbix \
cinder-api cinder-volume cinder-scheduler cinder-backup glance-api glance-registry neutron-server \
ironic-api ironic-conductor aodh-evaluator aodh-listener aodh-notifier gnocchi-metricd octavia-api octavia-worker \
octavia-health-manager octavia-housekeeping)

service_name=(zabbix-agent ceilometer-notification ceilometer-central)
service_proc=(zabbix_agentd ceilometer-agent-notification ceilometer-polling)
contr_serv=(${service_base[@]} ${service_name[@]})
contr_proc=(${service_base[@]} ${service_proc[@]})
contr_lens=${#contr_serv[@]}

comp_serv=(nova-compute ceilometer-compute neutron-metadata-agent)
comp_proc=(nova-compute ceilometer-polling neutron-metadata-agent)
comp_lens=${#comp_serv[@]}

net_serv=(neutron-openvswitch-agent neutron-dhcp-agent neutron-vpn-agent)
net_lens=${#net_serv[@]}

file=watchdog_result_`date +%Y-%m-%d`.log
echo "==================================" >> $file
echo "Test time `date +'%Y-%m-%d_%H-%M-%S'`" >> $file

function check_process_normal()
{
    ser=$1
    result=`ps -elf | grep -v grep | grep $ser | grep -v color`
    if [ -n "$result" ]
    then
        echo "OK. Now $ser process is normal."
    else
        echo "Fail. Now $ser process is not exist." >> $file
    fi
}

# When stop/kill service, process should not exist.
function check_process_stopped()
{
    ser=$1
    result=`ps -elf | grep -v grep | grep $ser | grep -v color`
    if [ -n "$result" ]
    then
        echo "Fail. After stop $ser service, process is not stopped." >> $file
    else
        echo "OK. Now $ser process is stopped."
    fi
}

function stop_service()
{
    serv_list=$1
    proc_list=$2
    echo "****stop service $serv_list****"
    service $serv_list stop
    sleep 6
    check_process_stopped $proc_list
}

function kill_service_process()
{
    serv_list=$1
    proc_list=$2
    echo "kill service $proc_list process"
    main_pid=`service $serv_list status | grep Main | awk '{print $3}'`
    kill -9 $main_pid
    sleep 6
    check_process_stopped $proc_list
}

function check_all_service()
{
    proc_list=$1
    for ser in ${proc_list[*]}
    do
        check_process_normal $ser
    done
}


### Test controller node service. ###
if [ $# == 0 ];then
echo "=====Begin test, stop all service.=====" | tee -a $file
for ((i=0; i<$contr_lens; i++))
do
    check_process_normal ${contr_proc[$i]}
    stop_service ${contr_serv[$i]} ${contr_proc[$i]}
done
sleep 60
echo "=====After test, check all service status.=====" | tee -a $file
check_all_service "${contr_proc[*]}"

sleep 20
echo "=====Begin test, kill service process.=====" | tee -a $file
for ((i=0; i<$contr_lens; i++))
do
    kill_service_process ${contr_serv[$i]} ${contr_proc[$i]}
done
sleep 60
echo "=====After test, check all service status.=====" | tee -a $file
check_all_service "${contr_proc[*]}"

scp $FILE root@$compute_ip:/root
scp $FILE root@$network_ip:/root
ssh -t -p 22 root@$compute_ip "$comp_cmd"
ssh -t -p 22 root@$network_ip "$net_cmd"
fi


### Test compute node service. ###
#if [ $1 -eq 'a' ];then
if [ $# == 1 ];then
echo "=====Begin test, stop all service on $compute_ip.=====" | tee -a $file
for ((i=0; i<$comp_lens; i++))
do
    check_process_normal ${comp_proc[$i]}
    stop_service ${comp_serv[$i]} ${comp_proc[$i]}
done
sleep 30
echo "=====After test, check all service status on $compute_ip.=====" | tee -a $file
check_all_service "${comp_proc[*]}"

sleep 10
echo "=====Begin test, kill service process on $compute_ip.=====" | tee -a $file
for ((i=0; i<$comp_lens; i++))
do
    kill_service_process ${comp_serv[$i]} ${comp_proc[$i]}
done
sleep 30
echo "=====After test, check all service status on $compute_ip.=====" | tee -a $file
check_all_service "${comp_proc[*]}"
fi


### Test network node service. ###
if [ $# == 2 ];then
echo "=====Begin test, stop all service on $network_ip.=====" | tee -a $file
for ((i=0; i<$net_lens; i++))
do
    check_process_normal ${net_serv[$i]}
    stop_service ${net_serv[$i]} ${net_serv[$i]}
done
sleep 30
echo "=====After test, check all service status on $network_ip.=====" | tee -a $file
check_all_service "${net_serv[*]}"

sleep 10
echo "=====Begin test, kill service process on $network_ip.=====" | tee -a $file
for ((i=0; i<$net_lens; i++))
do
    kill_service_process ${net_serv[$i]} ${net_serv[$i]}
done
sleep 30
echo "=====After test, check all service status on $network_ip.=====" | tee -a $file
check_all_service "${net_serv[*]}"
fi


