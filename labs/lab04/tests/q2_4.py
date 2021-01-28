test = {
  'name': '',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> concatenate_two_strings("Datascience ", "rules!") == "Datascience rules!"
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> concatenate_two_strings("", "") == ""
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
