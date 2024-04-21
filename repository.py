from aima3.utils import expr
from aima3.logic import FolKB, fol_fc_ask

def get_first_aid_instructions(*symptoms):
    # Define the knowledge base
    kb = FolKB()

    # Define variables
    x = expr('x')  # Variable representing a person

    # Add rules to the knowledge base for common warzone injuries
    kb.tell(expr('GunshotWound(x) ==> ApplyPressure(x)'))
    kb.tell(expr('GunshotWound(x) ==> ElevateInjuredArea(x)'))
    kb.tell(expr('BlastInjury(x) & TraumaticAmputation(x) ==> ApplyTourniquet(x)'))
    kb.tell(expr('BurnInjury(x) & SevereBurns(x) ==> CoolBurns(x)'))
    kb.tell(expr('SharpForceInjury(x) & SevereLaceration(x) ==> ApplyPressure(x)'))
    kb.tell(expr('CrushInjury(x) & SevereCompression(x) ==> StabilizeInjuredArea(x)'))
    kb.tell(expr('CrushInjury(x) & SevereCompression(x) ==> CheckCirculation(x)'))

    # Define the agenda
    agenda = []

    # Add patient symptoms to the agenda
    patient = expr('x')  # Constant representing a specific patient
    for symptom in symptoms:
        agenda.append(symptom)

    # Define first aid instructions for each injury
    first_aid_instructions = {
        'ApplyPressure(x)': """Apply direct pressure to the wound using a clean cloth or bandage.
        Use your palm or fingers to apply firm, even pressure to control bleeding.
        Maintain constant pressure on the wound until bleeding stops or medical help arrives.
        Avoid lifting the cloth or bandage to check the wound, as this may disrupt clot formation.
        Monitor the victim's condition closely for signs of shock, such as pale skin, rapid heartbeat, or shallow breathing.
        If the victim shows signs of shock, lay them down flat, elevate their legs slightly, and cover them with a blanket or jacket to keep them warm.
        Wait for medical help to arrive and provide relevant information about the victim's condition and the first aid measures you've taken.""",
        'ElevateInjuredArea(x)': """If the injury is in an extremity (arm or leg), gently raise the injured limb above the level of the heart.
        Use pillows, blankets, or other available items to support the limb in an elevated position.
        Elevating the injured area helps reduce swelling and bleeding by allowing gravity to assist in draining excess fluid away from the injury site.
        If the injury is in the head or neck, do not attempt to elevate the area.
        Instead, keep the victim lying flat and still until medical help arrives.
        Monitor the victim\'s condition closely for any changes, and be prepared to adjust their position if necessary.""",
        'ApplyTourniquet(x)': """If the bleeding is severe and cannot be controlled by direct pressure, consider applying a tourniquet.
        Select a wide, flat band or improvised tourniquet, such as a belt or strip of cloth, that is at least an inch or two wide.
        Position the tourniquet between the wound and the body's core, several inches above the injury site. Place the tourniquet high and tight, ensuring that it is snugly wrapped around the limb but not so tight that it causes additional pain or damage.
        Secure the tourniquet in place with a knot or clasp, ensuring that it will not loosen or slip during transport. Note the time the tourniquet was applied, as this information will be important for medical personnel.
        Monitor the victim's condition closely for any changes, and be prepared to adjust the tourniquet if necessary. Wait for medical help to arrive and provide relevant information about the victim's condition and the first aid measures you've taken.""",
        'CoolBurns(x)': """ Identify the burned area on the victim's body, noting the size and severity of the burn.
        If the burn is minor (first-degree) and covers a small area, immediately cool the burned area with cool (not cold) running water from a tap or shower.
        If running water is not available, apply cool compresses to the burn using a clean cloth soaked in cool water.
        Continue cooling the burn for at least 10 to 15 minutes to help reduce pain, swelling, and further tissue damage.
        Do not use ice or ice water to cool the burn, as this can cause additional tissue damage.
        If the burn is severe (second-degree or larger), cover the burned area loosely with a clean, dry cloth or sterile gauze to protect it from further injury.
        Do not apply any creams, ointments, or butter to the burn, as these can trap heat and increase the risk of infection.
        Monitor the victim's condition closely for any signs of shock, such as pale skin, rapid heartbeat, or shallow breathing.
        If the victim shows signs of shock, lay them down flat, elevate their legs slightly, and cover them with a blanket or jacket to keep them warm.
        Wait for medical help to arrive and provide relevant information about the victim's condition and the first aid measures you've taken.""",
        'StabilizeInjuredArea(x)': """Locate the injured area on the victim's body, noting its location and severity.
        If the injury involves a broken bone or joint, or if there is significant movement or deformity at the injury site, it's essential to stabilize the injured area to prevent further damage and reduce pain.
        Begin by supporting the injured limb or body part in the position in which you found it, avoiding any unnecessary movement.
        Use improvised splints, such as rolled-up newspapers, magazines, or sturdy sticks, to immobilize the injured area.
        Place the splint along the length of the injured limb, extending beyond the joint above and below the injury site.
        Secure the splint in place using bandages, cloth strips, or other available materials, ensuring that it is snug but not too tight.
        Check the injured area for any signs of circulation, such as pulse and capillary refill, to ensure that blood flow is not restricted by the splint.
        If circulation is compromised or if the victim experiences increased pain, loosen the splint slightly and reassess the position.
        Once the injured area is stabilized, keep the victim lying down and calm until medical help arrives.
        Monitor the victim's condition closely for any changes, and be prepared to adjust the splint if necessary.
        Wait for medical help to arrive and provide relevant information about the victim's condition and the first aid measures you've taken.""",
        'CheckCirculation(x)': """ If the injury involves significant bleeding, a crushed limb, or a suspected vascular injury, it's essential to check the circulation to assess blood flow to the affected area.
        Begin by gently palpating (feeling) for pulses in the injured limb or body part.
        Common pulse points include the wrist (radial pulse), neck (carotid pulse), and groin (femoral pulse).
        Use your fingertips to apply light pressure to the pulse point, feeling for the rhythmic pulsations of blood flow.
        If you cannot detect a pulse in the injured limb, try checking another pulse point or comparing with the pulse on the uninjured side of the body.
        Additionally, observe the color and temperature of the skin in the injured area.
        Normal skin color is pink or reddish, and the skin should feel warm to the touch.
        Pale or bluish skin, cold skin temperature, or delayed capillary refill (the time it takes for color to return after pressing on the skin) may indicate poor circulation.
        If you are unable to detect a pulse or if circulation appears compromised, notify emergency services immediately and continue providing first aid while awaiting medical help.
        Keep the victim lying down and calm, and avoid unnecessary movement of the injured limb or body part.
        Reassure the victim that help is on the way, and monitor their condition closely for any changes.
        Wait for medical help to arrive and provide relevant information about the victim's condition and the first aid measures you've taken.""",
        # Add more instructions for other first aid measures
    }

    # Temporary memory
    memory = {}

    # Run the expert system
    seen = set()  # Keep track of the conditions already processed
    while agenda:
        p = agenda.pop(0)
        if p in seen:
            continue  # Skip the condition if it has already been processed
        seen.add(p)
        if fol_fc_ask(kb, p):
            print(f'{p} is true.')
            memory[p] = True
        else:
            print(f'{p} is false.')
            memory[p] = False

        # Check if new rules can be activated
        if memory.get(expr('GunshotWound(x)'), False):
            agenda.append(expr('ApplyPressure(x)'))
            agenda.append(expr('ElevateInjuredArea(x)'))
        # Add similar conditions for other common injuries
        if memory.get(expr('BlastInjury(x)'), False) and memory.get(expr('TraumaticAmputation(x)'), False):
            agenda.append(expr('ApplyTourniquet(x)'))
        if memory.get(expr('BurnInjury(x)'), False) and memory.get(expr('SevereBurns(x)'), False):
            agenda.append(expr('CoolBurns(x)'))
        if memory.get(expr('SharpForceInjury(x)'), False) and memory.get(expr('SevereLaceration(x)'), False):
            agenda.append(expr('ApplyPressure(x)'))
        # Add similar conditions for other first aid measures
        if memory.get(expr('CrushInjury(x)'), False) and memory.get(expr('SevereCompression(x)'), False):
            agenda.append(expr('StabilizeInjuredArea(x)'))
            agenda.append(expr('CheckCirculation(x)'))
        # Add similar conditions for other first aid measures

    # Collect first aid instructions
    instructions = []
    for p, value in memory.items():
        print(f'p is {p}')
        if value:
            instruction = first_aid_instructions.get(str(p))
            print(f'instruction {instruction}')
            if instruction:
                instructions.append(instruction)

    return instructions