from django import template
from urllib.parse import urlencode

register = template.Library()

@register.filter
def as_querystring(data, options=""):
    """
    Convert a dict to a URL querystring, with optional whitelisting or blacklisting.
    Usage:
        {{ request.GET.dict|as_querystring }}  ← all keys
        {{ request.GET.dict|as_querystring:'only=title,author' }}
        {{ request.GET.dict|as_querystring:'exclude=page' }}
    """
    if not isinstance(data, dict):
        return ""

    only = None
    exclude = set()

    # Parse options string like 'only=title,author' or 'exclude=page'
    if options.startswith("only="):
        only = set(options[5:].split(","))
    elif options.startswith("exclude="):
        exclude = set(options[8:].split(","))

    # Filter keys
    if only is not None:
        filtered = {k: v for k, v in data.items() if k in only}
    else:
        filtered = {k: v for k, v in data.items() if k not in exclude}

    return urlencode(filtered)


@register.filter
def get_item(dictionary, key):
    return dictionary.get(str(key))