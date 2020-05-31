import collections
#HASH
#완주하지못한선수
participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
answer = ''
a = list(collections.Counter(participant)-collections.Counter(completion))
answer = a[0]
