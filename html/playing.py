#!/usr/bin/env python                                                           
# -*- coding: latin-1 -*-                                                       
import os, sys

class Person: 
    def __init__(self, n):
        self.name = n

    def displayInfo(self):
        print("Some info")


def moreAboutMe():
    me = Person("Josefine Klintberg")
    print("Showing some info about " + me.name) 
    me.displayInfo






