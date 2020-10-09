import random
from collections import Counter
candidate_12 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"] # With decreasing utility
weights = [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

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


if __name__ == "__main__" :
    votes = []
    votes = add_votes(1, rational_voters_1_cand, votes)
    votes = add_votes(2, rational_voters_2_cand, votes)
    votes = add_votes(3, rational_voters_3_cand, votes)
    votes = add_votes(4, rational_voters_3_cand, votes)
    z = []
    #Rational Voters
    for v in votes:
        for x in v:
            z.append(x)

    #Strategic Voters
    for m in range(500):
        z.append("L")

    winners = Counter(z)
    print(winners)







