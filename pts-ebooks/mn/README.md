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

- - -

## MN Issues / Notes

* Sutta 1 has a non-standard footer (addressed by removing manually)
* Sutta 120's "Thus Have I Heard" is formatted strangely (addressed by fixing manually)
* When a Title has an endnote, it appears in the TOC text (addressed by removing manually)

-------------------------------

# Expressions


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

#### Issues

* Sutta 6 is differently formatted at the beginning


### 4a. Rename Note Links
DotAll = OFF | Wrap = ON

Find:

a. `<a id="([fne])` (6654?)
b. `<a href="#([fne])` (54)
c. `a>\]<\/sup>` (6703)

Replace:

a. `<aNOTE id="\1`
b. `<aNOTE href="#\1`
c. `aNOTE>]</sup>`


### 4b. Remove Text Links
DotAll = OFF | Minimal Match = ON | Wrap = ON

`<\/?a(?:(?= )[^>]*)?>` (matches ALL anchor tags) (6888)


### 4c. Restore Note Links
DotAll = OFF | Wrap = ON

Find:

`aNOTE` (13410)

Replace:

`a`

#### Issues with Step 4.
Can be fixed manually in ~2 minutes

* Sutta 22 has a unique "<a id="non-returner">" tag
* Sutta 77 line 3021 has a unique footnote link within the footnote
* Sutta 152 line 517 ''


### 5. Remove Inline Images / Float Boxes (throws error?)
DotAll = ON | Minimal Match = ON | Wrap = ON

`<div class="float[lr](?:pp)?.*<\/div>`
and
`<p><img src="\..*</p>` (DotAll = OFF)


### 6. Remove Footers
DotAll = ON | Wrap = ON

`<p class="fine ctr c">.*<\/p>` (152)


### 7. Remove Boilerplate
DotAll = ON | Minimal Match = ON | Wrap = ON

`<h4 class="ctr.*<\/h4>` (4?)


### 8. Remove Copyright
DotAll = ON | Wrap = ON

`<p class="ctr">.*(?:Use|permission|Chow|Genaud).<\/p>` (160)


### 9. Remove Brackets on Endnotes
DotAll = OFF | Minimal Match = ON | Wrap = ON

Find:

`<sup>\[(.*)\]<\/sup>` (6700)

Replace:

`<sup>\1</sup>`


### 10. Fix "Thus Have I Heard" Bolding

Find:

`T<span class="f2"><b>HUS`

Replace:

`<span class="f2"><b>THUS`


### 11. Change "m" Style

Find:

`ɱ`

Replace:

`ṃ`

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
