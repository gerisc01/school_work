/**
 *
 * @author Evan Larson, Matt Rubins, and Scott Gerike
 * This is the playerlistener. The author of this file is JavaZoom and was given
 * to us on the first day of the project. We added some addition information
 * to the file but did not initially create the file
 */

//imports used from the javazoom package
import javazoom.jlgui.basicplayer.BasicPlayerListener;
import javazoom.jlgui.basicplayer.BasicPlayerEvent;
import javazoom.jlgui.basicplayer.BasicController;

//imports used from java
import java.util.Map;

public class PlayerListener implements BasicPlayerListener
{
    //declaration of variables
    static Map songInfo;
    static Map songProgress;
    static Integer frameTotal = null;
    static Integer songPosition = null;
    static JTunesSongClass myNewSong;
    private JTunesFrame jtFrame;

    public PlayerListener(JTunesFrame frameBack)
    {
        jtFrame = frameBack;
        songInfo = null;
        songProgress = null;
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
                songInfo = properties;
                System.out.println("OPENED" + songInfo);
                //JTunesSongClass myNewSong = new JTunesSongClass(songInfo);

                myNewSong = new JTunesSongClass(songInfo);

                //Gets the frame length of the song when opened
                Object frameObject = songInfo.get("audio.length.frames");
                String frameString = frameObject.toString();
                frameTotal = frameTotal.valueOf(frameString);
                jtFrame.getProgressBar().setMax(frameTotal);
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
                songProgress = properties;
		System.out.println("PROGRESS"+songProgress);

                //While the song is playing the value of the Progress Bar is constantly being updated
                Object framePositionObject = songProgress.get("mp3.frame");
                String framePositionString = framePositionObject.toString();
                songPosition = songPosition.valueOf(framePositionString);
                jtFrame.getProgressBar().setSongPlayerPosition(songPosition);

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
                    jtFrame.getProgressBar().setSongPlayerPosition(0);
                    JTunesControlPanel.playButton.setText("Play");
                    JTunesControlPanel.state = "stopped";
                    jtFrame.getProgressBar().resetTimeLabels();
		}
	}

	public void setController(BasicController controller)
	{
	    System.out.println("SET CONTROLLER:"+controller);
	}

}
