Regular Expressions: ain't nothing regular about them
=======

Introduction
-------
The term regular expression comes from a mathematical concept called regular
sets long lost to history. These days, all you need to know is that regular
expressions are a language that lets you do complex text searches. It's easier
to start with a demonstration:
```
The pattern "aard" will match (and find) all words in a piece of text that
contains that exact letter sequence. If you run this pattern on a
dictionary, you get:
    => aardwolf
    => aardvark
```
Regular expressions give you wildcards, allowing you to do the following search:
````
The pattern "h.t" will find all words starting with "h", followed by any
single character (or digit), followed by the letter "t":
    => hit
    => hot
    => hat
    => hut
```
You can also constrain your wildcards to match specific letters:
```
The pattern "[ghm][aeiou][aeiou]se" will match any word that begins with a
"g", "h", or "m", followed by any single vowel, followed by another vowel,
followed by the letters "se".
    => geese
    => goose
    => mouse
    => moose
    => house
    => guise
```
The most basic use of regular expression is as a plain text search, like you
might find in a word processor, but regex (as it is called) is a powerful
language that can do much more due to the ability to pattern match. Possibly
the most common use of a regular expression is scraping: extracting information
from a text document: an appropriate use of regular expressions is to find all
email addresses in an html file.

"The internet always misquotes me" -- Abraham Lincoln


Description
-------
Go through the exercises on [RegexOne](http://RegexOne.com). It will sometimes let you pass without actually satisfying the conditions, so make sure you're as thorough as possible.

If you complete them all, write regular expressions to find the following
patterns. Use egrep on the included word file.  Pipe your output (using |) to the 'wc' command to get a line count.

    From the file 'words'
    1. All the words that begin with the letter a, independent of case (17096 words)
    2. All the words that contain the sequence 'ing' (8852 words)
    3. All the words end in the sequence 'ing' (5539 words)
    4. All the words exactly 7 letters long (23869 words)
    5. All words with two adjacent 'a's (124 words)
    6. All words that end in either 'vark' or 'wolf' (8 words)

Concepts required:
* Regular expressions

Resources:
* http://regexone.com/
* http://docs.python.org/2/library/re.html
* http://docs.python.org/2/howto/regex.html
* http://regex101.com/ (for testing regular expressions in multiple languages)
* https://pythex.org/ (for testing in Python)

Other fun RegEx things to play with:
* http://regexcrossword.com/ (Crosswords with RegEx)
* http://regex.alf.nu/ (Regex Golf)

