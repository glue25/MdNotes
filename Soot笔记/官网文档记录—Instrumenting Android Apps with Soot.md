<a href='https://github.com/soot-oss/soot/wiki/Instrumenting-Android-Apps-with-Soot'>原文</a> 

前面介绍了这项工作是谁做的。

# How to instrument

提到的Android平台<a href=' https://github.com/Sable/android-platforms'>网址</a> 



<u>Next we implement a driver class with a main method into which we stick the following code</u>

具体是什么意义可以查文档，第一行是分析APK要的，第二行好像是要输出DEX码，

后两者是在Soot载入需要的类，看起来具体怎么写是视任务而定的。

```java
//prefer Android APK files// -src-prec apk
Options.v().set_src_prec(Options.src_prec_apk);

//output as APK, too//-f J
Options.v().set_output_format(Options.output_format_dex);

// resolve the PrintStream and System soot-classes
Scene.v().addBasicClass("java.io.PrintStream",SootClass.SIGNATURES);
Scene.v().addBasicClass("java.lang.System",SootClass.SIGNATURES);
```

然后添加Transform 

<u>This will walk through all Units of all Bodies in the APK and on every InvokeStmt will invoke the code which I labeled with “code here”.</u>InvokeStmt 看起来是一个类，它定义在哪呢？是做什么的呢？

```java
PackManager.v().getPack("jtp").add(new Transform("jtp.myInstrumenter", new BodyTransformer() {

	@Override
	protected void internalTransform(final Body b, String phaseName, @SuppressWarnings("rawtypes") Map options) {
		final PatchingChain units = b.getUnits();		
		//important to use snapshotIterator here
		for(Iterator iter = units.snapshotIterator(); iter.hasNext();) {
			final Unit u = iter.next();
			u.apply(new AbstractStmtSwitch() {

				public void caseInvokeStmt(InvokeStmt stmt) {
					//code here
				}

			});
		}
	}
}));
```

//code here;可以写作下面。

```java
InvokeExpr invokeExpr = stmt.getInvokeExpr();
if(invokeExpr.getMethod().getName().equals("onDraw")) {

	Local tmpRef = addTmpRef(b);
	Local tmpString = addTmpString(b);

	  // insert "tmpRef = java.lang.System.out;" 
    units.insertBefore(Jimple.v().newAssignStmt( 
              tmpRef, Jimple.v().newStaticFieldRef( 
              Scene.v().getField("<java.lang.System: java.io.PrintStream out>").makeRef())), u);

    // insert "tmpLong = 'HELLO';" 
    units.insertBefore(Jimple.v().newAssignStmt(tmpString, 
                  StringConstant.v("HELLO")), u);

    // insert "tmpRef.println(tmpString);" 
    SootMethod toCall = Scene.v().getSootClass("java.io.PrintStream").getMethod("void     println(java.lang.String)");                    
    units.insertBefore(Jimple.v().newInvokeStmt(
                  Jimple.v().newVirtualInvokeExpr(tmpRef, toCall.makeRef(), tmpString)), u);

    //check that we did not mess up the Jimple
    b.validate();
}
```

This causes Soot to insert a `System.out.println("HELLO")` just before the method invocation but only if the target of this invocation is an onDraw method.（onDraw 又是什么）

最后还是要调用

```java
soot.Main.main(args);
```



And that’s it! Piece of cake, isn’t it? All you now need to do is run your driver class with the following arguments:

```
-android-jars path/to/android-platforms -process-dir your.apk
```















