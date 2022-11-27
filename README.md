
Further to my submission I have improved the code. We had hit some issues in iterating over the dictionary objects used which have been resolved in the new code.

All the data provided in the [Election results](https://github.com/guardian/coding-exercises/tree/main/election-results) excercise has now also being used.

This code can be further improved with the use of classes. The use of nested for loops is suboptimal as it makes the code brittle and harder to maintain. My preferred approach will be the use of classes which will also be more performant than for-loops, pesudo-code below:

    class  Constituency_results:
    	def  __init__(self, sym, votes) -> None:
    		self.sym  =  sym
    		self.votes  =  votes
    	
    	def  constituency_results_extract(self, constituency_name, sym, votes)
    	#TODO: Method for storing the data and computing the %age of results
    
    for  city, data  in  voting_data.items():
    	for  sym, votes_cast  in  data.items():
    		election_data  =  Constituency_results()
    		election_data.constituency_results_extract(sym, votes_cast)



**IDE screenshot:**
![Screenshot 2022-11-27 at 10 15 50 pm](https://user-images.githubusercontent.com/9202957/204162889-cec0eccd-00a2-477b-aea0-6d31dd3f7536.png)
**Output:**

    >     `(base) saurabh@Saurabhs-MacBook-Pro guardian % /usr/local/bin/python3
    > /Users/saurabh/Documents/Learning/python/guardian/coding-exercise-project/python/election_res.py
    >     ====== Cardiff West had a total 35809 votes casted, results are as follows: ======
    >              Conservative Party have received 30.76 percentage votes
    >              Labour Party have received 49.72 percentage votes
    >              UKIP have received 13.75 percentage votes
    >              Liberal Democrats have received 5.78 percentage votes
    >     ====== Islington South & Finsbury had a total 79629 votes casted, results are as follows: ======
    >              Conservative Party have received 11.79 percentage votes
    >              Labour Party have received 28.32 percentage votes
    >              UKIP have received 4.24 percentage votes
    >              Liberal Democrats have received 6.06 percentage votes
    >              Green Party have received 4.23 percentage votes
    >              Independent have received 0.39 percentage votes
    >     (base) saurabh@Saurabhs-MacBook-Pro guardian %

