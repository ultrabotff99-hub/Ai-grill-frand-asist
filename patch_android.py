import glob, re
p = "android/app/src/main/AndroidManifest.xml"
s = open(p).read()
perms = '''<uses-permission android:name="android.permission.INTERNET"/>
    <uses-permission android:name="android.permission.RECORD_AUDIO"/>
    <uses-permission android:name="android.permission.BLUETOOTH"/>
    <uses-permission android:name="android.permission.BLUETOOTH_CONNECT"/>
    <queries>
        <intent><action android:name="android.intent.action.TTS_SERVICE"/></intent>
        <intent><action android:name="android.speech.RecognitionService"/></intent>
    </queries>
    <application'''
s = s.replace("<application", perms, 1)
open(p, "w").write(s)
for g in glob.glob("android/app/build.gradle*"):
    t = open(g).read()
    t = t.replace("flutter.minSdkVersion", "24").replace("minSdkVersion flutter.minSdkVersion", "minSdkVersion 24")
    open(g, "w").write(t)
print("patched")
