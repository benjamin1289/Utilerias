class MimeType():
    """
    Mimetype
    :see: https://developer.mozilla.org/es/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Common_types
    """
    # Microsoft:
    # https://stackoverflow.com/questions/4212861/what-is-a-correct-mime-type-for-docx-pptx-etc
    # https://www.thoughtco.com/mime-types-by-content-type-3469108
    # https://docs.microsoft.com/en-us/previous-versions/office/office-2007-resource-kit/ee309278(v=office.12)?redirectedfrom=MSDN
    CAT = "application/vnd.ms-pkiseccat"
    DOC = "application/msword"
    DOCX = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    DOCM = "application/vnd.ms-word.document.macroEnabled.12"
    DOT = "application/msword"
    DOTX = "application/vnd.openxmlformats-officedocument.wordprocessingml.template"
    DOTM = "application/vnd.ms-word.template.macroEnabled.12"
    MDB = "application/vnd.ms-access"
    MPP = "application/vnd.ms-project"
    MSG = "application/vnd.ms-outlook"
    ONE = "application/msonenote"
    ONETOC2 = ONE #"application/msonenote"
    ONETMP = ONE #"application/msonenote"
    ONEPKG = ONE #"application/msonenote"
    PPT = "application/vnd.ms-powerpoint"
    PPTX = "application/vnd.openxmlformats-officedocument.presentationml.presentation"
    PPTM = "application/vnd.ms-powerpoint.presentation.macroEnabled.12"
    PPS = PPT #"application/vnd.ms-powerpoint"
    PPSX = "application/vnd.openxmlformats-officedocument.presentationml.slideshow"
    PPSM = "application/vnd.ms-powerpoint.slideshow.macroEnabled.12"
    POT = PPT #"application/vnd.ms-powerpoint"
    POTX = "application/vnd.openxmlformats-officedocument.presentationml.template"
    POTM = "application/vnd.ms-powerpoint.template.macroEnabled.12"
    PPA = PPT #"application/vnd.ms-powerpoint"
    PPAM = "application/vnd.ms-powerpoint.addin.macroEnabled.12"
    SLDX = "application/vnd.openxmlformats-officedocument.presentationml.slide"
    SLDM = "application/vnd.ms-powerpoint.slide.macroEnabled.12"
    SST = "application/vnd.ms-pkicertstore"
    STL = "application/vnd.ms-pkistl"
    THMX = "application/vnd.ms-officetheme"
    WCM = "application/vnd.ms-works"
    WDB = WCM #"application/vnd.ms-works"
    WKS = WCM #"application/vnd.ms-works"
    WPS = WCM #"application/vnd.ms-works"
    HLP = "application/winhlp"
    XLS = "application/vnd.ms-excel"
    XLA = XLS #"application/vnd.ms-excel"
    XLAM = "application/vnd.ms-excel.addin.macroEnabled.12"
    XLC = XLS #"application/vnd.ms-excel"
    XLM = XLS #"application/vnd.ms-excel"
    XLSM = "application/vnd.ms-excel.sheet.macroEnabled.12"
    XLSX = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    XLT = XLS #"application/vnd.ms-excel"
    XLTX = "application/vnd.openxmlformats-officedocument.spreadsheetml.template"
    XLTM = "application/vnd.ms-excel.template.macroEnabled.12"
    XLSB = "application/vnd.ms-excel.sheet.binary.macroEnabled.12"
    XLW = XLS #"application/vnd.ms-excel"

    # IMAGES
    # https://www.thoughtco.com/mime-types-by-content-type-3469108
    BMP = "image/bmp"
    COD = "image/cis-cod"
    GIF = "image/gif"
    IEF = "image/ief"
    JPE = "image/jpeg"
    JPEG = JPE #"image/jpeg"
    JPG = JPE #"image/jpeg"
    JFIF = "image/pipeg"
    SVG = "image/svg+xml"
    TIF = "image/tiff"
    TIFF = "image/tiff"
    RAS = "image/x-cmu-raster"
    CMX = "image/x-cmx"
    ICO = "image/x-icon"
    PNM = "image/x-portable-anymap"
    PBM = "image/x-portable-bitmap"
    PGM = "image/x-portable-graymap"
    PPM = "image/x-portable-pixmap"
    RGB = "image/x-rgb"
    XBM = "image/x-xbitmap"
    XPM = "image/x-xpixmap"
    XWD = "image/x-xwindowdump"

    # VIDEO
    # https://www.thoughtco.com/mime-types-by-content-type-3469108
    AU = "audio/basic"
    SND = "audio/basic"
    MID = "audio/mid"
    RMI = "audio/mid"
    MP3 = "audio/mpeg"
    AIF = "audio/x-aiff"
    AIFC = AIF #"audio/x-aiff"
    AIFF = AIF #"audio/x-aiff"
    M3U = "audio/x-mpegurl"
    RA = "audio/x-pn-realaudio"
    RAM = "audio/x-pn-realaudio"
    WAV = "audio/x-wav"

    # Compression
    _7Z = "application/x-7z-compressed"
    BZ = "application/x-bzip"
    BZ2 = "application/x-bzip2"
    GZ = "application/gzip"
    ISO = "application/x-iso9660-image"
    RAR = "application/x-rar-compressed"
    TGZ = "application/x-gtar"
    TAR = "application/x-tar"
    TAR_GZ = TGZ #"application/x-gtar"
    TAR_Z = TGZ #"application/x-gtar"
    TAR_BZ2 = TGZ #"application/x-gtar"
    TBZ2 =  TGZ #"application/x-gtar"
    TAR_LZ = TGZ #"application/x-gtar"
    TLZ = TGZ #"application/x-gtar"
    TAR_XZ = TGZ #"application/x-gtar"
    TXZ = TGZ #"application/x-gtar"
    TAR_ZST = TGZ #"application/x-gtar"
    ZIP = "application/zip"
    ZIPX = ZIP #"application/zip"

    # OTHER
    PDF = "application/pdf"
    XML = "application/xml"
    EPUB = "application/epub+zip"
    JAR = "application/java-archive"
    JS = "application/javascript"
    JSON = "application/json"
    ODP = "application/vnd.oasis.opendocument.presentation"
    ODS = "application/vnd.oasis.opendocument.spreadsheet"
    ODT = "	application/vnd.oasis.opendocument.text"
    RTF = "application/rtf"
    SH = "application/x-sh"
    SWF = "application/x-shockwave-flash"


