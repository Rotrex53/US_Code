// Source code is decompiled from a .class file using FernFlower decompiler.
package utiles;

public class Checkers {
   public Checkers() {
   }

   public static void check(String textoRestriccion, Boolean condicion) {
      if (!condicion) {
         String var10002 = Thread.currentThread().getStackTrace()[2].getClassName();
         throw new IllegalArgumentException(var10002 + "." + Thread.currentThread().getStackTrace()[2].getMethodName() + ": " + textoRestriccion);
      }
   }

   public static void checkNoNull(Object... parametros) {
      for(int i = 0; i < parametros.length; ++i) {
         if (parametros[i] == null) {
            String var10002 = Thread.currentThread().getStackTrace()[2].getClassName();
            throw new IllegalArgumentException(var10002 + "." + Thread.currentThread().getStackTrace()[2].getMethodName() + ": el par\u00e1metro " + (i + 1) + " es nulo");
         }
      }

   }
}
