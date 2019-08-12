## Digha Nikaya

-------------------------------

# How to Reformat Content Using RegEx in Sigil

This guide assumes you've already added your HTML files into Sigil.

1. Double-click into first HTML file
2. Click top line of file
3. Click "Find & Replace"
4. Select "Regex" and "All HTML Files" at the bottom
5. Paste Regex line into "Find" field
6. Select options, if necessary
7. Click "Replace All"
8. Repeat Steps 5-7 for each desired operation

NOTE: Unless specified, the "Replace" field is left blank

### Resources for RegEx

* Online RegEx reference and playground: https://regexr.com/
* Excellent text editor that supports RegEx: https://www.sublimetext.com/3

-------------------------------

# DN Reformatting Notes

* Sutta 2/3 has an appendix that doesn't seem to fit
* Sutta 33 has several separate files, intro needs to be dragged to beginning, Subtitles need to be manually combined

-------------------------------

# DN Reformatting Expressions


### 1. Remove Headers + Homepage Line + Nav
DotAll = ON | Wrap = ON

Find:

`<head>.*Sections<\/a>]<\/p>`

Replace:

`<head></head><body>`



### 2. Reformat Titles
DotAll = ON | Minimal Match = ON | Wrap = ON

Find:

`<h4 class="ctr">.*Sutta (\d++).*>([^>]* Suttan?t?a?ɱ?).*<h1>(.*)<\/h1>`

Replace:

`<h1>\1. \3</h1><h3>\2</h3>`


#### Issues

* When there's an Introduction, the `<h1>` titles appear twice
	* solution: modify h-level of intro and sutta title
	* caveat: sometimes the 2nd instance of the Pali sutta title is missing, so cannot be used for TOC

Find: `<h4.*Introduction.*<\/h4>` or `<h4 [^ ]*Introduction.*<\/h4>` (DotAll = ON)
Replace: `<h2>Introduction</h2>`

Find: `<h4[^<]*>(.*Sutta)<\/h4>`
or
Find: `<h4[^<]*>[XVI]+\. (.*Sutta)<\/h4>` (strips Roman numerals for Sutta #) Minimal OFF DotAll OFF
or
Find: `<h4[^<]*>[XVI]+\. (.*Suttan?n?t?a?).*<\/h4>` (multi-line, for Sutta 26) DA = ON | M = OFF
Replace: `<h2>\1</h2>`

##### (decrements second title's header level) Minimal OFF DotAll OFF

Find: `<h1>([^\d<]*)<\/h1>` !misses when title has a footnote link
Replace: `<h3>\1</h3>`


### 3. Remove Translation Links
DotAll = OFF | Wrap = ON

`<span class="f[34]">\[?<[ab].*\]<\/span> ` (include the space at the end)

#### Issues




### 4a. Rename Note Links
DotAll = OFF | Wrap = ON

Find:

a. `<a id="([fne])` (3528)
b. `<a href="#([fne])` (8)
c. `a>\]<\/sup>` (3435)

Replace:

a. `<aNOTE id="\1`
b. `<aNOTE href="#\1`
c. `aNOTE>]</sup>`


### 4b. Remove Text Links
DotAll = OFF | Minimal Match = ON | Wrap = ON

`<\/?a(?:(?= )[^>]*)?>` (matches ALL anchor tags) (4715)


### 4c. Restore Note Links
DotAll = OFF | Wrap = ON

Find:

`aNOTE` (6971)

Replace:

`a`

#### Issues

* 


### 5. Remove Inline Images / Float Boxes
DotAll = ON | Minimal Match = ON | Wrap = ON

`<div class="float[lr](?:pp)?.*<\/div>` (49)


### 6. Remove Footers
DotAll = ON | Minimal Match = ON | Wrap = ON

a. `<p class="fine ctr c">.*<\/p>` (46)
b. `<hr\/>.*\[Contents \].*<\/p>` ?

#### Issues

* Suttas 1-13 have extra nav in footer


### 7. Remove Boilerplate (modify or omit)
DotAll = ON | Minimal Match = ON | Wrap = ON

`<h4 class="ctr.*<\/h4>` (4?)


### 8. Remove Copyright
DotAll = ON | Wrap = ON

`<p class="ctr">.*(?:Oxford)<\/p>` (41)


### 9. Remove Brackets on Endnotes
DotAll = OFF | Minimal Match = ON | Wrap = ON

Find:

`<sup>\[(.*)\]<\/sup>` (3437)

Replace:

`<sup>\1</sup>`


### 10. Fix "Thus Have I Heard" Bolding (remove?)

Find:

`T<span class="f2"><b>HUS`

Replace:

`<span class="f2"><b>THUS`


### 11. Change "m" and "n" Style

Find:

a. `ɱ`
b. `ŋ`

Replace:

a. `ṃ`
b. `ṅ`


- - -

## Deprecated / Unused


