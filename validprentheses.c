bool isValid(char * s){
    int len=0;
    int i=0;
    while(*(s+i)) {//find len of s without changing it
        len++;
        i++;
    }
    printf("%d",i);
    char* stack;
    stack = (char*)calloc(len+1, sizeof(char));
    int last=-1;  // -1 means stack is empty
    char op;
    i=0;
    while(*(s+i)){
        if (s[i]=='(' || s[i]=='[' || s[i]=='{'){
            stack[++last]=s[i];   // "push"
        }
        else{
            switch(s[i]){
                case ')':
                    op = '(';
                    break;
                case ']':
                    op = '[';
                    break;
                case '}':
                    op = '{';
                    break;          
            }
            printf("%c \n stack= %s",op,stack);
            if(last<0 || last>=len || stack[last]!=op){  //if we cant pop, or the popped value is not according to what should be
                free(stack);
                return false;
            }
            --last;
        }
       i++; 
    }
    free(stack);
    return (last==-1);    
}
