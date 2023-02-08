/**
 * Pitchers in the game
 * @author Catherine
 */
public class Pitcher {
	public int size = 0;
	public int contents = 0;
	
	public Pitcher(int nSize) {
		size = nSize;
	}
	public Pitcher(int nSize, int nContents) {
		size = nSize;
		contents = nContents;
	}
	
	public void fill() {
		contents = size;
	}
	
	public void empty() {
		contents = 0;
	}
	
	public void pourToX(Pitcher X) {
		if(X.size < contents) {
			X.contents = X.size;
		}
		else {
			X.contents = contents;
		}
		contents = 0;
	}
	
	
}
