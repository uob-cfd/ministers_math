test = {
  'name': 'Question boot_means',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'boot_means'
          >>> 'boot_means' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'boot_means'
          >>> # from its initial state (of ...)
          >>> boot_means is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> len(boot_means)
          10000
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> mean_diff = np.mean(boot_means) - np.mean(sample_marks)
          >>> -0.11 < mean_diff < 0.11
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> 3.12 < np.std(boot_means) < 3.3
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
