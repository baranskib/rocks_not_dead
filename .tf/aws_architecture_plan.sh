#!/usr/bin/env bash

# Run this script pointing to all libraries required to package them for the Lambda.

terraform init

cp -r /opt/homebrew/Caskroom/miniforge/base/envs/albums_analysis/lib/python3.9/site-packages/spotipy ../lambda_payloads/albums_released_by_year_payload/
cp -r /opt/homebrew/Caskroom/miniforge/base/envs/albums_analysis/lib/python3.9/site-packages/requests ../lambda_payloads/albums_released_by_year_payload/
cp -r /opt/homebrew/Caskroom/miniforge/base/envs/albums_analysis/lib/python3.9/site-packages/charset_normalizer/ ../lambda_payloads/albums_released_by_year_payload/


cp /Users/bartek/PycharmProjects/rocks_not_dead/albums_released_by_year.py ../lambda_payloads/albums_released_by_year_payload/

cd ../lambda_payloads/albums_released_by_year_payload/ || exit

zip -r ../../payload.zip *

cd ../../.tf/ || exit

terraform plan