def read_file_to_journey_plan(file_path: str, all_customers_wishlist : list) -> tuple:
    island_hops = 0
    customer_count = 0
    with open(file_path) as journey_plan_file:
        
        island_hops = int(journey_plan_file.readline().strip('\n'))
        customer_count = int(journey_plan_file.readline().strip('\n'))
        if customer_count > 400:
            print("Too many customers! Please provide path to text file with max 400 customers")
            exit()
        #journey_plan_file.readline() # I dont know why this makes it skip one line when reading input but it does,
        #maybe its because of the line pointer being moved or something like that because of the earlier line?
        for row in journey_plan_file:
            single_customer_wishlist = [] # Set list
            customer_choice = row.strip('\n')
            customer_preference = customer_choice.split(", ")
            for preference in customer_preference:
                hop, transport_choice = preference.split(" ")
                single_customer_wishlist.append((int(hop), transport_choice))
                
            all_customers_wishlist.append(single_customer_wishlist)
        #print(all_customers_wishlist)
    return island_hops, all_customers_wishlist


def planner(island_hops: int, all_customers_wishlist : list) -> tuple:
    
    def check_journey(journey : list, all_customers_wishlist : list) -> bool:
        
        def check_satisfaction_per_customer(journey : list, travel_type_selection : list) -> bool:
            for hop in travel_type_selection:
                if hop in journey:
                    return True
            return False
    
        for travel_type_selection in all_customers_wishlist:
            customer_satifaction = check_satisfaction_per_customer(journey, travel_type_selection)
            if not customer_satifaction:
                return False
        return True
    
    
    def plan_journey(journey: list, air_travel_count: int, index: int) -> bool:
   
        customer_wish_per_hop = []
        
        if index == len(journey):
            return check_journey(journey, all_customers_wishlist)
        
        for customer_wish in all_customers_wishlist: # Check customer wishes per index (island hop)
            for wish in customer_wish:
                if wish[0] == index:
                    customer_wish_per_hop.append(wish)
            
        if len(customer_wish_per_hop) == 0: # If the customer wish per index aka hop is empty then fill the slot with both index candidates for checking 
            customer_wish_per_hop.append((index, 'by-sea'))
            customer_wish_per_hop.append((index, 'airborne'))

        for travel_type in customer_wish_per_hop: # Check per island hop with each customer that has that index
            
            if travel_type[1] == 'airborne' and air_travel_count > 0:
                continue
            
            journey[index] = (index, travel_type[1])
            # if travel_type[1] == 'airborne':
            #     finished = plan_journey(journey, air_travel_count + 1, index + 1)
            #     if finished:
            #         return True
            # else:
            #     finished = plan_journey(journey, air_travel_count, index + 1)
            #     if finished:
            #         return True  
            if plan_journey(journey, air_travel_count +1 if travel_type[1] == 'airborne' else air_travel_count, index + 1): #Make recursive function call here
                return True
            journey[index] = None
            
        return False
    
        
    air_travel_count = 0
    journey = [None] * island_hops
    result = plan_journey(journey, air_travel_count, 0)
    return journey, result

if __name__ == "__main__":
    #print("Island hopper planner")
    path="island_hopper.txt" #provide a file path
    all_customers_wishlist = []
    island_hops, all_customers_wishlist =  read_file_to_journey_plan(file_path=path,
                                                                     all_customers_wishlist=all_customers_wishlist)
    journey, result = planner(island_hops, all_customers_wishlist)
    
    if result:
        print(", ".join("{} {}".format(hop[0],hop[1]) for hop in journey))
    else:
        print("NO ITINERARY")
    input()