import random

# Initial player stats
diplomatic_points = 10
global_tension = 20
public_opinion = 50
turn = 1
story_progress = {
    "european_crisis": False,
    "berlin_crisis": False,
    "cuban_crisis": False,
    "vietnam_crisis": False
}

def show_introduction():
    print("\n" + "="*80)
    print("🌍 COLD WAR DIPLOMACY SIMULATOR 🌍")
    print("="*80)
    print("\nHistorical Context:")
    print("The Cold War (1947-1991) was a period of intense geopolitical tension between the United")
    print("States and the Soviet Union. Following World War II, these two superpowers emerged with")
    print("diametrically opposed ideologies: American capitalism and democracy versus Soviet")
    print("communism and authoritarianism.")
    print("\nGame Overview:")
    print("You are the leader of a major power during the Cold War. Your decisions will shape the")
    print("course of history. Each choice you make will lead to different historical paths and")
    print("challenges. The story will evolve based on your decisions, creating a unique experience")
    print("each time you play.")
    print("\nGame Rules:")
    print("• You start with 10 Diplomatic Points to spend on actions")
    print("• Global Tension starts at 20 (if it reaches 100, the Cold War turns hot)")
    print("• Public Opinion starts at 50 (if it reaches 0, you lose public support)")
    print("• Each decision will lead to new challenges and opportunities")
    print("\n" + "="*80)
    input("\nPress Enter to begin your diplomatic journey...")
    print("\n" + "="*80)

def get_current_scenario():
    global story_progress
    
    # Starting scenario
    if not any(story_progress.values()):
        return {
            "description": "\nThe year is 1947. The Truman Doctrine has just been announced, and you must decide how to respond to the growing communist influence in Europe.",
            "choices": [
                "1. Implement the Marshall Plan to rebuild Europe",
                "2. Establish military bases in strategic locations",
                "3. Begin nuclear weapons development",
                "4. Focus on domestic stability"
            ],
            "next_scenario": "european_crisis"
        }
    
    # European Crisis Branch
    elif story_progress["european_crisis"] and not story_progress["berlin_crisis"]:
        return {
            "description": "\nYour European strategy has led to a critical moment. The Soviet Union has blockaded West Berlin, cutting off vital supplies to 2.5 million residents. How will you respond?",
            "choices": [
                "1. Launch a massive airlift operation to supply West Berlin",
                "2. Send military convoys to break the blockade",
                "3. Negotiate with the Soviets for a peaceful resolution",
                "4. Evacuate West Berlin to avoid confrontation"
            ],
            "next_scenario": "berlin_crisis"
        }
    
    # Berlin Crisis Branch
    elif story_progress["berlin_crisis"] and not story_progress["cuban_crisis"]:
        return {
            "description": "\nThe situation in Berlin has escalated. U-2 spy planes have discovered Soviet nuclear missiles in Cuba, just 90 miles from your coast. The world stands on the brink of nuclear war.",
            "choices": [
                "1. Impose a naval quarantine around Cuba",
                "2. Launch airstrikes on missile sites",
                "3. Offer to remove your missiles from Turkey in exchange",
                "4. Demand immediate Soviet withdrawal"
            ],
            "next_scenario": "cuban_crisis"
        }
    
    # Cuban Crisis Branch
    elif story_progress["cuban_crisis"] and not story_progress["vietnam_crisis"]:
        return {
            "description": "\nThe Cuban Missile Crisis has changed the global landscape. Now, the situation in Vietnam is escalating. The communist North is gaining ground in the South, and you must decide your next move.",
            "choices": [
                "1. Increase military support to South Vietnam",
                "2. Begin peace negotiations with North Vietnam",
                "3. Withdraw all forces to focus on other regions",
                "4. Launch a major offensive to end the conflict quickly"
            ],
            "next_scenario": "vietnam_crisis"
        }
    
    # Vietnam Crisis Branch
    elif story_progress["vietnam_crisis"]:
        return {
            "description": "\nThe Vietnam conflict has reached a critical point. Your previous decisions have led to this moment. The world watches as you make your final strategic move.",
            "choices": [
                "1. Escalate the conflict to force a resolution",
                "2. Begin a gradual withdrawal while maintaining honor",
                "3. Seek a diplomatic solution through the United Nations",
                "4. Focus on containing the conflict to Vietnam"
            ],
            "next_scenario": "endgame"
        }

