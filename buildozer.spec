[app]

title = WinGo Educational Simulator
package.name = wingosimulator
package.domain = org.educational

source.dir = .
source.include_exts = py,json,png,jpg,kv,atlas

version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.archs = arm64-v8a


[buildozer]

log_level = 2
warn_on_root = 1
