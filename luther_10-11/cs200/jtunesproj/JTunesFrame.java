/**
 *
 * @author Evan, Matt and Scott
 */
//JTunesFrame for JTunes project
//Made by Matt Rubins, Scott Gerike, and Evan Larson - 11/06/10


import javax.swing.*;
import java.awt.*;
import javax.swing.table.*;
import java.awt.event.*;
import java.awt.BorderLayout;
import java.util.*;
import javazoom.jlgui.basicplayer.*;
import java.io.*;
import javax.xml.stream.*;


public class JTunesFrame extends JFrame
{

   //Panels that are stored within the frame
   private JTunesControlPanel jtControlPanel;
   private JTunesProgressBarPanel jtProgressPanel;
   private JTunesMainTableView jtTableView;
   private JTunesRatingViewer jtRatingView;
   private JTunesPlaylistTableView jtPlaylistTableView;

   //Menu Stuff
   private JMenuBar jtBar;
   private JMenu fileMenu;
   private JMenu helpMenu;
   private JMenuItem openFile;
   private JMenuItem exitFile;
   private JMenuItem setRating;
   private JFileChooser songSelector;
   private JFileChooser multipleSongSelector;
   private JMenuItem addToLibrary;
   private JMenuItem addPlaylist;
   private ArrayList libraryPathNames;
   private ArrayList<JMenuItem> menuItems;

   private JFrame errorView;
   private JTunesFrame myJTFrame = this;

   private String fileName;

   public JTunesFrame()
      {
	super();

        //creating a frame for the error message dialog box
        errorView = new JFrame();
               
	this.setSize(700,650);
	this.setTitle("JTunes Prototype 2.0");

	//Setting up Menu Bar
	jtBar = new JMenuBar();

	//Creating elements for "File" menu
	openFile = new JMenuItem("Open");
        setRating = new JMenuItem("Set Rating");
        addToLibrary = new JMenuItem("Add to Library");
        addPlaylist = new JMenuItem("Add Playlist");
	exitFile = new JMenuItem("Exit");

        //Creating elements for "Help" menu
        JMenu howTo = new JMenu("How To:");
        JMenuItem songHelp = new JMenuItem("Add a song");
        JMenuItem ratingHelp = new JMenuItem("Rating System");
        JMenuItem playlistHelp = new JMenuItem("Create a Playlist");

	//Setting Up Main Menus
	fileMenu = new JMenu("File");
        helpMenu = new JMenu("Help");

	//Creating a File Chooser for Open option
	songSelector = new JFileChooser();
	openFile.addActionListener(new SongChooserListener());
        multipleSongSelector = new JFileChooser();
        multipleSongSelector.setMultiSelectionEnabled(true);

	//Adding menu bar to frame and then items to the menu bar
	this.setJMenuBar(jtBar);
	jtBar.add(fileMenu);
        jtBar.add(helpMenu);

        //Adding Action Listeners to the menu items
	exitFile.addActionListener(new ExitListener());
        addToLibrary.addActionListener(new AddSongsListener());
        songHelp.addActionListener(new SongHelpListener());
        ratingHelp.addActionListener(new RatingHelpListener());
        playlistHelp.addActionListener(new NewPlaylistHelpListener());
        addPlaylist.addActionListener(new AddPlaylistListener());
        setRating.addActionListener(new SetRatingListener());


	//Adding elements to main menus
	fileMenu.add(openFile);
        fileMenu.add(addToLibrary);
        fileMenu.add(addPlaylist);
        fileMenu.add(setRating);
	fileMenu.add(exitFile);


        //Help Menu Stuff
        helpMenu.add(howTo);
        howTo.add(songHelp);
        howTo.add(ratingHelp);
        howTo.add(playlistHelp);

        //Adding Panels to the frame in their proper spot
        this.setLayout(new BorderLayout());

        JPanel jtSouthPanel = new JPanel();

	jtControlPanel = new JTunesControlPanel(this);
        jtProgressPanel = new JTunesProgressBarPanel(this);
        jtTableView = new JTunesMainTableView(this);
        jtPlaylistTableView = new JTunesPlaylistTableView(jtTableView);
        jtRatingView = new JTunesRatingViewer(this);

        jtSouthPanel.add(jtProgressPanel, BorderLayout.WEST);
        jtSouthPanel.add(jtRatingView, BorderLayout.EAST);

	this.add(jtControlPanel, BorderLayout.NORTH);
        this.add(jtTableView, BorderLayout.EAST);
        
        jtRatingView.setPreferredSize(new Dimension(120,100));
        this.add(jtPlaylistTableView, BorderLayout.WEST);
        this.add(jtSouthPanel, BorderLayout.SOUTH);

        //initializing the fileName at null and initializing a couple of arrayLists
        fileName = null;
        libraryPathNames = new ArrayList<String>();
        menuItems = new ArrayList<JMenuItem>();
        
      }

