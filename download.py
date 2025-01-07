import kagglehub

# Download latest version
path = kagglehub.dataset_download("mysarahmadbhat/alcohol-consumption")

print("Path to dataset files:", path)