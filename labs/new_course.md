---
layout: default
title: Create a new course
---

# New course


There are three steps to bootstrapping a new course:

1. Create a new repo on github
2. Add the base template for a course
3. Enable github-pages on github



## Step 1. Create a repo on github

To setup a completely new course, start by adding a new repository on github.
Go to [repository creation page](https://github.com/organizations/NBISweden/repositories/new)

Please use a name that starts with `course-` for example: `course-proteomics`,
make it public and do not initialize the repository with a README.


## Step 2. Add base template

Add the common layout github repository as a submodule

{% highlight bash %}
git submodule add https://github.com/NBISweden/workshop-common.git workshop-common
git submodule init
git submodule sync
{% endhighlight %}

Then create a base `_config.yml` to tell Jekyll to look for layout stuff inside
the workshop-common folder and some other configuration options:

{% highlight yaml %}
title: "name of course"
baseurl: /workshop-name-of-course

# where things are
layouts_dir: ./workshop-common/layouts
includes_dir: ./workshop-common/includes
sass:
  sass_dir: ./workshop-common/sass

plugins:
  - jemoji

defaults:
  - values:
      logosnav: true

menu:
  - title: Overview
    url:
  - title: Schedule
    url: schedule
  - title: Pre-course material
    url: precourse
  - title: Travel info
    url: travel
  - title: Labs
    submenus:
      - title: Lab 1
        url: labs/lab1
      - title: Lab 2
        url: labs/lab2
{% endhighlight %}


Don't forget to commit and push:

{% highlight bash %}
git add _config.yml
git commit -m 'Base course template'
git push
{% endhighlight %}

## Step 3. Enable GitHub Pages

Go to the settings on github for your newly created repo to enable GitHub
Pages. Almost at the bottom of that page there is a section devoted to GitHub
Pages, the source should be `master branch`, ignore all other settings.
