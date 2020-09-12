#!/usr/bin/python3
############################################################################
#
#   © 2020 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	08/2020
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
#
def find_exif_gps_tag ( tag2bytes:bytes ) -> str:
    # 00
    if tag2bytes[0:1] == b'\x00':
        if tag2bytes[1:2] == b'\x00':
            return 'GPSVersionID'
        elif tag2bytes[1:2] == b'\x01':
            return  'GPSLatitudeRef'
        elif tag2bytes[1:2] == b'\x02':
            return  'GPSLatitude'
        elif tag2bytes[1:2] == b'\x03':
            return  'GPSLongitudeRef'
        elif tag2bytes[1:2] == b'\x04':
            return  'GPSLongitude'
        elif tag2bytes[1:2] == b'\x05':
            return  'GPSAltitudeRef'
        elif tag2bytes[1:2] == b'\x06':
            return  'GPSAltitude'
        elif tag2bytes[1:2] == b'\x07':
            return  'GPSTimeStamp'
        elif tag2bytes[1:2] == b'\x08':
            return  'GPSSatellites'
        elif tag2bytes[1:2] == b'\x09':
            return  'GPSStatus'
        elif tag2bytes[1:2] == b'\x0a':
            return  'GPSMeasureMode'
        elif tag2bytes[1:2] == b'\x0b':
            return  'GPSDOP'
        elif tag2bytes[1:2] == b'\x0c':
            return  'GPSSpeedRef'
        elif tag2bytes[1:2] == b'\x0d':
            return  'GPSSpeed'
        elif tag2bytes[1:2] == b'\x0e':
            return  'GPSTrackRef'
        elif tag2bytes[1:2] == b'\x0f':
            return  'GPSTrack'
        elif tag2bytes[1:2] == b'\x10':
            return  'GPSImgDirectionRef'
        elif tag2bytes[1:2] == b'\x11':
            return  'GPSImgDirection'
        elif tag2bytes[1:2] == b'\x12':
            return  'GPSMapDatum'
        elif tag2bytes[1:2] == b'\x13':
            return  'GPSDestLatitudeRef'
        elif tag2bytes[1:2] == b'\x14':
            return  'GPSDestLatitude'
        elif tag2bytes[1:2] == b'\x15':
            return  'GPSDestLongitudeRef'
        elif tag2bytes[1:2] == b'\x16':
            return  'GPSDestLongitude'
        elif tag2bytes[1:2] == b'\x17':
            return  'GPSDestBearingRef'
        elif tag2bytes[1:2] == b'\x18':
            return  'GPSDestBearing'
        elif tag2bytes[1:2] == b'\x19':
            return  'GPSDestDistanceRef'
        elif tag2bytes[1:2] == b'\x1a':
            return  'GPSDestDistance'
        elif tag2bytes[1:2] == b'\x1b':
            return  'GPSProcessingMethod'
        elif tag2bytes[1:2] == b'\x1c':
            return  'GPSAreaInformation'
        elif tag2bytes[1:2] == b'\x1d':
            return  'GPSDateStamp'
        elif tag2bytes[1:2] == b'\x1e':
            return  'GPSDifferential'
        elif tag2bytes[1:2] == b'\x1f':
            return  'GPSHPositioningError'
        else:
            return '<<Unknown Tag>>'
    else:
        return '<<Unknown Tag>>'

