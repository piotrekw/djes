Django Easier Settings
======================

``djes`` provides a few tools to help you keep your Django settings
clean and readable:

 * ``Settings`` class is a placeholder for you settings. Once instantiated,
   you can use it like a dictionary and then move its content into the local
   namespace of your ``settings.py``.

 * ``mode`` check if ``DJES_MODE`` environment variable was set. You can
   use it to provide different settings in a different environments.

