#/bin/sh

#source ~/miniconda2/etc/profile.d/conda.sh
#conda init zsh
#source /home/ubuntu/miniconda2/bin/activate /home/ubuntu/miniconda2/envs/py_scrap
#conda activate /home/ubuntu/miniconda2/envs/py_scrap
/home/ubuntu/miniconda2/condabin/conda run -p /home/ubuntu/miniconda2/envs/py_scrap python /home/ubuntu/carr_parr/main.py 
#conda run -n py_scrap python /home/ubuntu/carr_parr/main.py 
#python /home/ubuntu/carr_parr/main.py 
#/home/ubuntu/miniconda2/bin/python /home/ubuntu/carr_parr/main.py
mv /home/ubuntu/data* /var/www/html/.
#source /home/ubuntu/miniconda2/bin/deactivate
#conda deactivate