   //Getters for stuff we need, like the panels hooked up to the frame.
   public String getFileName()
   {
      return fileName;
   }

   public JTunesMainTableView getTable() {
       return jtTableView;
   }

   public JTunesProgressBarPanel getProgressBar() {
       return jtProgressPanel;
   }

   public JTunesControlPanel getControlPanel() {
       return jtControlPanel;
   }

   public JTunesRatingViewer getRatingViewer() {
       return jtRatingView;
   }

   public JTunesPlaylistTableView getPlaylistTableView() {
       return jtPlaylistTableView;
   }

   public ArrayList<JMenuItem> getMenuItems() {
       return menuItems;
   }

   private class SongChooserListener implements ActionListener //The action listener used for just opening files but not adding them to the library
   {
      public SongChooserListener()
      {
      }
	public void actionPerformed(ActionEvent e)
	{
	   songSelector.showOpenDialog(JTunesFrame.this);
	   fileName = songSelector.getSelectedFile().getPath();
           try
            {
                File mysong;
                mysong = new File(fileName);
                JTunesPlayer.controls.open(mysong); //opens the song that was selected
                JTunesPlayer.controls.play(); //plays the song that was selected, but progress bar doesn't work
            }
           catch (BasicPlayerException bpe)
            {
               //error pops up if you try to add .mp3 file that doesn't work
               JOptionPane wrongFileType = new JOptionPane(errorView, JOptionPane.ERROR_MESSAGE);
               wrongFileType.showMessageDialog(errorView, "We're Sorry, but we are unable to open files of that type.", "Wrong File Type",
               JOptionPane.ERROR_MESSAGE);
                bpe.printStackTrace();
            }
	}
   }

   private class AddSongsListener implements ActionListener
   {
       public AddSongsListener()
       {
       }
       public void actionPerformed(ActionEvent e)
       {
           multipleSongSelector.showOpenDialog(JTunesFrame.this); //allows multiple files to be added to the library
           File[] files = multipleSongSelector.getSelectedFiles(); //puts the selected file(s) into the File arrayList
           int size = files.length;
           int x;
           for (x=0; x<size; x=x+1) { //iterates through the File arrayList opening each song, eventually adding that song to the table
           fileName = files[x].getPath();
           try
           {
               JTunesPlayer.controls.open(new File(fileName));
           }
           catch (BasicPlayerException bpe)
           {
               bpe.printStackTrace();
           }
           catch (NullPointerException npe)
           {
               JFrame frame = new JFrame();
               // show a joptionpane dialog using showMessageDialog
               JOptionPane.showMessageDialog(frame,"We're Sorry, but we are unable to import a file of that type",
                       "Incompatable File Type", JOptionPane.ERROR_MESSAGE);
               fileName = null;
           }

           (PlayerListener.myNewSong).setPath(fileName);

           if (!(libraryPathNames.contains((PlayerListener.myNewSong).getPath()))){
           jtTableView.addSong(PlayerListener.myNewSong);
           JTunesPlaylistTableView.viewPlaylists.getPlaylists().get(0).getPlaylistSongs().add(PlayerListener.myNewSong);
           jtTableView.refreshTable();
           libraryPathNames.add((PlayerListener.myNewSong).getPath());
           }
           }
       }
   }

   private class AddPlaylistListener implements ActionListener
   {
       public AddPlaylistListener()
       {
       }

       public void actionPerformed(ActionEvent e)
       {
           //Brings up a dialog box and asks for a playlist name, and then adds a playlist class to the playlist table with that name as long as the cancel option wasn't selected
           String playlistname = JOptionPane.showInputDialog(null, "Playlist Name?", "Enter the name of the Playlist", JOptionPane.QUESTION_MESSAGE);
           if (playlistname != null) {PlaylistClass myNewPlaylist = new PlaylistClass(playlistname);
           jtPlaylistTableView.addPlaylist(myNewPlaylist);
           JMenuItem playlist = new JMenuItem(playlistname);
           jtTableView.getAddToPlaylistMenu().add(playlist);
           menuItems.add(playlist);
           playlist.addActionListener(new AddToPlaylistListener()); }

           }
           
       }


   private class SetRatingListener implements ActionListener
   {
       public SetRatingListener()
       {
       }

