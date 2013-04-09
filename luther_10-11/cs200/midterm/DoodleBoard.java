/* Scott Gerike
  CS 200
  This programs makes a paint-like program called the Doodle Board
  Things you can do with this: draw lines, change pen color & thickness, draw circles and squares, import a background image
*/

import javax.swing.*;
// Setting up the main window for the program to be in
public class DoodleBoard
{
    public static void main(String[]args)
    {
        DoodleFrame dframe = new DoodleFrame();
        
        dframe.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        dframe.setVisible(true);

    }
}