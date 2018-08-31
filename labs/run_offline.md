---
layout: default
title: Run Offline
---

# Run locally

Make sure you have followed all the steps in [precourse](../precourse).

Make sure you have cloned the course repository locally (`git clone ...`) and
have are in the base directory for the repo.


## Jekyll

Jekyll itself is written in ruby, if you don't have ruby installed yet (check
by typing `ruby` in a terminal). You have to first install that, it can be
found in all major package distribution systems.

To install ruby dependencies locally it's a good idea to use
[bundler](http://bundler.io/), install that by typing `gem install bundler` at
the terminal.


## Ruby dependencies

Type this to install all dependencies

{% highlight bash %}
$ bundle install
{% endhighlight %}

Sometimes the _nokogiri_ package complains, a solution that usually works is
to tell it to use the system libraries, like this:

{% highlight bash %}
$ bundle config build.nokogiri --use-system-libraries
$ bundle install
{% endhighlight %}

## Run jekyll

To start jekyll, use the following command:

{% highlight bash %}
$ bundle exec jekyll serve
{% endhighlight %}

Jekyll will reload the site everytime you make a change to the files in the
course directory.


## Run jekyll in Docker

{% highlight bash %}
$ docker run -t --rm -v "$PWD":/usr/src/app -p "4000:4000" starefossen/github-pages
{% endhighlight %}
