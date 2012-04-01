import re

def urldecode(url):
    """
    Decode an encoded url.
    
    Usage: 
    url = 'http://www.example.com/this%20is%20my%20test%20%26%20%23%24'
    decoded_url = urldecode(url)
    """
    if url.find(" ") == -1:
        url = url.replace("+", " ")
        
    p = re.compile("%(?=[0-9A-F]{2})")
    
    plist = p.split(url)
    if len(plist) > 1:
        for i in range(1, len(plist)):
            plist[i] = '%s%s' % (chr(int((plist[i])[:2], 16)), (plist[i])[2:])
        
        decoded_url = ''.join(plist)
        
        return decoded_url
    return url
