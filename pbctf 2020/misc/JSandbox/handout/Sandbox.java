import java.util.*;
import java.lang.reflect.*;
import static java.lang.System.out;


public class Sandbox {
  private static class FailedException extends Exception {
    public FailedException(String s) {
      super(s);
    }
  }

  private static Object data[] = new Object[8];
  private static int chkObj(int num) throws FailedException {
    if (num < 0 || num >= data.length)
      throw new FailedException("Invalid index");
    return num;
  }
  private static <E> E chkTyp(Class<E> cls, Object o) throws FailedException {
    if (!cls.isInstance(o)) {
      throw new FailedException("Expected type: " + cls);
    }
    return cls.cast(o);
  }
  private static Object arrayGet(Object arr, int index)
      throws FailedException {
    if (arr instanceof byte[]) return ((byte[])arr)[index];
    else if (arr instanceof char[]) return ((char[])arr)[index];
    else if (arr instanceof short[]) return ((short[])arr)[index];
    else if (arr instanceof int[]) return ((int[])arr)[index];
    else if (arr instanceof long[]) return ((long[])arr)[index];
    else if (arr instanceof float[]) return ((float[])arr)[index];
    else if (arr instanceof double[]) return ((double[])arr)[index];
    else if (arr instanceof boolean[]) return ((boolean[])arr)[index];
    else if (arr instanceof Object[]) return ((Object[])arr)[index];
    else throw new FailedException("Not an array");
  }
  private static void arraySet(Object arr, int index, Object val)
      throws FailedException {
    if (arr instanceof byte[]) ((byte[])arr)[index] = (byte)val;
    else if (arr instanceof char[]) ((char[])arr)[index] = (char)val;
    else if (arr instanceof short[]) ((short[])arr)[index] = (short)val;
    else if (arr instanceof int[]) ((int[])arr)[index] = (int)val;
    else if (arr instanceof long[]) ((long[])arr)[index] = (long)val;
    else if (arr instanceof float[]) ((float[])arr)[index] = (float)val;
    else if (arr instanceof double[]) ((double[])arr)[index] = (double)val;
    else if (arr instanceof boolean[]) ((boolean[])arr)[index] = (boolean)val;
    else if (arr instanceof Object[]) ((Object[])arr)[index] = val;
    else throw new FailedException("Not an array");
  }
  public static void main(String[] args) throws Exception{
    Scanner in = new Scanner(System.in);
    out.println("*** Java Sandbox ***");
    while (true) {
      try {
        out.print(">>> ");
        if (!in.hasNextLine()) return;

        Scanner line = new Scanner(in.nextLine());
        if (!line.hasNext()) continue;
        switch (line.next()) {
          case "class":
            int dst = chkObj(line.nextInt());
            try {
              data[dst] = Class.forName(line.next());
            } catch (ClassNotFoundException e) {
              e.printStackTrace();
              throw new FailedException("Class not found");
            }
            break;
          case "field":
            dst = chkObj(line.nextInt());
            int src = chkObj(line.nextInt());
            try {
              Field f = chkTyp(Class.class, data[src])
                .getDeclaredField(line.next());
              f.setAccessible(true);
              data[dst] = f;
            } catch (NoSuchFieldException e) {
              throw new FailedException("Field not found");
            }
            break;
          case "fields":
            int cls = chkObj(line.nextInt());
            for (Field f : chkTyp(Class.class, data[cls]).getDeclaredFields()) {
              out.println(f.getName());
            }
            break;
          case "imm":
            dst = chkObj(line.nextInt());
            switch (line.next()) {
              case "string": data[dst] = line.next(); break;
              case "byte": data[dst] = line.nextByte(); break;
              case "short": data[dst] = line.nextShort(); break;
              case "char": data[dst] = (char)line.nextInt(); break;
              case "int": data[dst] = line.nextInt(); break;
              case "long": data[dst] = line.nextLong(); break;
              case "float": data[dst] = line.nextFloat(); break;
              case "double": data[dst] = line.nextDouble(); break;
              case "boolean": data[dst] = line.nextBoolean(); break;
              case "null": data[dst] = null; break;
            }
            break;
          case "multiline":
            dst = chkObj(line.nextInt());
            String eof = line.next();
            StringBuilder ret = new StringBuilder();
            while (true) {
              String line2 = in.nextLine();
              if (line2.equals(eof)) break;
              ret.append(line2);
              ret.append('\n');
            }
            data[dst] = ret.toString();
            break;
          case "show":
            src = chkObj(line.nextInt());
            out.println(data[src]);
            break;
          case "fget":
            dst = chkObj(line.nextInt());
            src = chkObj(line.nextInt());
            int fld = chkObj(line.nextInt());
            try {
              data[dst] = chkTyp(Field.class, data[fld]).get(data[src]);
            } catch (IllegalAccessException e) {
              throw new FailedException(e.toString());
            }
            break;
          case "fset":
            dst = chkObj(line.nextInt());
            fld = chkObj(line.nextInt());
            src = chkObj(line.nextInt());
            try {
              chkTyp(Field.class, data[fld]).set(data[dst], data[src]);
            } catch (IllegalAccessException e) {
              throw new FailedException(e.toString());
            }
            break;
          case "classOf":
            dst = chkObj(line.nextInt());
            src = chkObj(line.nextInt());
            data[dst] = data[src].getClass();
            break;
          case "aget":
            dst = chkObj(line.nextInt());
            src = chkObj(line.nextInt());
            int ind = line.nextInt();
            data[dst] = arrayGet(data[src], ind);
            break;
          case "aset":
            dst = chkObj(line.nextInt());
            ind = line.nextInt();
            src = chkObj(line.nextInt());
            arraySet(data[dst], ind, data[src]);
            break;
          case "help":
            out.println("aget DSTi SRC IND            Gets the INDth array value of SRCi");
            out.println("aset DSTi IND SRCi           Sets the INDth array value of DSTi");
            out.println("                             with SRCi");
            out.println("fget DSTi SRCi FLDi          gets the field FLD from SRC object");
            out.println("field DSTi SRCi NAME         load a field from class");
            out.println("fset DSTi FLDi SRCi          sets the field FLD in DST object ");
            out.println("                             with SRC value");
            out.println("class DSTi NAME              load a class");
            out.println("classOf DSTi SRCi            obtains the class type of SRC");
            out.println("help                         prints this help message");
            out.println("imm DSTi {string|byte|short  load a primitive/constant value");
            out.println("  |char|int|long|float");
            out.println("  |double|boolean|null} [VAL]");
            out.println("multiline DSTi EOF           load a multi-line string, using the ");
            out.println("                             specified string as EOF identifier");
            out.println("quit                         exit program");
            out.println("show SRCi                    prints a string representation of");
            out.println("                             the object");
            break;
          case "quit":
            return;
          default:
            out.println("Invalid command");
        }
      } catch (NoSuchElementException e) {
        out.println("Syntax Error");
      } catch (RuntimeException e) {
        out.println("Runtime Error: " + e);
      } catch (FailedException e) {
        out.println("ERROR: " + e.getMessage());
      }
    }
  }
}
