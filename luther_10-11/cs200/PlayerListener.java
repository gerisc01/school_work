//PlayerListener.java

import javazoom.jlgui.basicplayer.BasicPlayerListener;
import javazoom.jlgui.basicplayer.BasicPlayerEvent;
import javazoom.jlgui.basicplayer.BasicController;

import java.util.Map;

public class PlayerListener implements BasicPlayerListener
{
    public PlayerListener()
    {
    }
    
    /**
	 * Open callback, stream is ready to play.
	 *
	 * properties map includes audio format dependant features such as
	 * bitrate, duration, frequency, channels, number of frames, vbr flag,
	 * id3v2/id3v1 (for MP3 only), comments (for Ogg Vorbis), ... 
	 *
	 * @param stream could be File, URL or InputStream
	 * @param properties audio stream properties.
	 */
	public void opened(Object stream, Map properties)
	{
		// Pay attention to properties. It's useful to get duration, 
		// bitrate, channels, even tag such as ID3v2.
		System.out.println("OPENED"+properties);		
	}
		
	/**
	 * Progress callback while playing.
	 * 
	 * This method is called severals time per seconds while playing.
	 * properties map includes audio format features such as
	 * instant bitrate, microseconds position, current frame number, ... 
	 * 
	 * @param bytesread from encoded stream.
	 * @param microseconds elapsed (<b>reseted after a seek !</b>).
	 * @param pcmdata PCM samples.
	 * @param properties audio stream parameters.
	 */
	public void progress(int bytesread, long microseconds, byte[] pcmdata, Map properties)
	{
		// Pay attention to properties. It depends on underlying JavaSound SPI
		// MP3SPI provides mp3.equalizer.
		System.out.println("PROGRESS"+properties);
	}
	
	/**
	 * Notification callback for basicplayer events such as opened, eom ...
	 *  
	 * @param event
	 */
	public void stateUpdated(BasicPlayerEvent event)
	{
		// Notification of BasicPlayer states (opened, playing, end of media, ...)
		System.out.println("UPDATE:"+event);
		
		if (event.getCode()==BasicPlayerEvent.STOPPED)
		{
			System.exit(0);
		}
	}
	
	public void setController(BasicController controller)
	{
	    System.out.println("SET CONTROLLER:"+controller);
	}
}