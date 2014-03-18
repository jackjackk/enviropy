# Purpose

This module provides some convenient functions to obtain commonly used paths, like the Dropbox home one.

# Requirements

At the moment only Windows is supported.

# Usage

    import environmentpy as ep
    appdataPath = ep.getEnvironmentVariable("APPDATA")
    dropboxHomePath = ep.getDropboxRoot()

# DISCLAIMER

THIS SOFTWARE IS PRIVIDED "AS IS" AND COMES WITH NO WARRANTY. USE AT YOUR OWN RISK. IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING BUT NOT LIMITED TO LOSS OR CORRUPTION OF DATA). USE AT YOUR OWN RISK.