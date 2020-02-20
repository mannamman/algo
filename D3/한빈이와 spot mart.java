Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();
        for(int test_case = 1; test_case <= T; test_case++)
        {
            int num = sc.nextInt();
            int MaxWeight = sc.nextInt();
            int[] array = new int[num];
            int Max = -1;
            for(int i=0;i<num;i++) {
                array[i] = sc.nextInt();
            }
             
            for(int i =0;i<num;i++)
            {
                int sum=0;
                for(int j=num-1;j>i;j--)
                {
                    sum = array[i]+array[j];
                    if(sum>Max && sum<=MaxWeight) {
                        Max = sum;
                    }
                }
            }
            System.out.println("#"+test_case+" "+Max);
        }