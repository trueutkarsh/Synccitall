import mechanize

br=mechanize.Browser()

br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)
base=br.open('http://google.com')
html=base.read()
print (html)