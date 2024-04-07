#
#  JShelter is a browser extension which increases level
#  of security, anonymity and privacy of the user while browsing the
#  internet.
#
#  Copyright (C) 2021  Matus Svancar
#  Copyright (C) 2022  Martin Bednar
#
# SPDX-License-Identifier: GPL-3.0-or-later
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

from values_tested import TestedValues


## Module contains definitions for expected values of default levels od JShelter.
#
#  Expected values are comparing during testing with current values of variables.
#  'REAL VALUE' means that current value should not be spoofed.
#  'EXACTLY' means that current value should not be rounded
#       (the small deviation caused by the script runtime is neglected)
#  This module can be edited when definition of default levels will be changed.


#  Note that we ignore Plugins and mimeTypes tests in Chrome:
#  The Selenium environment modifies the navigator.plugins object inconsistently
#  during the tests. We manually checked that
#  this difference only appears in a browser controlled by Selenium.
#  This issue is not caused by JShield, but by Selenium.
#  So until there is a proper fix, we IGNORE the Plugins and mimeTypes tests in Chrome.


## Expected values for default level 0 of JShelter.
JS_0 = TestedValues(
    addons = 'JShelter=0',
    userAgent={'firefox': 'REAL VALUE',
                'chrome': 'REAL VALUE'},
    appVersion='REAL VALUE',
    platform='REAL VALUE',
    vendor={'firefox': 'REAL VALUE',
            'chrome': 'REAL VALUE'},
    language='REAL VALUE',
    languages='REAL VALUE',
    doNotTrack='REAL VALUE',
    cookieEnabled='REAL VALUE',
    oscpu='REAL VALUE',
    gpsAccuracy={'value': 'REAL VALUE',
                  'accuracy': 'EXACTLY'},
    altitude={'value': 'REAL VALUE',
              'accuracy': 'EXACTLY'},
    altitudeAccurac={'value': 'REAL VALUE',
                      'accuracy': 'EXACTLY'},
    heading={'value': 'REAL VALUE',
             'accuracy': 'EXACTLY'},
    latitude={'value': 'REAL VALUE',
              'accuracy': 'EXACTLY'},
    longitude={'value': 'REAL VALUE',
               'accuracy': 'EXACTLY'},
    speed={'value': 'REAL VALUE',
           'accuracy': 'EXACTLY'},
    timestamp={'value': 'REAL VALUE',
               'accuracy': 'EXACTLY'},
    valid = True,
    deviceMemory={'firefox': 'REAL VALUE',
                 'chrome': 'REAL VALUE'},
    hardwareConcurrency={'value':'REAL VALUE'},
    IOdevices='REAL VALUE',
    #referrer='REAL VALUE',
    time={'value': 'REAL VALUE',
          'accuracy': 'EXACTLY'},
    plugins={'count': {'firefox': 0,
                       'chrome': 'IGNORE'}, # See note above
             'value': {'firefox': 'EMPTY',
                       'chrome': 'IGNORE'}}, # See note above
    mimeTypes='IGNORE', # See note above
    get_channel= 'REAL VALUE',
    get_channel2= '',
    copy_channel= 'REAL VALUE',
    copy_channel2= '',
    byte_time_domain= 'REAL VALUE',
    float_time_domain= 'REAL VALUE',
    byte_frequency= 'REAL VALUE',
    float_frequency= 'REAL VALUE',
    performance={'value': 'REAL VALUE',
                 'accuracy': 'EXACTLY'},
    protectCanvas=False,
    canvasImageData = 'REAL VALUE',
    canvasDataURL = 'REAL VALUE',
    canvasBlob = 'REAL VALUE',
    canvasPointPath = 'REAL VALUE',
    canvasPointStroke = 'REAL VALUE',
    webglParameters = 'REAL VALUE',
    webglPrecisions = 'REAL VALUE',
    webglPixels = 'REAL VALUE',
    webglDataURL = 'REAL VALUE',
    worker = 'REAL VALUE',
    methods_toString='REAL VALUE',
    ECMAarrays = ''
)

