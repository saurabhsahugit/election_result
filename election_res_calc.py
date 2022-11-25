from dis import dis
from multiprocessing.sharedctypes import Value
from election_data import city1, city2, party_sym_lookup


def extract_votes_per_party(city1: dict, party_sym_lookup):
    """
    :param `city` is the consituency votes for all parties
    """
    vote_count = 0
    party_name = ''
    total_votes = 0
    for constituency, votes_cast in city1.items():
        # for votes_cast in constituency:
            #print(party_votes)
            for key, value in votes_cast.items():
                print(key, value)
                vote_count +=  votes_cast[key]
                if key in party_sym_lookup:
                    party_name = party_sym_lookup[key]
                else:
                    party_name = 'Data Error'

    total_votes += vote_count
    #TODO: think of an efficient code to compute the %age of votes
    return vote_count, party_name

#def vote_percentage():






extract_votes_per_party(city1, party_sym_lookup)
