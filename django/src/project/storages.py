from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    location = 'static'
    bucket_name = os.environ.get('AWS_STATIC_STORAGE_BUCKET_NAME')


class MediaStorage(S3Boto3Storage):
    location = 'media'
    bucket_name = os.environ.get('AWS_MEDIA_STORAGE_BUCKET_NAME')
    file_overwrite = False
