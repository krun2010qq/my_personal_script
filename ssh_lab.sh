#!/usr/bin/expect
spawn  ssh paassupport@tanzu-csp-1.tanzu-gss-labs.vmware.com
expect "password:"
send "zj8&0lzyh4N#vW5Q\n";
interact
