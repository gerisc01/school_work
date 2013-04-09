import java.awt.*;

public class Dot
    {
        static String s = "square";
        private static String r = "round";
        private static int size;
        private static String shape;
        private static Color color;
        public Dot()
        {
            size = 5;
            shape = r;
            color = Color.black;
        }
        public static void setSize(int a)
        {
            size = a;
        }
        public static int getSize()
        {
            return size;
        }
        public static void setShape(String a)
        {
            shape = a;
        }
        public static String getShape()
        {
            System.out.println(shape);
            return shape;
        }
        public static void setColor(Color c)
        {
            color = c;
        }
        public static Color getColor()
        {
            return color;
        }
    }