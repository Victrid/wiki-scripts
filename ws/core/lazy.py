#! /usr/bin/env python3

# FIXME: sphinx does not recognize the wrapped method as 'property', i.e. it adds () to the name

class LazyProperty(property):
    """
    A `descriptor`_ wrapping a class method and exposing it as a lazily
    evaluated and cached property. It is intended to be used as a decorator.

    The wrapped method is evaluated once on the first access and its return
    value is cached for fast subsequent accessing. The cached value can be
    reset by deleting the attribute using the ``del`` operator, e.g.
    ``del object.attribute``, which will cause the wrapped method to be called
    again on the next access.

    .. _`descriptor`: https://docs.python.org/3/howto/descriptor.html
    """

    def __init__(self, func):
        self.func = func
        # descriptors must be set on class, so we manage a mapping
        # of the memoized values per instance
        self._cache = {}

    def __get__(self, instance, owner):
        if instance is None and owner is not None:
            # static access, e.g. by sphinx
            return self.func
        elif instance is None:
            # TODO: can this even happen?
            raise AttributeError

        if instance not in self._cache:
            self._cache[instance] = self.func(instance)
        return self._cache[instance]

    def __delete__(self, instance):
        if instance in self._cache:
            del self._cache[instance]

if __name__ == "__main__":
    class Foo:
        @LazyProperty
        def foo(self):
            print("Running foo()")
            return 42

    f = Foo()
    print(f.foo)
    print(f.foo)

    # reset the cache for an instance
    del f.foo

    print(f.foo)