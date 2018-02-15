---
layout: default
title:  'Schedule'
---

# Schedule

Course is held at SciLifeLab, Tomtebodavagen 23A, 171 65 Solna

Contact: [olga.dethlefsen@nbis.se](olga.dethlefsen@gmail.com); 0720 492 082

----

{% for day in site.data.schedule %}
### {{ day.day }}

{% for t in day.timeslots %}

**{{ t.start }} - {{ t.end }}**
{% if t.link %}[{% endif %}{{t.title}}{% if t.link %}]({{site.baseurl}}/{{t.link}}){% endif %}
{% if t.tas %}({{t.tas}}){% endif %}

{% endfor %}

----
{% endfor %}

_coffee and snacks will arrive twice a day_

_lunch will be at [Restaurang Konigs](http://restaurangkonigs.se)_
