//had problems with getting browser to do multiple queries, so I just restarted program every time.
//I know that isn't right, but that's how I had to make it work

import java.awt.*;
import java.awt.event.*;
import java.util.*;
import javax.swing.*;

import java.sql.*;

public class QueryFrame extends JFrame {
	private JTable myTable;
	private ArrayList<ArrayList<Object>> myList = new ArrayList();
	private String queryValue = null;
	private JTextField tf1;
	private String [] columnValues;
	private JScrollPane scrollPane;
	private JFrame errorView;
	private int numColumns;
	
	private class RunQueryListener implements ActionListener {
		public RunQueryListener() {}
		
		public void actionPerformed(ActionEvent e) {
			queryValue = tf1.getText();
			Connection conn = null;
			Statement stmt;
			ResultSet rs = null;
			ResultSetMetaData rsmd = null;
			ArrayList<Object> row;
			
			try {
				Class.forName("com.mysql.jdbc.Driver").newInstance();
			}
				catch(ClassNotFoundException E) {
					JOptionPane.showMessageDialog(errorView, "Sorry, but this is not a valid SQL Statement", "Bad SQL Statement",
				               JOptionPane.ERROR_MESSAGE);}
				catch(InstantiationException e1) {
					JOptionPane.showMessageDialog(errorView, "Sorry, but this is not a valid SQL Statement", "Bad SQL Statement",
				               JOptionPane.ERROR_MESSAGE);}
				catch(IllegalAccessException e1) {
					JOptionPane.showMessageDialog(errorView, "Sorry, but this is not a valid SQL Statement", "Bad SQL Statement",
				               JOptionPane.ERROR_MESSAGE);}
			
			String dbURL = "jdbc:mysql://db.luther.edu/DairyDatabase";
			String userName = "gerisc01";
			String password = "2009champs";
			try {
				conn = DriverManager.getConnection(dbURL,userName,password);
			}
				catch (SQLException e1) {
					JOptionPane.showMessageDialog(errorView, "Sorry, but this is not a valid SQL Statement", "Bad SQL Statement",
				               JOptionPane.ERROR_MESSAGE);}
			
			try {
				stmt = conn.createStatement();
				rs = stmt.executeQuery(queryValue);
				rsmd = rs.getMetaData();
				
			}
				catch (SQLException e1) {
					JOptionPane.showMessageDialog(errorView, "Sorry, but this is not a valid SQL Statement", "Bad SQL Statement",
				               JOptionPane.ERROR_MESSAGE);}
			try {
				while (rs.next()){
					row = new ArrayList();
					for (int i=1; i<=rsmd.getColumnCount(); i++) {
						String name = rsmd.getColumnName(i);
						String columnValue = rs.getString(name);
						row.add(columnValue);
					}
					myList.add(row);
				}
				numColumns = rsmd.getColumnCount();
				columnValues = new String[numColumns];
				for (int i=1; i<=rsmd.getColumnCount(); i++) {
					columnValues[i-1] = rsmd.getColumnName(i);
				}
				QueryTableModel qtm = new QueryTableModel(myList,columnValues);
				myTable.setModel(qtm);
				if (numColumns > 5) {
					myTable.setAutoResizeMode(JTable.AUTO_RESIZE_OFF);}
				if (numColumns <= 5) {myTable.setAutoResizeMode(JTable.AUTO_RESIZE_SUBSEQUENT_COLUMNS);}
				
			}
				catch (SQLException e1){
					JOptionPane.showMessageDialog(errorView, "Sorry, but this is not a valid SQL Statement", "Bad SQL Statement",
		               JOptionPane.ERROR_MESSAGE);}
		}
	}
		
	public QueryFrame() {
		JPanel topPanel = new JPanel();
		this.setLayout(new BorderLayout());
		this.add(topPanel,BorderLayout.NORTH);
		myTable = new JTable();
		this.add(myTable,BorderLayout.SOUTH);
		JButton button = new JButton();
		button.setText("Run");
		button.addActionListener(new RunQueryListener());
		tf1 = new JTextField("Enter Query Here",60);
		topPanel.add(tf1);
		topPanel.add(button);
		JScrollPane scrollPane = new JScrollPane(myTable);
		scrollPane.setPreferredSize(new Dimension (900,700));
		scrollPane.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_AS_NEEDED);
		this.add(scrollPane, BorderLayout.CENTER);
		}
	}
