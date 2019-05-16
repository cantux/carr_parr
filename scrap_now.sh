#/bin/bash

echo "before calling source: $PATH"
source /home/ubuntu/miniconda2/bin/activate py_scrap
echo "after calling source: $PATH"
python main.py
mv data* /var/www/html/.
source deactivate

