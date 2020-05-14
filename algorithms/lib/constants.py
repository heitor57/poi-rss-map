
FIELDS = ['problem',
          'methodology',
          'information']

PRETTY_PROBLEM = {
    'poi_rec': 'Poi rec.',
    'time_aware': 'Time-aware',
    'next_poi': 'Next Poi',
    'in_out_town': 'In/Out-of-town',
    'others': 'Others',
}

PRETTY_METHODOLOGY = {
    'link_based': 'Link-based',
    'cf': 'CF',
    'factorization': 'Factorization',
    'probabilistic': 'Probabilistic',
    'hybrid': 'Hybrid',
    'others': 'Others'
}

PRETTY_INFORMATION = {
    'user_pref': 'User Pref.',
    'geographical': 'Geographical',
    'social': 'Social',
    'textual': 'Textual',
    'categorical': 'Categorical',
    'sequential': 'Sequential',
    'temporal': 'Temporal',
}

PROBLEM_IDX = {j: i for i,j in enumerate(PRETTY_PROBLEM.keys())}

METHODOLOGY_IDX = {j: i for i,j in enumerate(PRETTY_METHODOLOGY.keys())}

INFORMATION_IDX = {j: i for i,j in enumerate(PRETTY_INFORMATION.keys())}

PRETTY_DATASET = {
    'foursquare': 'Foursquare',
    'gowalla': 'Gowalla',
    'yelp': 'Yelp',
    'brightkite': 'Brightkite',
    'weeplaces': 'Weeplaces',
    'twitter': 'Twitter',
    'tripadvisor': 'TripAdvisor',
    'world_wide': 'World-Wide',
    'weibo': 'Weibo',
    'dianping': 'DianPing',
    'instagram': 'Instagram',
    'ctrip': 'Ctrip',
    'flickr': 'Flickr',
    'others': 'Others',
}
