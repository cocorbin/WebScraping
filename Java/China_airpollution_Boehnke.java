/* Written by 
 * Jörn Boehnke 
 * For the winter 2015: 
 * Colloquium in Practical Computing for Economists
 * at the University of Chicago.
 * This file collects data on levels of air pollution in Shanghai. 
 */


import java.io.BufferedWriter;
import java.io.File;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStreamWriter;

import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.nodes.Element;
import org.jsoup.select.Elements;

public class Aqicn {
    
    public static void main(String[] args) {
        
        try {
            
            do {
                
                /*
                 * Connecting to the website.
                 */
                Document d = Jsoup.connect("http://aqicn.org/city/shanghai/")
                        .userAgent("Mozilla/5.0")
                        .timeout(10000)
                        .get();
                
                /*
                 * Select all "table"-tag(s) that are the child of tables of class
                 * "aqiwidget" and save the elements object to "e"
                 */
                Elements e;
                Element el;
                e = d.select("table.aqiwidget table:contains(Shanghai)");
                el = e.get(0).parent();
                e = el.select("table");
                el = e.get(e.size() - 1);
                e = el.select("td");
                
                String output = "";
                
                /*
                 * Starting for-loop at 1 instead of 0 to avoid printing the header
                 */
                for ( int nr=1; nr<(int)(e.size()/5); nr++ ) {
                    int add = 5 * nr;
                    output += e.get(add + 0).html().replaceAll("<\\s*\\/?\\s*\\w\\s*.*?>", "").replaceAll("\r?\n", " ").replaceAll("\\s+", " ").trim() + ",";
                    output += e.get(add + 1).html().replaceAll("<\\s*\\/?\\s*\\w\\s*.*?>", "") + ",";
                    output += e.get(add + 2).html() + ",";
                    output += e.get(add + 3).html() + ",";
                    output += e.get(add + 4).html() + "\r\n";
                }
                
                /*
                 * Call the "saveString" function defined below to save
                 * the string into the text file provided.
                 */
                saveString(new File("aqicn.txt"), output, true);
                System.out.print(output);
                System.out.println("---");
                
                /*
                 ***************************************************************
                 * VERY IMPORTANT: PAUSE TO NOT CRASH THE SERVER!!!
                 * (here we pause 1 hour = 60 * 60 * 1000 milliseconds)
                 * 
                 * ALWAYS USE THIS IF YOU ARE LOOPING WEB-REQUESTS
                 ***************************************************************
                 */
                sleep(60 * 60 * 1000);
                
            } while ( true );
            
        } catch ( IOException ex ) {
            
            System.out.println("Problem with the connection...");
            ex.printStackTrace();
            
        }
        
    }
    
    /*
     ***************************************************************
     * VERY IMPORTANT: PAUSE TO NOT CRASH THE SERVER!!!
     * 
     * ALWAYS USE THIS IF YOU ARE LOOPING WEB-REQUESTS
     ***************************************************************
     */
    private static void sleep(long millis) {
        try {
            Thread.sleep(millis);
        } catch ( InterruptedException ex ) {
            ex.printStackTrace();
        }
    }
    
    private static boolean saveString(File f, String s, boolean append) {
        try {
            FileOutputStream fos = new FileOutputStream(f, append); // new FileOutputStream(f, true); // if u want to append
            OutputStreamWriter osw = new OutputStreamWriter(fos);
            BufferedWriter bw = new BufferedWriter(osw);
            try {
                /*
                 * these two functions of the BufferedWriter object "bw"
                 * created above flush the string into the file provided
                 */
                bw.write(s);
                bw.flush();
            } finally {
                bw.close();
            }
        } catch ( Exception ex ) { // IOException, FileNotFoundException
            ex.printStackTrace();
            return false;
        }
        return true;
    }
    
}
