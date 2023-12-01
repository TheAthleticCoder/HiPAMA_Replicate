#!/bin/bash
# Change the name to what you want.
#SBATCH --job-name=my_run_gopt
# Replace with irel if you want to use irel account. Refrain from using irel if not necessary.
#SBATCH -A irel
# Specify the number of GPUs you need.
#SBATCH -c 25
# Specify the number of GPUs you need. It's zero in this script. Replace with 1 to 4, as you want.
#SBATCH -G 2
# Outputs from your job would get written to the file specified below.
#SBATCH -o gopt.out
# Time of the Job. The tie specified below if 4 days.
#SBATCH --time=4-00:00:00
#SBATCH --mail-type=ALL
# Memory per CPU that you need (in MBs)
#SBATCH --mem-per-cpu=2999

lr=1e-3
depth=3
head=1
batch_size=25
embed_dim=24
model=hipama
am=librispeech

exp_dir=../exp/gopt-${lr}-${depth}-${head}-${batch_size}-${embed_dim}-${model}-${am}-br

# repeat times
repeat_list=(0 1 2 3 4)

for repeat in "${repeat_list[@]}"
do
  mkdir -p $exp_dir-${repeat}
  python ./traintest.py --lr ${lr} --exp-dir ${exp_dir}-${repeat} --goptdepth ${depth} --goptheads ${head} \
  --batch_size ${batch_size} --embed_dim ${embed_dim} \
  --model ${model} --am ${am}
done

python ./collect_summary.py --exp-dir $exp_dir
