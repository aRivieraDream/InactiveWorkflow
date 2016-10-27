TODO:
Sources Analysis:
Prioritize: Europe VC & Core M&A
  1. MarketWire
    * Currently covering: Everything seemingly relevant
      - Financial Agreements
      - IPOs
      - Management changes
      - Mergers
    * Why we missed things:
      - Not covered in current RSS selection
  2. Financial News -- Swap for better source
  3. Drop Crunchbase?
  4. PR Newswire--Contact Dev to figure out what's going on with dupe stories so we can potentially add All PR Newswire news
    * Issue: do they print same story in multiple RSS feeds?
  Potential Sources
  A. BusinessPress24


Conclusions:  
1. A large portion of the deals that we didn't have, we did already collect news from the transaction.
* We can set strict M&A filters that will extract transactions from inactive sources.
  - If we do this we still deal with redundant news
* We can implement a short-term grouping logic that tries to identify dupe stories by excluding stories that are already attached to entities that have pass to secondary/entered/irr news within a week of that date.

Logic:  
1. Extract all news & entities from particular Sources
  * postgres & sql server
    - Text
    - Created Date
    - associated entities
  * Check story for keywords to determine if M&A event
    - If no, stop
  * Check associated entities for news within +/-5? days of created date.
    - If none, **assume story is new M&A event**
  * Get work orders for all those news
    - If any have type = M&A Round Event, assume round is already researched
    - Else, **assume story is new M&A event**
