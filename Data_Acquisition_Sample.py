# Find and download action datasets

import os
import kaggle
import random

kaggle.KaggleApi.configure(api_key=os.environ.get("KAGGLE_API_TOKEN"))

def download_action_dataset():
  """Searches for datasets containing "action" and downloads a random one."""

  # Find datasets with "action"
  datasets = kaggle.DatasetSearch(query="action").execute()

  # Check if any datasets found
  if datasets:
    # Pick one at random
    chosen_one = random.choice(datasets)

    # Download the first file (assuming it's important)
    try:
      chosen_one.download_files(quiet=False)
      print(f"Downloaded: {chosen_one.title}")
    except Exception as e:
      print(f"Download error: {e}")
  else:
    print("No action datasets found! Try a different search term.")

#  find action data
download_action_dataset()
