int isPalendrum(char* s, int i, int j){
    while(i < j){
        if(s[i] != s[j])
            return 0;
        i++; j--;
    }
    return 1;
}

char * longestPalindrome(char * s){
    int size = 0;
    for(char* c=s; *c; c++)
        size++;
    int fst, snd;
    fst = snd = 0;
    for(int i=0; i < size; i++)
        for(int j=size-1; j >= i; j--){
            if(snd - fst < j - i && isPalendrum(s, i, j))
                fst = i, snd = j;
        }
    s[snd+1] = 0;
    return s + fst;
}