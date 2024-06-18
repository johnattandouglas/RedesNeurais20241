#!/bin/bash
#SBATCH --job-name=GridSearchProjetoRedesNeurais
#SBATCH --ntasks=1
#SBATCH --mem 8G 
#SBATCH -c 1 	 # Total de cores que quero utilizar
#SBATCH --gpus=1 # total de GPUs que vou usar
#SBATCH -p short # Se vai ser um experimento tipo long (Até 7 dias ) ou  short (até 2 dias)
#SBATCH --mail-type=BEGIN,END,FAIL # quais ocorrências eu quero ser notificado por e-mail
#SBATCH --mail-user=jdfv@cin.ufpe.br
#SBATCH --output=out.text
#SBATCH --error=err.text

module load Python/3.10

# Ativando o módulo
source $HOME/lorien/bin/activate

pip install -r ../requirements.txt # instalando dependências necessárias

python gridsearch.py