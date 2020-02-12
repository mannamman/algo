import java.util.Scanner;
import java.io.FileInputStream;

class Solution
{
	public static void main(String args[]) throws Exception
	{
		Scanner sc = new Scanner(System.in);
		int T = sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int num = sc.nextInt();
            int[] array = new int[5];
            while(true){
                int check = 0;
            	if(num%2==0){
                	array[0]++;
                    num = num/2;
                    check++;
                }
                else if(num%3==0){
                	array[1]++;
                    num = num/3;
                    check++;
                }
                else if(num%5==0){
                	array[2]++;
                    num = num/5;
                    check++;
                }
                else if(num%7==0){
                	array[3]++;
                    num = num/7;
                    check++;
                }
                else if(num%11==0){
                	array[4]++;
                    num = num/11;
                    check++;
                }
    			if(check<1){
                	break;
                }
            }
            System.out.print("#"+test_case+" ");
            
            for(int j=0;j<5;j++){
            	System.out.print(array[j]+" ");
            }
            System.out.print("\n");
		}
	}
}