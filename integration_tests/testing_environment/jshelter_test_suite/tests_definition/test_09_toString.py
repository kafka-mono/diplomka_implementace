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

## Setup method - it is run before toString tests execution starts.
#
#  This setup method initialize variable methods_toString that contains methods.toString() and
#  this variable is provided to methods_toString test and the methods.toString() in the variable are compared with real values.
## Test methods.toString(). They should be always unchanged by JShelter.
def test_methods_toString(noaddon, jsrun):
	for method in jsrun.methods_toString:
		assert jsrun.methods_toString[method] == noaddon.methods_toString[method]
