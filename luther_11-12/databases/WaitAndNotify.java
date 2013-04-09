//Scott Gerike
//Bretton Finch

public class WaitAndNotify {
	public static void main(String[] args) {
			Thread t = new Thread(new MainThread());
			t.start();
			/*try {
				t.sleep(5000);
			} catch (InterruptedException ie) {
				ie.printStackTrace();
			}*/
		}
}

class MainThread implements Runnable {
	public void run() {
		int threadNum = 0;
		//SyncObject so = new SyncObject();
		while (threadNum != 5) {
			String threadString = Integer.toString(threadNum);
			System.out.println(threadString);
			Thread t = new Thread(new TimerThread());
			t.setName(threadString);
			t.start();
			//so.waitThread(t);
			threadNum ++;
			//so.awake()
		notifyAll();
	}
}
}
class TimerThread implements Runnable {
	   private String name = "";
		public void run() {
				//while(true) {
					System.out.println("Thread " + name + " started");
				//}
		}
		
		public String getName() {
			return name;
		}
		
		public void setName(String aStr) {
			name = aStr;
		}
	}
class SyncObject {
	synchronized public void waitThread(Thread t) {
		try {
			wait();
		}
		catch (InterruptedException ie) {}
	}
	public void awake(Thread t) {
		t.notifyAll();
	}
}