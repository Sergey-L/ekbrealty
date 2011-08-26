from website.models import Realty

def get_url_params(fields):
    for field in fields:
        if [field for field in fields if field not in [r_field.name for r_field in Realty._meta.fields]]:
            print u"Blya"
            continue
    params = '&'.join(["%s=%s" % (field[0], field[1][id]) for field in fields.items() for id in range(len(field[1]))])
    return '?' + params