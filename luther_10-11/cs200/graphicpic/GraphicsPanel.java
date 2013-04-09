import javax.swing.JPanel;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;
import java.awt.geom.Ellipse2D;
import java.awt.Color;

public class GraphicsPanel extends JPanel
{
    public GraphicsPanel()
    {
        super();
    }
    
    public void paintComponent(Graphics g)
    {
        super.paintComponent(g);
        
        Graphics2D g2 = (Graphics2D) g;
        
        Color ipodBase = new Color(0,204,102);
        g2.setPaint(ipodBase);
        Rectangle2D.Double ipod = new Rectangle2D.Double(150,50,200,350);
        g2.draw(ipod);
        g2.fill(ipod);
        g2.setPaint(Color.white);
        Rectangle2D.Double screen = new Rectangle2D.Double(165,65,170,135);
        g2.draw(screen);
        g2.fill(screen);
        g2.setPaint(Color.gray);
        Ellipse2D.Double scroll = new Ellipse2D.Double(175,220,150,150);
        g2.draw(scroll);
        g2.fill(scroll);
        g2.setPaint(Color.white);
        Ellipse2D.Double scrollcenter = new Ellipse2D.Double(226,270,50,50);
        g2.draw(scrollcenter);
        g2.fill(scrollcenter);
        g2.setPaint(Color.black);
        String song = "Fame<Infamy";
        String artist = "Fall Out Boy";
        String album = "Infinity on High";
        g2.drawString(song, 200, 110);
        g2.drawString(artist, 206, 130);
        g2.drawString(album, 198, 150);
        g2.setPaint(Color.lightGray);
        Rectangle2D.Double songlength = new Rectangle2D.Double(175, 160, 150, 15);
        g2.draw(songlength);
        g2.setPaint(Color.blue);
        Rectangle2D.Double songprogress = new Rectangle2D.Double(175,160, 80, 15);
        g2.draw(songprogress);
        g2.fill(songprogress);
        String progress = "1:39";
        String left = "-1:27";
        g2.setPaint(Color.black);
        g2.drawString(progress, 175, 190);
        g2.drawString(left, 290, 190);
        Rectangle2D.Double battery = new Rectangle2D.Double(300,75, 30, 12);
        g2.draw(battery);
        Rectangle2D.Double batteryremaining = new Rectangle2D.Double(300,75,5,11);
        Color lowbattery = new Color(204,0,0);
        g2.setPaint(lowbattery);
        g2.draw(batteryremaining);
        g2.fill(batteryremaining);
    }
}