LANG = 'en'
FIELDS = ['problem', 'methodology', 'information']

if LANG == 'en':
    PRETTY_PROBLEM = {
        'poi_rec': 'Poi rec.',
        'next_poi': 'Next Poi',
        'time_aware': 'Time-aware',
        'in_out_town': 'In/Out-of-town',
        'others': 'Others',
    }

    PRETTY_METHODOLOGY = {
        'cf': 'CF',
        'factorization': 'Factorization',
        'probabilistic': 'Probabilistic',
        'hybrid': 'Hybrid',
        'link_based': 'Link-based',
        'others': 'Others'
    }

    PRETTY_INFORMATION = {
        'geographical': 'Geographical',
        'user_pref': 'User Pref.',
        'temporal': 'Temporal',
        'social': 'Social',
        'categorical': 'Categorical',
        'sequential': 'Sequential',
        'textual': 'Textual',
    }
elif LANG == 'br':
    PRETTY_PROBLEM = {
        'poi_rec': 'POI rec.',
        'next_poi': 'Next POI',
        'time_aware': 'Time-aware',
        'in_out_town': 'In/Out-of-town',
        'others': 'Outros',
    }

    PRETTY_METHODOLOGY = {
        'cf': 'CF',
        'factorization': 'Fatoração',
        'probabilistic': 'Probabilístico',
        'hybrid': 'Híbrido',
        'link_based': 'Link-based',
        'others': 'Outros'
    }

    PRETTY_INFORMATION = {
        'geographical': 'Geográfica',
        'user_pref': 'Preferencial',
        'temporal': 'Temporal',
        'social': 'Social',
        'categorical': 'Categórica',
        'sequential': 'Sequencial',
        'textual': 'Textual',
    }

PROBLEM_IDX = {j: i for i, j in enumerate(PRETTY_PROBLEM.keys())}

METHODOLOGY_IDX = {j: i for i, j in enumerate(PRETTY_METHODOLOGY.keys())}

INFORMATION_IDX = {j: i for i, j in enumerate(PRETTY_INFORMATION.keys())}

PRETTY_DATASET = {
    'foursquare': 'Foursquare',
    'gowalla': 'Gowalla',
    'yelp': 'Yelp',
    'brightkite': 'Brightkite',
    'weeplaces': 'Weeplaces',
    'twitter': 'Twitter',
    'tripadvisor': 'TripAdvisor',
    # 'world_wide': 'World-Wide',
    'weibo': 'Weibo',
    'dianping': 'DianPing',
    'instagram': 'Instagram',
    'ctrip': 'Ctrip',
    'flickr': 'Flickr',
    'jiepang': 'Jiepang',
    # 'others': 'Others',
}

if LANG == 'en':
    PRETTY_DATASET['others'] = 'Others'
elif LANG == 'br':
    PRETTY_DATASET['others'] = 'Outros'

if LANG == 'en':
    PRETTY_METRIC = {
        'precision': 'Precision',
        'recall': 'Recall',
        'fm': 'F-measure',
        'ndcg': 'nDCG',
        'mae': 'MAE',
        'rmse': 'RMSE',
        'map': 'MAP',
        # 'averageprecision': 'AP',
        'hit': 'Hit Rate',
        'epc': 'EPC',
        'dcg': 'DCG',
        'mrr': 'MRR',
        'ild': 'ILD',
        'prg': 'PRg',
        'coverage': 'Coverage',
        'others': 'Others',
    }
elif LANG == 'br':
    PRETTY_METRIC = {
        'precision': 'Precisão',
        'recall': 'Revocação',
        'fm': 'F-measure',
        'ndcg': 'nDCG',
        'mae': 'MAE',
        'rmse': 'RMSE',
        'map': 'MAP',
        # 'averageprecision': 'AP',
        'hit': 'Taxa de acerto',
        'epc': 'EPC',
        'dcg': 'DCG',
        'mrr': 'MRR',
        'ild': 'ILD',
        'prg': 'PRg',
        'coverage': 'Coverage',
        'others': 'Outros',
    }
