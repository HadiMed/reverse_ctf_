# Write up 

first using apktool to extract files and decompile dex file to smali , we end up with this directoy : 

<br/>
<img src="apkoutput.PNG"/> 
<br/> 
nothing interesting at AndroidManifest  , lets look at smali files , the file MainActivity contains the first functionality of the application , its just calling <b> LoalLibrary </b> to Load a native Library included on the apk m then printing the String <b> "Welcome To Rockai Challenge" </b>
<br/>
<img src="mainactivity.PNG"/>
