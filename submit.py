#!/usr/bin/env python


'''CLI emoticode "Code" submitter'''
'''Original idea by v3nw http://www.emoticode.net/python/emoticode-net-post-your-snippet.html'''

__author__ = ["A'mmer Almadani:Mad_Dev", "penbang.sysbase.org"]
__email__  = ["mad_dev@linuxmail.org", "mail@sysbase.org"]
__credits__ = ['v3nw', 'http://www.emoticode.net/python/emoticode-net-post-your-snippet.html']

import mechanize
import argparse
import sys

'''
'ActionScript' = 171 
'ActionScript 3' = 172
'Ada' = 257
'Android SDK' = 255
'Apache' = 174
'AppleScript' = 175
'ASP' = 176
'Assembler' = 177
'AutoIt' = 178
'Awk' = 179
'Bash' = 180
'C' = 181
'C#' = 183
'C++' = 182
'Clojure' = 184
'CoffeeScript' = 259
'ColdFusion' = 185
'CSS' = 186
'Delphi' = 187
'Diff' = 188
'Django' = 189
'DOS Batch' = 190
'Emacs Lisp' = 191
'eZ Publish' = 192
'Falcon' = 256
'Forth' = 193
'Fortran' = 194
'Gnuplot' = 195
'Groovy' = 196
'HAML' = 197
'Haskell' = 198
'HTML' = 199
'iPhone' = 200
'Java' = 201
'JavaScript' = 202
'jQuery' = 203
'LaTeX' = 204
'lighttpd' = 205
'Lisp' = 206
'Lua' = 207
'Makefile' = 208
'MatLab' = 209
'Maxscript' = 210
'Mel' = 211
'MXML' = 212
'MySQL' = 213
'NewtonScript' = 214
'Objective C' = 215
'Open Firmware' = 216
'Other' = 217
'Pascal' = 218
'Perl' = 219
'PHP' = 220
'PicBasic' = 221
'PL/SQL' = 222
'Processing' = 223
'Prolog' = 224
'Pseudocode' = 225
'Python' = 226
'R' = 227
'Rails' = 228
'Regular Expression' = 229
'Revolution' = 230
'Ruby' = 231
'SAS' = 232
'SASS' = 233
'Scala' = 234
'Scheme' = 235
'SmallTalk' = 236
'Smarty' = 237
'SML' = 238
'SPSS' = 239
'SQL' = 240
'SVN' = 241
'Symfony' = 242
'TCL' = 243
'Textpattern' = 244
'TYPO3' = 245
'VB.NET' = 246
'VHDL' = 247
'VIM' = 258
'Visual Basic' = 248
'W-Language' = 249
'Windows PowerShell' = 250
'Windows Registry' = 251
'XHTML' = 252
'XML' = 253
'XSLT' = 254
'''

def getUserInput():
	try:
		title = raw_input('Title: ')
		desc = raw_input('Description:\n')
		lang = raw_input('Language: ')
		code_in = raw_input('Snippet Path: ')
		code = open(code_in).read()
		return title, desc, lang, code
	except KeyboardInterrupt:
			sys.exit('\nExit')


def submit(title, desc, lang, code, username, password, private):
	myBrowser = mechanize.Browser()
	myBrowser.set_handle_robots(False)
	myBrowser.open('http://www.emoticode.net/sign_in')
	myBrowser.form = list(myBrowser.forms())[0]
	myBrowser['session[who]'] = username
	myBrowser['session[password]'] = password
	myBrowser.submit()
	myBrowser.open('http://www.emoticode.net/source/new')
	myBrowser.form = list(myBrowser.forms())[0]
	myBrowser['source[description]'] = desc 
	myBrowser['source[language_id]'] = [lang]
	myBrowser['source[title]'] = title
	myBrowser['source[text]'] = str(code)
	if private == 'y':
		for i in range(0, len(myBrowser.find_control(type="checkbox").items)):
			myBrowser.find_control(type="checkbox").items[i].selected =True
		myBrowser.submit()
	else:
		myBrowser.submit()

if __name__ == '__main__':
	par = argparse.ArgumentParser(prog=__file__, formatter_class=argparse.ArgumentDefaultsHelpFormatter, 
		epilog="Thanks to v3nw for the orginal code and idea", description='EmotiCode Snippet Sumbitter')
	par.add_argument('-d',  required=False, help="Description", metavar='description')
	par.add_argument('-l',  help="Language | Check Source Code for Correct int", metavar='language')
	par.add_argument('-t',  help="Titile", metavar='title')
	par.add_argument('-s',  required=False, help="Snippet | path", metavar='Snippet')
	par.add_argument('-u',  required=True, help="Username", metavar='username')
	par.add_argument('-p',  required=True, help="Password", metavar='password')
	par.add_argument('-pr', help="Private | y | default: no", metavar='private')
	
	argvs = par.parse_args()
	if len(sys.argv) == 1:
		i = getUserInput()
		submit(i[0], i[1], i[2], i[3])
		#print i[0], i[1], i[2], i[3]
		sys.exit()

	elif len(sys.argv) > 1:
		title = argvs.t
		desc = argvs.d
		username = argvs.u
		password = argvs.p
		private = argvs.pr
		if argvs.l is not None:
			lang = argvs.l
		else:
			raise 'Language must be stated'
		if argvs.s is not None:
			code = open(argvs.s).read()
		else:
			raise 'Snippet must be stated'
		submit(title, desc, lang, code, username, password, private)
		#print title, desc, lang, code

	