#
def find_exif_tag( tag2bytes:bytes ) -> str:
    # 00
    if tag2bytes[0:1] == b'\x00':
        if tag2bytes[1:2] == b'\x00':
            return '<<NULL>>'
        elif tag2bytes[1:2] == b'\x01':
            return  'InteropIndex'
        elif tag2bytes[1:2] == b'\x02':
            return 'InteropVersion'
        elif tag2bytes[1:2] == b'\x0b':
            return 'ProcessingSoftware'
        elif tag2bytes[1:2] == b'\xfe':
            return 'SubfileType'
        elif tag2bytes[1:2] == b'\xff':
            return 'OldSubfileType'
        else:
            return '<<Unknown Tag>>'
    # 01
    elif tag2bytes[0:1] == b'\x01':
        if tag2bytes[1:2] == b'\x00':
            return 'ImageWidth'
        elif tag2bytes[1:2] == b'\x01':
            return 'ImageHeight'
        elif tag2bytes[1:2] == b'\x02':
            return 'BitsPerSample'
        elif tag2bytes[1:2] == b'\x03':
            return 'Compression'
        elif tag2bytes[1:2] == b'\x06':
            return 'PhotometricInterpretation'
        elif tag2bytes[1:2] == b'\x07':
            return 'Thresholding'
        elif tag2bytes[1:2] == b'\x08':
            return 'CellWidth'
        elif tag2bytes[1:2] == b'\x09':
            return 'CellLength'
        elif tag2bytes[1:2] == b'\x0a':
            return 'FillOrder'
        elif tag2bytes[1:2] == b'\x0d':
            return 'DocumentName'
        elif tag2bytes[1:2] == b'\x0e':
            return 'ImageDescription'
        elif tag2bytes[1:2] == b'\x0f':
            return 'Make'
        elif tag2bytes[1:2] == b'\x10':
            return 'Model'
        elif tag2bytes[1:2] == b'\x11':
            return 'StripOffsets'
        elif tag2bytes[1:2] == b'\x12':
            return 'Orientation'
        elif tag2bytes[1:2] == b'\x15':
            return 'SamplesPerPixel'
        elif tag2bytes[1:2] == b'\x16':
            return 'RowsPerStrip'
        elif tag2bytes[1:2] == b'\x17':
            return 'StripByteCounts'
        elif tag2bytes[1:2] == b'\x18':
            return 'MinSampleValue'
        elif tag2bytes[1:2] == b'\x19':
            return 'MaxSamplevalue'
        elif tag2bytes[1:2] == b'\x1a':
            return 'XResolution'
        elif tag2bytes[1:2] == b'\x1b':
            return 'YResolution'
        elif tag2bytes[1:2] == b'\x1c':
            return 'PlanarConfiguration'
        elif tag2bytes[1:2] == b'\x1d':
            return 'PageName'
        elif tag2bytes[1:2] == b'\x1e':
            return 'XPosition'
        elif tag2bytes[1:2] == b'\x1f':
            return 'YPosition'
        elif tag2bytes[1:2] == b'\x20':
            return 'FreeOffsets'
        elif tag2bytes[1:2] == b'\x21':
            return 'FreeByteCounts'
        elif tag2bytes[1:2] == b'\x22':
            return 'GrayResponseUnit'
        elif tag2bytes[1:2] == b'\x23':
            return 'GrayResponseCurve'
        elif tag2bytes[1:2] == b'\x24':
            return 'T4Options'
        elif tag2bytes[1:2] == b'\x25':
            return 'T6Options'
        elif tag2bytes[1:2] == b'\x28':
            return 'ResolutionUnit'
        elif tag2bytes[1:2] == b'\x29':
            return 'PageNumber'
        elif tag2bytes[1:2] == b'\x2c':
            return 'ColorResponseUnit'
        elif tag2bytes[1:2] == b'\x2d':
            return 'TransferFunction'
        elif tag2bytes[1:2] == b'\x31':
            return 'Software'
        elif tag2bytes[1:2] == b'\x32':
            return 'ModifyDate'
        elif tag2bytes[1:2] == b'\x3b':
            return 'Artist'
        elif tag2bytes[1:2] == b'\x3c':
            return 'HostComputer'
        elif tag2bytes[1:2] == b'\x3d':
            return 'Predictor'
        elif tag2bytes[1:2] == b'\x3e':
            return 'WhitePoint'
        elif tag2bytes[1:2] == b'\x3f':
            return 'PrimaryChromaticities'
        elif tag2bytes[1:2] == b'\x40':
            return 'ColorMap'
        elif tag2bytes[1:2] == b'\x41':
            return 'HalftoneHints'
        elif tag2bytes[1:2] == b'\x42':
            return 'TileWidth'
        elif tag2bytes[1:2] == b'\x43':
            return 'TileLength'
        elif tag2bytes[1:2] == b'\x44':
            return 'TileOffsets'
        elif tag2bytes[1:2] == b'\x45':
            return 'TileByteCounts'
        elif tag2bytes[1:2] == b'\x46':
            return 'BadFaxLines'
        elif tag2bytes[1:2] == b'\x47':
            return 'CleanFaxData'
        elif tag2bytes[1:2] == b'\x48':
            return 'ConsecutiveBadFaxLines'
        elif tag2bytes[1:2] == b'\x4a':
            return 'A100DataOffset'
        elif tag2bytes[1:2] == b'\x4c':
            return 'Inkset'
        elif tag2bytes[1:2] == b'\x4d':
            return 'InkNames'
        elif tag2bytes[1:2] == b'\x4e':
            return 'NumberOfInks'
        elif tag2bytes[1:2] == b'\x50':
            return 'DotRange'
        elif tag2bytes[1:2] == b'\x51':
            return 'TargetPrinter'
        elif tag2bytes[1:2] == b'\x52':
            return 'ExtraSamples'
        elif tag2bytes[1:2] == b'\x53':
            return 'SampleFormat'
        elif tag2bytes[1:2] == b'\x54':
            return 'SMinSampleValue'
        elif tag2bytes[1:2] == b'\x55':
            return 'SMaxSampleValue'
        elif tag2bytes[1:2] == b'\x56':
            return 'TransferRange'
        elif tag2bytes[1:2] == b'\x57':
            return 'ClipPath'
        elif tag2bytes[1:2] == b'\x58':
            return 'XClipPathUnits'
        elif tag2bytes[1:2] == b'\x59':
            return 'YClipPathUnits'
        elif tag2bytes[1:2] == b'\x5a':
            return 'Indexed'
        elif tag2bytes[1:2] == b'\x5b':
            return 'JPEGTables'
        elif tag2bytes[1:2] == b'\x5f':
            return 'OPIProxy'
        elif tag2bytes[1:2] == b'\x90':
            return 'GlobalParametersIFD'
        elif tag2bytes[1:2] == b'\x91':
            return 'ProfileType'
        elif tag2bytes[1:2] == b'\x92':
            return 'FaxProfile'
        elif tag2bytes[1:2] == b'\x93':
            return 'CodingMethods'
        elif tag2bytes[1:2] == b'\x94':
            return 'VersionYear'
        elif tag2bytes[1:2] == b'\x95':
            return 'ModeNumber'
        elif tag2bytes[1:2] == b'\xb1':
            return 'Decode'
        elif tag2bytes[1:2] == b'\xb2':
            return 'DefaultImageColor'
        elif tag2bytes[1:2] == b'\xb3':
            return 'T82Options'
        elif tag2bytes[1:2] == b'\xb5':
            return 'JPEGTables'
        else:
            return '<<Unknown Tag>>'
    # 02
    elif tag2bytes[0:1] == b'\x02':
        if tag2bytes[1:2] == b'\x00':
            return 'JPEGProc'
        elif tag2bytes[1:2] == b'\x01':
            return 'JPEGInterchangeFormat'
        elif tag2bytes[1:2] == b'\x02':
            return 'TJPEGInterchangeFormatLength'
        elif tag2bytes[1:2] == b'\x03':
            return 'JPEGRestartInterval'
        elif tag2bytes[1:2] == b'\x05':
            return 'JPEGLosslessPredictors'
        elif tag2bytes[1:2] == b'\x06':
            return 'JPEGPointTransforms'
        elif tag2bytes[1:2] == b'\x07':
            return 'JPEGQTables'
        elif tag2bytes[1:2] == b'\x08':
            return 'JPEGDCTables'
        elif tag2bytes[1:2] == b'\x09':
            return 'JPEGACTables'
        elif tag2bytes[1:2] == b'\x11':
            return 'YCbCrCoefficients'
        elif tag2bytes[1:2] == b'\x12':
            return 'YCbCRSubSampling'
        elif tag2bytes[1:2] == b'\x13':
            return 'YCbCrPositioning'
        elif tag2bytes[1:2] == b'\x14':
            return 'ReferenceBlackWhite'
        elif tag2bytes[1:2] == b'\x2f':
            return 'StripRowCounts'
        elif tag2bytes[1:2] == b'\xbc':
            return 'ApplicationNotes'
        else:
            return '<<Unknown Tag>>'
    # 03
    elif tag2bytes[0:1] == b'\x03':
        if tag2bytes[1:2] == b'\xe7':
            return 'USPTOMiscellaneous'
        else:
            return '<<Unknown Tag>>'
    # 10
    elif tag2bytes[0:1] == b'\x10':
        if tag2bytes[1:2] == b'\x00':
            return 'RelatedImageFileFormat'
        elif tag2bytes[1:2] == b'\x01':
            return 'RelatedImageWidth'
        elif tag2bytes[1:2] == b'\x02':
            return 'RelatedImageHeight'
        else:
            return '<<Unknown Tag>>'
    # 47
    elif tag2bytes[0:1] == b'\x47':
        if tag2bytes[1:2] == b'\x46':
            return 'Rating'
        elif tag2bytes[1:2] == b'\x47':
            return 'XP_DIP_XML'
        elif tag2bytes[1:2] == b'\x48':
            return 'StitchInfo'
        elif tag2bytes[1:2] == b'\x49':
            return 'RatingPercent'
        else:
            return '<<Unknown Tag>>'
    # 70
    elif tag2bytes[0:1] == b'\x70':
        if tag2bytes[1:2] == b'\x00':
            return 'SonyRawFileType'
        elif tag2bytes[1:2] == b'\x10':
            return 'SonyToneCurve'
        elif tag2bytes[1:2] == b'\x31':
            return 'VignettingCorrection'
        elif tag2bytes[1:2] == b'\x32':
            return 'VignettingCorrParams'
        elif tag2bytes[1:2] == b'\x34':
            return 'ChromaticAberrationCorrection'
        elif tag2bytes[1:2] == b'\x35':
            return 'ChromaticAberrationCorrParams'
        elif tag2bytes[1:2] == b'\x36':
            return 'DistortionCorrection'
        elif tag2bytes[1:2] == b'\x37':
            return 'DistortionCorrParams'
        else:
            return '<<Unknown Tag>>'
    # 74
    elif tag2bytes[0:1] == b'\x74':
        if tag2bytes[1:2] == b'\xc7':
            return 'SonyCropTopLeft'
        elif tag2bytes[1:2] == b'\xc8':
            return 'SonyCropSize'
        else:
            return '<<Unknown Tag>>'
    # 80
    elif tag2bytes[0:1] == b'\x80':
        if tag2bytes[1:2] == b'\x0d':
            return 'ImageID'
        elif tag2bytes[1:2] == b'\xa3':
            return 'WangTag1'
        elif tag2bytes[1:2] == b'\xa4':
            return 'WangAnnotation'
        elif tag2bytes[1:2] == b'\xa5':
            return 'WangTag3'
        elif tag2bytes[1:2] == b'\xa6':
            return 'WangTag4'
        elif tag2bytes[1:2] == b'\xb9':
            return 'ImageReferencePoints'
        elif tag2bytes[1:2] == b'\xba':
            return 'RegionXformTackPoint'
        elif tag2bytes[1:2] == b'\xbb':
            return 'WarpQuadrilateral'
        elif tag2bytes[1:2] == b'\xbc':
            return 'AffineTransformMat'
        elif tag2bytes[1:2] == b'\xe3':
            return 'Matteing'
        elif tag2bytes[1:2] == b'\xe4':
            return 'DataType'
        elif tag2bytes[1:2] == b'\xe5':
            return 'ImageDepth'
        elif tag2bytes[1:2] == b'\xe6':
            return 'TileDepth'
        else:
            return '<<Unknown Tag>>'
    # 82
    elif tag2bytes[0:1] == b'\x82':
        if tag2bytes[1:2] == b'\x14':
            return 'ImageFullWidth'
        elif tag2bytes[1:2] == b'\x15':
            return 'ImageFullHeight'
        elif tag2bytes[1:2] == b'\x16':
            return 'TextureFormat'
        elif tag2bytes[1:2] == b'\x17':
            return 'WrapModes'
        elif tag2bytes[1:2] == b'\x18':
            return 'FovCot'
        elif tag2bytes[1:2] == b'\x19':
            return 'MatrixWorldToScreen'
        elif tag2bytes[1:2] == b'\x1a':
            return 'MatrixWorldToCamera'
        elif tag2bytes[1:2] == b'\x7d':
            return 'Model2'
        elif tag2bytes[1:2] == b'\x8d':
            return 'CFARepeatPatternDim'
        elif tag2bytes[1:2] == b'\x8e':
            return 'CFAPattern2'
        elif tag2bytes[1:2] == b'\x8f':
            return 'BatteryLevel'
        elif tag2bytes[1:2] == b'\x90':
            return 'KodakIFD'
        elif tag2bytes[1:2] == b'\x98':
            return 'Copyright'
        elif tag2bytes[1:2] == b'\x9a':
            return 'ExposureTime'
        elif tag2bytes[1:2] == b'\x9d':
            return 'FNumber'
        elif tag2bytes[1:2] == b'\xa5':
            return 'MDFileTag'
        elif tag2bytes[1:2] == b'\xa6':
            return 'MDScalePixel'
        elif tag2bytes[1:2] == b'\xa7':
            return 'MDColorTable'
        elif tag2bytes[1:2] == b'\xa8':
            return 'MDLabName'
        elif tag2bytes[1:2] == b'\xa9':
            return 'MDSampleInfo'
        elif tag2bytes[1:2] == b'\xaa':
            return 'MDPrepDate'
        elif tag2bytes[1:2] == b'\xab':
            return 'MDPrepTime'
        elif tag2bytes[1:2] == b'\xac':
            return 'MDFileUnits'
        else:
            return '<<Unknown Tag>>'
    # 83
    elif tag2bytes[0:1] == b'\x83':
        if tag2bytes[1:2] == b'\x0e':
            return 'PixelScale'
        elif tag2bytes[1:2] == b'\x35':
            return 'AdventScale'
        elif tag2bytes[1:2] == b'\x36':
            return 'AdventRevision'
        elif tag2bytes[1:2] == b'\x5c':
            return 'UIC1Tag'
        elif tag2bytes[1:2] == b'\x5d':
            return 'UIC2Tag'
        elif tag2bytes[1:2] == b'\x5e':
            return 'UIC3Tag'
        elif tag2bytes[1:2] == b'\x5f':
            return 'UIC4Tag'
        elif tag2bytes[1:2] == b'\xbb':
            return 'IPTC-NAA'
        else:
            return '<<Unknown Tag>>'
    # 84
    elif tag2bytes[0:1] == b'\x84':
        if tag2bytes[1:2] == b'\x7e':
            return 'IntergraphPacketData'
        elif tag2bytes[1:2] == b'\x7f':
            return 'IntergraphFlagRegisters'
        elif tag2bytes[1:2] == b'\x80':
            return 'IntergraphMatrix'
        elif tag2bytes[1:2] == b'\x81':
            return 'INGRReserved'
        elif tag2bytes[1:2] == b'\x82':
            return 'ModelTiePoint'
        elif tag2bytes[1:2] == b'\xe0':
            return 'Site'
        elif tag2bytes[1:2] == b'\xe1':
            return 'ColorSequence'
        elif tag2bytes[1:2] == b'\xe2':
            return 'IT8Header'
        elif tag2bytes[1:2] == b'\xe3':
            return 'RasterPadding'
        elif tag2bytes[1:2] == b'\xe4':
            return 'BitsPerRunLength'
        elif tag2bytes[1:2] == b'\xe5':
            return 'BitsPerExtendedRunLength'
        elif tag2bytes[1:2] == b'\xe6':
            return 'ColorTable'
        elif tag2bytes[1:2] == b'\xe7':
            return 'ImageColorIndicator'
        elif tag2bytes[1:2] == b'\xe8':
            return 'BackgroundColorIndicator'
        elif tag2bytes[1:2] == b'\xe9':
            return 'ImageColorValue'
        elif tag2bytes[1:2] == b'\xea':
            return 'BackgroundColorValue'
        elif tag2bytes[1:2] == b'\xeb':
            return 'PixelIntensityRange'
        elif tag2bytes[1:2] == b'\xec':
            return 'TransparencyIndicator'
        elif tag2bytes[1:2] == b'\xed':
            return 'ColorCharacterization'
        elif tag2bytes[1:2] == b'\xee':
            return 'HCUsage'
        elif tag2bytes[1:2] == b'\xef':
            return 'TrapIndicator'
        elif tag2bytes[1:2] == b'\xf0':
            return 'CMYKEquivalent'
        else:
            return '<<Unknown Tag>>'
    # 85
    elif tag2bytes[0:1] == b'\x85':
        if tag2bytes[1:2] == b'\x46':
            return 'SEMInfo'
        elif tag2bytes[1:2] == b'\x68':
            return 'AFCP_IPTC'
        elif tag2bytes[1:2] == b'\xb8':
            return 'PixelMagicJBIGOptions'
        elif tag2bytes[1:2] == b'\xd7':
            return 'JPLCartoIFD'
        elif tag2bytes[1:2] == b'\xd8':
            return 'ModelTransform'
        else:
            return '<<Unknown Tag>>'
    # 86
    elif tag2bytes[0:1] == b'\x86':
        if tag2bytes[1:2] == b'\x02':
            return 'WB_GRGBLevels'
        elif tag2bytes[1:2] == b'\x06':
            return 'LeafData'
        elif tag2bytes[1:2] == b'\x49':
            return 'PhotoshopSettings'
        else:
            return '<<Unknown Tag>>'
    # 87
    elif tag2bytes[0:1] == b'\x87':
        if tag2bytes[1:2] == b'\x69':
            return 'ExifOffset'
        elif tag2bytes[1:2] == b'\x73':
            return 'ICC_Profile'
        elif tag2bytes[1:2] == b'\x7f':
            return 'TIFF_FXExtensions'
        elif tag2bytes[1:2] == b'\x80':
            return 'MultiProfiles'
        elif tag2bytes[1:2] == b'\x81':
            return 'SharedData'
        elif tag2bytes[1:2] == b'\x82':
            return 'T88Options'
        elif tag2bytes[1:2] == b'\xac':
            return 'ImageLayer'
        elif tag2bytes[1:2] == b'\xaf':
            return 'GeoTiffDirectory'
        elif tag2bytes[1:2] == b'\xb0':
            return 'GeoTiffDoubleParams'
        elif tag2bytes[1:2] == b'\xb1':
            return 'GeoTiffAsciiParams'
        elif tag2bytes[1:2] == b'\xbe':
            return 'JBIGOptions'
        else:
            return '<<Unknown Tag>>'
    # 88
    elif tag2bytes[0:1] == b'\x88':
        if tag2bytes[1:2] == b'\x22':
            return 'ExposureProgram'
        elif tag2bytes[1:2] == b'\x24':
            return 'SpectralSensitivity'
        elif tag2bytes[1:2] == b'\x25':
            return 'GPSInfo'
        elif tag2bytes[1:2] == b'\x27':
            return 'ISO'
        elif tag2bytes[1:2] == b'\x28':
            return 'Opto-ElectricConvFactor'
        elif tag2bytes[1:2] == b'\x29':
            return 'Interlace'
        elif tag2bytes[1:2] == b'\x2a':
            return 'TimeZoneOffset'
        elif tag2bytes[1:2] == b'\x2b':
            return 'SelfTimerMode'
        elif tag2bytes[1:2] == b'\x30':
            return 'SensitivityType'
        elif tag2bytes[1:2] == b'\x31':
            return 'StandartOutputSensitivity'
        elif tag2bytes[1:2] == b'\x32':
            return 'RecommendedExposureIndex'
        elif tag2bytes[1:2] == b'\x33':
            return 'ISOSpeed'
        elif tag2bytes[1:2] == b'\x34':
            return 'ISOSpeedLatitudeyyy'
        elif tag2bytes[1:2] == b'\x35':
            return 'ISOSpeedLatitudezzz'
        elif tag2bytes[1:2] == b'\x5c':
            return 'FaxRecvParams'
        elif tag2bytes[1:2] == b'\x5d':
            return 'FaxSubAddress'
        elif tag2bytes[1:2] == b'\x5e':
            return 'FaxRecvTime'
        elif tag2bytes[1:2] == b'\x71':
            return 'FedexEDR'
        elif tag2bytes[1:2] == b'\x8a':
            return 'LeafSubIFD'
        else:
            return '<<Unknown Tag>>'

    # 90
    elif tag2bytes[0:1] == b'\x90':
        if tag2bytes[1:2] == b'\x00':
            return 'ExifVersion'
        elif tag2bytes[1:2] == b'\x03':
            return 'DateTimeOriginal'
        elif tag2bytes[1:2] == b'\x04':
            return 'CreateDate'
        elif tag2bytes[1:2] == b'\x09':
            return 'GooglePlusUploadCode'
        elif tag2bytes[1:2] == b'\x10':
            return 'OffsetTime'
        elif tag2bytes[1:2] == b'\x11':
            return 'OffsetTimeOriginal'
        elif tag2bytes[1:2] == b'\x12':
            return 'OffsetTimeDigitized'
        else:
            return '<<Unknown Tag>>'
    # 91
    elif tag2bytes[0:1] == b'\x91':
        if tag2bytes[1:2] == b'\x01':
            return 'ComponentsConfiguration'
        elif tag2bytes[1:2] == b'\x02':
            return 'CompressedBitsPerPixel'
        else:
            return '<<Unknown Tag>>'
    # 92
    elif tag2bytes[0:1] == b'\x92':
        if tag2bytes[1:2] == b'\x01':
            return 'ShutterSpeedValue'
        elif tag2bytes[1:2] == b'\x02':
            return 'ApertureValue'
        elif tag2bytes[1:2] == b'\x03':
            return 'BrightnessValue'
        elif tag2bytes[1:2] == b'\x04':
            return 'ExposureCompensation'
        elif tag2bytes[1:2] == b'\x05':
            return 'MaxApertureValue'
        elif tag2bytes[1:2] == b'\x06':
            return 'SubjectDistance'
        elif tag2bytes[1:2] == b'\x07':
            return 'MeteringMode'
        elif tag2bytes[1:2] == b'\x08':
            return 'LightSource'
        elif tag2bytes[1:2] == b'\x09':
            return 'Flash'
        elif tag2bytes[1:2] == b'\x0a':
            return 'FocalLength'
        elif tag2bytes[1:2] == b'\x0b':
            return 'FlashEnergy'
        elif tag2bytes[1:2] == b'\x0c':
            return 'SpatialFrequencyResponse'
        elif tag2bytes[1:2] == b'\x0d':
            return 'Noise'
        elif tag2bytes[1:2] == b'\x0e':
            return 'FocalPlaneXResolution'
        elif tag2bytes[1:2] == b'\x0f':
            return 'FocalPlaneYResolution'
        elif tag2bytes[1:2] == b'\x10':
            return 'FocalPlaneResolutionUnit'
        elif tag2bytes[1:2] == b'\x11':
            return 'ImageNumber'
        elif tag2bytes[1:2] == b'\x12':
            return 'SecurityClassification'
        elif tag2bytes[1:2] == b'\x13':
            return 'ImageHistory'
        elif tag2bytes[1:2] == b'\x14':
            return 'SubjectArea'
        elif tag2bytes[1:2] == b'\x15':
            return 'ExposureIndex'
        elif tag2bytes[1:2] == b'\x16':
            return 'TIFF-EPStandartID'
        elif tag2bytes[1:2] == b'\x17':
            return 'Sensingmethod'
        elif tag2bytes[1:2] == b'\x3a':
            return 'CIP3DataFile'
        elif tag2bytes[1:2] == b'\x3b':
            return 'CIP3Sheet'
        elif tag2bytes[1:2] == b'\x3c':
            return 'CIP3Side'
        elif tag2bytes[1:2] == b'\x3f':
            return 'StoNits'
        elif tag2bytes[1:2] == b'\x7c':
            return 'MakerNote'
        elif tag2bytes[1:2] == b'\x86':
            return 'UserComment'
        elif tag2bytes[1:2] == b'\x90':
            return 'SubSecTime'
        elif tag2bytes[1:2] == b'\x91':
            return 'SubSecTimeOriginal'
        elif tag2bytes[1:2] == b'\x92':
            return 'SubSecTimeDigitized'
        else:
            return '<<Unknown Tag>>'

    # 93
    elif tag2bytes[0:1] == b'\x93':
        if tag2bytes[1:2] == b'\x2f':
            return 'MSDocumentText'
        elif tag2bytes[1:2] == b'\x30':
            return 'MSPropertySetStorage'
        elif tag2bytes[1:2] == b'\x31':
            return 'MSDocumentTextPosition'
        elif tag2bytes[1:2] == b'\x5c':
            return 'ImageSourceData'
        else:
            return '<<Unknown Tag>>'

    # 94
    elif tag2bytes[0:1] == b'\x94':
        if tag2bytes[1:2] == b'\x00':
            return 'AmbientTemperature'
        elif tag2bytes[1:2] == b'\x01':
            return 'Humidity'
        elif tag2bytes[1:2] == b'\x02':
            return 'Pressure'
        elif tag2bytes[1:2] == b'\x03':
            return 'WaterDepth'
        elif tag2bytes[1:2] == b'\x04':
            return 'Acceleration'
        elif tag2bytes[1:2] == b'\x05':
            return 'CameraElevationAngle'
        else:
            return '<<Unknown Tag>>'

    # 9c
    elif tag2bytes[0:1] == b'\x9c':
        if tag2bytes[1:2] == b'\x9b':
            return 'XPTitle'
        elif tag2bytes[1:2] == b'\x9c':
            return 'XPComment'
        elif tag2bytes[1:2] == b'\x9d':
            return 'XPAuthor'
        elif tag2bytes[1:2] == b'\x9e':
            return 'XPKeywords'
        elif tag2bytes[1:2] == b'\x9f':
            return 'XPSubject'
        else:
            return '<<Unknown Tag>>'

    # a0
    elif tag2bytes[0:1] == b'\xa0':
        if tag2bytes[1:2] == b'\x00':
            return 'FlashpixVersion'
        elif tag2bytes[1:2] == b'\x01':
            return 'ColorSpace'
        elif tag2bytes[1:2] == b'\x02':
            return 'ExifImageWidth'
        elif tag2bytes[1:2] == b'\x03':
            return 'ExifImageHeight'
        elif tag2bytes[1:2] == b'\x04':
            return 'RelatedSoundFile'
        elif tag2bytes[1:2] == b'\x05':
            return 'InteropOffset'
        elif tag2bytes[1:2] == b'\x10':
            return 'SamsungRawPointersOffset'
        elif tag2bytes[1:2] == b'\x11':
            return 'SamsungRawPointersLength'
        else:
            return '<<Unknown Tag>>'

    # a1
    elif tag2bytes[0:1] == b'\xa1':
        if tag2bytes[1:2] == b'\x01':
            return 'SamsungRawByteOrder'
        elif tag2bytes[1:2] == b'\x02':
            return 'SamsungRawUnknown?'
        else:
            return '<<Unknown Tag>>'

    # a2
    elif tag2bytes[0:1] == b'\xa2':
        if tag2bytes[1:2] == b'\x0b':
            return 'FlashEnergy'
        elif tag2bytes[1:2] == b'\x0c':
            return 'SpatialFrequencyResponse'
        elif tag2bytes[1:2] == b'\x0d':
            return 'Noise'
        elif tag2bytes[1:2] == b'\x0e':
            return 'FocalPlaneXResolution'
        elif tag2bytes[1:2] == b'\x0f':
            return 'FocalPlaneYResolution'
        elif tag2bytes[1:2] == b'\x10':
            return 'FocalPlaneResolutionUnit'
        elif tag2bytes[1:2] == b'\x11':
            return 'ImageNumber'
        elif tag2bytes[1:2] == b'\x12':
            return 'SecurityClassification'
        elif tag2bytes[1:2] == b'\x13':
            return 'ImageHistory'
        elif tag2bytes[1:2] == b'\x14':
            return 'SubjectLocation'
        elif tag2bytes[1:2] == b'\x15':
            return 'ExposureIndex'
        elif tag2bytes[1:2] == b'\x16':
            return 'TIFF-EPStandartID'
        elif tag2bytes[1:2] == b'\x17':
            return 'SensingMethod'
        else:
            return '<<Unknown Tag>>'

    # a3
    elif tag2bytes[0:1] == b'\xa3':
        if tag2bytes[1:2] == b'\x00':
            return 'FileSource'
        elif tag2bytes[1:2] == b'\x01':
            return 'SceneType'
        elif tag2bytes[1:2] == b'\x02':
            return 'CFAPattern'
        else:
            return '<<Unknown Tag>>'


    # a4
    elif tag2bytes[0:1] == b'\xa4':
        if tag2bytes[1:2] == b'\x01':
            return 'CustomRendered'
        elif tag2bytes[1:2] == b'\x02':
            return 'ExposureMode'
        elif tag2bytes[1:2] == b'\x03':
            return 'WhiteBalance'
        elif tag2bytes[1:2] == b'\x04':
            return 'DigitalZoomRatio'
        elif tag2bytes[1:2] == b'\x05':
            return 'FocalLengthIn35mmFormat'
        elif tag2bytes[1:2] == b'\x06':
            return 'SceneCaptureType'
        elif tag2bytes[1:2] == b'\x07':
            return 'GainControl'
        elif tag2bytes[1:2] == b'\x08':
            return 'Contrast'
        elif tag2bytes[1:2] == b'\x09':
            return 'Saturation'
        elif tag2bytes[1:2] == b'\x0a':
            return 'Sharpness'
        elif tag2bytes[1:2] == b'\x0b':
            return 'DeviceSettingDescription'
        elif tag2bytes[1:2] == b'\x0c':
            return 'SubjectDistanceRange'
        elif tag2bytes[1:2] == b'\x20':
            return 'ImageUniqueID'
        elif tag2bytes[1:2] == b'\x30':
            return 'OwnerName'
        elif tag2bytes[1:2] == b'\x31':
            return 'SerialNumber'
        elif tag2bytes[1:2] == b'\x32':
            return 'LensInfo'
        elif tag2bytes[1:2] == b'\x33':
            return 'LensMake'
        elif tag2bytes[1:2] == b'\x34':
            return 'LensModel'
        elif tag2bytes[1:2] == b'\x35':
            return 'LensSerialNumber'
        elif tag2bytes[1:2] == b'\x60':
            return 'CompositeImage'
        elif tag2bytes[1:2] == b'\x61':
            return 'CompositeImageCount'
        elif tag2bytes[1:2] == b'\x62':
            return 'CompositeImageExposureTimes'
        elif tag2bytes[1:2] == b'\x80':
            return 'GDALMetadata'
        elif tag2bytes[1:2] == b'\x81':
            return 'GDALNodata'
        else:
            return '<<Unknown Tag>>'

    # a5
    elif tag2bytes[0:1] == b'\xa5':
        if tag2bytes[1:2] == b'\x00':
            return 'Gama'
        else:
            return '<<Unknown Tag>>'

    # af
    elif tag2bytes[0:1] == b'\xaf':
        if tag2bytes[1:2] == b'\xc0':
            return 'ExpandSoftware'
        elif tag2bytes[1:2] == b'\xc1':
            return 'ExpandLens'
        elif tag2bytes[1:2] == b'\xc2':
            return 'ExpandFilm'
        elif tag2bytes[1:2] == b'\xc3':
            return 'ExpandFilterLens'
        elif tag2bytes[1:2] == b'\xc4':
            return 'ExpandScanner'
        elif tag2bytes[1:2] == b'\xc5':
            return 'ExpandFlashLamp'
        else:
            return '<<Unknown Tag>>'

    # b4
    elif tag2bytes[0:1] == b'\xb4':
        if tag2bytes[1:2] == b'\xc3':
            return 'HasselbladRawImage'
        else:
            return '<<Unknown Tag>>'

    # bc
    elif tag2bytes[0:1] == b'\xbc':
        if tag2bytes[1:2] == b'\x01':
            return 'PixelFormat'
        elif tag2bytes[1:2] == b'\x02':
            return 'Transformation'
        elif tag2bytes[1:2] == b'\x03':
            return 'Uncompressed'
        elif tag2bytes[1:2] == b'\x04':
            return 'ImageType'
        elif tag2bytes[1:2] == b'\x80':
            return 'ImageWidth'
        elif tag2bytes[1:2] == b'\x81':
            return 'ImageHeight'
        elif tag2bytes[1:2] == b'\x82':
            return 'WidthResolution'
        elif tag2bytes[1:2] == b'\x83':
            return 'HeightResolution'
        elif tag2bytes[1:2] == b'\xc0':
            return 'ImageOffset'
        elif tag2bytes[1:2] == b'\xc1':
            return 'ImageByteCount'
        elif tag2bytes[1:2] == b'\xc2':
            return 'AlphaOffset'
        elif tag2bytes[1:2] == b'\xc3':
            return 'AlphaByteCount'
        elif tag2bytes[1:2] == b'\xc4':
            return 'ImageDataDiscard'
        elif tag2bytes[1:2] == b'\xc5':
            return 'AlphaDataDiscard'
        else:
            return '<<Unknown Tag>>'

    # c4
    elif tag2bytes[0:1] == b'\xc4':
        if tag2bytes[1:2] == b'\x27':
            return 'OceScanjobDesc'
        elif tag2bytes[1:2] == b'\x28':
            return 'OceApplicationSelector'
        elif tag2bytes[1:2] == b'\x29':
            return 'OceIDNumber'
        elif tag2bytes[1:2] == b'\x2a':
            return 'OceIDImageLogic'
        elif tag2bytes[1:2] == b'\x4f':
            return 'Annotations'
        elif tag2bytes[1:2] == b'\xa5':
            return 'PrintIM'
        else:
            return '<<Unknown Tag>>'


    # c5
    elif tag2bytes[0:1] == b'\xc5':
        if tag2bytes[1:2] == b'\x1b':
            return 'HasselbladExif'
        elif tag2bytes[1:2] == b'\x73':
            return 'OriginalFileName'
        elif tag2bytes[1:2] == b'\x80':
            return 'USPTOOriginalContentType'
        elif tag2bytes[1:2] == b'\xe0':
            return 'CR2CFAPattern'
        else:
            return '<<Unknown Tag>>'


    # c6
    elif tag2bytes[0:1] == b'\xc6':
        if tag2bytes[1:2] == b'\x12':
            return 'DNGVersion'
        elif tag2bytes[1:2] == b'\x13':
            return 'DNGBackwardVersion'
        elif tag2bytes[1:2] == b'\x14':
            return 'UniqueCameraModel'
        elif tag2bytes[1:2] == b'\x15':
            return 'LocalizedCameraModel'
        elif tag2bytes[1:2] == b'\x16':
            return 'CFAPlaneColor'
        elif tag2bytes[1:2] == b'\x17':
            return 'CFALayout'
        elif tag2bytes[1:2] == b'\x18':
            return 'LinearizationTable'
        elif tag2bytes[1:2] == b'\x19':
            return 'BlackLevelRepeatDim'
        elif tag2bytes[1:2] == b'\x1a':
            return 'Blacklevel'
        elif tag2bytes[1:2] == b'\x1b':
            return 'BlackLevelDeltaH'
        elif tag2bytes[1:2] == b'\x1c':
            return 'BlackLevelDeltaV'
        elif tag2bytes[1:2] == b'\x1d':
            return 'WhiteLevel'
        elif tag2bytes[1:2] == b'\x1e':
            return 'DefaultScale'
        elif tag2bytes[1:2] == b'\x1f':
            return 'DefaultCropOrigin'
        elif tag2bytes[1:2] == b'\x20':
            return 'DefaultCropSize'
        elif tag2bytes[1:2] == b'\x21':
            return 'ColorMatrix1'
        elif tag2bytes[1:2] == b'\x22':
            return 'ColorMatrix2'
        elif tag2bytes[1:2] == b'\x23':
            return 'CameraCalibration1'
        elif tag2bytes[1:2] == b'\x24':
            return 'CameraCalibration2'
        elif tag2bytes[1:2] == b'\x25':
            return 'ReductionMatrix1'
        elif tag2bytes[1:2] == b'\x26':
            return 'ReductionMatrix2'
        elif tag2bytes[1:2] == b'\x27':
            return 'AnalogBalance'
        elif tag2bytes[1:2] == b'\x28':
            return 'AsShotNeutral'
        elif tag2bytes[1:2] == b'\x29':
            return 'AsShotWhiteXY'
        elif tag2bytes[1:2] == b'\x2a':
            return 'BaselineExposure'
        elif tag2bytes[1:2] == b'\x2b':
            return 'BaselineNoise'
        elif tag2bytes[1:2] == b'\x2c':
            return 'BaselineSharpness'
        elif tag2bytes[1:2] == b'\x2d':
            return 'BayerGreenSplit'
        elif tag2bytes[1:2] == b'\x2e':
            return 'LinearResponseLimit'
        elif tag2bytes[1:2] == b'\x2f':
            return 'CameraSerialNumber'
        elif tag2bytes[1:2] == b'\x30':
            return 'DNGLensInfo'
        elif tag2bytes[1:2] == b'\x31':
            return 'ChromaBlurRadius'
        elif tag2bytes[1:2] == b'\x32':
            return 'AntiAliasStrength'
        elif tag2bytes[1:2] == b'\x33':
            return 'ShadowScale'
        elif tag2bytes[1:2] == b'\x34':
            return 'DNG/Adobe/PrivateData'
        elif tag2bytes[1:2] == b'\x35':
            return 'MakerNoteSafety'
        elif tag2bytes[1:2] == b'\x40':
            return 'RawImageSegmentation'
        elif tag2bytes[1:2] == b'\x5a':
            return 'CalibrationIlluminant1'
        elif tag2bytes[1:2] == b'\x5b':
            return 'CalibrationIllumaninat2'
        elif tag2bytes[1:2] == b'\x5c':
            return 'BestQualityScale'
        elif tag2bytes[1:2] == b'\x5d':
            return 'RawDataUniqueID'
        elif tag2bytes[1:2] == b'\x60':
            return 'AliasLayerMetadata'
        elif tag2bytes[1:2] == b'\x8b':
            return 'OriginalRawFileName'
        elif tag2bytes[1:2] == b'\x8c':
            return 'OriginalRawFileData'
        elif tag2bytes[1:2] == b'\x8d':
            return 'ActiveArea'
        elif tag2bytes[1:2] == b'\x8e':
            return 'MaskedAreas'
        elif tag2bytes[1:2] == b'\x8f':
            return 'AsShotICCProfile'
        elif tag2bytes[1:2] == b'\x90':
            return 'AsShotPreProfileMatrix'
        elif tag2bytes[1:2] == b'\x91':
            return 'CurrentICCProfile'
        elif tag2bytes[1:2] == b'\x92':
            return 'CurrentPreProfileMatrix'
        elif tag2bytes[1:2] == b'\xbf':
            return 'ColorimetricReference'
        elif tag2bytes[1:2] == b'\xc5':
            return 'SRawType'
        elif tag2bytes[1:2] == b'\xd2':
            return 'PanasonicTitle'
        elif tag2bytes[1:2] == b'\xd3':
            return 'PanasonicTitle2'
        elif tag2bytes[1:2] == b'\xf3':
            return 'CameraCalibrationSig'
        elif tag2bytes[1:2] == b'\xf4':
            return 'ProfileCalibrationSig'
        elif tag2bytes[1:2] == b'\xf5':
            return 'ProfileIFD'
        elif tag2bytes[1:2] == b'\xf6':
            return 'AsShotProfileName'
        elif tag2bytes[1:2] == b'\xf7':
            return 'NoiseReductionApplied'
        elif tag2bytes[1:2] == b'\xf8':
            return 'ProfileName'
        elif tag2bytes[1:2] == b'\xf9':
            return 'ProfileHueSatMapDims'
        elif tag2bytes[1:2] == b'\xfa':
            return 'ProfileHueSatMapData1'
        elif tag2bytes[1:2] == b'\xfb':
            return 'ProfileHueSatMapData2'
        elif tag2bytes[1:2] == b'\xfc':
            return 'ProfileToneCurve'
        elif tag2bytes[1:2] == b'\xfd':
            return 'ProfileEmbedPolicy'
        elif tag2bytes[1:2] == b'\xfe':
            return 'ProfileCopyright'
        else:
            return '<<Unknown Tag>>'


    # c7
    elif tag2bytes[0:1] == b'\xc7':
        if tag2bytes[1:2] == b'\x14':
            return 'ForwardMatrix1'
        elif tag2bytes[1:2] == b'\x15':
            return 'ForwardMatrix2'
        elif tag2bytes[1:2] == b'\x16':
            return 'PreviewApplicationName'
        elif tag2bytes[1:2] == b'\x17':
            return 'PreviewApplicationVersion'
        elif tag2bytes[1:2] == b'\x18':
            return 'PreviewSettingsName'
        elif tag2bytes[1:2] == b'\x19':
            return 'PreviewSettingsDigest'
        elif tag2bytes[1:2] == b'\x1a':
            return 'PreviewColorSpace'
        elif tag2bytes[1:2] == b'\x1b':
            return 'PreviewDateTime'
        elif tag2bytes[1:2] == b'\x1c':
            return 'RawImageDigest'
        elif tag2bytes[1:2] == b'\x1d':
            return 'OriginalRawFileDigest'
        elif tag2bytes[1:2] == b'\x1e':
            return 'SubTileBlockSize'
        elif tag2bytes[1:2] == b'\x1f':
            return 'RowInterleaveFactor'
        elif tag2bytes[1:2] == b'\x25':
            return 'ProfileLookTableDims'
        elif tag2bytes[1:2] == b'\x26':
            return 'ProfileLookTableData'
        elif tag2bytes[1:2] == b'\x40':
            return 'OpcodeList1'
        elif tag2bytes[1:2] == b'\x41':
            return 'OpcodeList2'
        elif tag2bytes[1:2] == b'\x4e':
            return 'OpcodeList3'
        elif tag2bytes[1:2] == b'\x61':
            return 'NoiseProfile'
        elif tag2bytes[1:2] == b'\x63':
            return 'TimeCodes'
        elif tag2bytes[1:2] == b'\x64':
            return 'FrameRate'
        elif tag2bytes[1:2] == b'\x72':
            return 'TStop'
        elif tag2bytes[1:2] == b'\x89':
            return 'ReelName'
        elif tag2bytes[1:2] == b'\x91':
            return 'OriginalDefaultFinalSize'
        elif tag2bytes[1:2] == b'\x92':
            return 'OriginalBestQualitySize'
        elif tag2bytes[1:2] == b'\x93':
            return 'OriginalDefaultCropSize'
        elif tag2bytes[1:2] == b'\xa1':
            return 'CameraLabel'
        elif tag2bytes[1:2] == b'\xa3':
            return 'ProfileHueSatMapEncoding'
        elif tag2bytes[1:2] == b'\xa4':
            return 'ProfileLookTableEncoding'
        elif tag2bytes[1:2] == b'\xa5':
            return 'BaselineExposureOffset'
        elif tag2bytes[1:2] == b'\xa6':
            return 'DefaultBlackRender'
        elif tag2bytes[1:2] == b'\xa7':
            return 'NewRawImageDigest'
        elif tag2bytes[1:2] == b'\xa8':
            return 'RawToPreviewGain'
        elif tag2bytes[1:2] == b'\xaa':
            return 'CacheVersion'
        elif tag2bytes[1:2] == b'\xb5':
            return 'DefaultUserCrop'
        elif tag2bytes[1:2] == b'\xd5':
            return 'NikonNEFInfo'
        elif tag2bytes[1:2] == b'\xe9':
            return 'DepthFormat'
        elif tag2bytes[1:2] == b'\xea':
            return 'DepthNear'
        elif tag2bytes[1:2] == b'\xeb':
            return 'DepthFar'
        elif tag2bytes[1:2] == b'\xec':
            return 'DepthUnits'
        elif tag2bytes[1:2] == b'\xed':
            return 'DepthMeasureType'
        elif tag2bytes[1:2] == b'\xee':
            return 'EnhanceParams'
        else:
            return '<<Unknown Tag>>'


    # ea
    elif tag2bytes[0:1] == b'\xea':
        if tag2bytes[1:2] == b'\x1c':
            return 'Padding'
        elif tag2bytes[1:2] == b'\x1d':
            return 'OffsetSchema'
        else:
            return '<<Unknown Tag>>'

    # fd
    elif tag2bytes[0:1] == b'\xfd':
        if tag2bytes[1:2] == b'\xe8':
            return 'OwnerName'
        elif tag2bytes[1:2] == b'\xe9':
            return 'SerialNumber'
        elif tag2bytes[1:2] == b'\xea':
            return 'Lens'
        else:
            return '<<Unknown Tag>>'

    # fe
    elif tag2bytes[0:1] == b'\xfe':
        if tag2bytes[1:2] == b'\x00':
            return 'KDC_IFD'
        elif tag2bytes[1:2] == b'\x4c':
            return 'RawFile'
        elif tag2bytes[1:2] == b'\x4d':
            return 'Converter'
        elif tag2bytes[1:2] == b'\x4e':
            return 'WhiteBalance'
        elif tag2bytes[1:2] == b'\x51':
            return 'Exposure'
        elif tag2bytes[1:2] == b'\x52':
            return 'Shadows'
        elif tag2bytes[1:2] == b'\x53':
            return 'Brightness'
        elif tag2bytes[1:2] == b'\x54':
            return 'Contrast'
        elif tag2bytes[1:2] == b'\x55':
            return 'Saturation'
        elif tag2bytes[1:2] == b'\x56':
            return 'Sharpness'
        elif tag2bytes[1:2] == b'\x57':
            return 'Smoothness'
        elif tag2bytes[1:2] == b'\x58':
            return 'MoireFilter'
        else:
            return '<<Unknown Tag>>'


    # else
    else:
        return '<<Unknown Tag>>'