import random
from collections import Counter
candidate_12 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"] # With decreasing utility
weights = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

negative_weights = [1,2,3,4,5,6,7,8,9,10,11,12]

strategic_negative_weights = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 0]

strategic_voters_L = 500
rational_voters_1_cand = 200 
rational_voters_2_cand = 300 # Rational voters picking two candidates
rational_voters_3_cand = 200 # Rational voters picking three candidates
rational_voters_4_cand = 300


# for x in range(rational_voters_1_cand):
#     data = random.choices(candidate_12, weights = weights, k=1)
#     votes.append(data)


def add_votes(voter_k, voter_number, votes):
    for x in range(voter_number):
        data = random.choices(candidate_12, weights = weights, k=voter_k)
        votes.append(data)
    return votes

def add_negative_votes(voter_k, voter_number, votes):
    for x in range(voter_number):
        data = random.choices(candidate_12, weights = negative_weights, k=voter_k)
        votes.append(data)
    return votes





if __name__ == "__main__" :
    votes = []
    votes = add_votes(1, rational_voters_1_cand, votes)
    votes = add_votes(2, rational_voters_2_cand, votes)
    votes = add_votes(3, rational_voters_3_cand, votes)
    votes = add_votes(4, rational_voters_4_cand, votes)
    z = []
    #Rational Voters
    for v in votes:
        for x in v:
            z.append(x)

    #Strategic Voters
    for m in range(500):
        z.append("L")

    winners = Counter(z)

    negative_votes = []
    negative_votes = add_negative_votes(1, rational_voters_1_cand, negative_votes)
    negative_votes = add_negative_votes(2, rational_voters_2_cand, negative_votes)
    negative_votes = add_negative_votes(3, rational_voters_3_cand, negative_votes)
    negative_votes = add_negative_votes(3, rational_voters_4_cand, negative_votes)
    # print(negative_votes)

    nz = []
    
    # Strategic voters plan 1
    for m in range(strategic_voters_L):
        nz.append("A")
        nz.append("B")
        nz.append("C")
        nz.append("D")
        nz.append("E")
        nz.append("F")
        nz.append("G")
        nz.append("H")
        nz.append("I")
        nz.append("J")
        nz.append("K")

    # Strategic Plan 2, limiting the number of negative votes to 4
    # for x in range(strategic_voters_L):
    #     data = random.choices(candidate_12, weights = strategic_negative_weights, k=4)
    #     negative_votes.append(data)
    
    
    for nv in negative_votes:
        for nx in nv:
            nz.append(nx)
    





    
    negative_votes_count = Counter(nz)
    print("positive votes", winners)
    print("negative votes", negative_votes_count)
    finalresult = {}
    print(winners["A"]-negative_votes_count["A"])
    print(winners["L"]-negative_votes_count["L"])

   







