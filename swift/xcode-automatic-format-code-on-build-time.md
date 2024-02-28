- Date : 2024-02-28
- Tags : #swift #xcode #dev #macos

## XCode automatic format code on build time

XCode (the main IDE of Apple), but lacks much common features like auto formating code.
So we have to install a external tool (lol it's Apple tool itself) by `brew install swift-format`

Then I have to use a trick in **Build Phases** settings in XCode, we create a bash script run format tool on every build time (before source code has been built, because sometimes your code buidling will failed)

Here is the bash script, make sure the Run script below "Run Build Tool Plug-ins" step

![run script](https://github.com/khanhicetea/today-i-learned/assets/4528223/d5ece15c-6b25-4a4c-89f5-3e9f5a8b5a06)

```shell
echo "Formating all source codes"
cd $SOURCE_ROOT
/opt/homebrew/bin/swift-format --ignore-unparsable-files -i -p -r .
echo "Formated all source codes."
```

**Important** : You have to turn off Build Options named **User Script Sandboxing** (this diffenrence of App Sandboxing), to allow your shell scripts can affected real filesystem instead of shadowing sandbox files, below is the screenshot

![Turn of User Script Sandboxing](https://github.com/khanhicetea/today-i-learned/assets/4528223/486a72e2-7aad-4780-905b-3919c13788e7)


