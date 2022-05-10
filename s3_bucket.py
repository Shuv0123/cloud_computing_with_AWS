import boto3

Class S3:

     def __init__(self):
         self.s3_file = boto3.resource("s3")
         self.s3_client = boto3.client("s3")

     def make_bucket(self, bucket_name):
         location = {
             "LocationConstraint": "eu-west-1"
         }
         self.s3_client.create_bucket(Bucket=name, CreateBucketConfiguration=location)

     def upload_file(self, bucket_name, file_name):
         self.s3_client.upload_file(file_name, bucket_name, file_name)

     def retrieve_file(self, bucket_name, file_name):
         self.s3_client.download_file(file_name, bucket_name, file_name)

     def delete_data(self, bucket_name, file_name):
         self.s3_file.objects(bucket_name, file_name).delete()

     def delete_bucket(self, bucket_name):
         self.s3_client.Bucket(bucket_name).delet()


file = S3()
# file.make_bucket("eng110-shuvo-boto3")
# file.upload_file("eng110-shuvo-boto3", "s3_diagram.png")
# file.retrieve_file("eng110-shuvo-boto3", "s3_diagram.png")
# file.delete_data("eng110-shuvo-boto3", "s3_diagram.png")
# file.delete_bucket("eng110-shuvo-boto3")