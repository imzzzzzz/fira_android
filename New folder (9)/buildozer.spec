[app]

# Title of your application
title = TimePassedApp

# Package name
package.name = timepassedapp

# Package domain (needed for Android packaging)
package.domain = org.mydomain

# Source code directory
source.dir = .

# List of source files to include (let empty to include all files)
source.include_exts = py

# Application version
version = 1.0

# Application requirements
requirements = python3,kivy

# Supported orientations
orientation = portrait

[buildozer]
log_level = 2
warn_on_root = 1

[app@debug]
# Add specific debug settings here if needed
