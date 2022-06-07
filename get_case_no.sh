export CASE_NUM=$(osascript /Users/alexjiang/alex_scripts/get_chrome_title | awk '{print $1}')
export CASE_WORK_DIR="/Users/alexjiang/Downloads/$CASE_NUM"
export CASE_UPLOAD_PATH="https://securefiles.pivotal.io/dropzone/customer-service/$CASE_NUM"
