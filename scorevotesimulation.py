candidate_12 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"] # With decreasing utility
values = {
    "bad": 0,
    "average": 1,
    "good": 1.25,
    "best": 1.5
}


# Voter group: rational, idoits and corrupt

import random



def votecountfromdata(data):
    total = 0
    for x in data:
        total = total + x[1]
    
    return total


def votesbygroup(votersaccuracy, k, scores):
    o = 0
    myvotescount = {}
    for i in range(0, len(candidate_12), 3):
        
        for x in candidate_12[i:i+3]:
            weights = []
            population = []
            for s in scores:
                population.append([x, s])
            for m in range(0,4):
                if(o==m):
                    weights.append(votersaccuracy)
                else:
                    weights.append(0.3)
                
            # print("weights", weights)
            # print("population", population)
            data = random.choices(
                population = population,
                weights=weights,
                k = k
            )
            # print("data", data)
            votecount = votecountfromdata(data)
            # print("votecount"+ " " + x, votecount)
            myvotescount[x] = votecount
        o = o + 1
    return myvotescount

def corruptvoters(corruptionlevel, candidates_bribed_for, k, scores):
    o = 0
    myvotescount = {}
    for i in range(0, len(candidate_12), 3):
        
        for x in candidate_12[i:i+3]:
            weights = []
            population = []
            for s in scores:
                population.append([x, s])
            for m in range(0,4):
                # print(x, m)
                if(m == 0):
                    if x in candidates_bribed_for:
                        # print(x)
                        weights.append(corruptionlevel)
                    else:
                        weights.append(0.1)
                elif(m == 3):
                    if x not in candidates_bribed_for:
                        weights.append(corruptionlevel)
                    else:
                        weights.append(0.1)

                else:
                    weights.append(0.1)
                
            # print("weights", weights)
            # print("population", population)
            data = random.choices(
                population = population,
                weights=weights,
                k = k
            )
            # # print("data", data)
            votecount = votecountfromdata(data)
            # # print("votecount"+ " " + x, votecount)
            myvotescount[x] = votecount
        o = o + 1
    return myvotescount


def totalvotecount(data):
    myvotes = {}
    for can in candidate_12:
        totalvote = 0
        for d in data:
            totalvote = totalvote + d[can]
        myvotes[can] = totalvote
    
    return myvotes
        

def withscore(scores, vk, ck):
    voteraccuracy = 0.9
    rationalvoters = votesbygroup(voteraccuracy,vk, scores)    
    # print(rationalvoters)
    idiotsaccuracy = 0.7
    idiotsvoters = votesbygroup(idiotsaccuracy, vk, scores)
    # print(idiotsvoters)
    corruptionlevel = 0.9
    candidates_bribed_for = ["L"]
    corruption = corruptvoters(corruptionlevel, candidates_bribed_for, ck, scores)
    # print(corruption)
    allvotes = [rationalvoters, idiotsvoters, corruption]
    myvotes = totalvotecount(allvotes)
    return myvotes


if __name__ == "__main__" :
    vk = 1000
    ck = 2000
    scores = [1.25, 1.125, 1, 0]  
    score1 = withscore(scores, vk, ck)
    print(score1)
    print(score1["A"] - score1["L"])
    scores = [1.5, 1.25, 1, 0]
    score1 = withscore(scores, vk, ck)
    print(score1)
    print(score1["A"] - score1["L"])
    scores = [3, 2, 1, 0]
    score1 = withscore(scores, vk, ck)
    print(score1)
    print(score1["A"] - score1["L"])
    vk = 37500
    ck = 25000
    scores = [1.25, 1.125, 1, 0]  
    score1 = withscore(scores, vk, ck)
    print(score1)
    print(score1["A"] - score1["L"])
    scores = [1.5, 1.25, 1, 0]
    score1 = withscore(scores, vk, ck)
    print(score1)
    print(score1["A"] - score1["L"])
    scores = [3, 2, 1, 0]
    score1 = withscore(scores, vk, ck)
    print(score1)
    print(score1["A"] - score1["L"])

