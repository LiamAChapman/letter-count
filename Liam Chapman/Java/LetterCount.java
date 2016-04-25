import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.FileInputStream;
import java.lang.Character;
import java.util.Scanner;

public class LetterCount
{
 public static void main(String[]args) throws FileNotFoundException
    
 {
     //Intialise array to hold character count
     int[] letterCount = new int[26];
     String fileName ="";
     
     //If a file is suplied
     if(args.length == 1)
     {
         fileName = args[0];
     }
     //Otherwise get user to input a file name
     else
     {
         Scanner in = new Scanner(System.in);
         System.out.print("Enter File Name:> ");
         fileName = in.next();
     }
     
     //Attempt to open file
     try
     {
         FileInputStream in = null;
         try
         {
             in = new FileInputStream(fileName);
             //Read each individual symbol
             while (in.available() > 0)
             {
                 char symbol = (char) in.read();
             
                 //If it is an alpha character get its ascii value
                 if (Character.isLetter(symbol)){
                     letterCount[(int)(Character.toUpperCase(symbol)) - 65]++;
                 }
             
             }
         }
         //Error opening file
         catch (IOException e)
         {
             System.out.println("Sorry I can not find the file: " + fileName);
         }
         //Close File
         finally
         {
             if(in != null)
             {
                 in.close();
             }
         }
     
     }
     //Error occurred
     catch (Exception e)
     {
         System.out.println("Sorry there was an error." + e.getMessage());
     }
     //Iterate through file
     for(int i = 0; i < letterCount.length;i++){
     
         //If the letter has occurred
         if(letterCount[i] > 0)
         {
             //Print out its count
             System.out.println((char)(i + 65) + " Appears " + letterCount[i] + " times");
         }
     }
 }
}
