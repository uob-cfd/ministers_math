test = {
  'name': 'Question first_boot_sample',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # You need to set the value for 'first_boot_sample'
          >>> 'first_boot_sample' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You need to set the value for 'first_boot_mean'
          >>> 'first_boot_mean' in vars()
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'first_boot_sample'
          >>> # from its initial state (of ...)
          >>> first_boot_sample is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # You haven't changed the value for 'first_boot_mean'
          >>> # from its initial state (of ...)
          >>> first_boot_mean is not ...
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Sample should be same length as original.
          >>> len(first_boot_sample) == len(sample_marks)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # The boot sample values don't seem to come from the
          >>> # 2019 sample.
          >>> boot_set = set(first_boot_sample)
          >>> boot_set == boot_set.intersection(sample_marks)
          True
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> # Either you are extraordinarily unlucky, or you are
          >>> # not sampling with replacement.  Try running this
          >>> # test again, if you think you were unlucky.
          >>> np.all(np.array(first_boot_sample) == np.array(sample_marks))
          False
          >>> np.all(np.sort(first_boot_sample) == np.sort(sample_marks))
          False
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          >>> np.isclose(np.mean(first_boot_sample), first_boot_mean)
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
