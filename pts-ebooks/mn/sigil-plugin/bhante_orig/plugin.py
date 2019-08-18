#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
 
import sys 
import re  #for regex


text_type = str 
def run(bk):  
    for (id, href) in bk.text_iter():  #For each html file in the 'text' section of the epbu   
        print('Chapter found %s:' % href) #Print the section name   
        html = bk.readfile(id)   #Read the section into html   
        if not isinstance(html, text_type): #If the section is not str    
            html = text_type(html, 'utf-8') #then sets its type to 'utf-8'   

        html_orig = html     #Copy the text to html_orig 
 
        html = re.sub(r'<head>.*Sections<\/a>]<\/p>',r'<head></head><body>', html,0,re.DOTALL) 
        html = re.sub(r'<h4 class="ctr">.*Sutta (\d+).*>([^>]* Suttaṃ?).*<h1>(.*)<\/h1>',r'<h1>\1. \3</h1><h2>\2</h2>', html,0,re.DOTALL) 
        html = re.sub(r'<span class="f[34]"><[ab].*\]<\/span> ',r'', html) 
        html = re.sub(r'<span class="f[34]">[^>]*\[<a .*\]<\/span>',r'', html) 
   #     html = re.sub(r'<p class="ctr">.*(?:Use|permission|Chow|Genaud).<\/p>',r'', html, 0, re.DOTALL) 
        
 
        if not html == html_orig:   #If the text has changed         
            bk.writefile(id, html)   #Write the amended text to the book 
            
    return 0    # 0 - means success, anything else means failure  


def main():     
    print ("I reached main when I should not have\n")     
    return -1      
if __name__ == "__main__":     
    sys.exit(main()) 
 