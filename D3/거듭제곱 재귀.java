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
    	for(int i=0;i<10;i++) {
    		int T = Integer.parseInt(br.readLine());
    		StringTokenizer st = new StringTokenizer(br.readLine());
    		StringBuffer str = new StringBuffer();
    		str.append("#").append(i+1).append(" ");
    		int left = Integer.parseInt(st.nextToken());
    		int right = Integer.parseInt(st.nextToken());
    		int result = fun1(left,right);
    		str.append(result);
    		System.out.println(str);
    	}
    }
    public static int fun1(int left,int right) {
    	if(right ==1) {
    		return left*right;
    	}
    	else {
    		return left*fun1(left,right-1);
    	}
    }
}