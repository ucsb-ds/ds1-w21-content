test = {   'name': 'q0_1',
    'points': 1,
    'suites': [   {   'cases': [   {'code': ">>> flavor_count.labels == ('Flavor', 'count')\nTrue", 'hidden': False, 'locked': False},
                                   {'code': '>>> flavor_count.take(0).column("count").item(0) == 4\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> flavor_count.take(1).column("count").item(0) == flavor_count.take(2).column("count").item(0)\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
