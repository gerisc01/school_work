/**
 * @author Matt Rubins, Scott Gerike, and Evan Larson
 * This class is in charge of the progress bar panel for JTunes
 */

import javax.swing.*;
import javax.swing.event.*;

public class JTunesProgressBarPanel extends JPanel
{
   //declaration of variables
   private JTunesFrame jtFrame;
   private JProgressBar progressBar;
   private JLabel currentTime;
   private JLabel timeLeft;
   private Integer secondsLeft;
   private Integer minutesLeft;
   private Integer currentProgress;
   private Integer timeInMicroSec;
   private Integer timeInSec;
   private Integer timeInMinutes;
   private Integer finalTime;

   private boolean playing;


   public JTunesProgressBarPanel(JTunesFrame back)
   {
      super();

      jtFrame = back;

      //intitalizing information
      playing = false;
      progressBar = new JProgressBar();
      currentTime = new JLabel("00:00");
      currentProgress = 0;
      finalTime = 0;
      timeLeft = new JLabel("-00:00");
      progressBar.addChangeListener(new ProgressChangeListener());

      //add items to panel
      this.add(currentTime);
      this.add(progressBar);
      this.add(timeLeft);
   }

   public void setMax(Integer songLength)
   {
       progressBar.setMaximum(songLength);
       progressBar.setValue(0);
       System.out.println(progressBar.getMaximum());
   }

   public void setSongPlayerPosition(Integer position)
   {
       progressBar.setValue(position);
   }

   public void setUpSongInfo(String songLength)
   {
       finalTime = finalTime.valueOf(jtFrame.getTable().getSongDataTable().getSelectedSong().getLength()) / 1000000;
       timeLeft.setText(songLength);
       timeLeft.updateUI();
       JTunesSongClass mysong = jtFrame.getTable().getSongDataTable().getSelectedSong();
       playing = true;
       jtFrame.getRatingViewer().redrawBars();
   }

   //reset the time label
   public void resetTimeLabels()
   {
       currentProgress = 0;
       timeInMicroSec = 0;
       timeInSec = 0;
       timeInMinutes = 0;
       playing = false;
       currentTime.setText("00:00");
       timeLeft. setText("-00:00");
   }

   public boolean getPlayState()
   {
       return playing;
   }

   //progressChange listener
   public class ProgressChangeListener implements ChangeListener
   {
       public ProgressChangeListener()
       {
       }

       //Called whenever the state of the progress bar is called. Used to set the time labels on the progress bar.
       public void stateChanged(ChangeEvent ce) {
           currentProgress = currentProgress + 1;
           timeInMicroSec = currentProgress * 26122;
           timeInSec = timeInMicroSec / 1000000;
           this.setTimeLabel(timeInSec);
       }

       //Sets the label corresponding to the current song's progress based on the time ellapsed.
       public void setTimeLabel(Integer seconds)
       {
           timeInMinutes = seconds / 60;
           timeInSec = seconds;
           String secondsString = "00";
           String minString = "00";

           if (timeInMinutes >= 1)
           {
               timeInSec = seconds - (timeInMinutes * 60);
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

           currentTime.setText(minString + ":" + secondsString);
           this.setTimeLeftLabel(seconds);
       }

       public void setTimeLeftLabel(Integer seconds) 
       {
           secondsLeft = finalTime - seconds;
           minutesLeft = secondsLeft / 60;
           String remainingSecString = "00";
           String remainingMinString = "00";

           if (minutesLeft >= 1)
           {
               secondsLeft = secondsLeft - (minutesLeft * 60);
           }

           if (secondsLeft < 10)
           {
               remainingSecString = "0" + secondsLeft.toString();
           }

           else
           {
               remainingSecString = secondsLeft.toString();
           }

           if (minutesLeft < 10)
           {
               remainingMinString = "0" + minutesLeft.toString();
           }

           else
           {
               remainingMinString = minutesLeft.toString();
           }

           timeLeft.setText("-" + remainingMinString + ":" + remainingSecString);
       }
   }
}

