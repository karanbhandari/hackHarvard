
import http.client, urllib.request, urllib.parse, urllib.error, base64


body = {
    "documents": [
        {
            "id": "1",
            "text": "My name is karan"
        },
        {
            "id": "2",
            "text": "Final document. Calling Cognitive API again."
        }
    ]
}

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': 'needToReativateTheKey',
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, str(body), headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

