import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;


public class Swe
{
    public static void main(String[] args) throws NumberFormatException, IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        final int size = 8;
        for(int i=0;i<10;i++)
        {
        	StringBuffer sb = new StringBuffer();
        	sb.append("#").append(i+1).append(" ");
        	int len = Integer.parseInt(br.readLine());
        	char[][] arr = new char[8][8];
        	int count = 0;
        	
        	for(int j=0;j<size;j++)
        	{
        		String temp = br.readLine();
        		for(int k=0;k<size;k++)
        		{
        			arr[j][k] = temp.charAt(k);
        		}
        	}
        	
        	for(int j=0;j<size;j++)
        	{
        		for(int k=0;k<size-len+1;k++)
        		{
        			char[] temp1 = new char[len];
        			char[] temp2 = new char[len];
        			//부분문자열
        			for(int x = 0;x<len;x++)
        			{
        				temp1[x] = arr[j][k+x];
        				temp2[x] = arr[k+x][j];
        			}
        			int flag1=0;
        			int flag2=0;
        			
        			//검사
        			for(int x=0;x<len/2;x++)
        			{
        				flag1++;
        				flag2++;
        				if(!(temp1[x]==temp1[len-1-x]))
        				{
        					flag1=0;
        				}
        				if(!(temp2[x]==temp2[len-1-x]))
        				{
        					flag2=0;
        				}
        			}
        			if((int)len/2==flag1)
        			{
        				count++;
        			}
        			if((int)len/2==flag2)
        			{
        				count++;
        			}
        			
        		}
        	}
        	
        	sb.append(count);
        	System.out.println(sb);
        }
    }
}