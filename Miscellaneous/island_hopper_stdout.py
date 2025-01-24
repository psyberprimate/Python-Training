def journey_planner(all_customers_wishlist: list) -> tuple:

    island_hops = int(input("Enter number of island hops: "))
    
    while(True):
        customer_amount = int(input("Enter number of customers (max 400): "))
        if customer_amount > 400:
            print("Too many customer, max customer amount exceeded!")
            continue
        else:
            break
        
    #print("Please provide desired island hops at hop t starting from 0 to {}: ".format(island_hops-1))
    
    for _ in range(customer_amount):
        
        single_customer_wishlist = [] # Set list
        customer_choice = input("Please provide input: h(0 to {}) and t(by-sea | airborne) separated by ( ), and where pairs are separated by (, ): ".format(island_hops-1))
        customer_preference = customer_choice.split(", ")
        
        for preference in customer_preference:
            hop, transport_choice = preference.split(" ")
            single_customer_wishlist.append((int(hop), transport_choice))
            
        all_customers_wishlist.append(single_customer_wishlist)

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
    all_customers_wishlist = []
    island_hops, all_customers_wishlist = journey_planner(all_customers_wishlist)
    journey, result = planner(island_hops, all_customers_wishlist)
    
    if result:
        print(", ".join("{} {}".format(hop[0],hop[1]) for hop in journey))
    else:
        print("NO ITINERARY")
    input()