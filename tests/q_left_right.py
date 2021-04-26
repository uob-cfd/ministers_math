test = {
  'name': 'Question left_right',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'left' and 'right'
          >>> 'left' in vars()
          True
          >>> 'right' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'left'
          >>> # from its initial state (of ...)
          >>> left is not ...
          True
          >>> # You haven't changed the value for 'right'
          >>> # from its initial state (of ...)
          >>> right is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 54.4 < left < 54.9
          True
          >>> 62.6 < right < 63
          True
          """,
          'hidden': False,
          'locked': False
        },
      ],
      'scored': True,
      'setup': '',
      'teardown': '',
      'type': 'doctest'
    }
  ]
}
