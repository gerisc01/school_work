import javax.swing.JFrame;

public class GraphicsFrame extends JFrame
{
    private GraphicsPanel gpanel;
    
    public GraphicsFrame()
    {
        super();
        
        this.setSize(500,500);
        this.setTitle("Graphics Example");
        
        gpanel = new GraphicsPanel();
        this.add(gpanel);
    }
}