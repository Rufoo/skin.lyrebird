# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from future import standard_library
standard_library.install_aliases()

#
# Copyright (C) 2015 Philipp Temminghoff
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import xbmc
import xbmcgui
import sys

def main():
	
	info = sys.listitem.getVideoInfoTag()
	dbid = info.getDbId()
	db_type = info.getMediaType()
	remote_id = sys.listitem.getProperty("id")
	BASE = "RunScript(script.extendedinfo,info="
	if not dbid:
		dbid = sys.listitem.getProperty("dbid")
	if db_type == "movie":
		xbmc.executebuiltin("%sextendedinfo,dbid=%s,id=%s,name=%s)" % (BASE, dbid, remote_id, info.getTitle()))
	elif db_type == "tvshow":
		xbmc.executebuiltin("%sextendedtvinfo,dbid=%s,id=%s)" % (BASE, dbid, remote_id))
	elif db_type == "season":
		xbmc.executebuiltin("%sseasoninfo,tvshow=%s,season=%s)" % (BASE, info.getTVShowTitle(), info.getSeason()))
	elif db_type in ["actor", "director"]:
		xbmc.executebuiltin("%sextendedactorinfo,name=%s)" % (BASE, sys.listitem.getLabel()))

home = xbmcgui.Window(10000)
skin=home.getProperty("CurrentSkin")
if skin == "skin.lyrebird.rmod":
	main()
else:
	pass	 



