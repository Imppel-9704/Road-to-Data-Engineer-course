from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Optional: set a generation-match precondition to avoid potential race conditions
    # and data corruptions. The request to upload is aborted if the object's
    # generation number does not match your precondition. For a destination
    # object that does not yet exist, set the if_generation_match precondition to 0.
    # If the destination object already exists in your bucket, set instead a
    # generation-match precondition using its generation number.
    generation_match_precondition = 0

    blob.upload_from_filename(source_file_name, if_generation_match=generation_match_precondition)

    print(
        f"File {source_file_name} uploaded to {destination_blob_name}."
    )

if __name__ == "__main__":
    upload_blob(
        bucket_name="r2de-ws-data-lake",
        source_file_name="ws2-output.csv",
        destination_blob_name="folder/output.csv"
    )

## or you can fill later on your own.
# if __name__ == "__main__":
#     file_name= input("What's file to upload: ")
#     dest_file_name= input("What's destination file name: ")

#     upload_blob(
#         bucket_name="r2de-ws-data-lake",
#         source_file_name=file_name,
#         destination_blob_name=dest_file_name
#     )