import streamlit as st
import random

# Initialize session state
if 'diplomatic_points' not in st.session_state:
    st.session_state.diplomatic_points = 10
if 'global_tension' not in st.session_state:
    st.session_state.global_tension = 20
if 'public_opinion' not in st.session_state:
    st.session_state.public_opinion = 50
if 'turn' not in st.session_state:
    st.session_state.turn = 1
if 'story_progress' not in st.session_state:
    st.session_state.story_progress = {
        "european_crisis": False,
        "berlin_crisis": False,
        "cuban_crisis": False,
        "vietnam_crisis": False
    }
if 'game_over' not in st.session_state:
    st.session_state.game_over = False
if 'current_scenario' not in st.session_state:
    st.session_state.current_scenario = None
if 'last_event' not in st.session_state:
    st.session_state.last_event = None
if 'last_success_message' not in st.session_state:
    st.session_state.last_success_message = None
if 'last_info_messages' not in st.session_state:
    st.session_state.last_info_messages = []

def reset_game():
    """Reset all game state variables"""
    st.session_state.diplomatic_points = 10
    st.session_state.global_tension = 20
    st.session_state.public_opinion = 50
    st.session_state.turn = 1
    st.session_state.story_progress = {
        "european_crisis": False,
        "berlin_crisis": False,
        "cuban_crisis": False,
        "vietnam_crisis": False
    }
    st.session_state.game_over = False
    st.session_state.current_scenario = None
    st.session_state.last_event = None
    st.session_state.last_success_message = None
    st.session_state.last_info_messages = []

def show_introduction():
    st.title("🌍 Cold War Diplomacy Simulator")
    
    st.markdown("""
    ### Historical Context
    The Cold War (1947-1991) was a period of intense geopolitical tension between the United States and the Soviet Union. 
    Following World War II, these two superpowers emerged with diametrically opposed ideologies: American capitalism and 
    democracy versus Soviet communism and authoritarianism.
    
    ### Game Overview
    You are the leader of a major power during the Cold War. Your decisions will shape the course of history. 
    Each choice you make will lead to different historical paths and challenges. The story will evolve based on 
    your decisions, creating a unique experience each time you play.
    
    ### Game Rules
    - You start with 10 Diplomatic Points
    - Global Tension starts at 20 (game over if it reaches 100)
    - Public Opinion starts at 50 (game over if it reaches 0)
    - Each decision will lead to new challenges and opportunities
    """)

def get_current_scenario():
    # Starting scenario
    if not any(st.session_state.story_progress.values()):
        return {
            "description": "The year is 1947. The Truman Doctrine has just been announced, and you must decide how to respond to the growing communist influence in Europe.",
            "choices": [
                "Implement the Marshall Plan to rebuild Europe",
                "Establish military bases in strategic locations",
                "Begin nuclear weapons development",
                "Focus on domestic stability"
            ],
            "next_scenario": "european_crisis"
        }
    
    # European Crisis Branch
    elif st.session_state.story_progress["european_crisis"] and not st.session_state.story_progress["berlin_crisis"]:
        return {
            "description": "Your European strategy has led to a critical moment. The Soviet Union has blockaded West Berlin, cutting off vital supplies to 2.5 million residents. How will you respond?",
            "choices": [
                "Launch a massive airlift operation to supply West Berlin",
                "Send military convoys to break the blockade",
                "Negotiate with the Soviets for a peaceful resolution",
                "Evacuate West Berlin to avoid confrontation"
            ],
            "next_scenario": "berlin_crisis"
        }
    
    # Berlin Crisis Branch
    elif st.session_state.story_progress["berlin_crisis"] and not st.session_state.story_progress["cuban_crisis"]:
        return {
            "description": "The situation in Berlin has escalated. U-2 spy planes have discovered Soviet nuclear missiles in Cuba, just 90 miles from your coast. The world stands on the brink of nuclear war.",
            "choices": [
                "Impose a naval quarantine around Cuba",
                "Launch airstrikes on missile sites",
                "Offer to remove your missiles from Turkey in exchange",
                "Demand immediate Soviet withdrawal"
            ],
            "next_scenario": "cuban_crisis"
        }
    
    # Cuban Crisis Branch
    elif st.session_state.story_progress["cuban_crisis"] and not st.session_state.story_progress["vietnam_crisis"]:
        return {
            "description": "The Cuban Missile Crisis has changed the global landscape. Now, the situation in Vietnam is escalating. The communist North is gaining ground in the South, and you must decide your next move.",
            "choices": [
                "Increase military support to South Vietnam",
                "Begin peace negotiations with North Vietnam",
                "Withdraw all forces to focus on other regions",
                "Launch a major offensive to end the conflict quickly"
            ],
            "next_scenario": "vietnam_crisis"
        }
    
    # Vietnam Crisis Branch
    elif st.session_state.story_progress["vietnam_crisis"]:
        return {
            "description": "The Vietnam conflict has reached a critical point. Your previous decisions have led to this moment. The world watches as you make your final strategic move.",
            "choices": [
                "Escalate the conflict to force a resolution",
                "Begin a gradual withdrawal while maintaining honor",
                "Seek a diplomatic solution through the United Nations",
                "Focus on containing the conflict to Vietnam"
            ],
            "next_scenario": "endgame"
        }

