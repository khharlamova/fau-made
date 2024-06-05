#!/bin/bash

output_dir=~/project
processed_file_1="$output_dir/processed_co2_emissions_2018_2022.csv"
processed_file_2="$output_dir/processed_air_quality_2018_2022.csv"

python3 pipeline.py

# Check if the output files are created
if [[ -f "$processed_file_1" ]]; then
    echo "Test passed: $processed_file_1 exists."
else
    echo "Test failed: $processed_file_1 does not exist."
    exit 1
fi

if [[ -f "$processed_file_2" ]]; then
    echo "Test passed: $processed_file_2 exists."
else
    echo "Test failed: $processed_file_2 does not exist."
    exit 1
fi

echo "All tests passed."
