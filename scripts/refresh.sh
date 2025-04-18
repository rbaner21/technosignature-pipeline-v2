#!/usr/bin/env bash
# 1. Activate conda env
source ~/anaconda3/etc/profile.d/conda.sh
conda activate technosig-v2

# 2. Go to project root
cd ~/Documents/technosignature-pipeline-v2

# 3. Execute notebooks headlessly
jupyter nbconvert --to notebook --execute notebooks/1_data_access.ipynb --output temp1.ipynb
jupyter nbconvert --to notebook --execute notebooks/2_preprocessing.ipynb --output temp2.ipynb
jupyter nbconvert --to notebook --execute notebooks/3_feature_engineering.ipynb --output temp3.ipynb
jupyter nbconvert --to notebook --execute notebooks/4_modeling.ipynb --output temp4.ipynb

# 4. Generate HTML reports
python src/report.py

# 5. Append logs
) &>> logs/refresh.log
