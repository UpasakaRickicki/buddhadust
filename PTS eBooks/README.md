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


### 1. Remove Headers + Homepage Line + Nav
DotAll = ON | Wrap = ON

Find:

`<head>.*Sections<\/a>]<\/p>`

Replace:

`<head></head><body>`


### 2. Add Sutta # Before Title
DotAll = ON | Minimal Match = OFF | Wrap = ON

Find:

`(<h4 class="ctr">).*(Sutta \d+)(.*)(<h1>)(.*)<\/h1>`

Replace:

`<h1>\2 - \5</h1>`


### 3. Remove Translation Links
DotAll = OFF | Wrap = ON

`<span class="f[34]">\[<a .*<\/span>`


### 3a. Rename Note Links
DotAll = OFF | Wrap = ON

Find:

a. `<a id="([fne])`
b. `<a href="#([fne])`
c. `a>\]<\/sup>`

Replace:

a. `<aNOTE id="\1`
b. `<aNOTE href="#\1`
c. `aNOTE>]</sup>`


### 3b. Remove Text Links
DotAll = OFF | Minimal Match = ON | Wrap = ON

`<\/?a(?:(?= )[^>]*)?>` (matches ALL anchor tags)


### 3c. Restore Note Links

Find:

`aNOTE`

Replace:

`a`


### 4. Remove Inline Images / Float Boxes
DotAll = OFF | Wrap = ON

`<div class="floatrpp.*<\/div>`
or
`<p><img src="\..*</p>`


### 5. Remove Footers
DotAll = ON | Wrap = ON

`<p class="fine ctr c">.*<\/p>`


### 6. Remove Boilerplate
DotAll = ON | Wrap = ON

`<h4 class="ctr.*<\/h4>`


### 7. Remove Copyright
DotAll = ON | Wrap = ON

`<p class="ctr">Translated.*Use.<\/p>`


### 8. Remove Brackets on Endnotes
DotAll = OFF | Minimal Match = ON | Wrap = ON

Find:

`<sup>\[(.*)\]<\/sup>`

Replace:

`<sup>\1</sup>`

- - -

## Deprecated / Unused

### 8a. Fix CC Licence Links
DotAll = OFF | Wrap = ON

Find:

`(<a href="http:\/\/creativecommons.*>)(<img.*)</a>`

Replace:

`\1Creative Commons Licence</a>`


### 8b. Remove License Details Text
DotAll = OFF | Wrap = ON

`For details see.*Use\.`


### 1. Remove Headers
DotAll = ON | Wrap = ON

`<head>.*<\/head>`


### 2. Remove Homepage line
DotAll = OFF | Wrap = ON

`<p class="ctr"><img.*</p>`


### 3. Remove Nav
DotAll = OFF | Wrap = ON

`<p class="ctr f2">.*</p>`


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
