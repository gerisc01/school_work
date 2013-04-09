/**
 *
 * @author Matt Rubins,Evan Larson, Scott Gerike
 * The XML Parsing read file
 *
 * Created on November 22
 * Last Updated(What changed)
 */
import java.util.List;
import org.jdom.*;
import org.jdom.input.*;
import java.io.File;

public class XMLParsing {

    //public static void main(String[] args) {

    private JTunesFrame jtFrame;

    public XMLParsing(JTunesFrame jFramer) {
        jtFrame = jFramer;
    }

    public void readXML() {
        SAXBuilder builder = new SAXBuilder();
        try {
            String exfile = "/User/scottgerike/Documents/Luther 10-11/CS 200/jtunesproj/musiclib.xml";

            System.out.println("Getting ready to read XML!");
            Document doc = builder.build(new File(exfile));
            Element root = doc.getRootElement();
            List directoryList = root.getChildren();

            for (Object oMusicLib : directoryList) {
                Element directory = (Element) oMusicLib;
                String directoryName = directory.getAttributeValue("name");

                List artistList = directory.getChildren();

                for (Object oArtist : artistList) {
                    Element artist = (Element) (oArtist);
                    String artistName = artist.getAttributeValue("name");

                    List albumList = artist.getChildren();

                    for (Object oAlbum : albumList) {
                        Element album = (Element) (oAlbum);
                        String albumName = album.getAttributeValue("name");

                        List songList = album.getChildren();

                        for (Object osong : songList) {
                            Element song = (Element) osong;
                            String sname = song.getChildText("title");
                            String slength = song.getChildText("length");
                            String sFrames = song.getChildText("frameLength");
                            String sTrack = song.getChildText("trackNumber");
                            String sRating = song.getChildText("rating");
                            String sPath = song.getChildText("path");
                            System.out.println("The song name is: " + sname);
                            System.out.println("The Artist is: " + artistName);
                            System.out.println("The Album is: " + albumName);
                            System.out.println("The Track Number is: " + sTrack);
                            System.out.println("The Length is: " + slength);
                            System.out.println("The Rating is: " + sRating);
                            System.out.println("The Path is: " + sPath);

                            JTunesSongClass newSong = new JTunesSongClass(sname, artistName, albumName,
                                    slength,sFrames, sTrack, sRating, sPath);
                            jtFrame.getTable().addSong(newSong);

                        }
                    }
                }
            }
        } catch (Exception ex) {
            ex.printStackTrace();
        }
    }
}

