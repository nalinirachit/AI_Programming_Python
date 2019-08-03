#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Nalini Sharma
# DATE CREATED: 7/30/2019                             
# REVISED DATE: 8/1/2019
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Replace None with the results_dic dictionary that you created with this
    # function
    files_list = listdir(image_dir)
        
    results_dic = dict()
    
    # loop through files list
    for id in range(0, len(files_list), 1):
    
    # testing only
    # for id in range(0,3,1):
        
        # skip file if it starts with "."
        if files_list[id][0] != ".":
            pet_label = ""
            # get the file name, get lowercase, split by underscore
            pet_image_name_list = files_list[id].lower().split('_')
            # print('pet image name:', pet_image_name_list)
            
            # loop through each word and create another word separated by spaces
            for word in pet_image_name_list:
                # check for alphabetical and create a word with each word separated by spaces
                if word.isalpha():
                    pet_label += word + " "
            # remove leading and training spaces
            pet_label = pet_label.strip()
            
            # add key (filename) and value ( the space separated name) in a dictionary
            if files_list[id] not in results_dic:
                results_dic[files_list[id]] = [pet_label]
            else:
                print('**Warning - Duplicate files exist in directory:', files_list[id])
    
    # print(results_dic)
    
    return results_dic