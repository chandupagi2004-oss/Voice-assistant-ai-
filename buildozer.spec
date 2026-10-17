[app]

# (str) Title of your application
title = Voice Assistant AI

# (str) Package name
package.name = voiceassistant

# (str) Package domain (needed for android packaging)
package.domain = org.assistant

# (list) Source files to include (let it empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Source files to include (let it empty to include all the files)
source.dir = .

# (str) Application versioning (version or version_regex)
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation (landscape, portrait, all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET, RECORD_AUDIO

# (str) Indicate whether you accept the Android SDK license
android.accept_sdk_license = True

# (str) The Android API to use for targeting
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

android.archs = armeabi-v7a
