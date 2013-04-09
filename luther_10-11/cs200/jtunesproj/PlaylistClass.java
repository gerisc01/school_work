/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 *
 * @author gerisc01
 */

import java.util.*;
import javax.swing.*;

public class PlaylistClass {
    private String playlistName;
    private JTunesSongView playlistSongs;
    private ArrayList<JTunesSongClass> songs;
    private JTable jtable;

    public PlaylistClass(String listName)
    {
        //Sets the playlist name from the parameter as well as initializes a new JTunesSongView, a new song list, and a new JTable to be used for these playlist songs
        playlistName = listName;
        playlistSongs = new JTunesSongView();
        songs = new ArrayList<JTunesSongClass>();
        jtable = new JTable(playlistSongs);
    }

    public void setName(String name)
    {
        playlistName = name; //changes the name of the playlist
    }

    public String getName()
    {
        return playlistName; //gets the name of the playlist
    }

    public void addSong(JTunesSongClass song)
    {
        songs.add(song); //adds the songs to the ArrayList that stores the songs for the playlist
    }

    public JTunesSongView getPlaylist()
    {
        return playlistSongs; //get the JTuneSongView class for a particular playlist
    }

    public void addSongToTable(JTunesSongClass song)
    {
        //Adds a song to the SongView which then gets added to the table after the changes are fired and the UI is updated
        playlistSongs.getSongList().add(song);
        playlistSongs.fireTableDataChanged();
        jtable.updateUI();
    }

    public ArrayList<JTunesSongClass> getPlaylistSongs()
    {
        return songs; //returns the list that holds the songs for this particular playlist
    }

    public JTable getTable()
    {
        return jtable; //returns the table that holds the songs for this playlist
    }

}
