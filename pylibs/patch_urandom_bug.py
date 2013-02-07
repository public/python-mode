
import os

if not hasattr(os, 'urandom'):
    # There's some annoying bug with Vim builds on OS X that breaks os.urandom.
    # To work around this we temporarily patch it out and then hack in a
    # totally insecure version of os.urandom.

    def raise_notimpl(*args):
        """Force random to fallback to using time for a seed"""
        raise NotImplementedError()
    os.urandom = raise_notimpl

    import random
    import cStringIO

    def crappy_urandom_for_macports_bug(n):
        """Totally fail way of generating some random bytes"""
        buf = cStringIO.StringIO()
        for i in xrange(n):
            buf.write(chr(random.randint(0, 255)))
        return buf.getvalue()
    os.urandom = crappy_urandom_for_macports_bug
