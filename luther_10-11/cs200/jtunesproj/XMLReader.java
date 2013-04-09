/*
 * @author Evan Larson, Matt Rubins, and Scott Gerike
 * XML Class that reads from the XML file.
 */

//imports used
import java.io.IOException;
import java.util.List;
import java.util.logging.Level;
import java.util.logging.Logger;
import org.jdom.*;
import org.jdom.input.*;
import java.io.File;
import javax.swing.*;

public class XMLReader
{
    private JTunesFrame jtFrame;

    public XMLReader(JTunesFrame jFramer)
    {
        jtFrame = jFramer;
    }

    public void readXML()
    {
        SAXBuilder builder = new SAXBuilder();

        try
        {
            String exfile = "/Users/scottgerike/Documents/Luther 10-11/CS 200/jtunesproj/musiclib.xml";

            //build document and element in order to lookup the children and roots
            Document doc = builder.build(new File(exfile));
            Element root = doc.getRootElement();
            List directoryList = root.getChildren();

            //directoryList is the songs in the XML Writter
            for (Object oMusicLib : directoryList)
            {
                //get the name
                Element directory = (Element) oMusicLib;
                String directoryName = directory.getAttributeValue("name");
                PlaylistClass myplaylist;

                //get the playlist if any are present
                if (!directoryName.equals("My Music"))
                {
                    myplaylist = new PlaylistClass (directoryName);
                    jtFrame.getPlaylistTableView().addPlaylist(myplaylist);
                }

                //continue onto the rest of the file to get the other information
                else
                {
                    myplaylist = jtFrame.getPlaylistTableView().getPlaylistView().getPlaylists().get(0);
                }

                //get the children of the directory
                List songList = directory.getChildren();
                
                //iterate through the songlist to get the elements of the song
                for (Object osong : songList)
                {
                    Element song = (Element) osong;
                    String sname = song.getChildText("title");
                    String sArtist = song.getChildText("artist");
                    String sAlbum = song.getChildText("album");
                    String slength = song.getChildText("length");
                    String sFrames = song.getChildText("frameLength");
                    String sTrack = song.getChildText("trackNumber");
                    String sRating = song.getChildText("rating");
                    String sPath = song.getChildText("path");

                    //creat a new JTunesSongClass from the information in the songlist
                    JTunesSongClass newSong = new JTunesSongClass(sname, sArtist, sAlbum,
                                    slength,sFrames, sTrack, sRating, sPath);

                    //add song to the table
                    myplaylist.addSongToTable(newSong);
                    Integer playlistLocal = JTunesPlaylistTableView.viewPlaylists.getPlaylists().indexOf(myplaylist);
                    JTunesPlaylistTableView.viewPlaylists.getPlaylists().get(playlistLocal).getPlaylistSongs().add(newSong);

                    //add songs to playlist if any are present
                    if (myplaylist.getName() != "My Music")
                    {
                        JMenuItem jmenuitem = new JMenuItem(myplaylist.getName());
                        jtFrame.AddActionListenerDifferentClass(jmenuitem);
                        jtFrame.getMenuItems().add(jmenuitem);
                        jtFrame.getTable().getAddToPlaylistMenu().add(jmenuitem);
                    }
                }
            }
        }

        //catch and exceptions
        catch (JDOMException ex)
        {
            Logger.getLogger(XMLReader.class.getName()).log(Level.SEVERE, null, ex);
        }

        catch (IOException ex)
        {
            Logger.getLogger(XMLReader.class.getName()).log(Level.SEVERE, null, ex);
        }
    }
}