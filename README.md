# Sublime Text 2 EmotiCODE Plugin

A plugin to search and **Submit** on [EmotiCODE](http://www.emoticode.net) .

# How to Submit A Snippet
***Tested on ST3***   

edit `emoticode.ini` 

```
[CREDS]
username = YOUR_USERNAME
password = YOUR_PASSWORD

[PATH]
cache_path = /tmp/cache.txt #Your selection will be saved here
submit_script_path = /path/to/submit.py #The path to submit.py
python_path = /usr/bin/env python

[VAR]
title = 
description = 
language =
private = 
```

**Added private option:** When prompted; ``y`` for private, anything else is not.
***  

> You will need to select ```Input Metadata``` before you ```Submit to EmotiCODE```  

![Alt text](http://sysbase.org/preview.png "Optional title")

***

> As to `Language` codes; I will work on instant translation, until then:
```
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
```

***





***

# License

All of Sublime Text 2 EmotiCODE Plugin is licensed under the MIT license.

Copyright (c) 2013 Simone Margaritelli <evilsocket@gmail.com> - <http://www.evilsocket.net>

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.