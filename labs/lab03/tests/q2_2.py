test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> type(imdb2019) == tables.Table
          True
          >>> imdb2019.num_rows == 250
          True
          >>> imdb2019.select('Votes', 'Rating', 'Title', 'Year', 'Decade').sort(0).take(range(5))
          Votes | Rating | Title                   | Year | Decade
          25174 | 8.1    | White Heat              | 1949 | 1940
          25322 | 8      | Ace in the Hole         | 1951 | 1950
          25517 | 8.1    | The Red Shoes           | 1948 | 1940
          26005 | 8.2    | Drishyam                | 2013 | 2010
          26218 | 8      | The Exterminating Angel | 1962 | 1960
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
