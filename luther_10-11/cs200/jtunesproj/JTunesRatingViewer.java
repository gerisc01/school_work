

/**
 *
 * @author larsev01
 */
import javax.swing.*;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Rectangle2D;
import java.awt.Color;

import java.util.ArrayList;

public class JTunesRatingViewer extends JPanel {

    private JTunesFrame jtframe;
    private Integer rating;

    public JTunesRatingViewer(JTunesFrame jtf) {
        super();
        jtframe = jtf;
        rating = 0;
    }

    public void paintComponent(Graphics g)
   {
      super.paintComponent(g);

      Graphics2D g2 = (Graphics2D) g;

      /*Rectangle2D.Double rate1 = new Rectangle2D.Double(10,105,9,20);
      Rectangle2D.Double rate2 = new Rectangle2D.Double(30,95,9,30);
      Rectangle2D.Double rate3 = new Rectangle2D.Double(50,85,9,40);
      Rectangle2D.Double rate4 = new Rectangle2D.Double(70,75,9,50);
      Rectangle2D.Double rate5 = new Rectangle2D.Double(90,65,9,60);*/

      Rectangle2D.Double rate1 = new Rectangle2D.Double(15,40,9,20);
      Rectangle2D.Double rate2 = new Rectangle2D.Double(35,30,9,30);
      Rectangle2D.Double rate3 = new Rectangle2D.Double(55,20,9,40);
      Rectangle2D.Double rate4 = new Rectangle2D.Double(75,10,9,50);
      Rectangle2D.Double rate5 = new Rectangle2D.Double(95,0,9,60);

      ArrayList<Rectangle2D> ratingBars = new ArrayList<Rectangle2D>();
      ratingBars.add(rate1);
      ratingBars.add(rate2);
      ratingBars.add(rate3);
      ratingBars.add(rate4);
      ratingBars.add(rate5);

      Color mycolor = new Color(0,0,0);
      g2.setPaint(mycolor);

     //jtframe.getTable().getSongDataTable().getSelectedSong();
      if (jtframe.getProgressBar().getPlayState()) {
          rating = rating.valueOf(jtframe.getTable().getSongDataTable().getSelectedSong().getRating());

          for (Integer x = 0; x<rating; x=x+1) {
              g2.fill(ratingBars.get(x));
          }

          for (Integer x = ratingBars.size()-1; x > rating - 1; x=x-1) {
              g2.draw(ratingBars.get(x));
          }
      }
      else {
     
          g2.draw(rate1);
          g2.draw(rate2);
          g2.draw(rate3);
          g2.draw(rate4);
          g2.draw(rate5);
      }
      
      
   }

   public void redrawBars() {
       repaint();
   }
}
