#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright © 2018 Michael J. Hayford
""" **DEPRECATED**: optical model enums

    The enums in this module are deprecated in favor of strings conveying the 
    same information. The functions in this module are used to convert enums 
    into the corresponding strings.

.. Created on Tue Dec  4 11:32:57 2018

.. codeauthor: Michael J. Hayford
"""

from enum import Enum


class PupilType(Enum):
    """ **DEPRECATED**: enum for different aperture specifications """
    EPD = 0  #: entrance pupil diameter
    NAO = 1  #: object space numerical aperture
    FNO = 2  #: image space f/#
    NA = 3   #: image space numerical aperture


def get_ape_key_for_type(pupil_type):
    if pupil_type == PupilType.EPD:
        obj_img_key = 'object'
        value_key = 'pupil'
    elif pupil_type == PupilType.NAO:
        obj_img_key = 'object'
        value_key = 'NA'
    elif pupil_type == PupilType.FNO:
        obj_img_key = 'image'
        value_key = 'f/#'
    elif pupil_type == PupilType.NA:
        obj_img_key = 'image'
        value_key = 'NA'
    return 'aperture', obj_img_key, value_key


def get_ape_type_for_key(aperture_key):
    aperture, obj_img_key, value_key = aperture_key
    if obj_img_key == 'object':
        if value_key == 'pupil':
            pupil_type = PupilType.EPD
        elif value_key == 'NA':
            pupil_type = PupilType.NAO
    elif obj_img_key == 'image':
        if value_key == 'NA':
            pupil_type = PupilType.NA
        elif value_key == 'f/#':
            pupil_type = PupilType.FNO
    return pupil_type


class FieldType(Enum):
    """ **DEPRECATED**: enum for different field specifications """
    OBJ_ANG = 0  #: object space angle in degrees
    OBJ_HT = 1   #: object height
    IMG_HT = 2   #: image height
    IMG_ANG = 3   #: image space angle in degrees


def get_fld_key_for_type(field_type):
    if field_type == FieldType.OBJ_HT:
        obj_img_key = 'object'
        value_key = 'height'
    elif field_type == FieldType.OBJ_ANG:
        obj_img_key = 'object'
        value_key = 'angle'
    elif field_type == FieldType.IMG_HT:
        obj_img_key = 'image'
        value_key = 'height'
    elif field_type == FieldType.IMG_ANG:
        obj_img_key = 'image'
        value_key = 'angle'
    return 'field', obj_img_key, value_key


def get_fld_type_for_key(field_key):
    field, obj_img_key, value_key = field_key
    if obj_img_key == 'object':
        if value_key == 'height':
            field_type = FieldType.OBJ_HT
        elif value_key == 'angle':
            field_type = FieldType.OBJ_ANG
    elif obj_img_key == 'image':
        if value_key == 'height':
            field_type = FieldType.IMG_HT
    return field_type


class DimensionType(Enum):
    """ **DEPRECATED**: enum for different linear dimensions """
    MM = 0  #: millimeters
    CM = 1  #: centimeters
    M = 2   #: meters
    IN = 3  #: inches
    FT = 4  #: feet


def get_dimension_for_type(dimension_type):
    if dimension_type == DimensionType.MM:
        dimension_key = 'mm'
    elif dimension_type == DimensionType.CM:
        dimension_key = 'cm'
    elif dimension_type == DimensionType.M:
        dimension_key = 'meters'
    elif dimension_type == DimensionType.IN:
        dimension_key = 'inches'
    elif dimension_type == DimensionType.FT:
        dimension_key = 'feet'
    return dimension_key


class DecenterType(Enum):
    """ **DEPRECATED**: enum for different tilt and decenter types """
    LOCAL = 0  #: pos and orientation applied prior to surface
    REV = 1    #: pos and orientation applied following surface in reverse
    DAR = 2    #: pos and orientation applied prior to surface and then returned to initial frame
    BEND = 3   #: used for fold mirrors, orientation applied before and after surface


def get_decenter_for_type(decenter_type):
    if decenter_type == DecenterType.LOCAL:
        decenter_key = 'decenter'
    elif decenter_type == DecenterType.REV:
        decenter_key = 'reverse'
    elif decenter_type == DecenterType.DAR:
        decenter_key = 'dec and return'
    elif decenter_type == DecenterType.BEND:
        decenter_key = 'bend'
    return decenter_key
