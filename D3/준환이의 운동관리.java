import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
 
public class Swe {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine());
        for(int i=0;i<T;i++) {
        	StringTokenizer st = new StringTokenizer(br.readLine());
        	StringBuffer str = new StringBuffer();
        	str.append("#").append(i+1).append(" ");
        	int min = Integer.parseInt(st.nextToken());
        	int max = Integer.parseInt(st.nextToken());
        	int act = Integer.parseInt(st.nextToken());
        	int result = min-act;
        	if(max<act) {
        		result = -1;
        	}
        	else if(act>=min) {
        		result = 0;
        	}
        	str.append(result);
        	System.out.println(str);
        }
    }
}