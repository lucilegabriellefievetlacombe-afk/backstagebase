#!/bin/bash

kubectl cluster-info --context kind-kind

echo "\nName Spaces"
echo -e "kubectl get namespace -o jsonpath='{.items[*].metadata.name}'\n"

for ns in `kubectl get namespace -o jsonpath='{.items[*].metadata.name}'`
do
  echo -e "\n\n####################################"
  echo -e "######### $ns namespace #########"
  echo -e "####################################\n"
  echo "ingress (ing), deployments (deploy), nodes (no), replicatsets (rs), replication controllers (rc), daemonset (ds), endpoint (ep), services (svc), jobs, po (pods), events (ev), resourcequotas (quota), configmap (cm), componentstatus (cs)"
  for rt in ing deploy no rs rc ds ep svc jobs po ev quota cm cs roles
  do
    res=`kubectl get $rt -n $ns 2> /dev/null`
    if [ "$res" != "" ]; then
    	echo -e "\n$rt in $ns namespace (kubectl get $rt -n $ns)"
	echo -e "$res\n"
    fi
  done
  
  secs=`kubectl get secrets -n $ns -o jsonpath='{.items[*].metadata.name}'`
  if [ "^$secs" != "" ]; then
  	echo -e "\nSecrets in $ns namespace (kubectl get secrets -n $ns -o jsonpath='{.items[*].metadata.name}')\n"
  	for sec in $secs; 
 	do
    		pass=`kubectl get secrets -n $ns $sec -o jsonpath='{.data.password}' | base64 -d 2> /dev/null`
    		if [ "$pass" != "" ]; then
    			echo -e "\nSecret $sec in $ns namespace (kubectl get secrets -n $ns $sec -o jsonpath='{.data.password}' | base64 -d)"
			echo $pass
    		fi
  	done
  fi
done
