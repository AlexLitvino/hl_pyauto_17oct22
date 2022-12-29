from urllib.error import URLError

from Topics.OOP.P7_DesignPatterns.C05_Abstract_factory.connector import Connector
from Topics.OOP.P7_DesignPatterns.C05_Abstract_factory.factories import HTTPFactory, FTPFactory

domain = 'ftp.freebsd.org'
path = '/pub/FreeBSD/'

PROTOCOL = 'HTTP'
IS_SECURE = True

if PROTOCOL == 'HTTP':
    factory = HTTPFactory(is_secure=IS_SECURE)
elif PROTOCOL == 'FTP':
    factory = FTPFactory(is_secure=IS_SECURE)
else:
    raise Exception("Unknown protocol")

connector = Connector(factory)

try:
    content = connector.read(domain, path)
except URLError:
    print("Can't connect to resource")
print(connector.parse(content))
