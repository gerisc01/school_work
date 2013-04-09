import java.util.ArrayList;
import javax.swing.table.AbstractTableModel;

public class QueryTableModel extends AbstractTableModel {
	private ArrayList<ArrayList<Object>> myList;
	private String[] columnList;
	
	public QueryTableModel(ArrayList<ArrayList<Object>> aList, String [] aColumnList) {
		myList = aList;
		columnList = aColumnList;
	}

	public int getColumnCount() {
		if (myList != null)
			return myList.get(0).size();
		return 0;
	}

	public int getRowCount() {
		if (myList != null)
			return myList.size();
		return 0;
	}

	public Object getValueAt(int row, int col) {
		if (myList != null)
			return myList.get(row).get(col);
		return null;
	}
	
	public String getColumnName(int col)
	    {
	        return columnList[col];
	    }

}
