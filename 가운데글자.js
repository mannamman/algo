function solution(s) {
    let mid = s.length%2;
    if(mid===0){
        mid = s.length/2;
        return s[mid-1]+s[mid]
    }
    return s[Math.floor(s.length/2)];
}
