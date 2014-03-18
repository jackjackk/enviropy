import base64
import ctypes
import os
import re

def getEnvironmentVariable(name):
    """
    All credits to:
    Martin Miller (http://stackoverflow.com/users/355230/martineau)
    http://stackoverflow.com/questions/12118162/how-can-i-get-the-dropbox-folder-location-programmatically-in-python
    """
    """ read windows native unicode environment variables """
    # (could just use os.environ dict in Python 3)
    name = unicode(name) # make sure string argument is unicode
    n = ctypes.windll.kernel32.GetEnvironmentVariableW(name, None, 0)
    if not n:
        return None
    else:
        buf = ctypes.create_unicode_buffer(u'\0'*n)
        ctypes.windll.kernel32.GetEnvironmentVariableW(name, buf, n)
        return buf.value

def getDropboxRoot():
    """
    All credits to:
    Martin Miller (http://stackoverflow.com/users/355230/martineau)
    http://stackoverflow.com/questions/12118162/how-can-i-get-the-dropbox-folder-location-programmatically-in-python
    """
    # find the path for Dropbox's root watch folder from its sqlite host.db database.
    # Dropbox stores its databases under the currently logged in user's %APPDATA% path.
    # If you have installed multiple instances of dropbox under the same login this only finds the 1st one.
    # Dropbox stores its databases under the currently logged in user's %APPDATA% path.
    # usually "C:\Documents and Settings\<login_account>\Application Data"
    sConfigFile = os.path.join(getEnvironmentVariable("APPDATA"),
                               'Dropbox', 'host.db')

    # return null string if can't find or work database file.
    if not os.path.exists(sConfigFile):
        return None

    # Dropbox Watch Folder Location is base64 encoded as the last line of the host.db file.
    with open(sConfigFile) as dbxfile:
        for sLine in dbxfile:
            pass

    # decode last line, path to dropbox watch folder with no trailing slash.
    return base64.b64decode(sLine)

def getGoogleDriveRoot():
    sConfigFile = os.path.join(getEnvironmentVariable('LOCALAPPDATA'), 'Google/Drive/sync_config.db')
    sGoogleDriveDir = None
    with open(sConfigFile) as dbxfile:
        for sLine in dbxfile:
            m = re.search('\\\\\?\\\\(.*Google Drive)', sLine)
            if m != None:
                sGoogleDriveDir = m.group(1)
                break
    return sGoogleDriveDir
    # sqlite3 approach requires newest version of pysqlite
    # conn = sqlite3.connect(dbFilePath)
    # c = conn.cursor()
    # for row in c.execute("select * from data where entry_key='local_sync_root_path'"):
    #     print row
    # conn.close()
