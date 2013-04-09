/**
 * @author Matt Rubins, Scott Gerike, and Evan Larson
 * A class that is responsible for keeping information about a song. 
 */

//imports
import java.util.Map;

public class JTunesSongClass {

    //declaration variables
    private String songName;
    private String artistName;
    private String albumName;
    private String duration;
    private String viewDuration;
    private String lengthInFrames;
    private String trackNumber;
    private String rating;
    private String path;
    private Integer timeInSec;

    public JTunesSongClass(Map properties) 
    {
        //gets the properties of song title as converts into a string
        Object propertiesObject = properties.get("title");
        songName = propertiesObject.toString();
        
        //gets the properties of author as converts into a string
        propertiesObject = properties.get("author");
        artistName = propertiesObject.toString();
        
        //gets the properties of album as converts into a string
        propertiesObject = properties.get("album");
        albumName = propertiesObject.toString();

        //gets the properties of song duration as converts into a string
        propertiesObject = properties.get("duration");
        duration = propertiesObject.toString();

        //gets the properties the number of song frames as converts into a string
        propertiesObject = properties.get("audio.length.frames");
        lengthInFrames = propertiesObject.toString();

        //get the class path of the song and converts into a string
        propertiesObject = properties.get("mp3.id3tag.track");
        trackNumber = propertiesObject.toString();

        //itinally starting rating and second to 0 and null
        rating = "0";
        timeInSec = null;

    }

    //JTunesSongClass allows us to use "get" information about the songs through
    //out the program
    
    public JTunesSongClass(String title, String artist, String album, String length, String frameNum, String trackNum, String rate, String songPath) 
    {
        songName = title;
        artistName = artist;
        albumName = album;
        duration = length;
        lengthInFrames = frameNum;
        trackNumber = trackNum;
        rating = rate;
        path = songPath;
    }

    //returns the song name
    public String getSongName() 
    {
        return songName;
    }

    //returns the Artist Name
    public String getArtistName() 
    {
        return artistName;
    }

    //return the Album Name
    public String getAlbumName() 
    {
        return albumName;
    }

    //return the song length
    public String getLength() 
    {
        return duration;
    }

    //returns the frame length
    public String getFrameLength()
    {
        return lengthInFrames;
    }

    //returns the track number
    public String getTrackNum() 
    {
        return trackNumber;
    }

    //returns the song rating
    public String getRating() 
    {
        return rating;
    }

    //return the class path
    public String getPath()
    {
        return path;
    }

    //return the song Duration
    public String getViewDuration() 
    {
        return viewDuration;
    }

    //sets the song's class path
    public void setPath(String pathName) 
    {
        path = pathName;
    }

    //sets the song rating
    public void setRating(String rate) 
    {
        rating = rate;
        System.out.println(rating);
    }

    //class to have the duration you see in the table be of the type Min:Sec.
    public void convertMicroToMin() 
    {
       String microSecString = duration;
       timeInSec = timeInSec.valueOf(microSecString) / 1000000;
       Integer timeInMinutes = timeInSec / 60;
       String secondsString = "00";
       String minString = "0";

       if (timeInMinutes >= 1)
       {
           timeInSec = timeInSec - (timeInMinutes * 60);
       }

       if (timeInSec < 10) 
       {
           secondsString = "0" + timeInSec.toString();
       }

       else
       {
           secondsString = timeInSec.toString();
       }

       if (timeInMinutes < 10)
       {
           minString = "0" + timeInMinutes.toString();
       }
       else
       {
           minString = timeInMinutes.toString();
       }

       viewDuration = (minString + ":" + secondsString);

       }

}


