import java.awt.Dimension;

import javax.swing.JFrame;

public class DBbrowser {
	public static void main(String[] args) {
		QueryFrame qFrame = new QueryFrame();
		qFrame.pack();
		qFrame.setPreferredSize(new Dimension(300, 300));
		qFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		qFrame.setVisible(true);
		
		
	}
}
