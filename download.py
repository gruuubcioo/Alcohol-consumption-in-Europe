import kagglehub

# Download latest version
path = kagglehub.dataset_download("mattop/alcohol-consumption-per-capita-2016")

print("Path to dataset files:", path)