from aima3 import logic
from aima3.logic import *

def get_first_aid_instructions(*symptoms):
    kb = FolKB()

    x = expr('x')

    kb.tell(expr('Injured(x) & InjuryLocationHead(x) & GunshotWound(x) ==> GunshotWoundToTheHead(x)'))
    kb.tell(expr('Injured(x) & InjuryLocationChest(x) & GunshotWound(x) ==> GunshotWoundToTheChest(x)'))
    kb.tell(expr('Injured(x) & InjuryLocationAbdomen(x) & GunshotWound(x) ==> GunshotWoundToTheAbdomen(x)'))
    kb.tell(expr('Injured(x) & InjuryLocationLimbs(x) & GunshotWound(x) ==> GunshotWoundToTheLimbs(x)'))

    kb.tell(expr('Injured(x) & InjuryLocationHead(x) & BlastInjury(x) ==> BlastInjuryToTheHead(x)'))
    kb.tell(expr('Injured(x) & InjuryLocationChest(x) & BlastInjury(x) ==> BlastInjuryToTheChest(x)'))
    kb.tell(expr('Injured(x) & InjuryLocationAbdomen(x) & BlastInjury(x) ==> BlastInjuryToTheAbdomen(x)'))
    kb.tell(expr('Injured(x) & InjuryLocationLimbs(x) & BlastInjury(x) ==> BlastInjuryToTheLimbs(x)'))

    kb.tell(expr('Injured(x) & InjuryLocationHead(x) & BurnInjury(x) ==> BurnInjuryToTheHeadOrNeck(x)'))
    kb.tell(expr('Injured(x) & InjuryLocationChest(x) & BurnInjury(x) ==> BurnInjuryToTheTorsoOrExtremities(x)'))
    kb.tell(expr('Injured(x) & InjuryLocationAbdomen(x) & BurnInjury(x) ==> BurnInjuryToTheTorsoOrExtremities(x)'))
    kb.tell(expr('Injured(x) & InjuryLocationLimbs(x) & BurnInjury(x) ==> BurnInjuryToTheTorsoOrExtremities(x)'))

    print(f'symptoms {symptoms}')

    first_aid_instructions = {
        'GunshotWoundToTheHead(x)': {
            'ApplyPressure': """Immediately apply direct pressure to the wound using a clean cloth or bandage. 
            Use your palm or fingers to apply firm, even pressure to control bleeding. Maintain constant pressure 
            on the wound until medical help arrives.""",
            'ElevateInjuredArea': """Do not attempt to elevate the head. Instead, keep the victim lying flat and 
            still until medical help arrives. Monitor the victim's condition closely for any changes and be prepared 
            to adjust their position if necessary.""",
            'AdditionalInstructions': """While waiting for medical help, continue to monitor the victim's vital 
            signs and provide reassurance."""
        },
        'GunshotWoundToTheChest(x)': {
            'ApplyPressure': """Apply direct pressure to the wound using a clean cloth or bandage. Use your palm or 
            fingers to apply firm, even pressure to control bleeding. Maintain constant pressure on the wound until 
            medical help arrives.""",
            'ElevateInjuredArea': """Keep the victim lying flat. Do not elevate the chest. If the victim is having 
            difficulty breathing, encourage them to sit up slightly to ease breathing efforts.""",
            'AdditionalInstructions': """Monitor the victim's breathing closely. If the victim stops breathing or 
            shows signs of shock, perform CPR if trained to do so, and continue until medical help arrives."""
        },
        'GunshotWoundToTheAbdomen(x)': {
            'ApplyPressure': """Apply direct pressure to the wound using a clean cloth or bandage. Use your palm or 
            fingers to apply firm, even pressure to control bleeding. Maintain constant pressure on the wound until 
            medical help arrives.""",
            'ElevateInjuredArea': """Keep the victim lying flat. Do not elevate the abdomen. If there are signs of 
            internal bleeding (e.g., distended abdomen, rigidity), keep the victim lying flat with legs bent to 
            relieve pressure on the abdomen.""",
            'AdditionalInstructions': """Monitor the victim for signs of shock, such as pale skin, rapid heartbeat, 
            or shallow breathing. Keep the victim warm and comfortable while waiting for medical help."""
        },
        'GunshotWoundToTheLimbs(x)': {
            'ApplyPressure': """Apply direct pressure to the wound using a clean cloth or bandage. Use your palm or 
            fingers to apply firm, even pressure to control bleeding. Maintain constant pressure on the wound until 
            medical help arrives.""",
            'ElevateInjuredArea': """If the injury is in an extremity (arm or leg), gently raise the injured limb 
            above the level of the heart. Use pillows, blankets, or other available items to support the limb in an 
            elevated position. Elevating the injured area helps reduce swelling and bleeding by allowing gravity to 
            assist in draining excess fluid away from the injury site.""",
            'AdditionalInstructions': """Keep the victim calm and reassure them while waiting for medical help. If there 
            are signs of shock, such as pale skin or a rapid pulse, lay the victim flat, elevate their legs slightly, 
            and cover them with a blanket or jacket to keep them warm."""
        },

        'BlastInjuryToTheHead(x)': {
            'Assessment': """Assess the scene for safety before approaching the victim. Ensure the area is clear of 
            any further danger, including potential secondary explosions or structural collapse. If safe, approach the 
            victim cautiously and assess their level of consciousness, airway, breathing, and circulation (ABCs).""",
            'ControlBleeding': """If there is visible bleeding from the head or face, apply direct pressure to any 
            wounds using a clean cloth or bandage. Avoid putting pressure directly on any embedded objects or visible 
            skull fractures.""",
            'AirwayManagement': """If the victim is unconscious and not breathing normally, open the airway using the 
            head-tilt, chin-lift maneuver or jaw thrust maneuver if there is suspicion of a cervical spine injury. 
            Check for and remove any obstructions from the mouth or throat, and provide rescue breaths if necessary.""",
            'CirculationSupport': """Check for signs of circulation, such as a pulse or spontaneous movement. If the 
            victim's heart has stopped beating or there are no signs of circulation, initiate cardiopulmonary resuscitation 
            (CPR) immediately while awaiting advanced medical assistance.""",
            'Stabilization': """Immobilize the victim's head and neck if there is suspicion of spinal injury. Keep the 
            victim lying flat and still to prevent exacerbating any potential spinal cord damage.""",
            'AdditionalInstructions': """Monitor the victim's vital signs continuously and provide reassurance and 
            comfort. Keep the victim warm and protected from further harm while waiting for emergency medical services 
            to arrive."""
        },
        'BlastInjuryToTheChest(x)': {
            'Assessment': """Quickly assess the victim's condition and look for life-threatening injuries, including 
            severe bleeding, difficulty breathing, or signs of shock such as pale skin or rapid pulse.""",
            'ControlBleeding': """If there is visible bleeding from the chest, apply direct pressure to the wound using 
            a clean cloth or bandage. Cover the wound with a sterile dressing or clean cloth and apply pressure to control 
            bleeding.""",
            'AirwayManagement': """Ensure the victim's airway is clear and open. If breathing is difficult or absent, 
            provide artificial ventilation with rescue breaths. Monitor the victim's breathing closely for any changes.""",
            'CirculationSupport': """Check for signs of circulation, such as a pulse or spontaneous movement. If circulation 
            is compromised, begin CPR immediately while awaiting advanced medical assistance.""",
            'Stabilization': """Support the victim in a comfortable position that facilitates breathing. If there are signs 
            of chest trauma, avoid moving the victim unnecessarily to prevent further injury.""",
            'AdditionalInstructions': """Monitor the victim's vital signs continuously and provide reassurance. Keep the 
            victim warm and protected from further harm."""
        },
        'BlastInjuryToTheAbdomen(x)': {
            'Assessment': """Assess the victim's condition and look for signs of abdominal trauma, such as severe pain, 
            swelling, or internal bleeding. Check for signs of shock, such as pale skin, rapid heartbeat, or low blood pressure.""",
            'ControlBleeding': """Apply gentle pressure around any bleeding wounds on the abdomen with a clean cloth or 
            bandage. Avoid putting direct pressure on the abdomen, as this may worsen internal injuries.""",
            'AirwayManagement': """Ensure the victim's airway is clear and open. If consciousness is impaired or breathing 
            is difficult, place the victim in a position that facilitates breathing while protecting the abdomen from further 
            injury.""",
            'CirculationSupport': """Check for signs of circulation and monitor the victim's pulse and blood pressure. If 
            circulation is compromised, initiate CPR immediately while awaiting advanced medical assistance.""",
            'Stabilization': """Keep the victim lying flat and still to prevent exacerbating any potential abdominal injuries. 
            Avoid giving the victim anything to eat or drink, as this may interfere with subsequent medical treatment.""",
            'AdditionalInstructions': """Monitor the victim's vital signs continuously and provide reassurance. Keep the 
            victim warm and protected from further harm."""
        },
        'BlastInjuryToTheLimbs(x)': {
            'Assessment': """Assess the victim for any visible injuries to the limbs, such as bleeding, fractures, or 
            amputations. Check for signs of compartment syndrome, such as severe pain, swelling, or numbness.""",
            'ControlBleeding': """Apply direct pressure to any bleeding wounds on the limbs using a clean cloth or bandage. 
            Elevate the injured limb if possible to reduce swelling, but avoid elevating it above the level of the heart.""",
            'AirwayManagement': """Ensure the victim's airway is clear and open. If consciousness is impaired or breathing 
            is difficult, position the victim in a way that facilitates breathing while protecting the injured limb.""",
            'CirculationSupport': """Check for signs of circulation, such as a pulse or spontaneous movement, in the injured 
            limb. If circulation is compromised, immobilize the limb and seek immediate medical assistance.""",
            'Stabilization': """Immobilize the injured limb using splints or improvised materials to prevent further movement 
            and damage. Avoid manipulating the limb excessively to prevent exacerbating any fractures or soft tissue injuries.""",
            'AdditionalInstructions': """Monitor the victim's vital signs continuously and provide reassurance. Keep the 
            victim warm and protected from further harm."""
        },

        'BurnInjuryToTheHeadOrNeck(x)': {
            'Assessment': """Quickly assess the scene for safety before approaching the victim. Ensure the area is 
            free from any ongoing threats, such as fire or chemical hazards. If safe, approach the victim cautiously 
            and assess their level of consciousness, airway, breathing, and circulation (ABCs).""",
            'CoolBurnArea': """If the burn is caused by a heat source (e.g., fire, hot liquid), immediately cool the 
            affected area with cool running water for at least 10-20 minutes. Remove any clothing or jewelry from the 
            burned area, but do not remove any adherent clothing to avoid further skin damage.""",
            'CoverBurns': """After cooling the burn, cover the affected area loosely with a clean, dry cloth or sterile 
            dressing to protect it from further contamination and reduce the risk of infection. Avoid using adhesive 
            dressings or ointments on the burn.""",
            'AirwayManagement': """If the victim is conscious and breathing, encourage them to sit up slightly to ease 
            breathing efforts. If the burn affects the face or neck and causes difficulty breathing, encourage the victim 
            to maintain a position that maximizes airway patency, such as sitting upright with their head tilted slightly 
            forward.""",
            'PainManagement': """Assess and manage pain using appropriate pain relief measures, such as over-the-counter 
            pain medications or cold compresses. Be mindful of potential complications, such as shock or respiratory distress, 
            and monitor the victim's vital signs closely.""",
            'AdditionalInstructions': """Continue to monitor the victim's condition closely and provide reassurance. If 
            the burn is severe or covers a large area of the head or neck, seek medical assistance immediately."""
        },
        'BurnInjuryToTheTorsoOrExtremities(x)': {
            'Assessment': """Assess the severity of the burn and determine the extent of injury. Look for signs of 
            blistering, charring, or deep tissue damage. Assess the victim's pain level and overall condition.""",
            'CoolBurnArea': """If the burn is caused by a heat source, immediately cool the affected area with cool 
            running water for at least 10-20 minutes. Remove any clothing or jewelry from the burned area, but avoid 
            removing adherent clothing to prevent further skin damage.""",
            'CoverBurns': """After cooling the burn, cover the affected area loosely with a clean, dry cloth or sterile 
            dressing. Avoid using adhesive dressings or ointments, as they may trap heat and worsen the burn.""",
            'PainManagement': """Provide pain relief as needed using appropriate pain medications or cold compresses. 
            Monitor the victim for signs of shock or respiratory distress and provide supportive care as necessary.""",
            'Elevation': """If the burn affects the extremities, elevate the injured limb to reduce swelling and 
            discomfort. Support the limb in a comfortable position while awaiting medical assistance.""",
            'AdditionalInstructions': """Continue to monitor the victim's vital signs closely and provide reassurance. 
            Seek medical assistance promptly for burns that are severe, cover a large area, or involve sensitive areas 
            such as the hands, feet, or genitals."""
        }
    }

    memory = {}

    agenda = []

    for symptom in symptoms:
        agenda.append(expr(symptom))

    seen = set()
    while agenda:
        p = agenda.pop(0)
        print(f'p : {p}')
        if p in seen:
            print('p is seen')
            continue
        seen.add(p)
        if fol_fc_ask(kb, p):
            print(f'{p} is true.')
            memory[p] = True
        else:
            print(f'{p} is false.')
            memory[p] = False

        if memory.get(expr('Injured(x)'), False) and memory.get(expr('InjuryLocationHead(x)'), False) and memory.get(expr('GunshotWound(x)'), False):
            agenda.append(expr('GunshotWoundToTheHead(x)'))
            print('1st case')

        if memory.get(expr('Injured(x)'), False) and memory.get(expr('InjuryLocationChest(x)'), False) and memory.get(expr('GunshotWound(x)'), False):
            agenda.append(expr('GunshotWoundToTheChest(x)'))
            print('2nd case')

        if memory.get(expr('Injured(x)'), False) and memory.get(expr('InjuryLocationHeadAbdomen(x)'), False) and memory.get(expr('GunshotWound(x)'), False):
            agenda.append(expr('GunshotWoundToTheAbdomen(x)'))
            print('3rd case')

        if memory.get(expr('Injured(x)'), False) and memory.get(expr('InjuryLocationLimbs(x)'), False) and memory.get(expr('GunshotWound(x)'), False):
            agenda.append(expr('GunshotWoundToTheLimbs(x)'))
            print('4th case')

        # Blast Injury

        if memory.get(expr('Injured(x)'), False) and memory.get(expr('InjuryLocationHead(x)'), False) and memory.get(expr('BlastInjury(x)'), False):
            agenda.append(expr('BlastInjuryToTheHead(x)'))
            print('5th case')

        if memory.get(expr('Injured(x)'), False) and memory.get(expr('InjuryLocationChest(x)'), False) and memory.get(expr('BlastInjury(x)'), False):
            agenda.append(expr('BlastInjuryToTheChest(x)'))
            print('6th case')

        if memory.get(expr('Injured(x)'), False) and memory.get(expr('InjuryLocationHeadAbdomen(x)'), False) and memory.get(expr('BlastInjury(x)'), False):
            agenda.append(expr('BlastInjuryToTheAbdomen(x)'))
            print('7th case')

        if memory.get(expr('Injured(x)'), False) and memory.get(expr('InjuryLocationLimbs(x)'), False) and memory.get(expr('BlastInjury(x)'), False):
            agenda.append(expr('BlastInjuryToTheLimbs(x)'))
            print('8th case')

        # Burn Injury

        if memory.get(expr('Injured(x)'), False) and memory.get(expr('InjuryLocationHead(x)'), False) and memory.get(expr('BurnInjury(x)'), False):
            agenda.append(expr('BurnInjuryToTheHeadOrNeck(x)'))
            print('5th case')

        if memory.get(expr('Injured(x)'), False) and memory.get(expr('InjuryLocationChest(x)'), False) and memory.get(expr('BurnInjury(x)'), False):
            agenda.append(expr('BurnInjuryToTheTorsoOrExtremities(x)'))
            print('6th case')

        if memory.get(expr('Injured(x)'), False) and memory.get(expr('InjuryLocationHeadAbdomen(x)'), False) and memory.get(expr('BurnInjury(x)'), False):
            agenda.append(expr('BurnInjuryToTheTorsoOrExtremities(x)'))
            print('7th case')

        if memory.get(expr('Injured(x)'), False) and memory.get(expr('InjuryLocationLimbs(x)'), False) and memory.get(expr('BurnInjury(x)'), False):
            agenda.append(expr('BurnInjuryToTheTorsoOrExtremities(x)'))
            print('8th case')

    instructions = []
    for p, value in memory.items():
        print(f'p is {p}')
        if value:
            instruction = first_aid_instructions.get(str(p))
            print(f'instruction {instruction}')
            if instruction:
                instructions.append(instruction)

    print(f'agneda : {agenda}')
    print(f'memory : {memory}')

    return instructions