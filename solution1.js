function solution(n, record) {
    var answer = [];
    var dictServer = {};
    for (let i = 1; i <= n; i++) {
        dictServer[i] = [];
    }
    record.forEach((user) => {
        var info = user.split(" ");
        var server = info[0];
        var nickName = info[1];
        if (dictServer[server].indexOf(nickName) == -1) {
            if (dictServer[server].length == 5) {
                dictServer[server].shift();
            }
            dictServer[server].push(nickName);
        }
    });
    for (let i = 1; i <= n; i++) {
        dictServer[i].forEach((element) => {
            answer.push(element);
        });
    }
    return answer;
}

testcase = [
    {
        n: 1,
        record: [
            "1 fracta",
            "1 sina",
            "1 hana",
            "1 robel",
            "1 abc",
            "1 sina",
            "1 lynn",
        ],
    },
    {
        n: 4,
        record: [
            "1 a",
            "1 b",
            "1 abc",
            "3 b",
            "3 a",
            "1 abcd",
            "1 abc",
            "1 aaa",
            "1 a",
            "1 z",
            "1 q",
            "3 k",
            "3 q",
            "3 z",
            "3 m",
            "3 b",
        ],
    },
];

testcase.forEach((element) => {
    var n = element["n"];
    var record = element["record"];
    console.log(solution(n, record));
});
