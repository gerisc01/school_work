public class SieveNode extends Thread
{
	private SyncBuffer leftBuff;
	private float nodeNum;
	private SyncBuffer rightBuff;
	SieveNode(SyncBuffer s, int i)
	{
		leftBuff = s;
		nodeNum = i;
	}
	public void run()
	{
		while (true){
			int value = leftBuff.get();
			float division = value/nodeNum;
			if (division % 1 == 0.0) {
				System.out.println(value + " is NOT a prime number");
			}
			else {
				if (rightBuff == null){
					rightBuff = new SyncBuffer();
					Thread t = new Thread(new SieveNode(rightBuff,value));
					t.start();
					System.out.println(value + " is a PRIME NUMBER");
				}
				else {
					rightBuff.put(value);
				}
			}
		}
	}
}