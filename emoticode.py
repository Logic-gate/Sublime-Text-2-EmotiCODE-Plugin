import sublime, sublime_plugin
import subprocess
import webbrowser
import configparser
import os

p = str(os.path.dirname(os.path.abspath(__file__)))
def PerformSearch(text):
  if len(text):
    url = 'http://www.emoticode.net/search/' +  text.replace(' ','%20')
    webbrowser.open_new_tab(url)


def writeConfig(string, var):
  config = configparser.RawConfigParser()
  config.read(str(p)+'/emoticode.ini')
  config.set("VAR", string, var)
  with open(str(p)+'/emoticode.ini', 'w') as configfile:
    config.write(configfile)


def readConfig():
  config = configparser.ConfigParser()
  config.read(str(p)+'/emoticode.ini')
  username = config.get("CREDS", 'username')
  password = config.get("CREDS", "password")
  cache = config.get("PATH", "cache_path")
  script = config.get("PATH", "submit_script_path")
  python = config.get("PATH", "python_path")
  title = config.get("VAR", "title")
  desc = config.get("VAR", "description")
  lang = config.get("VAR", "language")
  private = config.get("VAR", "private")
  return username, password, cache, script, python, title, desc, lang, private


class EmoticodeSearchSelectionCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    for selection in self.view.sel():
      if selection.empty():
          text = self.view.word(selection)

      text = self.view.substr(selection).strip()

      PerformSearch(text)

class EmoticodeSearchInputCommand(sublime_plugin.WindowCommand):
    def run(self):
      self.window.show_input_panel('Search EmotiCODE for', '', self.on_done, self.on_change, self.on_cancel)

    def on_done(self, input):
      PerformSearch(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass

class EmoticodeSubmitInputDataCommand(sublime_plugin.WindowCommand):

    def run(self):
        self.window.show_input_panel('Title', '', self.desc, self.on_change, self.on_cancel)

    def desc(self, input):
        writeConfig('title', input)
        self.window.show_input_panel('Description', '', self.lang, self.on_change, self.on_cancel)
    def lang(self, input):
        writeConfig('description', input)
        self.window.show_input_panel('Language', '', self.private, self.on_change, self.on_cancel)

    def private(self, input):
        writeConfig('language', input)
        self.window.show_input_panel('Private', '', self.on_done, self.on_change, self.on_cancel)

    def on_done(self, input):
        writeConfig('private', input)
        submit()
    def on_change(self, input):
        pass

    def on_cancel(self):
        pass

class EmoticodeSubmitSelectionCommand(sublime_plugin.TextCommand):

  def run(self, edit):
    for selection in self.view.sel():
      if selection.empty():
          text = self.view.word(selection)

      text = self.view.substr(selection).strip()
      username = readConfig()[0]
      password = readConfig()[1]
      cache = readConfig()[2]
      script = readConfig()[3]
      python_path = readConfig()[4]
      title = readConfig()[5]
      desc = readConfig()[6]
      lang = readConfig()[7]
      private = readConfig()[8]
      if private == 'y':
        print(python_path+' '+script+' -u '+username+' -p '+password+' -d '+desc+' -t '+title+ ' -l '+lang+' -s '+cache+' -pr '+private)
        p = open(cache, 'w+')
        p.write(text)
        p.close()
        os.system(python_path+' '+script+' -u '+username+' -p '+password+' -d '+"'"+desc+"'"+' -t '+"'"+title+"'"+' -l '+lang+' -s '+cache+' -pr '+private)
      else:
        p = open(cache, 'w+')
        p.write(text)
        p.close()
        os.system(python_path+' '+script+' -u '+username+' -p '+password+' -d '+"'"+desc+"'"+' -t '+"'"+title+"'"+' -l '+lang+' -s '+cache)

      

     