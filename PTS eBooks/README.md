-------------------------------

# How to Remove Content Using RegEx in Sigil

This guide assumes you've already added your HTML files into Sigil.

1. Double-click into first HTML file
2. Click top line of file
3. Click "Find & Replace"
4. Select "Regex" and "All HTML Files" at the bottom
5. Paste Regex line into "Find" field
6. Select options, if necessary
7. Click "Replace All"
8. Repeat Steps 5-7 for each desired operation

NOTE: Unless otherwise specified, the "Replace" field is always left blank

### Resources for RegEx

* Online RegEx reference and playground: https://regexr.com/
* Excellent text editor that supports RegEx: https://www.sublimetext.com/3

-------------------------------

# Expressions I've Figured Out So Far

### 1. Remove Headers
DotAll = ON | Wrap = ON

`<head>.*<\/head>`


### 2. Remove Homepage line
DotAll = OFF | Wrap = ON

`<p class="ctr"><img.*</p>`


### 3. Remove Nav
DotAll = OFF | Wrap = ON

`<p class="ctr f2">.*</p>`


### 4. Add Sutta # Before Title
DotAll = ON | Wrap = ON

Find:

`(<h4 class="ctr">).*(Sutta \d+)(.*)(<h1>)(.*)<\/h1>`

Replace:

`<h1>\2 - \5</h1>`


### 5. Remove Translation Links
DotAll = OFF | Wrap = ON

`<span class="f3">\[<a .*\]<\/span>`


### 6. Remove Other Text Links (italics still throw some errors)
DotAll = OFF | Wrap = ON

Find:
* a. Italic: `<a href="\.\.\/\.\.\/\.\.\/.*<i>(\w.*)</\i><\/a>`
* b. Regular: `<a href="\.\.\/\.\.\/\.\.\/.*>(\w.*)<\/a>`

Replace:

`\1`


### 7. Remove Inline Images
DotAll = OFF | Wrap = ON

`<p><img src="\..*</p>`


### 8a. Fix CC Licence Links
DotAll = OFF | Wrap = ON

Find:

`(<a href="http:\/\/creativecommons.*>)(<img.*)</a>`

Replace:

`\1Creative Commons Licence</a>`


### 8b. Remove License Details Text
DotAll = OFF | Wrap = ON

`For details see.*Use\.`


### 9. Remove Footers
DotAll = ON | Wrap = ON

`<p class="fine ctr c">.*<\/p>`


### 10. Remove Boilerplate
DotAll = ON | Wrap = ON

`<h4 class="ctr.*<\/h4>`


### 11. Remove Brackets on Endnotes (partially working)
DotAll = OFF | Wrap = ON

Find:

`<sup>\[(.*)\]<\/sup>`

Replace:

`<sup>\1</sup>`


### // 8a? Remove Footers A
DotAll = ON | Wrap = ON

`<p class="ctr"><a href="\.\.\/\.\.\/\.\.\/backmatter.*Statement<\/a><\/p>`


### // 8b? Remove Footers B
DotAll = ON | Wrap = ON

`<p class="fine ctr c">.*Statement<\/p>`


### Fix Most External Links
_(alternative to removal, doesn't work for all though)_

DotAll = OFF | Wrap = ON

Find:

`\.\.\/\.\.\/\.\.\/`

Replace:

`http://www.buddhadust.net/`
