---
layout: default
title: Run Offline
---

# Run locally

Make sure you have followed all the steps in [precourse](../precourse).

Make sure you have cloned the course repository locally (`git clone ...`) and
have are in the base directory for the repo.

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
