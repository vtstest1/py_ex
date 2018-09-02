#!/bin/bash
EX_NAME=t4_${1}.py
touch ${EX_NAME} 
chmod +x ${EX_NAME}
echo "#!/usr/local/bin/python3">> ${EX_NAME}



