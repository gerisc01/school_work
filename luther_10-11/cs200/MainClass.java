import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class MainClass extends JPanel {

  public MainClass() {

    JButton btn1 = new JButton("Button1");
    btn1.addActionListener(new ButtonListener());
    add(btn1);

  }

  public static void main(String[] args) {
    JFrame frame = new JFrame();
    frame.getContentPane().add(new MainClass());

    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setSize(200, 200);
    frame.setVisible(true);
  }
}

class ButtonListener implements ActionListener {
  ButtonListener() {
  }

  public void actionPerformed(ActionEvent e) {
    if (e.getActionCommand().equals("Button1")) {
      System.out.println("Button1 has been clicked");
    }
  }
}