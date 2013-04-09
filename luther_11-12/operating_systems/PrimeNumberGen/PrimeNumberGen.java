public class PrimeNumberGen
{
	public static void main(String[] args)
	{
		SyncBuffer leftBuffer = new SyncBuffer();
		Thread t = new Thread(new SieveNode(leftBuffer,2));
		t.start();
		for (int i = 3; i <= 1000; i++){
			leftBuffer.put(i);
		}
	}
}