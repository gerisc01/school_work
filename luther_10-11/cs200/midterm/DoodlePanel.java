import java.awt.*;
import javax.swing.*;
import java.util.*;
import java.awt.event.*;
import java.awt.geom.*;

public class DoodlePanel extends JPanel //The place where the actual drawing takes place
{
    private ArrayList<Shape> drawlist = new ArrayList<Shape>(); //used to keep all the images drawn by the pen stay on the screen
    private ArrayList<Color> colorlist = new ArrayList<Color>(); //used to keep pen for the previous lines the same color it was drawn after it is changed
    private ArrayList<Integer> shapemakerlist = new ArrayList<Integer>(); //used to store x,y coordinates for the Shape Making option
    private ArrayList<Shape> choosershapelist = new ArrayList<Shape>(); //used to keep all the of shapes that where drawn by the Shape Maker on the screen
    private ArrayList<Color> choosercolorlist = new ArrayList<Color>(); //used to keep the right color for all of the shapes drawn by Shape Maker after color is changed
    static String circledraw = null; //when null, mouseClicked doesn't create any shapes or store coordinates (same for squaredraw)
    static String squaredraw = null; //changed from null when menu option is clicked
    public DoodlePanel()
    {
        super();
        
        this.addMouseMotionListener(new MouseBoardListener()); //Adding the listeners for the pen (motion listener) and Shape Makers (mouseClicked)
        this.addMouseListener(new CircleCreatorListener());
        this.addMouseListener(new SquareCreatorListener());

    }
    
    private class MouseBoardListener extends MouseMotionAdapter //Listener class for the pen
    {
        public MouseBoardListener() 
        {
            super();
        }
        public void mouseDragged(MouseEvent me)
        {
            int xloc = me.getX();//gets x & y coordinates so it knows where to draw the squares/circles for pen "ink"
            int yloc = me.getY();
            Color lineColor = Dot.getColor();//the color of the pen "ink" which was stored in the Dot class
            if (Dot.getShape() == "round")
            {
                Ellipse2D.Double circle = new Ellipse2D.Double(xloc,yloc,Dot.getSize(),Dot.getSize()); //circle pen shape
                drawlist.add(circle); //adding the circle to the list so it can be redrawn
                colorlist.add(lineColor); //adding the color to the list so it is remembered later
            }
            if (Dot.getShape() == "square")
            {
                Rectangle2D.Double square = new Rectangle2D.Double(xloc,yloc,Dot.getSize(),Dot.getSize()); //square pen shape
                drawlist.add(square); //adding the square to the list so it can be redrawn later
                colorlist.add(lineColor); //adding the color to the list so it is remembered
            }
        }
    }
    
    private class CircleCreatorListener extends MouseAdapter
    {
        public CircleCreatorListener() //creates the circle with the shape maker
        {
            
        }
        public void mouseClicked(MouseEvent me)
        {
            int xloc = me.getX(); //getting x & y locations
            int yloc = me.getY();
            if (circledraw != null) //if changed from null when menu option is selected
            {
                if (shapemakerlist.isEmpty() == false) //the second click that actually creates the circle; has to be first because if it isn't it would try to create circle with the same
                { //x & y coordinates it got on the fist click (because that would be the only click) which would create a circle with height and width of 0
                    Ellipse2D.Double a = new Ellipse2D.Double(shapemakerlist.get(0),shapemakerlist.get(1),xloc-shapemakerlist.get(0),yloc-shapemakerlist.get(1)); //creating the circle
                    choosershapelist.add(a); //adds to list so it can be redrawn
                    choosercolorlist.add(Dot.getColor()); //adds to list so it can remember color
                    shapemakerlist.clear(); //clears the list so x&y coordinates aren't re-used
                    repaint();
                    circledraw = null; //resets to null so it has to wait for menu click to create another circle
                }
                if (shapemakerlist.isEmpty() == true && circledraw != null)
                {
                    shapemakerlist.add(xloc); //saves the x&y coordinates until the second click
                    shapemakerlist.add(yloc);
                }
            }
        }
    }
    
    private class SquareCreatorListener extends MouseAdapter
    {
        public SquareCreatorListener()
        {
            
        }
        public void mouseClicked(MouseEvent me)
        {
            int xloc = me.getX(); //getting x & y locations
            int yloc = me.getY();
            if (squaredraw != null) //if cahgned from null when menu option is selected
            {
                if (shapemakerlist.isEmpty() == false) //the click that creates the circle; has to be first for the reasons stated above
                {
                    Rectangle2D.Double a = new Rectangle2D.Double(shapemakerlist.get(0),shapemakerlist.get(1),xloc-shapemakerlist.get(0),yloc-shapemakerlist.get(1)); //creating the square
                    choosershapelist.add(a); //adds to list so it can be redrawn
                    choosercolorlist.add(Dot.getColor()); //adds to list so it can remember color
                    shapemakerlist.clear(); //clears so x&y coordinates aren't re-used
                    repaint();
                    squaredraw = null; //resests to null so it has to wait for menu selection to create another square
                }
                if (shapemakerlist.isEmpty() == true && squaredraw != null)
                {
                    shapemakerlist.add(xloc);//saves the x&y coordinates
                    shapemakerlist.add(yloc);
                }
            }
        }
    }
    
    public void paintComponent(Graphics g) //the paintComponent that does all of the actual drawing
    {
        super.paintComponent(g);
        
        Graphics2D g2 = (Graphics2D) g;
        
        Integer x; //Initializing integers to be used for iteration
        Integer y;
        g2.setPaint(Color.black); 
        if (DoodleFrame.img != null) //the actual printing of the background image, as well as centering it; placed first so it will be behind the other drawings
        {
            int xcenter = (600-DoodleFrame.img.getWidth(null))/2; //finding the center horizontally
            int ycenter = (600-DoodleFrame.img.getHeight(null))/2; //finding the center vertically
            g2.drawImage(DoodleFrame.img,xcenter,ycenter,this); //drawing the image and placing it in the center of the screen
        }
        if (choosershapelist.isEmpty() == false) //takes the shapes that were created from listeners and draws them on the screen (plus draws the previous ones that were made )
        {
            for (y=0; y<choosershapelist.size(); y=y+1)
            {
                g2.setPaint(choosercolorlist.get(y)); //sets the paint to the color it needs to be for that particular shape
                g2.draw(choosershapelist.get(y)); //draws the actual shape
                g2.fill(choosershapelist.get(y)); //fills the shape with that right color
            }
        }
        for (x=0; x < drawlist.size(); x=x+1) //draws the lines that were made by the user
        {
            g2.setPaint(colorlist.get(x)); //sets the paint to the color it needs to be for the particular line
            g2.draw(drawlist.get(x)); //draws the actual squares or circles that make the line
            g2.fill(drawlist.get(x)); //fills in those shapes so it eventually can look like a line
        }
        
        repaint();
    }
}