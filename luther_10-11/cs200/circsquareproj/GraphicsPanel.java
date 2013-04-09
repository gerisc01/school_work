import javax.swing.JPanel;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import javax.swing.JButton;
import java.util.Random;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.geom.*;
import java.util.ArrayList;
import java.awt.Shape;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.awt.event.MouseAdapter;

public class GraphicsPanel extends JPanel
{
    private Random r = new Random();
    private Rectangle2D.Double square = null;
    private Ellipse2D.Double circle = null;
    private ArrayList<Shape> drawlist = new ArrayList<Shape>();
    public GraphicsPanel()
    {
        super();
        JButton randcolorbutton = new JButton("Change Background");
        randcolorbutton.addActionListener (new RandomButtonListener());
        this.add(randcolorbutton);
        
        JButton squarebutton = new JButton("Square");
        squarebutton.addActionListener(new SquareListener());
        squarebutton.addMouseListener(new MouseShapeListener());
        this.add(squarebutton);
        
        JButton circlebutton = new JButton("Circle");
        circlebutton.addActionListener(new CircleListener());
        circlebutton.addMouseListener(new MouseShapeListener());
        this.add(circlebutton);
        
        JButton clearbutton = new JButton("Clear");
        clearbutton.addActionListener(new ClearListener());
        this.add(clearbutton);
        
        this.addMouseListener(new MouseButtonListener());
    }
    
    private class RandomButtonListener implements ActionListener
    {
        public RandomButtonListener()
        {
            
        }
        public void actionPerformed(ActionEvent ae)
        {
            Color randcolor = new Color(r.nextInt(256),r.nextInt(256),r.nextInt(256));
            setBackground(randcolor);
        }
    }
    
    private class SquareListener implements ActionListener
    {
        public SquareListener()
        {
            
        }
        public void actionPerformed(ActionEvent ae)
        {
            square = new Rectangle2D.Double(r.nextInt(450),r.nextInt(450),50,50);
            drawlist.add(square);
            repaint();
        }
    }
    
    private class CircleListener implements ActionListener
    {
        public CircleListener()
        {
            
        }
        public void actionPerformed(ActionEvent ae)
        {
            circle = new Ellipse2D.Double(r.nextInt(450),r.nextInt(450),50,50);
            drawlist.add(circle);
            repaint();
        }
    }
    
    private class ClearListener implements ActionListener
    {
        public ClearListener()
        {
            
        }
        public void actionPerformed(ActionEvent ae)
        {
            drawlist.clear();
            repaint();
        }
    }
    
    private class MouseButtonListener extends MouseAdapter
    {
        public MouseButtonListener()
        {
            super();
        }
        public void mouseEntered(MouseEvent me)
        {
            square = null;
            circle = null;
            drawlist.clear();
            repaint();
        }
        public void mouseClicked(MouseEvent me)
        {
            int xloc = me.getX();
            int yloc = me.getY();
            square = new Rectangle2D.Double(xloc,yloc,50,50);
            drawlist.add(square);
            repaint();
        }
    }
    
    private class MouseShapeListener extends MouseAdapter
    {
        public MouseShapeListener()
        {
            super();
        }
        public void mouseEntered(MouseEvent me)
        {
            square = null;
            circle = null;
            drawlist.clear();
            repaint();
        }
    }
    
    public void paintComponent(Graphics g)
    {
        super.paintComponent(g);
        
        Graphics2D g2 = (Graphics2D) g;
        Integer x;
        if (circle != null | square != null)
        {
            for (x=0; x < drawlist.size(); x=x+1)
            {
                g2.draw(drawlist.get(x));
                g2.fill(drawlist.get(x));
                repaint();
            }
        }
        
    }
}
