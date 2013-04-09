/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author larsev01
 */
import javax.xml.stream.*;
import java.io.*;


public class XMLWriter {
    
    private File f;
    private XMLOutputFactory factory;
    private XMLStreamWriter writer;
    private String newLine;
    private String newTab;
    //private JTunesSongClass song;

    
    public XMLWriter() throws FileNotFoundException, XMLStreamException {
        

         f = new File("musicLib.xml");
         newLine = "\n";
         newTab = "  ";
    
         factory = XMLOutputFactory.newInstance();

         writer = factory.createXMLStreamWriter(new FileOutputStream(f));

         writer.writeDTD("<?xml version='1.0' encoding='UTF-8'?>");
         writer.writeCharacters(newLine);
         writer.writeStartElement("musicLibrary");
         writer.writeCharacters(newLine);

         writer.writeCharacters(newTab);
         writer.writeStartElement("directory");
         writer.writeAttribute("name" , "My Music");
         writer.writeCharacters(newLine);

         writer.writeCharacters(newTab + newTab);
         writer.writeStartElement("artist");
         writer.writeAttribute("name" , "Nickel Creek" );
         writer.writeCharacters(newLine);

         writer.writeCharacters(newTab + newTab + newTab);
         writer.writeStartElement("album");
         writer.writeAttribute("name", "This Side");
         writer.writeCharacters(newLine);

         writer.writeCharacters(newTab + newTab + newTab + newTab);
         writer.writeStartElement("song");
        // writer.writeCharacter("song");
         writer.writeCharacters(newLine);
         
         writer.writeCharacters(newTab + newTab + newTab + newTab + newTab);
         writer.writeStartElement("title");
         writer.writeCharacters("This Side");
         writer.writeEndElement();
         writer.writeCharacters(newLine);

         writer.writeCharacters(newTab + newTab + newTab + newTab + newTab);
         writer.writeStartElement("length");
         writer.writeCharacters("200090903");
         writer.writeEndElement();
         writer.writeCharacters(newLine);

         writer.writeCharacters(newTab + newTab + newTab + newTab + newTab);
         writer.writeStartElement("frameLength");
         writer.writeCharacters("20008");
         writer.writeEndElement();
         writer.writeCharacters(newLine);

         writer.writeCharacters(newTab + newTab + newTab + newTab + newTab);
         writer.writeStartElement("trackNumber");
         writer.writeCharacters("1");
         writer.writeEndElement();
         writer.writeCharacters(newLine);

         writer.writeCharacters(newTab + newTab + newTab + newTab + newTab);
         writer.writeStartElement("rating");
         writer.writeCharacters("3");
         writer.writeEndElement();
         writer.writeCharacters(newLine);

         writer.writeCharacters(newTab + newTab + newTab + newTab + newTab);
         writer.writeStartElement("path");
         writer.writeCharacters("/home/students/larsev01/ThisSide.mp3");
         writer.writeEndElement();
         writer.writeCharacters(newLine);

         writer.writeEndElement();
         writer.writeCharacters(newLine);
         writer.writeEndElement();
         writer.writeCharacters(newLine);
         writer.writeEndElement();
         writer.writeCharacters(newLine);
         writer.writeEndElement();
         writer.writeCharacters(newLine);
         writer.writeEndDocument();
    }
    
}
