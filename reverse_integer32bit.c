int reverse(long int x){
    
    long int out = 0;
    int flag=0;
    if(x<0){
        x=x*-1;
        flag = 1;
    }
    while(x!=0){
        long int rem = x%10;
        out = out*10+rem;
        x = x/10;
    }
    if(flag){
        out = out *-1;
    }
    if (( -2147483648 >out)||( out >2147483647)){
        return 0;
    }

    return out;
