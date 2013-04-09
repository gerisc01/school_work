/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author gerisc01
 */
import javax.swing.table.AbstractTableModel;
import java.util.*;

public class JTunesPlaylistView extends AbstractTableModel
{
    private int selectedIndex;
    private ArrayList<PlaylistClass> playlists;

    public JTunesPlaylistView()
    {
        //Sets it so that My Music is always showing when program opens, ArrayList holds all the playlist classes that are in the table
        selectedIndex = 0;
        playlists = new ArrayList<PlaylistClass>();
    }

    public int getRowCount()
    {
        return playlists.size(); //gets the amount of playlists in the table
    }

    public int getColumnCount()
    {
        return 1; //the only column is the playlist name, so it's always 1
    }

    public Object getValueAt (int row, int col)
    {
        return playlists.get(row).getName(); //gets the name of the playlist from the playlist class
    }

    public String getColumnName(int col) {
    String [] cnames = {"Playlists"}; //Sets the name of the column to "playlists"
    return cnames[col];
    }

    public void addPlaylistToTable() {
        this.fireTableDataChanged(); //updates the table to show the new info that has been added to the table
    }

    public ArrayList<PlaylistClass> getPlaylists() {
        return playlists; //returns the arrayList with all of the playlists in it
    }

    public void setSelectedPlaylistIndex(Integer x) {
        selectedIndex = x; //sets the selected playlist index to be used for the table to get whatever playlist is selected
    }

    public int getSelectedPlaylistIndex() {
        return selectedIndex; //used to set the selected index to whatever row is selected in the table
    }
}
