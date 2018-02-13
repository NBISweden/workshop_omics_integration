---
layout: default
title:  Pre-course material
---

# Pre-course

This contains all information needed for local development, which is
encouraged when developing a course so you don't have to wait for github to
regenerate the course pages.

If you are just going to make quick, small edits you can skip the rest of this
and go directly to Lesson X; edit on github.

## Prerequisites

If you are going to develop a full course or have to do extensive edits, it's
recommended to run jekyll locally. If you are just going to do a few small
edits it's probably easier to just edit diretcly on the github website.

Github pages uses jekyll which is a "static site generator", what it does is
take a bunch of source files, apply some transformations and create a HTML
website from that. We use markdown files that are converted into HTML files
for the site, there are also a few other files that are important for setting
up the site. Images, pdfs and other smallish files can also be put directly in
the repo.


### Git

Check [git-scm.com](https://git-scm.com/) for installation instructions in
case you don't already have it installed.


### Jekyll

Jekyll itself is written in ruby, if you don't have ruby installed yet (check
by typing `ruby` in a terminal). You have to first install that, it can be
found in all major package distribution systems.

To install ruby dependencies locally it's a good idea to use
[bundler](http://bundler.io/), install that by typing `gem install bundler` at
the terminal.
