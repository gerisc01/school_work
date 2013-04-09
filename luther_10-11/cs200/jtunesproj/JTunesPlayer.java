/**
 * @author Matt Rubins, Scott Gerike, and Evan Larson
 * The main class of the program. This class class everything together and
 * runs the program.
 */

//imports
import javazoom.jlgui.basicplayer.BasicPlayer;
import javazoom.jlgui.basicplayer.BasicController;
import javax.swing.JFrame;
import java.io.*;
import javax.xml.stream.*;

public class JTunesPlayer
{

    public static BasicController controls;
    public static BasicPlayer player;

    public static void main(String[] args) throws FileNotFoundException, XMLStreamException
    {

        BasicPlayer player = new BasicPlayer();
        controls = (BasicController)player;

        JTunesFrame jtFrame = new JTunesFrame();
        
        XMLReader reader = new XMLReader(jtFrame);
        reader.readXML();

        PlayerListener plistener = new PlayerListener(jtFrame);
        player.addBasicPlayerListener(plistener);

	jtFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
	jtFrame.setVisible(true);
    }

}
