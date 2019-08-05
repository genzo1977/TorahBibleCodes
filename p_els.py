## IMPORT MODULES
## IMPORT MODULES
## IMPORT MODULES

import mod_1GetUserInput1 ## MODULE.FUNCTION() #1 - GET USER INPUT; CHOOSE TEXT TO SEARCH
import mod_2TextFileOpen ## MODULE.FUNCTION() #2 - TEXT FILE OPEN
import mod_3ATextFilePreprocess ## MODULE.FUNCTION() #3A - TEXT FILE PREPROCESS; CALLS MODULE.FUNCTION() #3B - TEXT FILE PARSE
import mod_4ConvertJSONStringsToDicts ## MODULE.FUNCTION() #4 - CONVERT PARSED JSON STRINGS TO LIST OF DICTS
import mod_5GetNumberOfTextChosen ## MODULE.FUNCTION() #5 - GET NUMBER OF TEXT CHOSEN
import mod_6ZippedTupleCreate ## MODULE.FUNCTION() #6 - CREATE ZIPPED TUPLE OF (BOOK NUMBER, BOOK NAME)
import mod_7DictionaryOfVersesCreate ## MODULE.FUNCTION #7 - CREATE DICTIONARY OF VERSES OF TEXTS CHOSEN TO BE SEARCHED
import mod_8DataObjectsCreate ## MODULE.FUNCTION #8 - DATA OBJECTS CREATE; RETURNS 1.) STRING OF LETTERS, 2.) LIST OF LETTERS, 3.) DICT OF LETTERS, 4.) DICT OF LETTERS
import mod_9GetNumberValues ## MODULE.FUNCTION #9 - GET NUMBER VALUE OF EACH LETTER IN STRING

#import mod_GetUserInput2 ## MODULE.FUNCTION() # - GET USER INPUT; INPUT ELS SEARCH TERM
import pprint

## DECLARE VARIABLES
## DECLARE VARIABLES
## DECLARE VARIABLES

## n = START POSITION OF ELS IN STRING/LIST/DICTIONARY

## d = LENGTH OF SKIP BETWEEN LETTERS IN ELS

## k = LENGTH OF ELS: i.e. SEARCH TERM // USER INPUT 2

## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM
## BEGIN MAIN PROGRAM

## CALL MODULES.FUNCTIONS
## CALL MODULES.FUNCTIONS
## CALL MODULES.FUNCTIONS

## CALL MODULE.FUNCTION() #1 - GET USER INPUT 1 - CHOOSE TEXT TO SEARCH
TextChosen = mod_1GetUserInput1.fn_GetUserInput1()

## CALL MODULE.FUNCTION() #2 - TEXT FILE OPEN
JSON = mod_2TextFileOpen.fn_TextFileOpen(TextChosen)

## CALL MODULE.FUNCTION() #3A - TEXT FILE PREPROCESS; CALLS MODULE.FUNCTION() #3B - TEXT FILE PARSE
ListOfJSONStringsParsed = mod_3ATextFilePreprocess.fn_TextFilePreprocess(JSON)

## CALL MODULE.FUNCTION() #4 - CONVERT PARSED JSON STRINGS TO DICTIONARIES; RETURN LIST OF DICTIONARIES
ListOfDictsOfJSONStringsParsed = mod_4ConvertJSONStringsToDicts.fn_ConvertJSONStringsToDicts(ListOfJSONStringsParsed)

## CALL MODULE.FUNCTION() #5 - GET NUMBER OF TEXT CHOSEN
SearchTextChosen = mod_5GetNumberOfTextChosen.fn_GetNumberOfTextChosen(ListOfDictsOfJSONStringsParsed)

## CALL MODULE.FUNCTION() #6 - ZIPPED TUPLE(S) CREATE
ZippedTuple = mod_6ZippedTupleCreate.fn_ZippedTupleCreate(ListOfDictsOfJSONStringsParsed, SearchTextChosen)

## CALL MODULE.FUNCTION() #7 - DICTIONARY OF VERSES CREATE
D = mod_7DictionaryOfVersesCreate.fn_DictionaryOfVersesCreate(ZippedTuple)

## CALL MODULE.FUNCTION() #8 - DATA OBJECTS CREATE - RETURNS 1.) STRING OF LETTERS, 2.) LIST OF LETTERS, 3.) DICT OF LETTERS, 4.) DICT OF LETTERS
S, L, DL, D5 = mod_8DataObjectsCreate.fn_DataObjectsCreate(D)

## CALL MODULE.FUNCTION() #9 - GET NUMBER VALUE - RETURNS LIST OF NUMBER VALUES FOR EACH LETTER OF STRING
N = mod_9GetNumberValues.fn_GetNumberValues(S)








class cls_L(object):
    """ Letter Object """

    def __init__(self):
        self.name = self
        self.gematria = ""
        
    def printself(self):
        print(self.name, self.gematria)
        



    

## CALL MODULE.FUNCTION() # - GET USER INPUT 2 - INPUT TEXT EQUIDISTANT LETTER SEQUENCES (ELS = K) TO SEARCH
# UserInput2 = mod_GetUserInput2.fn_GetUserInput2()



## END MAIN PROGRAM
## END MAIN PROGRAM
## END MAIN PROGRAM

## GAME OVER
## GAME OVER
## GAME OVER
