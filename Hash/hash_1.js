function solution(participant, completion) {
    var answer = "";
    var dictObject = {};
    participant.forEach(function (each) {
        if (each in dictObject) {
            dictObject[each] += 1;
        } else {
            dictObject[each] = 1;
        }
    });
    completion.forEach(function (each) {
        dictObject[each] -= 1;
    });
    for (const [k, v] of Object.entries(dictObject)) {
        if (v > 0) {
            return k;
        }
    }
}

test = [
    {
        participant: ["leo", "kiki", "eden"],
        completion: ["eden", "kiki"],
    },
    {
        participant: ["marina", "josipa", "nikola", "vinko", "filipa"],
        completion: ["josipa", "filipa", "marina", "nikola"],
    },
    {
        participant: ["mislav", "stanko", "mislav", "ana"],
        completion: ["stanko", "ana", "mislav"],
    },
];

test.forEach(function (t) {
    participant = t["participant"];
    completion = t["completion"];
    console.log(solution(participant, completion));
});
