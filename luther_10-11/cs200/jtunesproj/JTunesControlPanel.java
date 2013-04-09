/**
 *
 * @author larsev01
 */
//JTunesControlPanel for JTunes project
//Made by Matt Rubins, Scott Gerike, and Evan Larson - 11/06/10
//Last edited 11/20/10 (Added Pause Functionality)

import javax.swing.*;
import javax.swing.event.ChangeListener;
import java.awt.event.*;
import java.io.File;
import javazoom.jlgui.basicplayer.BasicPlayerException;
import javax.swing.event.ChangeEvent;

public class JTunesControlPanel extends JPanel{

   static JTunesFrame jtFrame;

   public static JButton playButton;
   private JButton stopButton;
   private JButton nextSongButton;
   private JButton lastSongButton;
   public static String state;
   private JSlider volumeControl;

   private JTunesSongClass mysong;
   private JTunesSongClass playingSong;


   public JTunesControlPanel(JTunesFrame back){

      super();

      jtFrame = back;

      //Make Control Buttons
      playButton = new JButton("Play");
      stopButton = new JButton("Stop");
      nextSongButton = new JButton("Next Song");
      lastSongButton = new JButton("Previous Song");

      //create volume Slider
      volumeControl = new JSlider(0,100);

      //Add Action Listeners
      playButton.addActionListener(new PlayButtonListener());
      stopButton.addActionListener(new StopButtonListener());
      volumeControl.addChangeListener(new VolumeSlidderListener());
      lastSongButton.addActionListener(new LastSongListener());
      nextSongButton.addActionListener(new NextSongListener());

      
      this.add(lastSongButton);
      this.add(playButton);
      this.add(stopButton);
      this.add(nextSongButton);
      this.add(volumeControl);
   }

   public JTunesSongClass getPlayingSong() {
       return playingSong;
   }

   private class LastSongListener implements ActionListener{
       public LastSongListener(){

       }
       public void actionPerformed(ActionEvent e){
           try{

           JTunesSongClass mysong;
           int songNum;
           songNum = JTunesPlaylistTableView.viewPlaylists.getPlaylists().get(JTunesPlaylistTableView.currentPlaylist).getPlaylist().getSelectedSongIndex();

           if(songNum == 0){
               songNum = jtFrame.getTable().getSongDataTable().getSongList().size();
               mysong = jtFrame.getTable().getSongDataTable().getSongList().get(songNum-1);
               JTunesPlayer.controls.open(new File(mysong.getPath()));
               JTunesPlayer.controls.play();

               JTunesPlaylistTableView.viewPlaylists.getPlaylists().get(JTunesPlaylistTableView.currentPlaylist).getPlaylist().setSelectedSongIndex(jtFrame.getTable().getSongDataTable().getSongList().size()-1);
               jtFrame.getProgressBar().setUpSongInfo(mysong.getLength());
               playButton.setText("Pause");
               state = "playing";
           }
           
           else {
               mysong = jtFrame.getTable().getSongDataTable().getSongList().get(songNum-1);
               JTunesPlayer.controls.open(new File(mysong.getPath()));
               JTunesPlayer.controls.play();

               JTunesPlaylistTableView.viewPlaylists.getPlaylists().get(JTunesPlaylistTableView.currentPlaylist).getPlaylist().setSelectedSongIndex(songNum - 1);
               jtFrame.getProgressBar().setUpSongInfo(mysong.getLength());
               playButton.setText("Pause");
               state = "playing";
           }      
          }
           catch (BasicPlayerException bpe){
                bpe.printStackTrace();
            }

       }
   }

     private class NextSongListener implements ActionListener{

       public NextSongListener(){

       }
       public void actionPerformed(ActionEvent e){

           try{

           JTunesSongClass mysong;
           int songNum;

           songNum = JTunesPlaylistTableView.viewPlaylists.getPlaylists().get(JTunesPlaylistTableView.currentPlaylist).getPlaylist().getSelectedSongIndex();
           System.out.println(jtFrame.getTable().getSongDataTable().getSongList().size());


           if(jtFrame.getTable().getSongDataTable().getSongList().size()-1 == songNum) {
               mysong = jtFrame.getTable().getSongDataTable().getSongList().get(0);
               JTunesPlayer.controls.open(new File(mysong.getPath()));
               JTunesPlayer.controls.play();
               JTunesPlaylistTableView.viewPlaylists.getPlaylists().get(JTunesPlaylistTableView.currentPlaylist).getPlaylist().setSelectedSongIndex(0);
               jtFrame.getProgressBar().setUpSongInfo(mysong.getLength());
               playButton.setText("Pause");
               state = "playing";
           }
           
           else {
               mysong = jtFrame.getTable().getSongDataTable().getSongList().get(songNum+1);
               JTunesPlayer.controls.open(new File(mysong.getPath()));
               JTunesPlayer.controls.play();
               JTunesPlaylistTableView.viewPlaylists.getPlaylists().get(JTunesPlaylistTableView.currentPlaylist).getPlaylist().setSelectedSongIndex(songNum + 1);
               jtFrame.getProgressBar().setUpSongInfo(mysong.getLength());
               playButton.setText("Pause");
               state = "playing";
           }
          }
           catch (BasicPlayerException bpe)
           {
                bpe.printStackTrace();
            }
       }
   }

   private class PlayButtonListener implements ActionListener {
      public PlayButtonListener() {
          state = "stopped";
      }
      public void actionPerformed(ActionEvent e) {
        if (state == "stopped") {
            try {
                mysong = jtFrame.getTable().getSongDataTable().getSelectedSong();
                JTunesPlayer.controls.open(new File(mysong.getPath()));
                JTunesPlayer.controls.play();
                jtFrame.getProgressBar().setUpSongInfo(mysong.getViewDuration());
                JTunesPlayer.controls.setPan(0.0);
                playButton.setText("Pause");
                state = "playing";
                jtFrame.getRatingViewer().redrawBars();

            }
            catch (BasicPlayerException bpe) {
                bpe.printStackTrace();
            }
        }

        else {
        if (state == "paused") {
            try {
                playButton.setText("Pause");
                state = "playing";
                JTunesPlayer.controls.resume();
            }
            catch (BasicPlayerException bpe) {
                bpe.printStackTrace();
            }
          }
        else {
            try {
                playButton.setText("Play");
                state = "paused";
                JTunesPlayer.controls.pause();
            }
            catch (BasicPlayerException bpe) {
                bpe.printStackTrace();
            }
        }
       }
      }
   }

   public void SetPlayButtonText(String s)
   {
       playButton.setText(s);
   }

   private class StopButtonListener implements ActionListener  {

      public StopButtonListener()  {
      }

      public void actionPerformed(ActionEvent e)  {

	try {
            
            JTunesPlayer.controls.stop();
            playButton.setText("Play");
            state = "stopped";
            playingSong = null;
            jtFrame.getRatingViewer().redrawBars();
        }
        catch (BasicPlayerException bpe)
        {
            bpe.printStackTrace();
        }
      }

   }
   private class VolumeSlidderListener implements ChangeListener
   {
       public VolumeSlidderListener()
       {

       }
       public void stateChanged(ChangeEvent e)
       {

        try
        {
        JSlider volume = (JSlider) e.getSource();
        JTunesPlayer.controls.setGain(((double)volume.getValue())/100);
        }

        catch (BasicPlayerException bpe)
        {
            bpe.printStackTrace();
        }
       }

   }
}
