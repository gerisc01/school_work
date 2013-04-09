import javax.swing.JPanel;
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JButton;
import java.util.Random;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class GraphicsPanel extends JPanel
{
    private Random r = new Random();
    public GraphicsPanel()
    {
        super();
        JButton randcolorbutton = new JButton("Change Background");
        randcolorbutton.addActionListener (new RandomButtonListener());
        this.add(randcolorbutton);
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
    public void paintComponent(Graphics g)
    {
        
    }
}