import json
import logging

# See https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types
dtype_text = 'text/plain'
dtype_json = 'application/json'
dtype_bin  = 'application/octet-stream'

CONTENT_TYPE = 'Content-Type'

logger = logging.getLogger(__name__)


# Convert python objects to binary for writing to the stream
def to_binary(obj):
    if obj is None:
        obj = ''
    if isinstance(obj, str):
        return obj.encode(), dtype_text
    elif isinstance(obj, (bytes, bytearray)):
        return obj, dtype_bin
    else:
        try:
            jstring = json.dumps(obj)
            return jstring.encode(), dtype_json
        except TypeError:
            logger.error('Unsupported object type of %s' % type(obj))
            return None, ''

# Convert binary stream data into a python object
def from_binary(data, ctype):
    if ctype == dtype_text:
        return data.decode()
    elif ctype == dtype_json:
        return json.loads(data)
    elif ctype == dtype_bin:
        return data
    else:
        logger.error('Invalid content type: %s' % ctype)
        return None