def get_random_event():
    events = [
        ("Nuclear Test", 15, -8, "Your rival conducts a nuclear test, escalating the arms race!"),
        ("Space Race", -5, 10, "Your nation achieves a major space milestone, boosting national pride!"),
        ("Economic Crisis", 5, -15, "Global markets react to Cold War tensions, causing economic instability!"),
        ("Proxy War", 10, -5, "A proxy conflict breaks out in a developing nation, testing your resolve!")
    ]
    return random.choice(events)

def check_end_conditions():
    if st.session_state.global_tension >= 100:
        st.error("⚠️ Global tension reached critical level. The Cold War turned hot. Game over.")
        return True
    elif st.session_state.public_opinion <= 0:
        st.error("👎 Public lost trust in your leadership. You were voted out. Game over.")
        return True
    elif st.session_state.diplomatic_points <= 0:
        st.error("💬 You're out of diplomatic leverage. Stalemate. Game over.")
        return True
    return False

def process_choice(choice, scenario):
    # Clear previous messages
    st.session_state.last_success_message = None
    st.session_state.last_info_messages = []
    
    if scenario["next_scenario"] == "european_crisis":
        if choice == 0:  # Marshall Plan
            st.session_state.diplomatic_points -= 2
            st.session_state.global_tension -= 5
            st.session_state.public_opinion += 5
            st.session_state.last_success_message = "You implemented the Marshall Plan!"
            st.session_state.last_info_messages = [
                "This massive economic aid program helps rebuild Europe and contain communism.",
                "The Soviet Union views this as a direct challenge to their influence."
            ]
        elif choice == 1:  # Military bases
            st.session_state.diplomatic_points -= 3
            st.session_state.global_tension += 10
            st.session_state.last_success_message = "You established military bases!"
            st.session_state.last_info_messages = [
                "This shows strength but increases tensions with the Soviet Union.",
                "The Soviets respond by strengthening their own military presence."
            ]
        elif choice == 2:  # Nuclear weapons
            st.session_state.diplomatic_points -= 4
            st.session_state.global_tension += 15
            st.session_state.last_success_message = "You began nuclear weapons development!"
            st.session_state.last_info_messages = [
                "This escalates the arms race significantly.",
                "The Soviet Union accelerates their own nuclear program in response."
            ]
        elif choice == 3:  # Domestic stability
            st.session_state.diplomatic_points += 2
            st.session_state.public_opinion += 10
            st.session_state.last_success_message = "You focused on domestic stability!"
            st.session_state.last_info_messages = [
                "This improves your nation's internal situation.",
                "However, the Soviet Union sees this as a sign of weakness."
            ]
        
        st.session_state.story_progress["european_crisis"] = True
    
    elif scenario["next_scenario"] == "berlin_crisis":
        if choice == 0:  # Airlift
            st.session_state.diplomatic_points -= 3
            st.session_state.global_tension -= 5
            st.session_state.public_opinion += 15
            st.session_state.last_success_message = "You launched the Berlin Airlift!"
            st.session_state.last_info_messages = [
                "This humanitarian effort saves West Berlin and wins global support.",
                "The Soviet Union is forced to back down, but tensions remain high."
            ]
        elif choice == 1:  # Military convoys
            st.session_state.diplomatic_points -= 4
            st.session_state.global_tension += 20
            st.session_state.last_success_message = "You sent military convoys!"
            st.session_state.last_info_messages = [
                "This risks direct confrontation with Soviet forces.",
                "The situation becomes increasingly volatile."
            ]
        elif choice == 2:  # Negotiate
            st.session_state.diplomatic_points -= 2
            st.session_state.global_tension -= 10
            st.session_state.last_success_message = "You chose to negotiate!"
            st.session_state.last_info_messages = [
                "This reduces tensions but may be seen as weakness.",
                "The Soviet Union becomes more aggressive in other regions."
            ]
        elif choice == 3:  # Evacuate
            st.session_state.diplomatic_points -= 1
            st.session_state.public_opinion -= 20
            st.session_state.last_success_message = "You evacuated West Berlin!"
            st.session_state.last_info_messages = [
                "This is seen as a major defeat in the Cold War.",
                "Your allies begin to question your commitment."
            ]
        
        st.session_state.story_progress["berlin_crisis"] = True
    
    elif scenario["next_scenario"] == "cuban_crisis":
        if choice == 0:  # Quarantine
            st.session_state.diplomatic_points -= 3
            st.session_state.global_tension += 10
            st.session_state.last_success_message = "You imposed a naval quarantine!"
            st.session_state.last_info_messages = [
                "This shows resolve but risks confrontation.",
                "The Soviet Union sends more ships to challenge the blockade."
            ]
        elif choice == 1:  # Airstrikes
            st.session_state.diplomatic_points -= 4
            st.session_state.global_tension += 30
            st.session_state.last_success_message = "You launched airstrikes!"
            st.session_state.last_info_messages = [
                "This could trigger nuclear war!",
                "The world holds its breath as the situation escalates."
            ]
        elif choice == 2:  # Remove missiles
            st.session_state.diplomatic_points -= 2
            st.session_state.global_tension -= 15
            st.session_state.last_success_message = "You offered to remove missiles from Turkey!"
            st.session_state.last_info_messages = [
                "This diplomatic solution reduces tensions.",
                "Both sides begin to de-escalate the crisis."
            ]
        elif choice == 3:  # Demand withdrawal
            st.session_state.diplomatic_points -= 1
            st.session_state.global_tension += 20
            st.session_state.last_success_message = "You demanded immediate withdrawal!"
            st.session_state.last_info_messages = [
                "This ultimatum increases tensions significantly.",
                "The Soviet Union refuses to back down."
            ]
        
        st.session_state.story_progress["cuban_crisis"] = True
    
    elif scenario["next_scenario"] == "vietnam_crisis":
        if choice == 0:  # Increase support
            st.session_state.diplomatic_points -= 3
            st.session_state.global_tension += 15
            st.session_state.public_opinion -= 10
            st.session_state.last_success_message = "You increased military support!"
            st.session_state.last_info_messages = [
                "This escalates the conflict further.",
                "The war becomes increasingly unpopular at home."
            ]
        elif choice == 1:  # Peace negotiations
            st.session_state.diplomatic_points -= 2
            st.session_state.global_tension -= 10
            st.session_state.public_opinion += 5
            st.session_state.last_success_message = "You began peace negotiations!"
            st.session_state.last_info_messages = [
                "This shows willingness to resolve the conflict.",
                "The path to peace is long and difficult."
            ]
        elif choice == 2:  # Withdraw
            st.session_state.diplomatic_points -= 1
            st.session_state.global_tension -= 5
            st.session_state.public_opinion -= 15
            st.session_state.last_success_message = "You withdrew all forces!"
            st.session_state.last_info_messages = [
                "This is seen as a major defeat.",
                "Your global standing is significantly weakened."
            ]
        elif choice == 3:  # Major offensive
            st.session_state.diplomatic_points -= 4
            st.session_state.global_tension += 20
            st.session_state.public_opinion -= 20
            st.session_state.last_success_message = "You launched a major offensive!"
            st.session_state.last_info_messages = [
                "This escalates the conflict dramatically.",
                "The war becomes increasingly brutal and costly."
            ]
        
        st.session_state.story_progress["vietnam_crisis"] = True
    
    elif scenario["next_scenario"] == "endgame":
        if choice == 0:  # Escalate
            st.session_state.diplomatic_points -= 5
            st.session_state.global_tension += 25
            st.session_state.public_opinion -= 20
            st.session_state.last_success_message = "You chose to escalate the conflict!"
            st.session_state.last_info_messages = [
                "This decision will have far-reaching consequences.",
                "The world stands on the brink of a major war."
            ]
        elif choice == 1:  # Gradual withdrawal
            st.session_state.diplomatic_points -= 3
            st.session_state.global_tension -= 15
            st.session_state.public_opinion += 10
            st.session_state.last_success_message = "You began a gradual withdrawal!"
            st.session_state.last_info_messages = [
                "This preserves some honor while ending the conflict.",
                "The war comes to a close, but at what cost?"
            ]
        elif choice == 2:  # Diplomatic solution
            st.session_state.diplomatic_points -= 2
            st.session_state.global_tension -= 10
            st.session_state.public_opinion += 15
            st.session_state.last_success_message = "You sought a diplomatic solution!"
            st.session_state.last_info_messages = [
                "This shows wisdom and restraint.",
                "The world breathes a sigh of relief."
            ]
        elif choice == 3:  # Containment
            st.session_state.diplomatic_points -= 4
            st.session_state.global_tension += 5
            st.session_state.public_opinion -= 5
            st.session_state.last_success_message = "You focused on containment!"
            st.session_state.last_info_messages = [
                "This limits the conflict but prolongs the suffering.",
                "The war continues, but in a more controlled manner."
            ]
        
        st.session_state.last_info_messages.append("The Cold War continues, but your decisions have shaped its course.")
        st.session_state.game_over = True

