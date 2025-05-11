// Reverse encryption program
// BSD Licensed

import java.util.Scanner;

public class reverseCipher {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    System.out.println("Enter a message to be reversed: ");
    String input = scanner.nextLine();
    String translated = "";
    for (int i = input.length() - 1; i >= 0; i--) {
      translated += input.charAt(i);
    }
    System.out.println(translated);
    scanner.close();
  }
}
