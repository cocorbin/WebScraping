/* Written by 
 * Jörn Boehnke 
 * For the winter 2015 colloquium in practical computing for economists
 * at the University of Chicago
 */

public class RegEx {
    
    public static void main(String[] args) {
        
        /*
         * This short program is meant to demonstrate how to implement RegEx into Java.
         */
        
        /*
         * In this program, we will delete all HTML tags (e.g. "<b>") in the string
         * htmlTag.
         */
        String htmlTag = "<b>Forecast</b><small><a style='color:#888;' href='/forecast/asia/'>Click for more details</a></small>";
        
        /*
         * The most important thing to remember when implementing RegEx in Java is that
         * "\" is Java's string escape character.  Therefore, when using "\" for RegEx
         * (and not as a Java escape sequence), one needs to write "\\".
         */
        String regexToSelectTags = "<\\s*\\/?\\s*\\w\\s*.*?>";
        
        /*
         * The s.replaceAll(a,b) method RegEx-matches all appearances of a in s and
         * replaces them with b. 
         */
        String plainTextDashes = htmlTag.replaceAll(regexToSelectTags, "-");
        
        /*
         * Printing the result to screen.
         */
        System.out.println(plainTextDashes);
        
        /*
         * Some more replacing.
         */
        String plainText = plainTextDashes.replaceAll("[-]{2,}", "-").replaceAll("(^-+|-+$)", "");
        
        /*
         * Some more printing.
         */
        System.out.println(plainText);
        
    }
    
}
