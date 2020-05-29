package packtest2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;


public class Swe
{
    public static void main(String[] args) throws NumberFormatException, IOException
    {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	final int T = Integer.parseInt(br.readLine());
    	for(int i=0;i<T;i++) {
    		int Max2 = 0;
    		int Max = 0;
    		int X = Integer.parseInt(br.readLine());
    		ArrayList<Integer> arr = new ArrayList<Integer>();
    		StringTokenizer st = new StringTokenizer(br.readLine());
    		StringBuffer str = new StringBuffer();
    		str.append("#").append(i+1).append(" ");
    		
    		for(int j=0;j<X;j++) {
    			int cur = Integer.parseInt(st.nextToken());
    			arr.add(cur);
    			if(j>0) {
    				int before = arr.get(j-1);
    				if(before<cur && Max<(cur-before)) {
        				Max = cur-before;
        			}
        			if(before>cur && Max2<(before-cur)) {
        				Max2 = before-cur;
        				System.out.println(Max2);
        			}
    			}
    		}
    		
    		str.append(Max).append(" ").append(Max2);
    		System.out.println(str);
    	}
    }
    
}