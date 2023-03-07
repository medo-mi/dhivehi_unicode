# Python Dhivehi (Thaana) ASCII, accent to unicode converter

Python package to convert Dhivehi (Thaana) ASCII and accent text to Unicode

### accent_to_unicode
```Python
from  dhivehi_unicode  import  DhivehiConverter  as  dv
text = "clIAWmcsia udwmcawHum"
unicode = dv.accent_to_unicode(text)
print(unicode)
```

Output
> މުޙައްމަދު  އިސްމާޢީލް


### ascii_to_unicode

```Python
from  dhivehi_unicode  import  DhivehiConverter  as  dv
text = "muHawqmadu wisqmAWIlq"
unicode = dv.ascii_to_unicode(text)
print(unicode)
```
Output
> މުޙައްމަދު  އިސްމާޢީލް
