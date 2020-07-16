function solution(a, b) {
    let answer = 0;
    let months = {
        1:31,
        2:29,
        3:31,
        4:30,
        5:31,
        6:30,
        7:31,
        8:31,
        9:30,
        10:31,
        11:30,
        12:31
    };
    let days = ['THU','FRI','SAT','SUN','MON','TUE','WED'];
    let daysum=b;
    for(var i in months){
        if(i==a){
            break;
        }
        daysum = daysum + months[i];
    }
    answer = days[(daysum%7)];
    
    return answer;
}
