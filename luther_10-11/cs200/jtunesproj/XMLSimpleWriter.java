/*
 * @author Evan Larson, Matt Rubins, and Scott Gerike
 * XML Class that writes the XML file.
 */

//imports
import javax.xml.stream.*;
import java.io.*;
import java.util.ArrayList;

public class XMLSimpleWriter {

    //declaration of variables
    private File f;
    private XMLOutputFactory factory;
    private XMLStreamWriter writer;
    private String newLine;
    private String newTab;
    private JTunesFrame myjtframe;
    private ArrayList<JTunesSongClass> songList;


    public XMLSimpleWriter(JTunesFrame jtframer) throws FileNotFoundException, XMLStreamException {

         myjtframe = jtframer;

         //writes the starting files
         //f = new File("musiclib.xml");
         newLine = "\n";
         newTab = "  ";
      
         factory = XMLOutputFactory.newInstance();
      
         writer = factory.createXMLStreamWriter(new FileOutputStream(new File("musicLib.xml")));
      
         //writes the starting code for the top of the file
         writer.writeDTD("<?xml version='1.0' encoding='UTF-8'?>");
         writer.writeCharacters(newLine);
         writer.writeStartElement("musicLibrary");
         writer.writeCharacters(newLine);
      
         //determines which directory will be written
         for (PlaylistClass myplaylist: JTunesPlaylistTableView.viewPlaylists.getPlaylists()) 
         {
             writer.writeCharacters(newTab);
             writer.writeStartElement("directory");
             writer.writeAttribute("name" , myplaylist.getName());
             writer.writeCharacters(newLine);
      
         //adds the songs to the xml file
         for (JTunesSongClass mysong: myplaylist.getPlaylistSongs())
         {
            //add song tage
            writer.writeStartElement("song");
            writer.writeCharacters(newLine);
      
            //add song title
            writer.writeStartElement("title");
            writer.writeCharacters(mysong.getSongName());
            writer.writeEndElement();
            writer.writeCharacters(newLine);
      
            //add artist name
            writer.writeStartElement("artist");
            writer.writeCharacters(mysong.getArtistName());
            writer.writeEndElement();
            writer.writeCharacters(newLine);
      
            //add ablum name
            writer.writeStartElement("album");
            writer.writeCharacters(mysong.getAlbumName());
            writer.writeEndElement();
            writer.writeCharacters(newLine);
      
            //add song length
            writer.writeStartElement("length");
            writer.writeCharacters(mysong.getLength());
            writer.writeEndElement();
            writer.writeCharacters(newLine);
      
            //add frame length
            writer.writeStartElement("frameLength");
            writer.writeCharacters(mysong.getFrameLength());
            writer.writeEndElement();
            writer.writeCharacters(newLine);
      
            //add track number
            writer.writeStartElement("trackNumber");
            writer.writeCharacters(mysong.getTrackNum());
            writer.writeEndElement();
            writer.writeCharacters(newLine);
      
            //add rating
            writer.writeStartElement("rating");
            writer.writeCharacters(mysong.getRating());
            writer.writeEndElement();
            writer.writeCharacters(newLine);
      
            //add class path
            writer.writeStartElement("path");
            writer.writeCharacters(mysong.getPath());
            writer.writeEndElement();
            writer.writeCharacters(newLine);
      
            //close elements/tags
            writer.writeEndElement();
            writer.writeCharacters(newLine);
         }
         //add file end tag
         writer.writeEndElement();
      }
       //end the file
       writer.writeEndDocument();

    }
}


