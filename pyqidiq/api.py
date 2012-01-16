import urllib
import urllib2
import json
import logging
import sys

log = logging.getLogger(__name__)

class QidiqAPI(object):

  def __init__(self, *args, **kwargs):
    self.api_key = kwargs['api_key']
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s', stream=sys.stdout)
    log.debug("Initializing QidiqAPI class.")

  # Dynamically create the API call by intercepting method calls
  def __getattribute__(self, name):

    # Try to get the attribute off this object
    try:
      attr = object.__getattribute__(self, name)
      return attr
    except AttributeError, e:
      pass

    api_method = name

    def new_api_method(*args, **kwargs):

      payload = {
        'api_key': self.api_key,
        '%s' % api_method : 1
      }
      payload.update(kwargs)

      log.debug("API call parameters: %s" % payload)
      data = urllib.urlencode({'params' : json.dumps(payload) })

      try:
        req = urllib2.Request("http://www.qidiq.com/api/query", data)
        response = urllib2.urlopen(req)

        # Decode the response as JSON data and return it        
        return json.loads(response.read())
      except urllib2.HTTPError, e:
        print e

    return new_api_method
