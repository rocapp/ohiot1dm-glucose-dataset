#!/usr/bin/env sh

set -e

# convert2parquet.sh :
# convert the OhioData.zip to .parquet

sh -c "$HOME/Git/pfun-data/dependencies/zip-to-parquet/result/bin/zip-to-parquet" \
   --input ohiot1dm_glucose_dataset/data/OhioData.zip \
   --output ohiot1dm_glucose_dataset/data/OhioData.parquet \
   --glob '**/*.csv'
