/* Scott Gerike
  CS 200
Creating an evaluator for postfix equations using two scanners */

import java.util.*;
public class PostfixEvaluate
{
    public static void main (String [] args)
    {
        Scanner sc1;
        sc1 = new Scanner(System.in);
        System.out.print("Enter a Postfix equation: ");
        String line;
        line = sc1.nextLine();
        Scanner sc2;
        sc2 = new Scanner(line);
        Stack<Double> stack = new Stack<Double>();
        System.out.println(stack.size())
        while (sc2.hasNext() == true) {
            String nextvalue = sc2.next();
            if (nextvalue.equals("+"))
            {
                Double b = stack.pop();
                Double a = stack.pop();
                Double c = a + b;
                stack.push(c);
            } else{
            if (nextvalue.equals("-"))
            {
                Double b = stack.pop();
                Double a = stack.pop();
                Double c = a - b;
                stack.push(c);
            } else {
            if (nextvalue.equals("*"))
            {
                Double b = stack.pop();
                Double a = stack.pop();
                Double c = a * b;
                stack.push(c);
            } else {
            if (nextvalue.equals("/"))
            {
                Double b = stack.pop();
                Double a = stack.pop();
                Double c = a / b;
                stack.push(c);
            }                     
            else
            {
                Double dub = Double.parseDouble(nextvalue);
                stack.push(dub);
            }}}}
            
        }
        Double answer = stack.pop();
        System.out.println(answer);
    }
}