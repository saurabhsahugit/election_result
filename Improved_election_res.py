from election_data import voting_data, party_sym_lookup

def exctract_consti_party_votes(voting_data, party_sym_lookup):
    constituency_name = []
    party_results = {}
    total_votes = 0
    for city, data in voting_data.items():
        # Adds to a dictionary of constituencies
        constituency_name.append(city)
        for sym, votes_cast in data.items():
            if sym in party_sym_lookup:  # validation
                sym = party_sym_lookup[sym]
                party_results[sym] = votes_cast
                # print(f"{sym} has {party_results[sym]}")
                total_votes += votes_cast
            else:
                print(f"Data Error: {sym} not found")
        print(
            f"====== {city} had a total {total_votes} votes casted, results are as follows: ======")
        for key, vals in party_results.items():
            pcentage = round((vals / total_votes) * 100, 2)
            print(f"\t {key} have received {pcentage} percentage votes")

exctract_consti_party_votes(voting_data, party_sym_lookup)
