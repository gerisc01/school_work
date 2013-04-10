/* Where the menu bar lives, along with all of the menu options and menu listeners as well
  Also initialize the Dot class from here */

import javax.swing.*;
import java.awt.event.*;
import java.awt.*;
import java.util.*;

public class DoodleFrame extends JFrame
{
    static Color selectedColor; //used for changing the pen color
    static Image img = null; //used for the background image; initialized at null so paintComponent doesn't try to paint something that isn't there
    private DoodlePanel dpanel; 
    private Scanner sc1 = new Scanner(System.in); //used for the user importing the file name for the image 
    
    public DoodleFrame()
    {
        super();
        
        this.setSize(600,600);
        this.setTitle("Doodle Board");
        
        dpanel = new DoodlePanel();
        this.add(dpanel);
        
        JMenuBar menuBar = new JMenuBar(); //Creating the menu bar and adding the subsection called options
        setJMenuBar(menuBar);
        JMenu optionsMenu = new JMenu("Options");
        menuBar.add(optionsMenu);
        
        JMenuItem color = new JMenuItem("Pen Color"); //Creating the menu option to change the pen color
        optionsMenu.add(color);
        color.addActionListener (new ColorListener());
        
        JMenu penSize = new JMenu("Pen Size"); //Creating a sub-menu with options to change the Pen Size
        optionsMenu.add(penSize);
        JMenuItem large = new JMenuItem("Large"); //Creating the Large, Medium and Small options under the Pen Size sub-menu
        JMenuItem medium = new JMenuItem("Medium");
        JMenuItem small = new JMenuItem("Small");
        penSize.add(large); //Adding Action Listeners to menu options plus adding them to the Pen Size menu
        large.addActionListener (new LargePenSizeListener());
        penSize.add(medium);
        medium.addActionListener (new MediumPenSizeListener());
        penSize.add(small);
        small.addActionListener (new SmallPenSizeListener());
        
        JMenu penShape = new JMenu("Pen Shape"); //Creating the Pen Shape menu option 
        optionsMenu.add(penShape);
        ButtonGroup shapeGroup = new ButtonGroup(); //Creating the Button Group to have the Round and Square Pens in it so that Radio Buttons can be used
        JRadioButtonMenuItem roundPen = new JRadioButtonMenuItem("Round Pen"); //Creating Round Pen and Square Pen as Radio Buttons
        roundPen.setSelected(true);
        JRadioButtonMenuItem squarePen = new JRadioButtonMenuItem("Square Pen");
        shapeGroup.add(roundPen); //Adding them to the same group so they switch between each other correctly
        shapeGroup.add(squarePen);
        penShape.add(roundPen); //Adding Action Listeners to options plus adding them to the Pen Shape menu
        roundPen.addActionListener (new RoundPenListener()); 
        penShape.add(squarePen);
        squarePen.addActionListener (new SquarePenListener());
        
        JMenu shapeMaker = new JMenu("Shape Maker"); //Creating the Shape Maker sub-menu with Circle and Square under it
        optionsMenu.add(shapeMaker);
        JMenuItem shapeCircle = new JMenuItem("Circle");
        JMenuItem shapeSquare = new JMenuItem("Square");
        shapeMaker.add(shapeCircle); // Adding Action Listeners and adding them to Shape Maker sub-menu
        shapeCircle.addActionListener (new CircleListener());
        shapeMaker.add(shapeSquare);
        shapeSquare.addActionListener (new SquareListener());
        
        JMenuItem importBackground = new JMenuItem("Import Background Image"); //Option for Importing a Background item to the center of the Doodle Board
        optionsMenu.add(importBackground);
        importBackground.addActionListener(new BackgroundListener());
        
        //Initializing the Size, Shape, and Color for the Dot class (because it's a static class)
        Dot.setShape(Dot.r);
        Dot.setSize(Dot.small);
        Dot.setColor(Dot.defaultColor);
        
    }
    
    
    private class ColorListener implements ActionListener //Uses the JColorChooser to switch the colors of the Pen
    {
        public ColorListener()
        {
            
        }
        public void actionPerformed(ActionEvent ae)
        {
            Color defaultColor = Dot.getColor(); // Getting the default color so it can show up in the JColorChooser as the default
            Color selectedColor = JColorChooser.showDialog(DoodleFrame.this ,"Choose Pen Color", defaultColor);
            if (selectedColor != null) // So that if the window is cancelled out, it doesn't change the color to null
            {
                Dot.setColor(selectedColor);
            }
        }
    }
    
    private class LargePenSizeListener implements ActionListener //Setting pen to large using static variable in Dot class
    {
        public LargePenSizeListener()
        {
            
        }
        public void actionPerformed(ActionEvent ae)
        {
            Dot.setSize(Dot.large);
        }
    }
    
    private class MediumPenSizeListener implements ActionListener //Setting pen to medium using static variable in Dot class
    {
        public MediumPenSizeListener()
        {
            
        }
        public void actionPerformed(ActionEvent ae)
        {
            Dot.setSize(Dot.medium);
        }
    }
    
    private class SmallPenSizeListener implements ActionListener //Setting pen to small using static variable in Dot class (Default)
    {
        public SmallPenSizeListener()
        {
            
        }
        public void actionPerformed(ActionEvent ae)
        {
            Dot.setSize(Dot.small);
        }
    }
    
    private class RoundPenListener implements ActionListener // Changes to round pen using static variable in Dot class (Default)
    {
        public RoundPenListener()
        {
            
        }
        public void actionPerformed(ActionEvent ae)
        {
            Dot.setShape(Dot.r);
        }
    }
    
    private class SquarePenListener implements ActionListener //Changes to square pen using static variable in Dot class
    {
        public SquarePenListener()
        {
            
        }
        public void actionPerformed(ActionEvent ae)
        {
            Dot.setShape(Dot.s);
        }
    }
    
    private class CircleListener implements ActionListener //Changes the variable from null so that Listener in DoodlePanel can be activated to draw Circle
    {
        public CircleListener()
        {
            
        }
        public void actionPerformed(ActionEvent ae)
        {
            DoodlePanel.circledraw = "draw";
        }
    }
    
    private class SquareListener implements ActionListener //Changes the variable from null so that Listener in DoodlePanel can be activated to draw Square
    {
        public SquareListener()
        {
            
        }
        public void actionPerformed(ActionEvent ae)
        {
            DoodlePanel.squaredraw = "draw";
        }
    }
    
    private class BackgroundListener implements ActionListener //Changes the Image variable img from null to a image so that it can be drawn by paintComponent
    {
        public BackgroundListener()
        {
            
        }
        public void actionPerformed(ActionEvent ae)
        {
            System.out.print("File Name (Make sure the file is in same directory as the program): "); //Prompt posted for the user in the terminal
            String inputtedImage = sc1.nextLine(); //the file name that the user inputted from the terminal -- needs to be in the same directory as this program to make it work easiest (just less typing for user)
            img = Toolkit.getDefaultToolkit().getImage(inputtedImage); //takes the file name and then inputs an actual image that can be drawn
        }
    }
}