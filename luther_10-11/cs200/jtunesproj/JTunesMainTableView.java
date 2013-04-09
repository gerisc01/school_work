/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author larsev01
 */
//Class for the actual Table View that uses the JTunesSongView class to populate
//Made by Matt Rubins, Scott Gerike, and Evan Larson - 11/21/10
//Last edited 11/22/10 (Works, but shows up too small when added to the JTunesFrame. Will have to talk to Ranum about sizing issues or look it up)
//Last edited 11/29/10 (Still a little too small. Added selection mode stuff. Almost ready to have play from table option.)


import javax.swing.event.*;
import javax.swing.*;
import java.awt.event.*;
import javazoom.jlgui.basicplayer.BasicPlayerException;
import java.io.File;
import java.util.*;


public class JTunesMainTableView extends JPanel {
    private JTable songView;
    private JTunesMainTableView jtMainView = this;
 
    //static JTable songView;
    private JTunesSongView viewSongs;
    private JPopupMenu rightClickMenu;
    private JMenuItem playPopupMenu;
    private JMenuItem stopPopupMenu;
    private JMenu addToPlaylist;
    private ArrayList<String> libraryPathNames;
    private String additionStatus = "off";

    private JTunesFrame jtFrame;
    
    public JTunesMainTableView(JTunesFrame back) {
        super();
        jtFrame = back;
    }

        public void createTable() {
        JTunesPlaylistTableView.viewPlaylists.getPlaylists().add(new PlaylistClass("My Music"));
        viewSongs = JTunesPlaylistTableView.viewPlaylists.getPlaylists().get(JTunesPlaylistTableView.currentPlaylist).getPlaylist();

        songView = new JTable(viewSongs);
        JScrollPane scpane = new JScrollPane(songView);
        //viewSongs.getSongList().add(new JTunesSongClass("This Side", "Nickle Creek", "Unknown", "5000000", "1000", "6", "4", "/home/students/gerisc01/Music/Kick-off.mp3"));


        songView.setAutoCreateRowSorter(true);

        songView.getSelectionModel().setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        songView.getSelectionModel().addListSelectionListener(new TableListener());

        this.add(scpane);

        //scpane.createVerticalScrollBar();
        //scpane.add(this);

        rightClickMenu = new JPopupMenu();
        playPopupMenu = new JMenuItem("Play");
        stopPopupMenu = new JMenuItem("Stop");
        addToPlaylist = new JMenu("Add to Playlist");

        rightClickMenu.add(playPopupMenu);
        rightClickMenu.add(stopPopupMenu);
        rightClickMenu.add(addToPlaylist);

        songView.setComponentPopupMenu(rightClickMenu);
        rightClickMenu.addMouseListener(new PopupMenuListener());
        playPopupMenu.addActionListener(new PlayRightClickListener());
        stopPopupMenu.addActionListener(new StopRightClickListener());
    }

    public JTunesSongView getSongDataTable() {
        return viewSongs;
    }

    public JMenu getAddToPlaylistMenu() {
        return addToPlaylist;
    }


    public void addSong(JTunesSongClass mysong) {
        additionStatus = "on";
        viewSongs.getSongList().add(mysong);
        viewSongs.fireTableDataChanged();
        //viewSongs.addSongToTable();
        this.updateUI();
    }

    public void refreshTable() {
        viewSongs.fireTableDataChanged();
        this.updateUI();
        System.out.println("updated");
    }

    public JTable getTable() {
        return songView;
    }

    private class TableListener implements ListSelectionListener {

        public TableListener() {

        }

        public void valueChanged(ListSelectionEvent le) {
            if (!le.getValueIsAdjusting()) {
                viewSongs = JTunesPlaylistTableView.viewPlaylists.getPlaylists().get(JTunesPlaylistTableView.currentPlaylist).getPlaylist();
                //songView.getSelectedRow();
                //System.out.println(songView.getValueAt(songView.getSelectedRow(),0));

                //Sets the song index equal to the index of it in the table.
                if (additionStatus == "off") {
               viewSongs.setSelectedSongIndex(songView.convertRowIndexToModel(songView.getSelectedRow())); }
                additionStatus = "off";
                //System.out.println(viewSongs.getSongList().get(songView.convertRowIndexToModel(songView.getSelectedRow())));
            }
        }

        //this.add(songView);
        
    }

    private class PopupMenuListener extends MouseAdapter
    {
        public PopupMenuListener()
        {
            
        }
        public void mouseClicked(MouseEvent e) 
        {
            if(rightClickMenu.isPopupTrigger(e))
            {
                rightClickMenu.show(e.getComponent(), e.getX(), e.getY());
            }
        }
        public void mouseReleased(MouseEvent e)
        {
            if(rightClickMenu.isPopupTrigger(e))
            {
                rightClickMenu.show(e.getComponent(), e.getX(), e.getY());
            }
        }
    }
    private class PlayRightClickListener implements ActionListener
    {
        public PlayRightClickListener()
        {

        }
        public void actionPerformed(ActionEvent e)
        {
           try
           {
               JTunesSongClass mysong;
               mysong = JTunesControlPanel.jtFrame.getTable().getSongDataTable().getSelectedSong();
               JTunesPlayer.controls.open(new File(mysong.getPath()));
               JTunesPlayer.controls.play();
               jtFrame.getProgressBar().setUpSongInfo(mysong.getLength());
               jtFrame.getControlPanel().SetPlayButtonText("Pause");
               JTunesControlPanel.state = "playing";

           }
           catch (BasicPlayerException bpe)
           {
                bpe.printStackTrace();
           }

        }
    }
   private class StopRightClickListener implements ActionListener
    {
        public StopRightClickListener()
        {

        }
        public void actionPerformed(ActionEvent e)
        {
           try
           {
               JTunesPlayer.controls.stop();
               JTunesControlPanel.state = "stopped";
           }
           catch (BasicPlayerException bpe)
           {
                bpe.printStackTrace();
           }

        }
    }
}

