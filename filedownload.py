import kagglehub

# Download latest version
path = kagglehub.dataset_download("rohitgrewal/hr-data-mnc")

print("Path to dataset files:", path)