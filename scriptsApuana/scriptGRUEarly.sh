#!/bin/bash
#SBATCH --job-name=GridSearch
#SBATCH --ntasks=1
# SBATCH --cpus-per-task=4
#SBATCH --mem 16G 
#SBATCH -c 8 	 # Total de cores que quero utilizar
#SBATCH --gpus=1 # total de GPUs que vou usar
#SBATCH -p short # Se vai ser um experimento tipo long (Até 7 dias ) ou  short (até 2 dias)
#SBATCH --mail-type=BEGIN,END,FAIL # quais ocorrências eu quero ser notificado por e-mail
#SBATCH --mail-user=jdfv@cin.ufpe.br
# SBATCH --output=job_output.txt
# SBATCH --error=job_error.txt

# carregar versão python
module load Python/3.10
# Ativando ambiente
source $HOME/lorien/bin/activate

python gridSearchEarlyGRU.py