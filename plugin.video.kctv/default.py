import sys
import xbmcgui
import xbmcplugin

addon_handle = int(sys.argv[1])

xbmcplugin.setContent(addon_handle, 'Korea Central Television')

urls = ['http://121.167.43.161:50000/chosun']
titles = ['Direct KCTV stream']
i=0
while i<len(urls):
	li = xbmcgui.ListItem(titles[i], iconImage='korean_central_tv.jpg')
	xbmcplugin.addDirectoryItem(handle=addon_handle, url=urls[i], listitem=li)
	i=i+1

xbmcplugin.endOfDirectory(addon_handle)
