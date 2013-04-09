
/**
 *
 * @author gerisc01
 */

import javax.swing.*;
import javax.swing.event.*;
import java.awt.*;
import java.util.*;

public class JTunesPlaylistTableView extends JPanel
{
    private JTable playlistview;
    static JTunesPlaylistView viewPlaylists;
    static int currentPlaylist = 0;
    private JTunesMainTableView jtMainTable;
    private ArrayList<PlaylistClass> selectedPlaylist;
    private String additionStatus = "off";

    public JTunesPlaylistTableView(JTunesMainTableView back)
    {
        //Initializes the playlist view class as well as creates the main table in JTunesMainTable
        super();
        jtMainTable = back;
        viewPlaylists = new JTunesPlaylistView();
        jtMainTable.createTable(); //JTunesMainTable initialized here because it needs playlist elements to be create, and had to have those created before it could be created

        //Makes playlist table and scroll pane
        playlistview = new JTable(viewPlaylists);
        JScrollPane scpane = new JScrollPane(playlistview);
        this.add(scpane);

        //Shows the playlist table what its selection model needs to be (single selection) along with adding a listener for the table
        playlistview.getSelectionModel().setSelectionMode(ListSelectionModel.SINGLE_SELECTION);
        playlistview.getSelectionModel().addListSelectionListener(new PlaylistTableListener());

        //sets the size for the Playlist table
        Dimension d = playlistview.getPreferredSize();
        d.setSize(200,400);
        playlistview.setPreferredScrollableViewportSize(d);

        //A shortcut to get to the list of all the playlists
        selectedPlaylist = JTunesPlaylistTableView.viewPlaylists.getPlaylists();
    }

    public void addPlaylist(PlaylistClass myplaylist)
    {
        //playlist add to the table and calling addPlaylistToTable method which fires Table Changes
        additionStatus = "on";
        viewPlaylists.getPlaylists().add(myplaylist);
        viewPlaylists.addPlaylistToTable();
        //this.updateUI();

    }

    public JTunesPlaylistView getPlaylistView() {
        return viewPlaylists; //Returns the Playlist View
    }

    private class PlaylistTableListener implements ListSelectionListener {

        public PlaylistTableListener()
        {
        }

        public void valueChanged(ListSelectionEvent le) {
            if (!le.getValueIsAdjusting()) {
                //Sets the song index equal to the index of it in the table
                if (additionStatus == "off") {
               viewPlaylists.setSelectedPlaylistIndex(playlistview.convertRowIndexToModel(playlistview.getSelectedRow())); }
               additionStatus = "off";
               currentPlaylist = viewPlaylists.getSelectedPlaylistIndex(); //gives the index of the playlist that is currently selected
               jtMainTable.getTable().setModel(selectedPlaylist.get(currentPlaylist).getPlaylist()); //refreshes the main table so that it corresponds to the songs in the playlist currently selected
            }
        }
    }

}
