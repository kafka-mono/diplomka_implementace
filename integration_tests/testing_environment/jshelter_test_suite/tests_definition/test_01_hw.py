#
#  JShelter is a browser extension which increases level
#  of security, anonymity and privacy of the user while browsing the
#  internet.
#
#  Copyright (C) 2021  Martin Bednar
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

## Setup method - it is run before hw tests execution starts.
#
#  This setup method initialize variable device that contains current data about device and
#  this variable is provided to device tests and values in device variable are compared with expected values.



## Test device memory.
def test_device_memory(noaddon, jsrun, expected, browser):
	if noaddon.device.deviceMemory == "null" and jsrun.device.deviceMemory == "null":
		return # This browser does not support deviceMemory so JShelter should not spoof that value
	elif noaddon.device.deviceMemory == "null":
		assert jsrun.device.deviceMemory == "null"
	if expected.device.deviceMemory[browser] == 'SPOOF VALUE':
		assert jsrun.device.deviceMemory in expected.device.deviceMemory['valid_values']
		assert jsrun.device.deviceMemory <= noaddon.device.deviceMemory
	else:
		assert jsrun.device.deviceMemory == noaddon.device.deviceMemory


## Test hardware concurrency.
def test_hardware_concurrency(noaddon, jsrun, expected):
	if expected.device.hardwareConcurrency['value'] == 'REAL VALUE':
		assert jsrun.device.hardwareConcurrency == noaddon.device.hardwareConcurrency
	elif expected.device.hardwareConcurrency['value'] == 'SPOOF VALUE':
		expectedval = expected.device.hardwareConcurrency['valid_values']
		if expectedval == "UP TO REAL VALUE":
			expectedval = range(noaddon.device.hardwareConcurrency + 1)
		assert jsrun.device.hardwareConcurrency in expectedval
	else:
		assert False # We should not get here


## Test IOdevices.
def test_IOdevices(noaddon, jsrun, expected):
	if expected.device.IOdevices == 'REAL VALUE':
		assert len(jsrun.device.IOdevices) == len(noaddon.device.IOdevices)
		for i in range(len(jsrun.device.IOdevices)):
			assert jsrun.device.IOdevices[i]['kind'] == noaddon.device.IOdevices[i]['kind']
	elif expected.device.IOdevices == 'EMPTY':
		if jsrun.device.IOdevices == 'ERROR':
			assert jsrun.device.IOdevices == 'ERROR'
		else:
			assert jsrun.device.IOdevices == []
			assert len(jsrun.device.IOdevices) == 0
	else:
		assert len(jsrun.device.IOdevices) in expected.device.IOdevices
