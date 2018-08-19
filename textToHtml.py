import re
import os




def text_to_html ():
    file_start = '<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml">\n'
    fp = open('rime.txt', 'r')
    fw = open('rime.html', 'w')

    fisrt_line =fp.readline()
    start_text = re.findall('.*[^\n]',fisrt_line)

    title = '  <title>' + start_text[0] + '</title>'

    first = file_start + '<head>\n' + title + '\n  <meta charset="utf-8"/>\n' +'</head>\n'

    fw.write(first)
    fw.write('<body>\n')
    h1 = '<h1>' + start_text[0] + '</h1>\n'
    fw.write(h1)
    fw.write(start_text[0]+'\n')

    h2List = ['ARGUMENT.', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII']
    regex_h2list = ['^A.{6}T\.$', '^[I?V?]{1,3}\.$']
    regex_plist = ['^How.*Country\.$']
    h2Count = 0
    while(True):

        text = fp.readline()

        if (text == ''):
            break

        if re.findall(regex_h2list[0],text):
            h2 = re.findall(regex_h2list[0],text)

            h2 = '<h2>' + h2[0] + '</h2>\n'
            fw.write(h2)
            h2Count +=1

        if re.findall(regex_h2list[1],text):
            h2 = re.findall(regex_h2list[1], text)
            h2 = '<h2>' + h2[0] + '</h2>\n'
            fw.write(h2)
            h2Count +=1

        if re.findall(regex_plist[0],text):
            p = re.findall(regex_plist[0],text)
            p = '<p>' + p[0] + '</p>\n'
            fw.write(p)

        if h2Count >= 2 and not (re.findall(regex_h2list[1],text)):
            input= text[:-1] + '</br>\n'
            fw.write(input)

    fw.write('</p></body>\n')

    fw.write('</html>\n')
    fp.close()
    fw.close()

text_to_html()