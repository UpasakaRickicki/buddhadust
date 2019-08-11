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


### 2. Reformat Titles
DotAll = ON | Minimal Match = OFF | Wrap = ON

Find:

`<h4 class="ctr">.*Sutta (\d+).*>([^>]* Suttaɱ?).*<h1>(.*)<\/h1>`

Replace:

`<h1>\1. \3</h1><h2>\2</h2>`


### 3. Remove Translation Links
DotAll = OFF | Wrap = ON

`<span class="f[34]">[^>]*\[<a .*\]<\/span>`
or
`<span class="f[34]"><[ab].*\]<\/span> ` (include the space at the end) (267)


### 3a. Rename Note Links
DotAll = OFF | Wrap = ON

Find:

a. `<a id="([fne])` (6654?)
b. `<a href="#([fne])` (54)
c. `a>\]<\/sup>` (6703)

Replace:

a. `<aNOTE id="\1`
b. `<aNOTE href="#\1`
c. `aNOTE>]</sup>`


### 3b. Remove Text Links
DotAll = OFF | Minimal Match = ON | Wrap = ON

`<\/?a(?:(?= )[^>]*)?>` (matches ALL anchor tags) (6888)


### 3c. Restore Note Links
DotAll = OFF | Wrap = ON

Find:

`aNOTE` (13410)

Replace:

`a`

#### Issues with Step 3.
Can be fixed manually in ~2 minutes

* Sutta 22 has a unique "<a id="non-returner">" tag
* Sutta 77 line 3021 has a unique footnote link within the footnote
* Sutta 152 line 517 ''


### 4. Remove Inline Images / Float Boxes (throws error?)
DotAll = ON | Minimal Match = ON | Wrap = ON

`<div class="float[lr](?:pp)?.*<\/div>`
and
`<p><img src="\..*</p>` (DotAll = OFF)


### 5. Remove Footers
DotAll = ON | Wrap = ON

`<p class="fine ctr c">.*<\/p>` (152)


### 6. Remove Boilerplate
DotAll = ON | Minimal Match = ON | Wrap = ON

`<h4 class="ctr.*<\/h4>` (4?)


### 7. Remove Copyright
DotAll = ON | Wrap = ON

`<p class="ctr">.*(?:Use|permission|Chow|Genaud).<\/p>` (160)


### 8. Remove Brackets on Endnotes
DotAll = OFF | Minimal Match = ON | Wrap = ON

Find:

`<sup>\[(.*)\]<\/sup>` (6700)

Replace:

`<sup>\1</sup>`

- - -

## MN Exceptions / Bugs / Notes

* Sutta 1 has a non-standard footer (addressed by removing manually)
* Suttas 74 and 112 use "Sutta" instead of "Suttaɱ" (addressed by matching "ɱ" optionally)
* Sutta 78 has the "Middle Length Sayings" underneath the header (addressed by removing boilerplate)
* Suttas 107-10, 118-120, 125 have differently formatted copyright text (addressed in step 7)
* Sutta 120's "Thus Have I Heard" is formatted strangely (addressed by fixing manually)

- - -

## Deprecated / Unused

### 2. Add Sutta # Before Title
DotAll = ON | Minimal Match = OFF | Wrap = ON

Find:

`(<h4 class="ctr">).*(Sutta \d+)(.*)(<h1>)(.*)<\/h1>`

Replace:

`<h1>\2 - \5</h1>`


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