# -*- coding: utf-8 -*-
"""Untitled10.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1idS0QUV_X21RVowiHajkOWez4TJDpmiC
"""

import pandas as pd

# DataFrame yaratish
data = {
    "Ism": ["Ali", "Vali", "Aziz", "Olim", "Anvar"],
        "Yosh": [25, 30, 22, 29, 32],
            "Shahar": ["Toshkent", "Samarqand", "Buxoro", "Andijon", "Namangan"]
            }

            df = pd.DataFrame(data)

            # Yosh > 25 bo'lganlarni filterlash
            filtered_df = df[df["Yosh"] > 25]

            print("Asosiy DataFrame:")
            print(df)

            print("\nFilterlangan DataFrame (Yosh > 25):")
            print(filtered_df)





