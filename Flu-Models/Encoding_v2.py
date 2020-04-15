# -*- coding: utf-8 -*-
def encodingUsingPd(sequence, lb):
    y2 = list(sequence)
    y = lb.fit_transform(y2)
    return y

def encoding(sequence):
    encoded = []
    for i in sequence: # turns base pairs into numbers        
        # encoded.append(str(ord(i) - ord('A')))       
        if i == 'A':
            encoded.append('1')
        if i == 'T':
            encoded.append('2')
        if i == 'G':
            encoded.append('3')
        if i == 'C':
            encoded.append('4')    
        if i == '*':
            encoded.append('0')   

    # print encoded prints fine

    seq = []

    for i in range(len(encoded)): # joins chunks of 15 digits together
        if i%15 == 0:
            a = encoded[i:i+15]
            a = ''.join(a)
            a = float(a)
            seq.append(a)
        
    return(seq)
    
def decoding(seq):
    ans = ''
    for i in seq:
        for j in i:
            for c in str(j).split('.')[0]:
                curChar = '';
                if c == '1':
                    curChar = 'A'
                elif c == '2':
                    curChar = 'T'
                elif c == '3':
                    curChar = 'G'
                else:
                    curChar = 'C'
                ans += curChar

    return(ans)

def compare_strains(seq1,seq2): # Compare 2 sequences for total number of mutations
    counter = 0
    nums = []
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            pass
        else:
            counter += 1
            nums.append(i+1)
    
    return(counter,nums)

def compare_sequences(seq1, seq2):
    i = 0
    cur = ''
    while i < len(seq1):
        if seq1[i] != seq2[i]:
           print(f'{seq1[i]} at idx: {i} -> {seq2[i]}')         
        i+=1

# Entropy function
import math
from collections import Counter
def entropy(labels):
    num_labels = len(labels)    
    probability = [count / num_labels for count in Counter(labels).values()]            
    if num_labels <= 1:
        return(0)
    return(sum(-probability * math.log(probability,2))) # this is the formula

