/* Scott Gerike
A Stack Class implemented with an ArrayList
methods: empty, peek, pop, push */
import java.util.ArrayList;
public class DoubleStack
{
    private ArrayList<Double> items;
    public DoubleStack()
    {
        items = new ArrayList<Double>();
    }
    public boolean empty()
    {
        return items.isEmpty();
    }
    public Double peek()
    {
        return items.get(items.size());
    }
    public Double pop()
    {
        Double value = items.get(items.size()-1);
        items.remove(items.size()-1);
        return value;
    }
    public void push(Double a)
    {
        items.add(a);
    }
    public Integer size()
    {
        return items.size();
    }
    public String toString()
    {
        String print;
        print = "bottom ";
        Integer x;
        for (x = 0; x < items.size(); x=x+1)
        {
            print = print + items.get(x) + " ";
        }
        print = print + "top";
        return print;
    }
    public boolean equals(Object obj)
    {
        if (obj == null)
        {
            return false;
        } else{
        if (this == obj)
        {
            return true;
        }
        else {if (obj instanceof DoubleStack)
                {DoubleStack otherobj = (DoubleStack)obj;
                return this.items.equals(otherobj.items);}
                else { return false; }}}
    }
}