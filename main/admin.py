from django.contrib import admin
from main.models import (Main, BI_PE, LAW, POLIT, M, E, HIST, Main_ngram, BI_PE_ngram, LAW_ngram, POLIT_ngram,
                         M_ngram, E_ngram, HIST_ngram, Main_pecase, school_pecase, uni_pecase)
# Register your models here.

admin.site.register(Main),
admin.site.register(BI_PE),
admin.site.register(LAW),
admin.site.register(POLIT),
admin.site.register(M),
admin.site.register(E),
admin.site.register(HIST),
admin.site.register(Main_ngram),
admin.site.register(BI_PE_ngram),
admin.site.register(LAW_ngram),
admin.site.register(POLIT_ngram),
admin.site.register(M_ngram),
admin.site.register(E_ngram),
admin.site.register(HIST_ngram),
admin.site.register(Main_pecase),
admin.site.register(school_pecase),
admin.site.register(uni_pecase),
