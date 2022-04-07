# Downloading a web page with the requests.get() function
import requests

# capture a response from this site
res = requests.get('https://research.easyequities.co.za/weekly-dividends-update-4?utm_campaign=Research%20Portal%202017&utm_medium=email&_hsmi=208883129&_hsenc=p2ANqtz--KLHM7jveEV6cVt4fQV-mAiST_5eh0sJzG3I-6CiqIZODtABEfpGc2Q0DCLS_GiF631a_5216z6z95F-9LyY1nENiyzu9fLrPs_0lXHTBLXWHnUos&utm_content=208883129&utm_source=hs_email')

# Error handling
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
    
print(res.status_code)