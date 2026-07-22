[app]

title = Guess Game
package.name = guessgame
package.domain = org.example
source.dir = .
source.include_exts = py,kv,png,jpg
version = 1.0

requirements = python3,kivy

orientation = portrait
fullscreen = 0


[buildozer]

log_level = 2

[android]

android.api = 35
android.minapi = 24
android.archs = arm64-v8a,armeabi-v7a
