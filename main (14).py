import random

# Function to train the AI model
def train (t_num, t_quality):
  Probability = [50]*20 # A list to store the initial probabilities, all set to 50
  x = [1]*20 # A list with 20 elements, all set to 1 
  succ_count=[0]*20 # A list to track success count for each Element
  fail_count=[0]*20 # A list to track failure count for each Element
  for _i in range(t_num):
    n= random.randint(0,19) # Randomly select an Question number from 1 to 20
    float1 = random.random() # Generate a random float between 0 and 1

    # Check if the generated random float is greater than t_quality
    if float1 > t_quality:
      if (succ_count[n-1] >0) and (fail_count[n-1]==0):
        succ_count[n-1] =0
        Probability[n-1] -=1
        fail_count[n-1] +=1

      elif fail_count[n-1] == 0 :
        Probability[n-1] -= 1
        fail_count[n-1] += 1

      elif fail_count[n-1] >=1:
        Probability[n-1] -= 1*(2**fail_count[n-1])
        fail_count[n-1] += 1

    # Check If the random float is less than t_quality
    elif float1 < t_quality:
      if (fail_count[n-1]>0) and(succ_count[n-1]==0):
        succ_count[n-1]+=1
        fail_count[n-1]=0
        Probability[n-1]+=1

      elif succ_count[n-1] == 0:
        Probability[n-1] += 1
        succ_count[n-1] += 1

      elif succ_count[n-1] >=1:
        Probability[n-1] += 1*(2**succ_count[n-1])
        succ_count[n-1] += 1

    Probability[n-1] = max(0, min(100, Probability[n-1])) # Ensure Probability[n-1] stays within the range [0, 100]    
    # print(Probability)

  return Probability # return Probability

# train(100,0.6)


# Function to test the AI model
def test(prob_list):
  randomlist = []
  for i in range(0,20):
    n = random.randint(1,101) # Generate 20 random numbers between 1 and 100
Instructor
| 09/27 at 6:44 pm
Grading comment:
you want this to be (0,100)

    randomlist.append(n)
  # Count the number of elements where the corresponding Probability is greater than the random number
  count = sum([1 for a, b in zip(prob_list, randomlist) if a > b])
  # If count is greater than or equal to 15, return 1; otherwise, return 0
  if count>=15:
    return 1
  else:
    return 0


# Functions below to train and test the AI 1000 times in succession and calculate the pass rate
def pass_rate(t_num, t_quality):
  pass_count = 0
  total_tests = 1000 # Total number of tests to run

  for _ in range(total_tests):
    Probability = train(t_num, t_quality) # Train the model and get updated Probability list
    result = test(Probability)  # Test the model with the updated Probability
    pass_count += result

  # Calculate and print the pass rate percentage
  pass_rate_percentage = (pass_count / total_tests)*100
  print(f"The pass rate for this AI is {pass_rate_percentage:.1f}%")



pass_rate(100, 0.9) #Called the pass_rate function to see the pass rate percentage