def show_status():
    print(f"\n[Turn {turn}] Diplomatic Points: {diplomatic_points} | Global Tension: {global_tension} | Public Opinion: {public_opinion}")

def check_end_conditions():
    if (global_tension >= 100):
        print("\n⚠️ Global tension reached critical level. The Cold War turned hot. Game over.")
        return True
    elif (public_opinion <= 0):
        print("\n👎 Public lost trust in your leadership. You were voted out. Game over.")
        return True
    elif (diplomatic_points <= 0):
        print("\n💬 You're out of diplomatic leverage. Stalemate. Game over.")
        return True
    return False

def get_random_event():
    events = [
        ("Nuclear Test", 15, -8, "Your rival conducts a nuclear test, escalating the arms race!"),
        ("Space Race", -5, 10, "Your nation achieves a major space milestone, boosting national pride!"),
        ("Economic Crisis", 5, -15, "Global markets react to Cold War tensions, causing economic instability!"),
        ("Proxy War", 10, -5, "A proxy conflict breaks out in a developing nation, testing your resolve!")
    ]
    return random.choice(events)

def take_turn():
    global diplomatic_points, global_tension, public_opinion, story_progress, turn
    
    scenario = get_current_scenario()
    print(scenario["description"])
    for choice in scenario["choices"]:
        print(choice)

    choice = input("\nEnter your action (1-4): ")
    
    # Process choice based on current scenario
    if scenario["next_scenario"] == "european_crisis":
        if choice == "1":
            diplomatic_points -= 2
            global_tension -= 5
            public_opinion += 5
            print("\nYou implemented the Marshall Plan!")
            print("This massive economic aid program helps rebuild Europe and contain communism.")
            print("The Soviet Union views this as a direct challenge to their influence.")
        elif choice == "2":
            diplomatic_points -= 3
            global_tension += 10
            print("\nYou established military bases!")
            print("This shows strength but increases tensions with the Soviet Union.")
            print("The Soviets respond by strengthening their own military presence.")
        elif choice == "3":
            diplomatic_points -= 4
            global_tension += 15
            print("\nYou began nuclear weapons development!")
            print("This escalates the arms race significantly.")
            print("The Soviet Union accelerates their own nuclear program in response.")
        elif choice == "4":
            diplomatic_points += 2
            public_opinion += 10
            print("\nYou focused on domestic stability!")
            print("This improves your nation's internal situation.")
            print("However, the Soviet Union sees this as a sign of weakness.")
        
        story_progress["european_crisis"] = True
    
    elif scenario["next_scenario"] == "berlin_crisis":
        if choice == "1":
            diplomatic_points -= 3
            global_tension -= 5
            public_opinion += 15
            print("\nYou launched the Berlin Airlift!")
            print("This humanitarian effort saves West Berlin and wins global support.")
            print("The Soviet Union is forced to back down, but tensions remain high.")
        elif choice == "2":
            diplomatic_points -= 4
            global_tension += 20
            print("\nYou sent military convoys!")
            print("This risks direct confrontation with Soviet forces.")
            print("The situation becomes increasingly volatile.")
        elif choice == "3":
            diplomatic_points -= 2
            global_tension -= 10
            print("\nYou chose to negotiate!")
            print("This reduces tensions but may be seen as weakness.")
            print("The Soviet Union becomes more aggressive in other regions.")
        elif choice == "4":
            diplomatic_points -= 1
            public_opinion -= 20
            print("\nYou evacuated West Berlin!")
            print("This is seen as a major defeat in the Cold War.")
            print("Your allies begin to question your commitment.")
        
        story_progress["berlin_crisis"] = True
    
    elif scenario["next_scenario"] == "cuban_crisis":
        if choice == "1":
            diplomatic_points -= 3
            global_tension += 10
            print("\nYou imposed a naval quarantine!")
            print("This shows resolve but risks confrontation.")
            print("The Soviet Union sends more ships to challenge the blockade.")
        elif choice == "2":
            diplomatic_points -= 4
            global_tension += 30
            print("\nYou launched airstrikes!")
            print("This could trigger nuclear war!")
            print("The world holds its breath as the situation escalates.")
        elif choice == "3":
            diplomatic_points -= 2
            global_tension -= 15
            print("\nYou offered to remove missiles from Turkey!")
            print("This diplomatic solution reduces tensions.")
            print("Both sides begin to de-escalate the crisis.")
        elif choice == "4":
            diplomatic_points -= 1
            global_tension += 20
            print("\nYou demanded immediate withdrawal!")
            print("This ultimatum increases tensions significantly.")
            print("The Soviet Union refuses to back down.")
        
        story_progress["cuban_crisis"] = True
    
    elif scenario["next_scenario"] == "vietnam_crisis":
        if choice == "1":
            diplomatic_points -= 3
            global_tension += 15
            public_opinion -= 10
            print("\nYou increased military support!")
            print("This escalates the conflict further.")
            print("The war becomes increasingly unpopular at home.")
        elif choice == "2":
            diplomatic_points -= 2
            global_tension -= 10
            public_opinion += 5
            print("\nYou began peace negotiations!")
            print("This shows willingness to resolve the conflict.")
            print("The path to peace is long and difficult.")
        elif choice == "3":
            diplomatic_points -= 1
            global_tension -= 5
            public_opinion -= 15
            print("\nYou withdrew all forces!")
            print("This is seen as a major defeat.")
            print("Your global standing is significantly weakened.")
        elif choice == "4":
            diplomatic_points -= 4
            global_tension += 20
            public_opinion -= 20
            print("\nYou launched a major offensive!")
            print("This escalates the conflict dramatically.")
            print("The war becomes increasingly brutal and costly.")
        
        story_progress["vietnam_crisis"] = True
    
    elif scenario["next_scenario"] == "endgame":
        if choice == "1":
            diplomatic_points -= 5
            global_tension += 25
            public_opinion -= 20
            print("\nYou chose to escalate the conflict!")
            print("This decision will have far-reaching consequences.")
            print("The world stands on the brink of a major war.")
        elif choice == "2":
            diplomatic_points -= 3
            global_tension -= 15
            public_opinion += 10
            print("\nYou began a gradual withdrawal!")
            print("This preserves some honor while ending the conflict.")
            print("The war comes to a close, but at what cost?")
        elif choice == "3":
            diplomatic_points -= 2
            global_tension -= 10
            public_opinion += 15
            print("\nYou sought a diplomatic solution!")
            print("This shows wisdom and restraint.")
            print("The world breathes a sigh of relief.")
        elif choice == "4":
            diplomatic_points -= 4
            global_tension += 5
            public_opinion -= 5
            print("\nYou focused on containment!")
            print("This limits the conflict but prolongs the suffering.")
            print("The war continues, but in a more controlled manner.")
        
        print("\nThe Cold War continues, but your decisions have shaped its course.")
        return True

    # Show consequences
    print(f"\nDiplomatic Points: {diplomatic_points}")
    print(f"Global Tension: {global_tension}")
    print(f"Public Opinion: {public_opinion}")

    # Random event occurs
    event = get_random_event()
    print(f"\n🌍 Random Event: {event[0]}")
    print(f"Event Details: {event[3]}")
    global_tension += event[1]
    public_opinion += event[2]
    
    return False

# Game loop
show_introduction()
game_over = False
while not game_over:
    show_status()
    game_over = take_turn()
    if check_end_conditions():
        break
    turn += 1

