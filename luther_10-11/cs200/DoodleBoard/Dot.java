import java.awt.*;

// class that holds the information needed to draw the line, including the constants and global variables

public class Dot
    {
        static int small = 2; //the width of the small line
        static int medium = 6; //the width of the medium line
        static int large = 10; //the width of the large line
        static Color defaultColor = Color.black; //the default color of the pen
        static String s = "square"; //the string used to determine if pen is round or square
        static String r = "round"; //the string used to determine if the pen is round or square
        static int size; //global variable for size
        static String shape; //global variable for shape
        static Color color; //global variable for color
        public Dot()
        {

        }
        public static void setSize(int a) //sets the size of the pen line
        {
            size = a;
        }
        public static int getSize() //gets the size of the pen line
        {
            return size;
        }
        public static void setShape(String a) //sets the shape of the pen line
        {
            shape = a;
        }
        public static String getShape() //gets the shape for the pen line
        {
            return shape;
        }
        public static void setColor(Color c) //sets the color for the pen line
        {
            color = c;
        }
        public static Color getColor() //gets the color for the pen line
        {
            return color;
        }
    }