## Expected values for default level 1 of JShelter.
JS_1 = TestedValues(
    addons = 'JShelter=1',
    userAgent={'firefox': 'REAL VALUE',
                'chrome': 'REAL VALUE'},
    appVersion='REAL VALUE',
    platform='REAL VALUE',
    vendor={'firefox': 'REAL VALUE',
            'chrome': 'REAL VALUE'},
    language='REAL VALUE',
    languages='REAL VALUE',
    doNotTrack='REAL VALUE',
    cookieEnabled='REAL VALUE',
    oscpu='REAL VALUE',
    gpsAccuracy={'value': 'REAL VALUE',
                  'accuracy': 1},
    altitude={'value': 'REAL VALUE',
              'accuracy': 100},
    altitudeAccurac={'value': 'REAL VALUE',
                      'accuracy': 100},
    heading={'value': 'REAL VALUE',
             'accuracy': 100},
    latitude={'value': 'REAL VALUE',
              # Use accuracy of kilometers. It means maximally +- 0.1 degree from the real position. Look at: https://www.nhc.noaa.gov/gccalc.shtml
              'accuracy': 0.1},
    longitude={'value': 'REAL VALUE',
               # Use accuracy of kilometers. It means maximally +- 0.1 degree from the real position. Look at: https://www.nhc.noaa.gov/gccalc.shtml
               'accuracy': 0.1},
    speed={'value': 'REAL VALUE',
           'accuracy': 100},
    timestamp={'value': 'REAL VALUE',
               'accuracy': 0.001},
    valid = True,
    deviceMemory={'firefox': None,
                   'chrome': 'SPOOF VALUE',
                   'valid_values': {0.25,0.5,1,2,4,8,16,32,64,128,256,512,1024}},
    hardwareConcurrency={'value':'SPOOF VALUE',
                          'valid_values': "UP TO REAL VALUE"},
    IOdevices='REAL VALUE',
    #referrer='REAL VALUE',
    time={'value': 'REAL VALUE',
          'accuracy': 1},
    plugins={'count': {'firefox': 0,
                       'chrome': 'IGNORE'}, # See note above
             'value': {'firefox': 'EMPTY',
                       'chrome': 'IGNORE'}}, # See note above
    mimeTypes='IGNORE', # See note above
    get_channel= 'REAL VALUE',
    get_channel2= '',
    copy_channel= 'REAL VALUE',
    copy_channel2= '',
    byte_time_domain= 'REAL VALUE',
    float_time_domain= 'REAL VALUE',
    byte_frequency= 'REAL VALUE',
    float_frequency= 'REAL VALUE',
    performance={'value': 'REAL VALUE',
                 'accuracy': 1},
    protectCanvas=False,
    canvasImageData = 'REAL VALUE',
    canvasDataURL = 'REAL VALUE',
    canvasBlob = 'REAL VALUE',
    canvasPointPath = 'REAL VALUE',
    canvasPointStroke = 'REAL VALUE',
    webglParameters = 'REAL VALUE',
    webglPrecisions = 'REAL VALUE',
    webglPixels = 'REAL VALUE',
    webglDataURL = 'REAL VALUE',
    worker = 'REMOVED',
    methods_toString='REAL VALUE',
    ECMAarrays = ''
)

