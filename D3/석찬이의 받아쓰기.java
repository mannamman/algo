Scanner sc = new Scanner(System.in);
		int T;
		T=sc.nextInt();
		for(int test_case = 1; test_case <= T; test_case++)
		{
			int length = sc.nextInt();
			String[] array_ori =sc.next().split("");
			String[] array_write = sc.next().split("");
			int cnt=0;
			for(int i=0;i<length;i++) {
				if(array_ori[i].equals(array_write[i])) {
					cnt++;
				}
			}
			System.out.println("#"+test_case+" "+cnt);
		}