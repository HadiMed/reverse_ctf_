# Write up 

first using apktool to extract files and decompile dex file to smali , we end up with this directoy : 

<br/>
<img src="apkoutput.PNG"/> 
<br/> 
nothing interesting at AndroidManifest  , lets look at smali files , the file MainActivity contains the first functionality of the application , its just calling <b> LoalLibrary </b> to Load a native Library included on the apk m then printing the String <b> "Welcome To Rockai Challenge" </b>
<br/>
<br/>
<img src="mainactivity.PNG"/>
<br/>
<br/>
Then there is the MainActivity$1 that will include the main functionality of the applciation <br/>
this is the ghidra Decompilation  : <br/>
<img src="ghidraoutput.PNG"/>