       public void actionPerformed(ActionEvent e) //sets the rating for a song
       {
           Object[] possibilities = {"Badass", "I'd listen to that some more", "It's okay I guess", "Meh", "Please don't make me listen to that again"};
            String s = (String)JOptionPane.showInputDialog(
                    null,
                    "Set the Rating for your song:\n"
                    ,
                    "Set Your Song Rating",
                    JOptionPane.PLAIN_MESSAGE,
                    null,
                    possibilities,
                    "");
            //If a string was returned, say so.
            if ((s != null) && (s.length() > 0)) {
                if (s.equals("Badass")) {
                    s = "5";
                    jtTableView.getSongDataTable().getSelectedSong().setRating(s);
                    jtTableView.getSongDataTable().fireTableDataChanged();
                    jtTableView.updateUI();;
                }
                else if (s.equals("I'd listen to that some more")) {
                    s = "4";
                    jtTableView.getSongDataTable().getSelectedSong().setRating(s);
                    jtTableView.getSongDataTable().fireTableDataChanged();
                    jtTableView.updateUI();
                }
                else if (s.equals("It's okay I guess")) {
                    s = "3";
                    jtTableView.getSongDataTable().getSelectedSong().setRating(s);
                    jtTableView.getSongDataTable().fireTableDataChanged();
                    jtTableView.updateUI();
                }
                else if (s.equals("Meh")) {
                    s = "2";
                    jtTableView.getSongDataTable().getSelectedSong().setRating(s);
                    jtTableView.getSongDataTable().fireTableDataChanged();
                    jtTableView.updateUI();
                }
                else if (s.equals("Please don't make me listen to that again")) {
                    s = "1";
                    jtTableView.getSongDataTable().getSelectedSong().setRating(s);
                    jtTableView.getSongDataTable().fireTableDataChanged();
                    jtTableView.updateUI();
                }
            }
       }
   }

   private class ExitListener implements ActionListener
   {
      public ExitListener()
      {
      }
	public void actionPerformed(ActionEvent e) //If the program is exited in this way the XML is written to the file
	{
           try
           {
               XMLSimpleWriter xmlSaver = new XMLSimpleWriter(myJTFrame);
           }
           catch (FileNotFoundException fnf)
           {
               fnf.printStackTrace();
           }
           catch (XMLStreamException swe)
           {
               swe.printStackTrace();
           }
           
	   System.exit(0);
	}
   }

   private class SongHelpListener implements ActionListener {

       public SongHelpListener()
       {
       }

       public void actionPerformed(ActionEvent e) {
           JFrame frame = new JFrame();
           // show a joptionpane dialog using showMessageDialog
           JOptionPane.showMessageDialog(frame,"If you want to add a song to your library, go to the File menu, and then select 'Add to Library'\n" +
                   "A file navigator will appear and from there you can select a .mp3 file to add to your music library.\n" +
                   "Unfortuanetly not every .mp3 file can be added due to encoding issues.","Adding a Song", JOptionPane.PLAIN_MESSAGE);
       }

   }
   private class RatingHelpListener implements ActionListener {

     public RatingHelpListener()
     {
     }

     public void actionPerformed(ActionEvent e)
     {
           JFrame frame = new JFrame();
           // show a joptionpane dialog using showMessageDialog
           JOptionPane.showMessageDialog(frame,"If you want to rate a song in your library, go to the File menu, and then select 'Set Rating' '\n" +
                   "A Drop down menu will appear and from there you can select a feeling on the song. 'Badass' is a 5 rating and '\n" +
                   "Please Don't make me listen to that again' is a 1. ENJOY!!","Rating a Song", JOptionPane.PLAIN_MESSAGE);
       }

   }

   private class NewPlaylistHelpListener implements ActionListener {

       public NewPlaylistHelpListener()
       {
       }

       public void actionPerformed(ActionEvent e) {
           JFrame frame = new JFrame();
           // show a joptionpane dialog using showMessageDialog
           JOptionPane.showMessageDialog(frame,"If you want to add a new playlist, go to the File menu, and then select 'Add Playlist'\n" +
                   "A prompt will appear and from there you type in a name to give your playlist.\n" + "To then add a song to that playlist, select a song and" +
                   " right click on it\n" + "and select: Add to Playlist -> and select the playlist you want to add to."
                   ,"Adding a Playlist", JOptionPane.PLAIN_MESSAGE);
       }

   }

   public void AddActionListenerDifferentClass(JMenuItem jmi) {
       jmi.addActionListener(new AddToPlaylistListener());
   }

   private class AddToPlaylistListener implements ActionListener {
       public AddToPlaylistListener()
       {
       }
       public void actionPerformed(ActionEvent e)
       {
           Object source = e.getSource();
           source = (JMenuItem)source;
           int itemIndex = menuItems.indexOf(source);
           JTunesPlaylistTableView.viewPlaylists.getPlaylists().get(itemIndex + 1).getPlaylistSongs().add(jtTableView.getSongDataTable().getSelectedSong());
           JTunesPlaylistTableView.viewPlaylists.getPlaylists().get(itemIndex + 1).addSongToTable(jtTableView.getSongDataTable().getSelectedSong());
  
       }
  }
}