## Expected values for default level 2 of JShelter.
JS_2 = TestedValues(
    addons = 'JShelter=2',
    userAgent={'firefox': 'REAL VALUE',
                'chrome': 'REAL VALUE'},
    appVersion='REAL VALUE',
    platform='REAL VALUE',
    vendor={'firefox': 'REAL VALUE',
            'chrome': 'REAL VALUE'},
    language='REAL VALUE',
    languages='REAL VALUE',
    doNotTrack='REAL VALUE',
    cookieEnabled='REAL VALUE',
    oscpu='REAL VALUE',
    gpsAccuracy={'value': 'REAL VALUE',
                  'accuracy': 1},
    altitude={'value': 'REAL VALUE',
              'accuracy': 100},
    altitudeAccurac={'value': 'REAL VALUE',
                      'accuracy': 100},
    heading={'value': 'REAL VALUE',
             'accuracy': 100},
    latitude={'value': 'REAL VALUE',
              # Use accuracy of kilometers. It means maximally +- 0.1 degree from the real position. Look at: https://www.nhc.noaa.gov/gccalc.shtml
              'accuracy': 0.1},
    longitude={'value': 'REAL VALUE',
               # Use accuracy of kilometers. It means maximally +- 0.1 degree from the real position. Look at: https://www.nhc.noaa.gov/gccalc.shtml
               'accuracy': 0.1},
    speed={'value': 'REAL VALUE',
           'accuracy': 100},
    timestamp={'value': 'REAL VALUE',
               'accuracy': 0.001},
    valid = True,
    deviceMemory={'firefox': None,
                   'chrome': 'SPOOF VALUE',
                   'valid_values': {0.25,0.5,1,2,4,8}},
    hardwareConcurrency={'value':'SPOOF VALUE',
                          'valid_values': "UP TO REAL VALUE"},
    IOdevices= {0,1,2,3,4,5,6,7,8,9},
    #referrer='REAL VALUE',
    time={'value': 'REAL VALUE',
          'accuracy': 1},
    plugins={'count': {'firefox': 0,
                       'chrome': 'IGNORE'}, # See note above
             'value': {'firefox': 'EMPTY',
                       'chrome': 'IGNORE'}}, # See note above
    mimeTypes='IGNORE', # See note above
    get_channel= 'SPOOF VALUE',
    get_channel2= '',
    copy_channel= 'SPOOF VALUE',
    copy_channel2= '',
    byte_time_domain= 'SPOOF VALUE',
    float_time_domain= 'SPOOF VALUE',
    byte_frequency= 'SPOOF VALUE',
    float_frequency= 'SPOOF VALUE',
    performance={'value': 'REAL VALUE',
                 'accuracy': 1},
    protectCanvas=False,
    canvasImageData = 'SPOOF VALUE',
    canvasDataURL = 'SPOOF VALUE',
    canvasBlob = 'SPOOF VALUE',
    canvasPointPath = 'SPOOF VALUE',
    canvasPointStroke = 'SPOOF VALUE',
    webglParameters = 'SPOOF VALUE',
    webglPrecisions = 'REAL VALUE',
    webglPixels = 'SPOOF VALUE',
    webglDataURL = 'SPOOF VALUE',
    worker = 'REMOVED',
    methods_toString='REAL VALUE',
    ECMAarrays = ''
)

## Expected values for default level 2 of JShelter.
JS_2_uo = TestedValues(
    addons = 'JShelter=2',
    userAgent={'firefox': 'REAL VALUE',
                'chrome': 'REAL VALUE'},
    appVersion='REAL VALUE',
    platform='REAL VALUE',
    vendor={'firefox': 'REAL VALUE',
            'chrome': 'REAL VALUE'},
    language='REAL VALUE',
    languages='REAL VALUE',
    doNotTrack='REAL VALUE',
    cookieEnabled='REAL VALUE',
    oscpu='REAL VALUE',
    gpsAccuracy={'value': 'REAL VALUE',
                  'accuracy': 1},
    altitude={'value': 'REAL VALUE',
              'accuracy': 100},
    altitudeAccurac={'value': 'REAL VALUE',
                      'accuracy': 100},
    heading={'value': 'REAL VALUE',
             'accuracy': 100},
    latitude={'value': 'REAL VALUE',
              # Use accuracy of kilometers. It means maximally +- 0.1 degree from the real position. Look at: https://www.nhc.noaa.gov/gccalc.shtml
              'accuracy': 0.1},
    longitude={'value': 'REAL VALUE',
               # Use accuracy of kilometers. It means maximally +- 0.1 degree from the real position. Look at: https://www.nhc.noaa.gov/gccalc.shtml
               'accuracy': 0.1},
    speed={'value': 'REAL VALUE',
           'accuracy': 100},
    timestamp={'value': 'REAL VALUE',
               'accuracy': 0.001},
    valid = True,
    deviceMemory={'firefox': None,
                   'chrome': 'SPOOF VALUE',
                   'valid_values': {0.25,0.5,1,2,4,8}},
    hardwareConcurrency={'value':'SPOOF VALUE',
                          'valid_values': "UP TO REAL VALUE"},
    IOdevices= {0,1,2,3,4,5,6,7,8,9},
    #referrer='REAL VALUE',
    time={'value': 'REAL VALUE',
          'accuracy': 1},
    plugins={'count': {'firefox': 0,
                       'chrome': 'IGNORE'}, # See note above
             'value': {'firefox': 'EMPTY',
                       'chrome': 'IGNORE'}}, # See note above
    mimeTypes='IGNORE', # See note above
    get_channel= 'SPOOF VALUE',
    get_channel2= '',
    copy_channel= 'SPOOF VALUE',
    copy_channel2= '',
    byte_time_domain= 'SPOOF VALUE',
    float_time_domain= 'SPOOF VALUE',
    byte_frequency= 'SPOOF VALUE',
    float_frequency= 'SPOOF VALUE',
    performance={'value': 'REAL VALUE',
                 'accuracy': 1},
    protectCanvas=False,
    canvasImageData = 'SPOOF VALUE',
    canvasDataURL = 'SPOOF VALUE',
    canvasBlob = 'SPOOF VALUE',
    canvasPointPath = 'SPOOF VALUE',
    canvasPointStroke = 'SPOOF VALUE',
    webglParameters = 'SPOOF VALUE',
    webglPrecisions = 'REAL VALUE',
    webglPixels = 'SPOOF VALUE',
    webglDataURL = 'SPOOF VALUE',
    worker = 'REMOVED',
    methods_toString='REAL VALUE',
    ECMAarrays = ''
)


