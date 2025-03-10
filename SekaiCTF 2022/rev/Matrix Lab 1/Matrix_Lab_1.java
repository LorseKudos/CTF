/*
 * Decompiled with CFR 0.150.
 *
 * Could not load the following classes:
 *  Sekai
 */
import java.util.Scanner;

/*
 * Exception performing whole class analysis ignored.
 */
public class Sekai {
    private static int length = (int)Math.pow(2.0, 3.0) - 2;

    public static void main(String[] arrstring) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the flag: ");
        String string = scanner.next();
        if (string.length() != 43) {
            System.out.println("Oops, wrong flag!");
            return;
        }
        String string2 = string.substring(0, length);
        String string3 = string.substring(length, string.length() - 1);
        String string4 = string.substring(string.length() - 1);
        if (string2.equals("SEKAI{") && string4.equals("}")) {
            assert (string3.length() == length * length);
            if (Sekai.solve((String)string3)) {
                System.out.println("Congratulations, you got the flag!");
            } else {
                System.out.println("Oops, wrong flag!");
            }
        } else {
            System.out.println("Oops, wrong flag!");
        }
    }

    public static String encrypt(char[] arrc, int n) {
        int n2;
        char[] arrc2 = new char[length * 2];
        int n3 = length - 1;
        int n4 = length;
        for (n2 = 0; n2 < length * 2; ++n2) {
            arrc2[n2] = arrc[n3--];
            arrc2[n2 + 1] = arrc[n4++];
            ++n2;
        }
        n2 = 0;
        while (n2 < length * 2) {
            int n5 = n2++;
            arrc2[n5] = (char)(arrc2[n5] ^ (char)n);
        }
        return String.valueOf(arrc2);
    }

    public static char[] getArray(char[][] arrc, int n, int n2) {
        int n3;
        char[] arrc2 = new char[length * 2];
        int n4 = 0;
        for (n3 = 0; n3 < length; ++n3) {
            arrc2[n4] = arrc[n][n3];
            ++n4;
        }
        for (n3 = 0; n3 < length; ++n3) {
            arrc2[n4] = arrc[n2][length - 1 - n3];
            ++n4;
        }
        return arrc2;
    }

    public static char[][] transform(char[] arrc, int n) {
        char[][] arrc2 = new char[n][n];
        for (int i = 0; i < n * n; ++i) {
            arrc2[i / n][i % n] = arrc[i];
        }
        return arrc2;
    }

    public static boolean solve(String string) {
        char[][] arrc = Sekai.transform((char[])string.toCharArray(), (int)length);
        for (int i = 0; i <= length / 2; ++i) {
            for (int j = 0; j < length - 2 * i - 1; ++j) {
                char c = arrc[i][i + j];
                arrc[i][i + j] = arrc[length - 1 - i - j][i];
                arrc[Sekai.length - 1 - i - j][i] = arrc[length - 1 - i][length - 1 - i - j];
                arrc[Sekai.length - 1 - i][Sekai.length - 1 - i - j] = arrc[i + j][length - 1 - i];
                arrc[i + j][Sekai.length - 1 - i] = c;
            }
        }
        return "oz]{R]3l]]B#50es6O4tL23Etr3c10_F4TD2".equals(Sekai.encrypt((char[])Sekai.getArray((char[][])arrc, 0, 5), 2) + Sekai.encrypt((char[])Sekai.getArray((char[][])arrc, 1, 4), 1) + Sekai.encrypt((char[])Sekai.getArray((char[][])arrc, 2, 3), 0));
    }
}
