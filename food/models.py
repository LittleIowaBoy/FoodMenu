from django.db import models

# Create your models here.



class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAh1BMVEX///8AAADd3d2Ojo68vLydnZ3r6+unp6f29vazs7NYWFj7+/v09PTx8fHW1tb8/Pw6OjrPz89ra2skJCSHh4eAgIBGRkZlZWXU1NQuLi5ZWVnFxcXm5ubLy8tLS0vc3Ny2traWlpY4ODirq6scHBx0dHRAQEB6enoTExNnZ2cWFhYqKipJSUk4xYv2AAAS4ElEQVR4nN1de18yLRDNvOe11LTUckvNt/r+n+/tqZxzgGGXvWDZ+asfucDAMDcGuLiIjk5/2Ggns/n73WR7qNVqh+3k7n0+S9qNYb8Tv/mo6KzWyW5fS8N+V2+szpPOznV7fpdKHHB3n1yfGZWr9kMgcTSb7cef7nYgeotpbuqOmJ3BVF6/hLKmjsnL9U+TkIZB86kUeV+4S1o/TYgH1/cVkPeF+/VPE+Ois0nXCh84vI33tw9XD7f78dsh68dP3d+1Invtib+zk/lLvTtcrVqd3vHnndZq9dj4sALSPmv2Uts8KdreKdm1l/1RypejD7W58xLZPBkF6XjWu3c3W4ZKjMFy5hFRz1F7Hob1WOvZvH2Zs55V9z+tovEySq9z9Guu9Oq+OyhU2aCh1raquM+5kLgdemuXEYKdZ4Vdk8r6mxfXbm925S2ShSt57n7IznHMz0O9GmOklWztqqeVVJwPl46Eea5OR3eebf0zziu5SqNpz187/fe9wXDZbbeb/9Bud5fDQS9NTyo69rTKsWMLPb/9MVotmrN7Td29Xc2ai5X3w17TovH+hHbco+Uh7XzaYdi9UdUls9/8eej5evBi/vTO98PK0TUb3uu+eadx85pB3RGH+UYfo0fLnO/GJAuom62qC3DwnDeMsW+rRLbNX51Cpo5MdaVZHL2lZptk436jrDTLarpJl08VoGPOjTKBrWmKS5SB7UwZMNOyf4gsb/pG75/c/jwWmz7g3hUnK0NaTYoZvYFYGQTOnP9fX5Wk7x8e3BDGzCAxoiluErix/71ICdTs/5vVm5vlevG4WC83zfrsv5Sox9XCrnrD/95Gs29W3MyrrSMGN57+3jQbg44rIEadwbLp+2Zus+KjoXkizWKL27i1Fvwo0To62TWyOjNo7FTJVLfGxBRxUUhscUdurH+ulTjwPgm1QR6TW/fzN9u75/meRAipDti0tBRvz3XpXpN8i+XS9ZhqO4tP2F27q16issS2nO5rxzq7KhJdWTuC6mB5vgn9b1yYEg9YzVl+jGXFfYx9UVm3erGrspiFbbh5wUY8YAYx7ZiBvYSmZZZIyx6uW7M2JrFSG5UNJ3MGbQ59KSsCBjOzwoOp/5nECoOpQy+Blun/UIUUX1mGkckzHFyozF/sU6V14z9mMGrbqKjBhqkhTeswof/0K2qQxnTH5SMzSj2rqr0P9W6y6tzQ/qSarqppjgbtwfiH6UhVG9O8Nup+MEikdisJFlNbTxw26hnRpXnVW2Emg9z5Wq5gXHtka7Ac6Ri+QYw9IsPz3fMSIBdgW35kietZkPQMFnW8nUow5HDiLZPSQPnO+3kglqjLEKNM4DiW191nPrnl/5BhUHL7rQO5bcgtVlnziMEhNhY9HZiUC9yQwuNFyMLcjWVUCV9LtBRLWW9kzGyoOJp1qICNCranKK5RxrSBX8suL63NE+xeJtQarzk4xHfFK0f4/kDCmqMZp4hBs7tBdn0fkrZwsL8DVbihYhJwL4W7nQe0Fsck1cCnk6JKEfzB3ia1V7ET6gVJVJY2iAkUXCvEjcQcpGzfS3U7D0j7ktmhdzAHIMVI1w9Qa9zwugHeTKBWsUILyQOihUqJYU6Z0nuJZu9ROlLpDgbW2waFxKMn2q38Bu3KEp9C2BSYREzhHoUkoU8jRgGE4VhzQa7nn8REGzPM692p0z87sD5InoKncotTmNw0hbQaTEvpsjntmjppkUw3Zo3Lej3NDVg1mtNpe+mfCrIgKR4rk5hbJ4LvqVsw6M2A1JdMY3f706R6JWP9a2Nl7yGg03w71vz27OsqJCcFU2BB5pULMjZvWm1vxm+PowGl9N0Zij18W5H3FxrM9KNXX19lFHjUpfDW85UHYAlqDlsXZpT2OBqyFERKyRIWZ0dRMStnr/RKX+SIGD2hEMyWz8WASEEZVrW5tyamhRhxQk/d+dYN6JhRtS94dnnhTpD0k7J8jqp8Ri4ZptCMbAuF4oSLRBIKZaSd5I21QmDNECZKSzyJYPE8BGLqQQxWoSlmylFI4tmEKpMgbLAS4e1vclAoli55DxCklrArQ+HI3Rf9hio4evJvCtqIIfmgfaID3IChguyx0yDLUOjLVKh5VDhYEnIFzBXuYUh/JlpfbH1VgkKOh7x3r6/bvNOsLcWemI0k7cQ4CVeJ4lpCPIE/nLEtQSHpie/ekWpU/etE/g2NIoJf17YKwKQwUxBid1ihOIXkqQzTytS+oSbom1A2Be+gTOxe16coTiE2yMlIQajyP61z4mNQhE2rJhUy63C6HlMGtjCFEF6Gskb4RdMY+Ag9mar1pEDmC8aZKKIn9+eFKZSOHQxSoCLVHa0np3JYDYGRU6hQWcyjfUqjhSmUdizhJdtdqk4UiYDIYkdqCssjkCqwDjCsik1clEJwviUgwIgam4IcWPGymxq2jylrGb0RGa5tnBelUMocIa8sE4IYVzA9RDqFxVYkQwYqVyrVdGpRCnfeSmXVq6dIuk57YIdtCIGSW4KNOTCGxjZFKRRd4Rgvoq7sFMhPIEYmHUQ8NSQfRKq/d4tU27YghR3xzp0a+6ntwS+AlyhMFqIRhach4RKnxxVQ2DqamIqIP/76SXX2pTtKDzOOX31CTGwsc9EVakZCQQrlR4o1eRQ1r6qXKLIWGZjpfG1BzHvollpqg2UpVOSf8KFqaA5EFrqVBaSd9rfO5zJm+rIoSKHIP8XUkmWlm9IyAOCpY8k2W9RI7xAJFnNf3xw4+RzC3IOokYWUnb27cIdWqbBKCnOvQ23IxUzJTl5S+iIjqkckTy5LtWUjGmCTSaHYE5gwseb1eLtoYPE7XArF7IP9EqIPPdmVPadF7LOpCs2A2FIy3YOj7HnVv8CukJ9CUUG0uVHUprmAYbkVLpbFlZ3nJrE5YRDpry9a55jCDoWIPZDoKGqXXtC6kcGRac/OnpCPpUS43udBI0678lAowzYmRi/qW1xQFAKS4ViSmTbcE4UvReJB+ywi4ZDaeKVSiF0QHqSC/uE/iFyBGXos2WftI4qVjlCpjLXXvaRDT5+jYO7MXNOJDEMaS2kuH/8fxElHl6TfWZvTA7f25FjkTcU3Tgfe3txILGlMf/+DyUJIZ8kTp/kHUYgYm1u1rjQKsTikI/7rqUKv+DKlJtjUMGvSY22fkAgpVP5V5kffcDcDtWVtA31NhW31FYmXfkIRfiLMsqLCQiFUkRhEKSlCnpuUTDhirkDM+wuKTSsaN5hCaE5Z+GmhOvsmEAUPrpTLv2/xBRFlSi+DKcT8B1GYPYtaOjjvPT10F4vMvSe7l6BQOC2YQsx/GIUXw/QLE3VlmrJ/mGZgVjKH+dbhJ7p+Gr1norxfpCaPVLIOIcgCZOkR19Mr52D2Yb/z3Fxi9NVGqtBXZKmEvYMphOAL0IeEfqvVEjtvNmi1BunHMTy5GOn8Ih8p+jCLQtH4CGKIeNtkfCtwvacUaPk0h4xYhKgUOB9HGXXI0vidInapjVwUXrRCc6IAEdxwvI5ObKZdipNvUiQsEXwXVT4KbWW6zU44ELsHC+dYMs7MUUzxD4OTZvNSeNFHbuKTNzeRIOLd9Q+zk2pc+06UT3D2X24KaRqDzhK7ARBFB/ggmlMiKhIjPoR2NzqFxzAd4jQir7IZTUISGykSUyo08zk2hbLbhxh+jlibEtkUVRN6VDQ2hRI2gdJWwpWZX8NsU6Y1HbEpbLj1i9GWPQvSO0RbpcLQdJXYFM7cH4uSy963UPaexIMPFaaxKRRR6iqLbYCsELkC0/BYEpo3FplC2fFQJiHk2hrhaMROxAoIPN8fmULRDOApWUghe8BiEcFuT3L2ODKFIvkQSxT/J8R2VhIvpChwIUam8D2Fy0I8PFGn8ENwCi5sIcalENs8YsFiZQYZJSJMIanEWA1J5ohNobhOCFqLEp+kfAeItgGby9oMY9O4FAqTwptLjkVhGlvJG0NCZtAxv6gUIukrMO/OBfgcATLRsUFecFQK5ZfgJ1zzFKiwn9zWpNqgLNyoFErIEotItGHoNXWyEKE+EfQLUfoxKUTgCkwqRkqo4azl6ku0KMRoiEmhUENnW6W/obn6g4P7hXbWy4uIFELmQajIjHgSjBSI+qOgh9QccC48IoXYN0agWcLd4bdYYNcag4LT4tlmQzwKka2MPRmoj01wc/gGrAD2yJ7EeBRiCiFnsIBynMnXjvTNwyuKRiEUHzGkdlgyE9hqhhuMLZRMmRyNQiTmwIdADkGuaxs1asQezIyFxKIQWpnsY+1QdgDA77DcMIlZ5/xiUYg8FEwhGDff5R8YLcpXwj04GfwQiUJYInT3TxLMWRZwrhllyF87pO+exKFwhItVyHSUsrw3fULWkNOLvIL0LM44FEIjkyGC/KK818OOxISnS0PoortUCzAKhbQdDsOxJ2kDd7nvNsTg0CQik3SbphRjUDjAyX2qVe1lIHB4m64IxZClqtcYFOLCVmIquly1wPWUiTZmlFaQ4u1HoJA2wknMgKeK3NgGI5fNNLqw1R+arJ5CGlkScnQdWaFLnRKtUrpp8OANilROIeKhxtYLhrvYpXt9Vf/QaHpvw5JYVvhLYuKwaYlXHf1qZHTlteBF2xBUfCEjptaf93C0fsKvaD8ynHqhled6ayQy5hek30AmHk8GtecTqMP8vPMdydb0LN17zWMK4VP8AlNK/+Rru1DqtW0uP4bhkO/2reWHJtpre9T8JASti1DzIx2YLo5E8kMC/uSOqu5PZgJ5kWJtlrl7nsbJc4dvUHSxDPiBF2YKUpClHmRIUM9CL458TSvfPc/LeqEX50cPwsa42p6zl+2HkSpE553aYW6hfj2VXA605oyMMb5KPNobWiu+J8vgFRrh0s940E3Mhv42XpCr6ukOE5zJb0ZO6ELxcLPJC0pP512ZkfFWSgXtODAe1TEOa7BdVUFDnGtuSC2DxNuyL+jYaBlvEBnWE7//VskCobMipiVqHpbYVNGWoGHUbYgAuqu1qnc1iBJTuVqvwVT33FvLfMHGNCvIaqxKGY8mvjqt006FDWAL1gkj00Oh8Z5U9u4EM745niYz1SZBRzIyYL/DZwpqNuIqfCOQ5bYZWr60DlfOy97ybT9kemdWyI9BlHydxASzo0liz35a9b8yND7aR72sp6p9r11UAGaOlAftPvFQ9Iki9yFTa2UzgZVfKH7vr/zSOfQybucPK3S6zhPe9pPxPMzBt0AGw3j+yJbSzhOIH6OwzmOQ99bO04euocQcrBxILQ0OBzkNXCoPiW5flmFEjpYvymOr9oPmPbahxlH8mQ53w3l2WD8l+9C+TtdZo2Fbf6PctlaMt4jfIjlsfUNR2bK6M63puJq2hy13XfZbl89T3xvQU5sEw8+4q+6VPgsDQxY40nrlPikrmDzMd9Pmc7exbHSfm9Pd/CHlffKdo8oN4+kp4tMhfYPE/5zVvko5uRyMG8df6Blm6jjaDH7CZCtX8Q2mh1opzFw3bGFUWdGrjn6Ys6REgfrtlDfFMzBuKgyYGD+JHdu7sHWfLdM/MVSUWwBeNFvo8t34TYxggoOu2S89mLfMuyJv9FhPYv7qRI/bLMyr4iceG/+6Hsqu+9la15prU+C+xnlJUsHAUmNe73619mq8I65mS+/XlttyFeFBdS9s7T7zGxmdViN5uVUk7PgmabRSvrMedz7JK3aEtf2eej3zfqbHdWPT/YdNY/2YeS9AYtV/qNTfDcHA9nxrSXVM1LLpq81P9wQa0LV7UXupJnCysvkzzmu8ARg4LnntqjwvLd1a708pYqzeKE+M1MuEoVcOe1b4oHkh9BTv/sMpLEbkSnUVM0VYbNhK6wv7JC+Rj03VPqgwkF4cCyWCUctrIutG3u3JjJgMrFUa85CoErg/uQpMgSIA8+xGbZSvKxDL1WKo0Bgq5Fvup/e/hT8Zg7ptfIbewfBufXeo/5wCTEevYQnWsESQxJq+TYRob3VoNY0JCeE1TrGq3TZ/6/QRBm34rdvs6aBM5kn7DMj7BCU3ZKsMCrLGysuJANpwy4qskKKoapP8JCDVkW52kaKofr8sJigHVXkDi0DG6E9b2DlBJ1zSQpzkmvw2EyYTFKvyb3pT+taJ40wVYIQNVe9ljT288Fs2h/InQEk4vpv+yKM4I0UB0K6wrjIolHVWigIglaHZKmerKIA+osaalwG3OfPe2F+LVJVxzooCSFEZZ60oCFAZ1uFoOrZcRSLzz4FUhnkug3IPfkO8sARIZfDeQ1cvPkuok+Wd2nMEbnUglUGRjrNVFIAiNElRFE1F/VVwVMZfURQAvNxPL4NyHMdn6FFosAJT5+5RaDBUxl9SFACFwilR9PwVBcCHo4EzCz2lQ3umo4rzNb8I7n7/H1EUgL1Lv/8jigJYWRSeuUehwUyh+kOKAuBshL+kKAC66Sn8otHzAgJTf0xRAEeV8ecUBfCVEp39YNEZo/1UezpxBP9/Mf3sMemNsmcAAAAASUVORK5CYII=')