## Expected values for default level 3 of JShelter.
JS_3 = TestedValues(
    addons = 'JShelter=3',
    userAgent={'firefox': 'REAL VALUE',
                'chrome': 'REAL VALUE'},
    appVersion='REAL VALUE',
    platform='REAL VALUE',
    vendor={'firefox': 'REAL VALUE',
            'chrome': 'REAL VALUE'},
    language='REAL VALUE',
    languages='REAL VALUE',
    doNotTrack='REAL VALUE',
    cookieEnabled='REAL VALUE',
    oscpu='REAL VALUE',
    gpsAccuracy={'value': "null"},
    altitude={'value': "null"},
    altitudeAccurac={'value': "null"},
    heading={'value': "null"},
    latitude={'value': "null"},
    longitude={'value': "null"},
    speed={'value': "null"},
    timestamp={'value': "null"},
    valid = True,
    deviceMemory={'firefox': None,
                   'chrome': 'SPOOF VALUE',
                   'valid_values': {4}},
    hardwareConcurrency={'value':'SPOOF VALUE',
                          'valid_values': {2}},
    IOdevices= "EMPTY",
    #referrer='REAL VALUE',
    time={'value': 'REAL VALUE',
          'accuracy': 1.0},
    plugins={'count': {'firefox': 0,
                       'chrome': 0}, # Modified by JShelter
             'value': {'firefox': 'EMPTY',
                       'chrome': 'EMPTY'}}, # Modified by JShelter
    mimeTypes='EMPTY', # Modified by JShelter
    get_channel= 'SPOOF VALUE',
    get_channel2= '',
    copy_channel= 'SPOOF VALUE',
    copy_channel2= '',
    byte_time_domain= 'SPOOF VALUE',
    float_time_domain= 'SPOOF VALUE',
    byte_frequency= 'SPOOF VALUE',
    float_frequency= 'SPOOF VALUE',
    performance={'value': 'REAL VALUE',
                 'accuracy': 1},
    protectCanvas=True,
    canvasImageData = 'SPOOF VALUE',
    canvasDataURL = 'SPOOF VALUE',
    canvasBlob = 'SPOOF VALUE',
    canvasPointPath = 'FALSE VALUE',
    canvasPointStroke = 'FALSE VALUE',
    webglParameters = 'ZERO VALUE',
    webglPrecisions = 'ZERO VALUE',
    webglPixels = 'SPOOF VALUE',
    webglDataURL = 'SPOOF VALUE',
    worker = 'REMOVED',
    methods_toString='REAL VALUE',
    ECMAarrays = ''
)

