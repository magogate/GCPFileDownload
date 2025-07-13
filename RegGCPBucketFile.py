from google.cloud import storage

def read_gcs_file(bucket_name, file_name):
    # Initialize the client
    client = storage.Client()

    # Get the bucket
    bucket = client.get_bucket(bucket_name)

    # Get the blob (file) from the bucket
    blob = bucket.blob(file_name)

    # Download the file's content as a string
    file_content = blob.download_as_text()

    return file_content

def read_gcs_file_line_by_line(bucket_name, file_name):

    rowCnt = 0

    # Initialize the Google Cloud Storage client
    client = storage.Client()

    # Get the bucket
    bucket = client.get_bucket(bucket_name)

    # Get the blob (file) from the bucket
    blob = bucket.blob(file_name)

    # Download the file content as a string
    file_content = blob.download_as_text()

    # Read the file line by line
    for line in file_content.splitlines():
        # print(type(line))
        rowCnt = rowCnt + 1
        print(f"line number {str(rowCnt)}" + " Content - " + line)

# Example usage
bucket_name = "mandargogate-gk-c14"
file_name = "Countries.csv"

# content = read_gcs_file(bucket_name, file_name)
content = read_gcs_file_line_by_line(bucket_name, file_name)
print(content)
