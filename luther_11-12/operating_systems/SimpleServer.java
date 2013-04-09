import java.net.*;
import java.io.*;

public class SimpleServer
{
	public static void main(String[] args) {
		try {
			ServerSocket sock = new ServerSocket(6013);

			while(true) {
				Socket client = sock.accept();

				Thread t = new Thread(new ServerConnection(client));
				t.start();
				}
		}
		catch (IOException ioe) {
			System.err.println(ioe);
		}
	}
}

class ServerConnection extends Thread
{
	private Socket client;
	ServerConnection(Socket s)
	{
		client = s;
	}
	public void run()
	{
		try {
			InputStream in = client.getInputStream();
			BufferedReader bin = new BufferedReader(new InputStreamReader(in));

			PrintWriter pout = new PrintWriter(client.getOutputStream(), true);

			String line;
			while((line = bin.readLine()) != null) {
				if (line.equals("exit")) {
					in.close();
					pout.close();
					client.close();
				}
				else {
					InetAddress hostAddress = InetAddress.getByName(line);
					pout.println(hostAddress.getHostAddress());
				}
			}
		} catch (IOException ioe) {
			System.err.println(ioe);
		}
	}
}