uo = TestedValues(
    addons = 'JShelter=0',
    userAgent={'firefox': 'REAL VALUE',
                'chrome': 'REAL VALUE'},
    appVersion='REAL VALUE',
    platform='REAL VALUE',
    vendor={'firefox': 'REAL VALUE',
            'chrome': 'REAL VALUE'},
    language='REAL VALUE',
    languages='REAL VALUE',
    doNotTrack='REAL VALUE',
    cookieEnabled='REAL VALUE',
    oscpu='REAL VALUE',
    gpsAccuracy={'value': 'REAL VALUE',
                  'accuracy': 'EXACTLY'},
    altitude={'value': 'REAL VALUE',
              'accuracy': 'EXACTLY'},
    altitudeAccurac={'value': 'REAL VALUE',
                      'accuracy': 'EXACTLY'},
    heading={'value': 'REAL VALUE',
             'accuracy': 'EXACTLY'},
    latitude={'value': 'REAL VALUE',
              'accuracy': 'EXACTLY'},
    longitude={'value': 'REAL VALUE',
               'accuracy': 'EXACTLY'},
    speed={'value': 'REAL VALUE',
           'accuracy': 'EXACTLY'},
    timestamp={'value': 'REAL VALUE',
               'accuracy': 'EXACTLY'},
    valid = True,
    deviceMemory={'firefox': 'REAL VALUE',
                 'chrome': 'REAL VALUE'},
    hardwareConcurrency={'value':'REAL VALUE'},
    IOdevices='REAL VALUE',
    #referrer='REAL VALUE',
    time={'value': 'REAL VALUE',
          'accuracy': 'EXACTLY'},
    plugins={'count': {'firefox': 0,
                       'chrome': 'IGNORE'}, # See note above
             'value': {'firefox': 'EMPTY',
                       'chrome': 'IGNORE'}}, # See note above
    mimeTypes='IGNORE', # See note above
    get_channel= 'REAL VALUE',
    get_channel2= '',
    copy_channel= 'REAL VALUE',
    copy_channel2= '',
    byte_time_domain= 'REAL VALUE',
    float_time_domain= 'REAL VALUE',
    byte_frequency= 'REAL VALUE',
    float_frequency= 'REAL VALUE',
    performance={'value': 'REAL VALUE',
                 'accuracy': 'EXACTLY'},
    protectCanvas=False,
    canvasImageData = 'REAL VALUE',
    canvasDataURL = 'REAL VALUE',
    canvasBlob = 'REAL VALUE',
    canvasPointPath = 'REAL VALUE',
    canvasPointStroke = 'REAL VALUE',
    webglParameters = 'REAL VALUE',
    webglPrecisions = 'REAL VALUE',
    webglPixels = 'REAL VALUE',
    webglDataURL = 'REAL VALUE',
    worker = 'REAL VALUE',
    methods_toString='REAL VALUE',
    ECMAarrays = ''
)


JS_3_uo = TestedValues(
    addons = 'JShelter=3',
    userAgent={'firefox': 'REAL VALUE',
                'chrome': 'REAL VALUE'},
    appVersion='REAL VALUE',
    platform='REAL VALUE',
    vendor={'firefox': 'REAL VALUE',
            'chrome': 'REAL VALUE'},
    language='REAL VALUE',
    languages='REAL VALUE',
    doNotTrack='REAL VALUE',
    cookieEnabled='REAL VALUE',
    oscpu='REAL VALUE',
    gpsAccuracy={'value': "null"},
    altitude={'value': "null"},
    altitudeAccurac={'value': "null"},
    heading={'value': "null"},
    latitude={'value': "null"},
    longitude={'value': "null"},
    speed={'value': "null"},
    timestamp={'value': "null"},
    valid = True,
    deviceMemory={'firefox': None,
                   'chrome': 'SPOOF VALUE',
                   'valid_values': {4}},
    hardwareConcurrency={'value':'SPOOF VALUE',
                          'valid_values': {2}},
    IOdevices= "EMPTY",
    #referrer='REAL VALUE',
    time={'value': 'REAL VALUE',
          'accuracy': 1.0},
    plugins={'count': {'firefox': 0,
                       'chrome': 0}, # Modified by JShelter
             'value': {'firefox': 'EMPTY',
                       'chrome': 'EMPTY'}}, # Modified by JShelter
    mimeTypes='EMPTY', # Modified by JShelter
    get_channel= 'SPOOF VALUE',
    get_channel2= '',
    copy_channel= 'SPOOF VALUE',
    copy_channel2= '',
    byte_time_domain= 'SPOOF VALUE',
    float_time_domain= 'SPOOF VALUE',
    byte_frequency= 'SPOOF VALUE',
    float_frequency= 'SPOOF VALUE',
    performance={'value': 'REAL VALUE',
                 'accuracy': 1},
    protectCanvas=True,
    canvasImageData = 'SPOOF VALUE',
    canvasDataURL = 'SPOOF VALUE',
    canvasBlob = 'SPOOF VALUE',
    canvasPointPath = 'FALSE VALUE',
    canvasPointStroke = 'FALSE VALUE',
    webglParameters = 'ZERO VALUE',
    webglPrecisions = 'ZERO VALUE',
    webglPixels = 'SPOOF VALUE',
    webglDataURL = 'SPOOF VALUE',
    worker = 'REMOVED',
    methods_toString='REAL VALUE',
    ECMAarrays = ''
)
