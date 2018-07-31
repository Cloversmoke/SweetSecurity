import hashlib


def getHash(fileName):
    if fileName == 'elasticsearch-6.3.2.deb':
        return 'A53A77652AAA85FA04F1D382D3391E921A7E9A6A'
    elif fileName == 'kibana-6.3.2-linux-x86_64.tar.gz':
        return '34EE24FEC22FA00A349A1FD1CDA3855B3432A08A'
    elif fileName == 'kibana-6.3.2-linux-x86.tar.gz':
        return '47d7707b1b8feb490276fd69b597d27af610d28b'
    elif fileName == 'logstash-6.3.2.deb':
        return 'B4BB7B6F4041634B6A3FED551DB3ED260863D608'
    elif fileName == 'bro-2.5.4.tar.gz':
        return 'DF170B6626F43753B610C0A8DE8D085DEE4EE0B4'
    return ''

def checkHash(fileName):
    BUF_SIZE = 65536
    sha1 = hashlib.sha1()
    with open(fileName, 'rb') as file:
        while True:
            data = file.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
    sha1=sha1.hexdigest()
    if sha1 == getHash(fileName):
        return True
    else:
        return False