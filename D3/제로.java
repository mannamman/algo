Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int num = sc.nextInt();
			int[] array = new int[num];
			int pointer=0;
			int sum=0;
			for(int i=0;i<num;i++)
			{
				int check = sc.nextInt();
				if(check==0)
				{
					sum = sum-array[pointer-1];
					pointer--;
				}
				else
				{
					array[pointer] = check;
					sum = sum+array[pointer];
					pointer++;
				}
			}
			System.out.println("#"+test_case+" "+sum);
		}