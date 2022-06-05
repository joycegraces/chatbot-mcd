import aiml, os
# membuat kernel dan mempelajari berkas AIML

kern = aiml.Kernel()
if os.path.isfile("bot_brain.brn"):
    kern.bootstrap(brainFile = "bot_brain.brn")
else:
    kern.bootstrap(learnFiles = "star.xml", commands = "AIML A")
    kern.saveBrain("bot_brain.brn")


def get_respond(msg):
    #print(kernel.respond(input("User: >> ")))
    if (kern.respond(msg)):
        return (kern.respond(msg))
    else:
        return  "Maaf Ka, saya kurang mengerti. Bisakah diulangi lagi?"