def main():
    if not st.session_state.current_scenario:
        show_introduction()
        if st.button("Start Game"):
            reset_game()  # Reset all game state before starting
            st.session_state.current_scenario = get_current_scenario()
            st.rerun()
    else:
        # Display game status
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Diplomatic Points", st.session_state.diplomatic_points)
        with col2:
            st.metric("Global Tension", st.session_state.global_tension)
        with col3:
            st.metric("Public Opinion", st.session_state.public_opinion)
        
        st.markdown(f"### Turn {st.session_state.turn}")
        
        # Display current scenario
        scenario = st.session_state.current_scenario
        st.markdown(f"#### {scenario['description']}")
        
        # Display choices
        choice = st.radio("Choose your action:", scenario["choices"])
        if st.button("Make Decision"):
            process_choice(scenario["choices"].index(choice), scenario)
            
            # Random event
            event = get_random_event()
            st.markdown(f"### 🌍 Random Event: {event[0]}")
            st.info(event[3])
            st.session_state.global_tension += event[1]
            st.session_state.public_opinion += event[2]
            
            # Update game state
            st.session_state.turn += 1
            st.session_state.current_scenario = get_current_scenario()
            
            if check_end_conditions() or st.session_state.game_over:
                st.session_state.game_over = True
                st.rerun()
            else:
                st.rerun()
        
        # Display last success and info messages if they exist
        if st.session_state.last_success_message:
            st.success(st.session_state.last_success_message)
        for message in st.session_state.last_info_messages:
            st.info(message)
        
        # Show Return Home button if game is over
        if st.session_state.game_over:
            st.markdown("### Game Over!")
            if st.session_state.global_tension >= 100:
                st.error("The Cold War turned hot! Global tension reached critical levels, leading to nuclear war. Your leadership failed to maintain peace.")
            elif st.session_state.public_opinion <= 0:
                st.error("The public has lost all faith in your leadership! Your approval ratings have plummeted to zero, forcing you to step down.")
            elif st.session_state.diplomatic_points <= 0:
                st.error("You've run out of diplomatic leverage! Without any diplomatic points, you can no longer influence international affairs effectively.")
            else:
                st.markdown("Your decisions have led to this outcome. The Cold War continues, but your leadership has ended.")
            
            if st.button("Return Home"):
                st.session_state.current_scenario = None
                st.rerun()

if __name__ == "__main__":
    main()