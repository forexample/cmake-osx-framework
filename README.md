Example of building/adding `Mac OS X`/`iOS` framework with CMake and build.py.

### OS X

Build framework `foo`:


```bash
> rm -rf _* # remove _builds/_install/_framework
> build.py --toolchain libcxx --verbose --config Release --framework --home Foo
...
Framework created: /.../_framework/libcxx/foo.framework
...
```

You can check framework manually:


```bash
> ls _framework/libcxx/foo.framework/Headers/foo.hpp
_framework/libcxx/foo.framework/Headers/foo.hpp
> ls _framework/libcxx/foo.framework/Versions/A/foo
_framework/libcxx/foo.framework/Versions/A/foo

```

Use framework:

```bash
> rm -rf _builds _install
> build.py --toolchain libcxx --verbose --config Release --test --home Boo
...
1: Hello from foo
...

```

### iOS

Build framework `foo`:


```bash
> rm -rf _* # remove _builds/_install/_framework
> build.py --toolchain ios-8-2 --verbose --config Release --framework --home Foo
...
Framework created: /.../_framework/ios-8-2/foo.framework
...
```

You can check framework manually:


```bash
> ls _framework/ios-8-2/foo.framework/Headers/foo.hpp
_framework/ios-8-2/foo.framework/Headers/foo.hpp
> ls _framework/ios-8-2/foo.framework/Versions/A/foo
_framework/ios-8-2/foo.framework/Versions/A/foo

```

Use framework:

```bash
> rm -rf _builds _install
> build.py --toolchain ios-8-2 --verbose --config Release --open --home Boo
> # Run application on device/simulator using Xcode

```
