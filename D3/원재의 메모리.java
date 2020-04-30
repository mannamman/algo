package packtest2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Swe
{
    public static void main(String[] args) throws NumberFormatException, IOException
    {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	int T = Integer.parseInt(br.readLine());
    	for(int i=0;i<T;i++) {
    		StringTokenizer st = new StringTokenizer(br.readLine());
    		StringBuffer str = new StringBuffer();
    		str.append("#").append(i+1).append(" ");
    		String s = st.nextToken();
    		String[] arr = s.split("");
    		int count=0;
    		for(int j=1;j<arr.length;j++) {
    			if(!(arr[j-1].equals(arr[j]))) {
    				count++;
    				System.out.println(arr[j]+ " "+arr[j-1]);
    			}
    		}
    		if(arr[0].equals("1")) {
    			count++;
    		}
    		str.append(count);
    		System.out.println(str);
    	}
    }
    
}