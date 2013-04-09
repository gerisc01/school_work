public class SyncBuffer
{
   private int sharedvalue;
   private boolean valuepresent;

   public SyncBuffer()
   {
      valuepresent = false;
   }

   public synchronized void put(int item)
   {

         while (valuepresent)
            try
            {
               wait();
            }
            catch (InterruptedException ie)
            {}

         sharedvalue = item;
         valuepresent = true;
         notify();
      

   }

   public synchronized int get()
   {

         while (!valuepresent)
           try
           {
               wait();
           }
           catch (InterruptedException ie)
           {}

         valuepresent = false;
         notify();
         return sharedvalue;


   }
}
