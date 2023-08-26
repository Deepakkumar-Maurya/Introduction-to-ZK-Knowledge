import hashlib
import random

def challenge():
  return random.randrange(0,100)


def hashing(secret):
  return hashlib.sha256(secret.encode()).hexdigest()

def proveKnowledge(secret):
  return hashing(secret)

def verifyKnowledge(hashedSecret, expectedSecret):
  flag = 0
  for i in range(0,100):
    hashExpectedSecret = hashing(expectedSecret + str(i))
    if (hashExpectedSecret == hashedSecret):
      flag = 1
      break

  if (flag == 1):
    return True
  else:
    return False

#A-Prover
secret =  "Treasure Location is AYZ"
challengeValue = challenge()
hashedSecret = proveKnowledge(secret + str(challengeValue))

#B-Verifier
expectedSecret =  "Treasure Location is XYZ"

if (verifyKnowledge(hashedSecret, expectedSecret)):
  print ("Treasure locations are the same")
else:
  print ("Treasure locations are not same")