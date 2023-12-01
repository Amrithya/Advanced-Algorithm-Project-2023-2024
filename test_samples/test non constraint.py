# -*- coding: utf-8 -*-
"""test.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1hVdUawblriYFp2jeyYYqyzk_vq058fP1
"""

tests = [
    {   "matrix" : None,
        "expected_result": "No matrix",
        "subarray_indices": "NIL"
    },
    {
        "matrix": [[1, 2, -1, -4, -20, None]
        ],
        "expected_result": "1D matrix",
        "subarray_indices": "NIL"
    },

    {
        "matrix": [[1, 2, -1, -4, -20]
        ],
        "expected_result": "1D matrix",
        "subarray_indices": "NIL"
    },
    {
        "matrix": [[1, 1],
                   [1, 1], [1, 1], [1, 1]],
        "expected_result": 8,
        "subarray_indices": [(0, 0), (3, 1)],
    },
    {
        "matrix": [[1, 1, 1],
                   [1, 1, 1], [1, 1, 1], [1, 1, 1]],
        "expected_result": 12,
        "subarray_indices": [(0,0),(3,2)],
    },

     {
        "matrix": [[1, 2], [3, 4]],
        "expected_result": 10,
        "subarray_indices": [(0,0),(1,1)],
    },

    {
        "matrix": [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]],
        "expected_result": -1,
        "subarray_indices": [(0, 0), (0, 0)],
    },
     {
        "matrix": [[-1, -2, -3], [-4, -5, -6], [-7, -8, -9], [-10, -11, -12]],
        "expected_result": -1,
        "subarray_indices": [(0, 0), (0,0)],
    },
     {
        "matrix": [[-2, 5, -1, 4], [8, -6, 3, 1], [2, 2, -4, -1], [-3, 2, 6, -1]],
        "expected_result": 15,
        "subarray_indices": [(0, 0), (3, 3)],
    },

    {
        "matrix": [
            [2, -1, 4, -6, 2],
            [-3, 2, -1, 4, -3],
            [1, -5, 2, -1, 5],
            [4, -2, 3, 7, -2],
        ],
        "expected_result": 14,
        "subarray_indices": [(0, 2), (3, 4)],
    },

    {
        "matrix": [  [5,  16,  25, -19, -37],
                    [14,  18, -20,  37, -47],
                     [-44, -41,  38,   5, -31],
                     [48, -30, -25, -12,  30],
                     [6,  49,  -2,  40, -11],
                      [-25,  50,  18,  43,  39],
                      [42, -33,  49,  23,  42]],

        "expected_result": 341,
        "subarray_indices": [(3, 0), (6, 4)],
    },

   {
        "matrix": [[-89,  45,  97, -13, -15, -68, -25,  10,  69, -84,  56, -64,  67, -48,  50],
[-51, -57,  94,  94,  45, -77,  56, -58,  22,  44, -98,  33,  25,  51, -31],
[-98,  58, -55,  75, -43,  80,  95, -20, -61, -59,  87, -32,  47,  29,  60],
[-51,  99,  46,  90,  55,  13, -74, -89, -96, -33, -60,  61, -78,  64,  26],
[-21, -89,  18, -82,  11,  53, -86, -54, -98,  70,  90, -99,  26, -20, -80],
[84,  68, -10,  32,  23, -47,  73,  23, -64, -31, -20,  74,  50, -86,  48],
 [24, -78, -71,  32,  74, -50, -85,  67, -47, -10,  46,  90, -62,  49,  11],
 [10,  19, -33, -50, -47, -82,  91, -71,  24, -16,  52,  83,  36, -15, -76],
 [ 14,  99, -34,  82,  13,  34,  16, -74,  56, -97,  97,  55,  10,  38,  99]] ,
        "expected_result": 741,
        "subarray_indices": [(0,10),(8,14)], #top left and bottom right indices
    },

    {
        "matrix": [[-50,  20,  87,  15, -76,  63, -91,  11,  96,  38, -16,  56, -93, -98,  62,  80, -36, -32,  99, -72],
 [53,  76,  89, -23,  18, -70, -14,  49, -27,  44, -82,  87, -38,  84,  43,  13, -46, -61,  37, -42],
 [45, -47,  34, -59, -87,  92, -85, -38, -32,  87, -46,  41,  25, -96,  64, -95, -40,  34,  10,  98],
[-91,  50,  11,  14,  52, -10, -75, -98,  95,  59,  16,  39,  80,  31, -65,  84, -79, -53,  70,  13],
[-54,  32, -41,  62,  93, -33, -91,  64, -92, -47,  54,  92,  45, -65,  69,  89, -81, -43,  49,  27],
[-43,  51, -68, -56,  47,  73, -70,  86,  52, -67, -47, -97, -50, -71,  81,  78, -86,  57,  59, -24],
[-32,  53, -23, -48, -67,  61,  26,  13, -20,  77, -49, -95, -11, -57,  72, -90,  26, -53,  12, -35],
[-62, -81,  82,  97,  72,  49, -58,  84,  65,  37, -18, -92,  27, -23, -26, -49, -23,  60,  79, -30],
 [18,  89, -44, -13, -62,  61, -87, -99,  26,  98, -18,  42,  84, -34, -69, -10,  11, -96,  98,  93],
 [16,  43,  85, -84,  25, -70,  80, -63,  21, -71,  20, -24,  42,  29, -38, -59,  66,  20,  41, -23] ],
        "expected_result": 682,
        "subarray_indices": [(0,1),(7,9)], #top left and bottom right indices
    },


    {
        "matrix": [[-12, -69, -61, -44, -99,  77,  29,  98,  75, -53,  35, -67,  84, -64,  65,  92,  19,  14,  60, -90, -63,  32, -76, -48, -87, -81, -93,  34,  48],
  [11, -36, -78,  50,  70, -12, -39,  58,  77, -61, -85,  14,  60,  18, -90,  73,  34, -42, -80,  71,  93,  68,  16,  12,  94, -77, -73,  59, -55],
  [97, -99, -22,  50,  76,  82,  67, -34,  24,  76, -64, -15, -32, -51, -29,  76, -77, -80,  10, -92, -68, -40, -38, -47, -93,  26,  62,  15,  97],
  [23, -50, -53,  89, -93, -12,  91,  91,  54,  98, -53,  25,  13, -35,  13, -56,  85, -36,  89,  76,  85,  36, -65, -41,  22, -32,  92, -47,  40],
  [88, -77, -95,  38, -27, -69,  90, -91, -24,  93, -43,  96,  23, -31,  65,  86,  55,  44, -47, -64, -74, -42, -74, -41, -45,  17, -26,  66, -99],
  [97, -73,  47, -16,  80,  93,  25, -32,  29, -97, -20, -91,  11, -79, -82, -41, -14,  47, -60,  14, -57, -43, -32,  86,  74,  18,  21,  54, -23],
  [11,  93, -19,  73,  94, -46, -70, -48,  76,  80, -84, -59, -93, -22,  77, -56,  38, -21, -15,  38,  17, -31,  89, -32,  86, -89, -14,  40, -47],
  [44,  38, -54,  27,  89,  97,  50, -29, -24, -86, -85,  71, -38, -46,  88,  76, -13, -95, -62, -61,  33,  89, -75,  73,  85,  20,  95, -96,  27],
  [21,  11, -15, -57, -29,  19, -16, -32, -99,  69,  82,  77,  26, -10, -18,  87, -79, -33,  73, -84,  71, -24, -40, -60,  57, -36,  68,  48, -86],
[-100, -53,  69,  90,  67, -64,  93,  35, -99, -82, -56,  35,  85, -63,  95,  57,  80, -50, -31,  75, -93,  38,  44,  50, -69,  25,  43,  65,  20],
 [-4,  25,  66, -17, -92,  55, -47,  40,  84, -76,  86,  11,  29,  71, -24, -56, -73,  91, -73, -16,  38,  59,  77,  65,  49, -48,  94, -89, -19],
[-100,  45, -11,  33,  40,  98, -15,  80, -68, -68,  32, -92,  24,  16, -91,  10,  11,  73, -44,  80,  62, -75, -67, -32, -31, -70,  96,  58, -73],
  [26, -12, -86,  88,  94,  93, -82, -66, -45, -11,  59,  51, -18,  56, -56, -32,  19,  54, -97, -74, -89,  68,  43, -87,  34, -75, -91,  18, -98],
  [38,  51,  13,  87,  62,  62, -66,  91,  25, -35,  99, -87, -16, -22, -54,  76,  69,  97, -53,  46, -91, -53, -99,  97, -95,  84,  94,  65, -59],
  [24,  21,  63,  70,  51, -31,  68,  19,  85,  77,  94,  90, -20, -41,  91,  16,  32, -90, -56, -19,  66, 45, -92, 65, 1, 23, -99, 100, 12, -9]],
        "expected_result": 2372,
        "subarray_indices": [(0, 3), (14, 3)],
    },

    {
        "matrix": [[-72, -66,  60, -40, -55, -85,  84, -70],
[-38, -73,  57, -34,  48,  62,  71,  96],
[-86,  41, -14,  92,  29,  40, -91, -54],
[25, -39,  37,  29,  45, -97, -10, -71],
[-46, -65,  59, -74,  17,  89,  32, -66],
[-18, -82, -16,  31, -77,  94, -69,  79],
[-55,  51, -16, -61,  38, -38, -81,  74],
  [3,  23,  57,  74,  96,  18,  21, -86],
 [23, -33,  83,  25,  43, -74, -59, -24],
[-85,  80,  53, -74,  14,  48, -29, -48],
[-99,  59, -35, -23, -99,  12,  70,  56],
[-64,  84,  80, -94,  20, -84, -77, -86],
 [87,  75, -50,  92,  75,  57,  19, -69],
 [26, -38, -71, -77,  97, -61, -32, -74],
 [53,  61, -66,  42,  20, -40,  17,  66],
 [77, -17,  80,  89, -41, -90,  34, -92],
 [82,  61, -65,  96, -55,  64,  38, -59],
  [2, -60, -85,  53, -87, -18,  56, -84],
 [66, -12, -14,  19,  53, -19, -48, -47],
 [60,  77, -97, -67,  94, -46,  71, -73],
 [65, -92,  93, -38, -46, -97,  88,  20],
 [12, -71,  12,  42,  26,  48, -20,  89],
  [0, -67,  44,  62, -98, -48, -82,  10],
[-62,  27,  22, -27, -45,  32, -72, -90],
[-57, -47,  56, -94, -97,  16, -55, -14],
 [41, -45,  26,  26, -47,  29, -99,  68],
 [17,  57,  81, -36, -38,  57,  81,  44],
 [63,  63, -51,  40,  29,  35, -47,  24],
 [52,  15,  19, -82,  95,  25, -94, -84],
 [50,  82, -43, -84,  91,  21,  46, -71],
 [53,  83, -74,  69, -25, -15,  64,  27],
 [62,  87,  77, -12, -27, -29,  93, -98],
[-67, -82, -79,  95, -98, -85,  24, -69],
 [79,  22,  85, -96,  57, -67,  47,  73],
 [69,  14, -13,  24, -68,  56,  66,  89],
[-85,  38,  26, -10, -26, -96,  26, -97],
 [57, -91,  29,  33,  47, -32, -23,  90],
 [73,  50, -89, -82, -75, -60, -54,  10],
 [24, -63,  65,  47,  75,  76,  71, -25],
 [12, -11,  19, -51, -38, -45,  80, -25],
[-82,  85,  18,  29,  19, -84, -74, -76],
 [15,  89, -97,  93, -82, -57,  93,  15],
[-60, -76,  48, -16, -35, -69, -11,  91],
[-96, -13,  21, -82,  68,  21, -50, -98],
 [50,  87,  91,  11,  38, -49, -58, -57],
  [8, -35, -88, -58,  95,  16,  85,  12],
[-69,  41, -91, -23,  29,  43,  87, -77],
 [77, -16, -86, -51, -43,  71,  69, -46],
[-29,  53, -50, -60, -27, -79, -59, -94],
[-91, -16,  38,  98,  24, -41, -25,  70]],
        "expected_result": 1324,
        "subarray_indices": [(7, 0), (41, 3)],
    },

]