import pandas as pd
import json

# Variable contenant les données
data = '''
{"idAnnonce":201122761,"idTypeTransaction":1,"idTiers":[559130],"localisation":{"idDivision":2243,"codeDept":"59"},"stickyBar":{"img":"https://v.seloger.com/s/width/800/visuels/0/e/3/u/0e3uu3hoi3vgbk09i2dog5twsh25qlte3uyeej4oz.jpg","imgAlt":"Local commercial","title":"Local commercial, 145 m²","montant":{"label":"3 500 €","suffix":" par mois C.C.-T.T.C."}},"contact":{"hasPhone":true,"mandataires":[{"idAgence":477201,"logo":"https://v.seloger.com/s/width/150/logos/0/u/p/o/0upoaaoi5sckd1zph7gstemqyepwmf487nc5xony0.jpg","telephone":"03 62 26 36 36","adresse":"","cp":"59650","ville":"VILLENEUVE-D'ASCQ","website":"","nom":"ENTERPRISE IMMO TRANSACTION"}]},"visuels":{"photoList":["https://v.seloger.com/s/width/800/visuels/0/e/3/u/0e3uu3hoi3vgbk09i2dog5twsh25qlte3uyeej4oz.jpg"],"alt":"Location Local commercial Lille","defaultVisuel":"/Content/App/dist/img/visuals/default-boutique.svg","isExclusive":false},"map":{"coordinates":{"latitude":50.63404,"longitude":3.05829,"precision":2},"polygon":"POLYGON ((3.0618700000923127 50.631739999982528, 3.0663499999791384 50.633709999965504, 3.0646399999968708 50.635189999942668, 3.0637399998959154 50.634270000038669, 3.0609999999869615 50.634740000008605, 3.0595299999695271 50.635770000051707, 3.0619099999312311 50.636779999942519, 3.0628500001039356 50.637199999997392, 3.0595199998933822 50.638679999974556, 3.0566700000781566 50.636249999981374, 3.0545799999963492 50.636850000009872, 3.056150000076741 50.635920000029728, 3.0593799999915063 50.633150000008754, 3.0618700000923127 50.631739999982528))"},"specifications":[{"icon":0,"label":"Disponibilité","value":"Immédiate"}],"traffic":{"pedestrianTraffic":{"flowScoring":4,"flowScoringLabel":"dense","isEmpty":false,"weekDayDistribution":{"t08/10":8,"t10/12":9,"t12/14":14,"t14/16":13,"t16/18":13,"t18/20":12,"t20/22":9},"weekEndDistribution":{"t08/10":5,"t10/12":8,"t12/14":10,"t14/16":12,"t16/18":14,"t18/20":11,"t20/22":7}},"vehiclesTraffic":{"flowScoring":4,"flowScoringLabel":"dense","isEmpty":false,"weekDayDistribution":{"t08/10":12,"t10/12":10,"t12/14":12,"t14/16":11,"t16/18":14,"t18/20":14,"t20/22":9},"weekEndDistribution":{"t08/10":7,"t10/12":10,"t12/14":11,"t14/16":12,"t16/18":14,"t18/20":13,"t20/22":9}},"isEmpty":false},"transport":{"radiusSearched":500,"city":0,"lines":[{"displayName":"1","name":"1","color":"#ffcd09","poiType":3,"stations":[{"name":"Rihour","distance":413.58143140240571,"isEmpty":false}],"isEmpty":false}],"isEmpty":false},"financialData":{"financialDataBlock":{"title":"","hasChiffreAffaire":false,"hasResultat":false,"financialDataSet":[]},"copropriete":{"nbLotsCopropriete":0,"chargesAnnuelles":0.0,"descriptionProcedureSyndicat":"","siProcedureSyndicat":false,"siCopropriete":false},"repartitionMontantBlock":{"infoSet":[{"label":"Honoraires","value":"Nous consulter"}]},"montants":[{"tabTitle":"par mois","wordingUnite":"€/mois","typePrix":0,"libelleMontant":"3 500","isUnitePrincipal":true,"unitePrix":"€/mois","unitePrixValue":3,"libelleComplement":"C.C.-T.T.C."},{"tabTitle":"par an","wordingUnite":"€/an","typePrix":0,"libelleMontant":"42 000","isUnitePrincipal":false,"unitePrix":"€/an","unitePrixValue":1,"libelleComplement":"C.C.-T.T.C."},{"tabTitle":"par m²/an","wordingUnite":"€/m²/an","typePrix":0,"libelleMontant":"290","isUnitePrincipal":false,"unitePrix":"€/m²/an","unitePrixValue":2,"libelleComplement":"C.C.-T.T.C."}]}}
'''

# Charger les données JSON dans un dictionnaire Python
data_dict = json.loads(data)

# Extraire les valeurs des clés pertinentes
idAnnonce = data_dict.get('idAnnonce')
idTypeTransaction = data_dict.get('idTypeTransaction')
cardTitle = data_dict.get('stickyBar', {}).get('title')
cardDescription = data_dict.get('stickyBar', {}).get('montant', {}).get('label')
space = data_dict.get('stickyBar', {}).get('title').split(',')[1].strip()
latitude = data_dict.get('map', {}).get('coordinates', {}).get('latitude')
longitude = data_dict.get('map', {}).get('coordinates', {}).get('longitude')
monthlyPrice = data_dict.get('stickyBar', {}).get('montant', {}).get('label')
buyPrice = data_dict.get('prices', {}).get('buy', {}).get('price')

# Créer un DataFrame avec les données extraites
df = pd.DataFrame({
    'idAnnonce': [idAnnonce],
    'idTypeTransaction': [idTypeTransaction],
    'cardTitle': [cardTitle],
    'cardDescription': [cardDescription],
    'space': [space],
    'latitude': [latitude],
    'longitude': [longitude],
    'monthlyPrice': [monthlyPrice],
    'buyPrice': [buyPrice]
})

# Sauvegarder le DataFrame dans un fichier Excel
df.to_excel('donnees.xlsx', index=False)
