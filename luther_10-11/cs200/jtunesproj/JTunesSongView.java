/**
 * @author Matt Rubins, Scott Gerike, and Evan Larson
 * Class for setting up the table view using the AbstractTableModel Class
 */

//imports 
import javax.swing.table.AbstractTableModel;
import java.util.ArrayList;

public class JTunesSongView extends AbstractTableModel 
{
    private int selectedIndex;
    private ArrayList<JTunesSongClass> songs;

    public JTunesSongView() 
    {
        super();
        songs = new ArrayList<JTunesSongClass>();
    }

    //get the row count as integer
    public int getRowCount() 
    {
        return songs.size();
    }

    //get the row count as integer
    public int getColumnCount()
    {
        return 6;
    }

    //get value at certain row and column and check to return that value
    public Object getValueAt(int row, int col) 
    {
        if (col == 0)
        {
           return songs.get(row).getSongName(); 
        }          
        else
        {
            if (col == 1)
            {
                return songs.get(row).getArtistName();
            }
            else
            {
                if (col == 2)
                {
                    return songs.get(row).getAlbumName();
                }
                else
                {
                    if (col == 3)
                    {
                        return songs.get(row).getTrackNum();
                    }
                    else
                    {
                        if (col == 4) 
                        {
                            songs.get(row).convertMicroToMin();
                            return songs.get(row).getViewDuration();
                        }
                        else
                        {
                            if (col == 5)
                            {
                                return songs.get(row).getRating();
                            }
                            else
                            {
                                return 0;
                            }
                        }
                    }
                }
            }
        }
    }


    //Setting Column Names
    //@Override
    public String getColumnName(int col)
    {
        String [] cnames = {"Title" , "Artist" , "Album" , "Track Number" , "Duration" , "Rating"};
        return cnames[col];
    }

    //returns the arraylist of JTunesSong
    public ArrayList<JTunesSongClass> getSongList()
    {
        return songs;
    }

    //sets the SongList of the arraylist of newSongs
    public void setSongList(ArrayList<JTunesSongClass> newSongList)
    {
        songs = newSongList;
    }

    //sets the Selected Song Index to x as an integer
    public void setSelectedSongIndex(Integer x)
    {
        selectedIndex = x;
    }

    //returns the song index as an integer
    public int getSelectedSongIndex()
    {
        return selectedIndex;
    }

    //returns the song at selected Index
    public JTunesSongClass getSelectedSong()
    {
        return songs.get(selectedIndex);
    }

}