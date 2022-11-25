bool isPalindrome(int x){
    long int old = x;
    long int new = 0;
    while(x>0){
        new = new*10 + x%10;
        x = x/10;
    }
    return new==old;

}
