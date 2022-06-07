#tar -zcvf $CASE_WORK_DIR".tar.gz" -C $CASE_WORK_DIR
scp -C -r $CASE_WORK_DIR gpadmin@10.193.94.7:/data/logs/
