"""Everything made up lives in this one file.

BUSINESS     the business the receptionist answers the phone for. The sidebar and the
             Settings page read it. Change it here to use another business.
SAMPLE_CALLS the fake phone calls that "python seed.py" puts into the
             database, so the dashboard has something to show before real
             calls exist.

All phone numbers use 555-01xx, a range that is reserved for examples.
"""

from datetime import datetime

BUSINESS = {
    "name": "Sunrise Dental Clinic",
    "phone": "+1 (555) 010-0100",
    "address": "123 Main Street, Suite 2, Edison, NJ 08817",
    "hours": [
        "Monday to Friday: 9:00 AM to 6:00 PM",
        "Saturday: 9:00 AM to 1:00 PM",
        "Sunday: closed",
    ],
    "services": [
        "Check-up and exam",
        "Teeth cleaning",
        "Filling",
        "Crown fitting",
        "Root canal consult",
        "Whitening consult",
        "Braces consult",
    ],
    "languages": ["English", "Hindi", "Hinglish", "Telugu", "Tamil", "Spanish"],
    "greeting": "Thank you for calling Sunrise Dental Clinic. How can I help you today?",
}


# Each call is one dictionary. "appointments" may be an empty list.
# datetime(2026, 11, 23, 14, 5) means 23 Nov 2026, 2:05 PM.
SAMPLE_CALLS = [
    {
        "caller_number": "+1 (555) 010-0142",
        "language": "Telugu",
        "started_at": datetime(2026, 11, 23, 14, 5),
        "duration_seconds": 134,
        "sms_sent": True,
        "summary": [
            "Greeted the caller in Telugu",
            "Booked a teeth cleaning for Tuesday 2:00 PM",
            "Asked for a follow-up check on 8 December, waiting for your OK",
            "Cancelled the old Friday appointment",
            "Sent an SMS confirmation",
        ],
        "transcript": [
            "Receptionist: నమస్కారం, సన్‌రైజ్ డెంటల్ క్లినిక్‌కి కాల్ చేసినందుకు ధన్యవాదాలు. నేను మీకు ఎలా సహాయం చేయగలను?",
            "Caller: నమస్తే, నా పేరు ప్రియ. నాకు శుక్రవారం సాయంత్రం 4 గంటలకు వైటెనింగ్ అపాయింట్‌మెంట్ ఉంది. దాన్ని రద్దు చేసి, పళ్ళ క్లీనింగ్ బుక్ చేయాలి.",
            "Receptionist: తప్పకుండా. శుక్రవారం అపాయింట్‌మెంట్ రద్దు చేశాను. క్లీనింగ్ కోసం రేపు, మంగళవారం మధ్యాహ్నం 2 గంటలకు స్లాట్ ఉంది. అది సరిపోతుందా?",
            "Caller: అవును, మంగళవారం 2 గంటలు బాగుంది.",
            "Receptionist: బుక్ అయింది. ఇంకేమైనా కావాలా?",
            "Caller: క్లీనింగ్ తర్వాత ఫాలో-అప్ చెకప్ కూడా కావాలి. డిసెంబర్ 8 ఉదయం 10:30కి వీలవుతుందా?",
            "Receptionist: ఆ సమయాన్ని క్లినిక్ నిర్ధారించాలి. నేను రిక్వెస్ట్ పెట్టాను, నిర్ధారణ అయిన వెంటనే మీకు తెలియజేస్తాం.",
            "Caller: సరే, ధన్యవాదాలు.",
            "Receptionist: మంగళవారం అపాయింట్‌మెంట్ వివరాలు మీకు SMS లో పంపాను. ధన్యవాదాలు!",
        ],
        "appointments": [
            {
                "customer_name": "Priya R.",
                "service": "Teeth cleaning",
                "starts_at": datetime(2026, 11, 24, 14, 0),
                "status": "Confirmed",
            },
            {
                "customer_name": "Priya R.",
                "service": "Follow-up check",
                "starts_at": datetime(2026, 12, 8, 10, 30),
                "status": "Pending",
            },
            {
                "customer_name": "Priya R.",
                "service": "Whitening consult",
                "starts_at": datetime(2026, 11, 27, 16, 0),
                "status": "Cancelled",
            },
        ],
    },
    {
        "caller_number": "+1 (555) 010-0117",
        "language": "English",
        "started_at": datetime(2026, 11, 23, 11, 40),
        "duration_seconds": 96,
        "sms_sent": False,
        "summary": [
            "Greeted the caller in English",
            "Explained what a first visit includes",
            "Said the front desk will confirm the caller's insurance plan",
            "Caller will call back to book",
        ],
        "transcript": [
            "Receptionist: Thank you for calling Sunrise Dental Clinic. How can I help you today?",
            "Caller: Hi, I'm new to the area. Do you take new patients, and how long is a first visit?",
            "Receptionist: Yes, we are taking new patients. A first visit is an exam and a cleaning, and it takes about an hour.",
            "Caller: Do you accept my insurance? I have a PPO plan through work.",
            "Receptionist: I can't check a specific plan on this call. The front desk will confirm it when you bring your insurance card. Would you like me to book a first visit now?",
            "Caller: Not yet, let me find my card first. I'll call back.",
            "Receptionist: No problem. We are open Monday to Friday 9 AM to 6 PM, and Saturday 9 AM to 1 PM. Have a great day!",
        ],
        "appointments": [],
    },
    {
        "caller_number": "+1 (555) 010-0163",
        "language": "Spanish",
        "started_at": datetime(2026, 11, 23, 9, 15),
        "duration_seconds": 151,
        "sms_sent": True,
        "summary": [
            "Greeted the caller in Spanish",
            "Caller has had a strong toothache since yesterday",
            "Booked a toothache exam for Tuesday 9:00 AM",
            "Sent an SMS confirmation",
        ],
        "transcript": [
            "Receptionist: Hola, gracias por llamar a Sunrise Dental Clinic. ¿En qué puedo ayudarle?",
            "Caller: Hola, me llamo María. Tengo un dolor de muela muy fuerte desde ayer. ¿Me pueden atender pronto?",
            "Receptionist: Lo siento mucho. Tenemos una cita disponible mañana, martes 24 de noviembre, a las 9 de la mañana. ¿Le queda bien?",
            "Caller: Sí, perfecto.",
            "Receptionist: Listo, María. Su cita para revisar el dolor de muela es mañana a las 9 de la mañana. Le acabo de enviar un mensaje de texto con los detalles.",
            "Caller: Muchas gracias.",
            "Receptionist: Gracias a usted. ¡Que se mejore pronto!",
        ],
        "appointments": [
            {
                "customer_name": "María G.",
                "service": "Toothache exam",
                "starts_at": datetime(2026, 11, 24, 9, 0),
                "status": "Confirmed",
            },
        ],
    },
    {
        "caller_number": "+1 (555) 010-0128",
        "language": "Hinglish",
        "started_at": datetime(2026, 11, 21, 16, 30),
        "duration_seconds": 118,
        "sms_sent": False,
        "summary": [
            "Greeted the caller in Hinglish",
            "Answered after closing time on Saturday",
            "Asked for a child's check-up next Saturday 10:00 AM, waiting for your OK",
            "Told the caller the clinic will confirm by text",
        ],
        "transcript": [
            "Receptionist: Hello, Sunrise Dental Clinic mein call karne ke liye thank you. Main aapki kya help kar sakti hoon?",
            "Caller: Hi, mera naam Rohan hai. Mujhe apne bete Aarav ka dental check-up karwana hai. Agle Saturday ko koi slot milega?",
            "Receptionist: Saturday 28 November ko subah 10 baje ka slot khaali hai. Saturday ke slots clinic khud confirm karta hai, toh main aapki request daal deti hoon.",
            "Caller: Theek hai, 10 baje chalega. Confirm kab tak hoga?",
            "Receptionist: Clinic Monday tak confirm kar dega, aur aapko SMS aa jayega.",
            "Caller: Okay, thanks.",
            "Receptionist: Thank you, aapka din achha rahe!",
        ],
        "appointments": [
            {
                "customer_name": "Aarav M.",
                "service": "Child check-up",
                "starts_at": datetime(2026, 11, 28, 10, 0),
                "status": "Pending",
            },
        ],
    },
    {
        "caller_number": "+1 (555) 010-0155",
        "language": "Hindi",
        "started_at": datetime(2026, 11, 21, 10, 5),
        "duration_seconds": 172,
        "sms_sent": True,
        "summary": [
            "Greeted the caller in Hindi",
            "Cancelled the filling on Monday 23 November",
            "Booked the filling again for Monday 30 November, 3:00 PM",
            "Sent an SMS confirmation",
        ],
        "transcript": [
            "Receptionist: नमस्ते, सनराइज़ डेंटल क्लिनिक में कॉल करने के लिए धन्यवाद। मैं आपकी क्या मदद कर सकती हूँ?",
            "Caller: नमस्ते, मैं सुनीता बोल रही हूँ। सोमवार को तीन बजे मेरी फिलिंग की अपॉइंटमेंट है, लेकिन मैं उस दिन नहीं आ पाऊँगी।",
            "Receptionist: कोई बात नहीं। क्या मैं इसे अगले सोमवार, 30 नवंबर को तीन बजे कर दूँ?",
            "Caller: हाँ, वह ठीक रहेगा।",
            "Receptionist: हो गया। 23 नवंबर की अपॉइंटमेंट रद्द कर दी है, और 30 नवंबर, सोमवार दोपहर 3 बजे की नई अपॉइंटमेंट बुक कर दी है।",
            "Caller: क्या मुझे कोई मैसेज मिलेगा?",
            "Receptionist: जी हाँ, मैंने अभी आपको SMS भेज दिया है।",
            "Caller: धन्यवाद।",
            "Receptionist: धन्यवाद, आपका दिन शुभ हो!",
        ],
        "appointments": [
            {
                "customer_name": "Sunita K.",
                "service": "Filling",
                "starts_at": datetime(2026, 11, 30, 15, 0),
                "status": "Confirmed",
            },
            {
                "customer_name": "Sunita K.",
                "service": "Filling",
                "starts_at": datetime(2026, 11, 23, 15, 0),
                "status": "Cancelled",
            },
        ],
    },
    {
        "caller_number": "+1 (555) 010-0109",
        "language": "Tamil",
        "started_at": datetime(2026, 11, 20, 18, 45),
        "duration_seconds": 88,
        "sms_sent": True,
        "summary": [
            "Greeted the caller in Tamil",
            "Answered after closing time",
            "Booked a root canal consult for Tuesday 1 December, 11:00 AM",
            "Sent an SMS confirmation",
        ],
        "transcript": [
            "Receptionist: வணக்கம், சன்ரைஸ் டென்டல் கிளினிக்கிற்கு அழைத்ததற்கு நன்றி. நான் உங்களுக்கு எப்படி உதவலாம்?",
            "Caller: வணக்கம், என் பெயர் கார்த்திக். எனக்கு பல் வலி அதிகமாக இருக்கிறது. ரூட் கெனால் பற்றி டாக்டரிடம் பேச வேண்டும்.",
            "Receptionist: சரி, புரிகிறது. கிளினிக் இப்போது மூடியிருக்கிறது, ஆனால் நான் உங்களுக்கு அப்பாயின்ட்மென்ட் பதிவு செய்ய முடியும். டிசம்பர் 1, செவ்வாய்க்கிழமை காலை 11 மணிக்கு நேரம் இருக்கிறது. அது சரியா?",
            "Caller: சரி, செவ்வாய்க்கிழமை 11 மணி பரவாயில்லை.",
            "Receptionist: பதிவு செய்துவிட்டேன். டிசம்பர் 1, செவ்வாய்க்கிழமை காலை 11 மணிக்கு ரூட் கெனால் ஆலோசனை. விவரங்களை SMS மூலம் அனுப்பியிருக்கிறேன்.",
            "Caller: நன்றி.",
            "Receptionist: நன்றி, நல்ல நாளாக அமையட்டும்!",
        ],
        "appointments": [
            {
                "customer_name": "Karthik S.",
                "service": "Root canal consult",
                "starts_at": datetime(2026, 12, 1, 11, 0),
                "status": "Confirmed",
            },
        ],
    },
    {
        "caller_number": "+1 (555) 010-0171",
        "language": "English",
        "started_at": datetime(2026, 11, 20, 13, 20),
        "duration_seconds": 45,
        "sms_sent": False,
        "summary": [
            "Greeted the caller in English",
            "Gave the opening hours",
            "Gave the clinic address",
        ],
        "transcript": [
            "Receptionist: Thank you for calling Sunrise Dental Clinic. How can I help you today?",
            "Caller: Hi, what time do you close today? And where exactly are you?",
            "Receptionist: We are open until 6 PM today. The clinic is at 123 Main Street, Suite 2, in Edison.",
            "Caller: Great, that's all I needed. Thanks.",
            "Receptionist: You're welcome. Have a great day!",
        ],
        "appointments": [],
    },
    {
        "caller_number": "+1 (555) 010-0134",
        "language": "Spanish",
        "started_at": datetime(2026, 11, 20, 8, 50),
        "duration_seconds": 127,
        "sms_sent": True,
        "summary": [
            "Greeted the caller in Spanish",
            "Answered before opening time",
            "Cancelled today's 2:00 PM teeth cleaning",
            "Caller will call back for a new date",
            "Sent an SMS confirmation of the cancellation",
        ],
        "transcript": [
            "Receptionist: Hola, gracias por llamar a Sunrise Dental Clinic. ¿En qué puedo ayudarle?",
            "Caller: Buenos días, soy Luis. Tengo una limpieza hoy a las 2 de la tarde, pero no voy a poder ir.",
            "Receptionist: Entiendo. ¿Quiere que la cancele, o prefiere cambiarla a otro día?",
            "Caller: Cancélela, por favor. Yo llamo después para hacer otra cita.",
            "Receptionist: De acuerdo, su cita de hoy a las 2 de la tarde queda cancelada. Le envié un mensaje de texto para confirmarlo.",
            "Caller: Gracias.",
            "Receptionist: Gracias a usted. ¡Que tenga un buen día!",
        ],
        "appointments": [
            {
                "customer_name": "Luis H.",
                "service": "Teeth cleaning",
                "starts_at": datetime(2026, 11, 20, 14, 0),
                "status": "Cancelled",
            },
        ],
    },
    {
        "caller_number": "+1 (555) 010-0188",
        "language": "Telugu",
        "started_at": datetime(2026, 11, 19, 17, 10),
        "duration_seconds": 143,
        "sms_sent": True,
        "summary": [
            "Greeted the caller in Telugu",
            "Booked a crown fitting for Thursday 3 December, 1:30 PM",
            "Sent an SMS confirmation",
        ],
        "transcript": [
            "Receptionist: నమస్కారం, సన్‌రైజ్ డెంటల్ క్లినిక్‌కి కాల్ చేసినందుకు ధన్యవాదాలు. నేను మీకు ఎలా సహాయం చేయగలను?",
            "Caller: నమస్తే, నా పేరు లక్ష్మి. నా క్రౌన్ ఫిట్టింగ్ కోసం అపాయింట్‌మెంట్ కావాలి.",
            "Receptionist: తప్పకుండా. డిసెంబర్ 3, గురువారం మధ్యాహ్నం 1:30కి స్లాట్ ఉంది. అది మీకు సరిపోతుందా?",
            "Caller: సరిపోతుంది.",
            "Receptionist: మీ అపాయింట్‌మెంట్ బుక్ అయింది. వివరాలు మీకు SMS లో పంపాను.",
            "Caller: చాలా ధన్యవాదాలు.",
            "Receptionist: ధన్యవాదాలు!",
        ],
        "appointments": [
            {
                "customer_name": "Lakshmi V.",
                "service": "Crown fitting",
                "starts_at": datetime(2026, 12, 3, 13, 30),
                "status": "Confirmed",
            },
        ],
    },
    {
        "caller_number": "+1 (555) 010-0146",
        "language": "Hinglish",
        "started_at": datetime(2026, 11, 19, 12, 30),
        "duration_seconds": 104,
        "sms_sent": False,
        "summary": [
            "Greeted the caller in Hinglish",
            "Said the cost of braces is given after a consult",
            "Asked for a braces consult on Friday 4 December, 4:30 PM, waiting for your OK",
            "Told the caller the clinic will confirm by text",
        ],
        "transcript": [
            "Receptionist: Hello, Sunrise Dental Clinic mein call karne ke liye thank you. Main aapki kya help kar sakti hoon?",
            "Caller: Hi, braces lagwane ka kitna kharcha aata hai?",
            "Receptionist: Braces ka cost doctor ke consultation ke baad hi bataya ja sakta hai. Kya main aapke liye ek consultation book kar doon?",
            "Caller: Haan, kisi Friday shaam ko ho sakta hai?",
            "Receptionist: Friday 4 December ko shaam 4:30 baje ka time khaali hai. Braces ke consultation clinic khud confirm karta hai, toh main aapki request daal deti hoon.",
            "Caller: Theek hai, daal dijiye. Mera naam Aman hai.",
            "Receptionist: Request daal di hai, Aman. Confirm hote hi aapko SMS mil jayega. Thank you!",
        ],
        "appointments": [
            {
                "customer_name": "Aman S.",
                "service": "Braces consult",
                "starts_at": datetime(2026, 12, 4, 16, 30),
                "status": "Pending",
            },
        ],
    },
    {
        "caller_number": "+1 (555) 010-0192",
        "language": "Hindi",
        "started_at": datetime(2026, 11, 18, 15, 40),
        "duration_seconds": 67,
        "sms_sent": False,
        "summary": [
            "Greeted the caller in Hindi",
            "Said the clinic is closed on Sunday and gave the opening hours",
            "Offered to book an appointment, caller said not now",
        ],
        "transcript": [
            "Receptionist: नमस्ते, सनराइज़ डेंटल क्लिनिक में कॉल करने के लिए धन्यवाद। मैं आपकी क्या मदद कर सकती हूँ?",
            "Caller: नमस्ते, क्या आपका क्लिनिक रविवार को खुला रहता है?",
            "Receptionist: रविवार को क्लिनिक बंद रहता है। हम सोमवार से शुक्रवार सुबह 9 से शाम 6 बजे तक, और शनिवार को सुबह 9 से दोपहर 1 बजे तक खुले रहते हैं।",
            "Caller: ठीक है, मैं शनिवार को फिर कॉल करूँगा।",
            "Receptionist: ज़रूर। क्या मैं अभी आपके लिए अपॉइंटमेंट बुक कर दूँ?",
            "Caller: नहीं, अभी नहीं। धन्यवाद।",
            "Receptionist: धन्यवाद, आपका दिन शुभ हो!",
        ],
        "appointments": [],
    },
    {
        "caller_number": "+1 (555) 010-0120",
        "language": "English",
        "started_at": datetime(2026, 11, 18, 9, 5),
        "duration_seconds": 162,
        "sms_sent": True,
        "summary": [
            "Greeted the caller in English",
            "Booked a teeth cleaning for Emily on Wednesday 2 December, 10:00 AM",
            "Booked a teeth cleaning for Jack right after, at 10:30 AM",
            "Sent an SMS confirmation",
        ],
        "transcript": [
            "Receptionist: Thank you for calling Sunrise Dental Clinic. How can I help you today?",
            "Caller: Hi, this is Emily. I'd like to book cleanings for me and my son Jack, back to back if you can.",
            "Receptionist: Of course. I have Wednesday 2 December at 10:00 AM and 10:30 AM, one after the other. Does that work?",
            "Caller: That's perfect. Put me first, please.",
            "Receptionist: Done. Emily at 10:00 AM and Jack at 10:30 AM on Wednesday 2 December. I've sent a text with both times.",
            "Caller: Got it. Thank you!",
            "Receptionist: You're welcome. See you both then!",
        ],
        "appointments": [
            {
                "customer_name": "Emily T.",
                "service": "Teeth cleaning",
                "starts_at": datetime(2026, 12, 2, 10, 0),
                "status": "Confirmed",
            },
            {
                "customer_name": "Jack T.",
                "service": "Teeth cleaning",
                "starts_at": datetime(2026, 12, 2, 10, 30),
                "status": "Confirmed",
            },
        ],
    },
]
