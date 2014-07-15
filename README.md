Django Easier Settings
======================

``djes`` provides a few tools to help you keep your Django settings
clean and readable:

 * ``Settings`` class is a placeholder for you settings. Once instantiated,
   you can use it like a dictionary and then move its content into the local
   namespace of your ``settings.py``.

 * ``mode`` check if ``DJES_MODE`` environment variable was set. You can
   use it to provide different settings in a different environments.

Examples
--------

Define settings with ``djes``:

```python
import djes

settings = djes.Settings()
settings['debug'] = True  # you don't have to use uppercase notation
settings.install(locals())
```

Different settings based on the ``DJES_MODE`` variable:

```python
def production(settings):
    settings['debug'] = False
  
def developments(settings):
    settings['debug'] = True
 
import djes

settings = djes.Settings()

if djes.mode('prod'):
    production(settings)
elif djes.mode('dev') or djes.is_local():
    development(settings)
else:
    raise ValueError('Invalid mode')
```
