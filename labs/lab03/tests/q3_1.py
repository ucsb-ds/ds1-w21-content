test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
         {
          'code': r"""
          >>> movie_title[1] != '' and movie_title[2] != ''
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # It looks like your movies are not 
          >>> # starting with your most favorite movie.
          >>> movie_ranking[0] >= movie_ranking[1]
          True
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
