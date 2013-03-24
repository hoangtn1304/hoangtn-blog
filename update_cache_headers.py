"""Set cache headers in S3."""


from os import environ

from boto.s3.connection import S3Connection


connection = S3Connection()
bucket = connection.get_bucket(environ.get('AWS_BUCKET'))


for key in bucket.list():

    patched = True
    if key.name.endswith('.png'):
        key.metadata.update({
            'Content-Type': 'image/png',
            'Surrogate-Control': 'max-age=31536000',
            'Cache-Control': 's-maxage=31536000, max-age=31536000, public',
        })
    elif key.name.endswith('.gif'):
        key.metadata.update({
            'Content-Type': 'image/gif',
            'Surrogate-Control': 'max-age=31536000',
            'Cache-Control': 's-maxage=31536000, max-age=31536000, public',
        })
    elif key.name.endswith('.html'):
        key.metadata.update({
            'Content-Type': 'text/html; charset=utf-8',
            'Surrogate-Control': 'max-age=31536000',
            'Cache-Control': 's-maxage=31536000, max-age=31536000, public',
        })
    elif key.name.endswith('.css'):
        key.metadata.update({
            'Content-Type': 'text/css; charset=utf-8',
            'Surrogate-Control': 'max-age=31536000',
            'Cache-Control': 's-maxage=31536000, max-age=31536000, public',
        })
    elif key.name.endswith('.js'):
        key.metadata.update({
            'Content-Type': 'application/javascript; charset=utf-8',
            'Surrogate-Control': 'max-age=31536000',
            'Cache-Control': 's-maxage=31536000, max-age=31536000, public',
        })
    elif key.name.endswith('.xml'):
        key.metadata.update({
            'Content-Type': 'application/xml; charset=utf-8',
            'Surrogate-Control': 'max-age=31536000',
            'Cache-Control': 's-maxage=31536000, max-age=31536000, public',
        })
    elif key.name.endswith('.txt'):
        key.metadata.update({
            'Content-Type': 'text/plain; charset=utf-8',
            'Surrogate-Control': 'max-age=31536000',
            'Cache-Control': 's-maxage=31536000, max-age=31536000, public',
        })
    else:
        patched = False

    if patched:
        key.copy(
            key.bucket.name,
            key.name,
            key.metadata,
            preserve_acl = True,
        )
        print 'Fixed:', key.name
