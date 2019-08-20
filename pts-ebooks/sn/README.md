## Samyutta Nikaya

-------------------------------

### How to Reformat Content Using RegEx in Sigil

This guide assumes you've already added your HTML files into Sigil.

1. Double-click into first HTML file
2. Click top line of file
3. Click "Find & Replace"
4. Select "Regex" and "All HTML Files" at the bottom
5. Paste Regex line into "Find" field
6. Select options, if necessary
7. Click "Replace All"
8. Repeat Steps 5-7 for each desired operation

NOTE: Unless specified, the "Replace" field is left blank and "Wrap" is always ON

### Resources for RegEx

* Online RegEx reference and playground: https://regexr.com/
* Excellent text editor that supports RegEx: https://www.sublimetext.com/3

-------------------------------

# SN Reformatting Notes

* 


# Build Steps

1. Re-order Suttas
2. Run expressions
3. Build TOC, removing items and endnote numbers
4. Add HTML TOC
5. Add Cover

-------------------------------

# SN Reformatting Expressions


### 1. Change "m" and "n" Style
DotAll = OFF

Find:

a. `ɱ`
b. `ŋ`

Replace:

a. `ṃ`
b. `ṅ`


### 2. Remove Headers + Homepage Line + Nav
DotAll = ON

Find:

`<head>.*(?=<div class="main">)`

Replace:

`<head><title></title></head><body>`



### 3. Reformat Titles





### 4. Remove Translation Links
DotAll = OFF | Wrap = ON

`<span class="f[34]">\[?<[ab].*\]<\/span> ` (include the space at the end) (4365)



### 5a. Rename Note Links
DotAll = OFF

Find:

`(<sup>.*<)(a)(.*\/)(a)>(?=.*<\/sup>)`

Replace:

`\1aNOTE\3aNOTE>`


### 5b. Remove Text Links
DotAll = OFF | Minimal Match = ON | Wrap = ON

`<\/?a(?:(?= )[^>]*)?>`



### 6c. Restore Note Links
DotAll = OFF | Wrap = ON

Find:

`aNOTE` (21670)

Replace:

`a`


### 7. Remove Inline Images / Float Boxes
DotAll = ON

`<div class="float[lr](?:pp)?.*?<\/div>`


### 8. Remove Footers
DotAll = ON


Find `<p class="fine ctr c">.*<\/p>`



### 10. Remove Copyright
DotAll = ON

Find:

`<p class="(?:c|f)[^>]*?>Translated.*?(?:Use\.|Domain)<\/p>`



### 11. Remove Brackets on Endnotes
DotAll = OFF

Find:

`<sup>.*?)\[(.*?)\](.*?<\/sup>`

Replace:

`\1\2\3`



- - -

## Deprecated / Unused


### 12. Fix "Thus Have I Heard" Bolding (remove?)

Find:

`T<span class="f2"><b>HUS`

Replace:

`<span class="f2"><b>THUS`


### 9. Remove Boilerplate before title (do not use?)
DotAll = ON | Minimal Match = ON | Wrap = ON

`<h4.*Aṅguttar.*Suttas.*h2>`

or

Find: `<h4.*Aṅguttar.*Suttas.*([XVI]+)` Replace: `<h4>\1` 
(strips everything before the roman numerals of the Book title)

#### Issues

* Roman numeral use before title is inconsistent


### 3b. Promote Suttas H4s to H2
DotAll = OFF

Find:

`(?:<h4)(.*Suttas.*)(?:h4>)` (Works, but a couple of headers have additional text)

Replace:

`<h2\1h2>`


### 3c. Promote individual Sutta headers to H2
DotAll = OFF

Find: `(?:<h4)(.*Sutta \d+.*)(?:h4>)`
Replace: `<h2\1h2>`
