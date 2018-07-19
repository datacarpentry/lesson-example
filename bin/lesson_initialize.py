ROOT_INDEX_MD = '''\
---
layout: lesson
---
FIXME: home page introduction

> ## Prerequisites
>
> FIXME
{: .prereq}
'''

ROOT_REFERENCE_MD = '''\
---
layout: reference
permalink: /reference/
---

## Glossary

FIXME
'''

ROOT_SETUP_MD = '''\
---
layout: page
title: Setup
permalink: /setup/
---
FIXME
'''

EPISODES_INTRODUCTION_MD = '''\
---
title: "Introduction"
teaching: 0
exercises: 0
questions:
- "Key question"
objectives:
- "First objective."
keypoints:
- "First key point."
---
'''

EXTRAS_ABOUT_MD = '''\
---
layout: page
title: About
permalink: /about/
---
{% include carpentries.html %}
'''

EXTRAS_DISCUSS_MD = '''\
---
layout: page
title: Discussion
permalink: /discuss/
---
FIXME
'''

EXTRAS_FIGURES_MD = '''\
---
layout: page
title: Figures
permalink: /figures/
---
{% include all_figures.html %}
'''

EXTRAS_GUIDE_MD = '''\
---
layout: page
title: "Instructors' Guide"
permalink: /guide/
redirect_to: https://carpentries.github.io/lesson-example
---
FIXME
'''

INCLUDES_ALL_FIGURES_HTML = '''\
<!-- empty -->
'''

BOILERPLATE = (
    ('AUTHORS', ROOT_AUTHORS),
    ('CITATION', ROOT_CITATION),
    ('CONTRIBUTING.md', ROOT_CONTRIBUTING_MD),
    ('_config.yml', ROOT_CONFIG_YML),
    ('index.md', ROOT_INDEX_MD),
    ('reference.md', ROOT_REFERENCE_MD),
    ('setup.md', ROOT_SETUP_MD),
    ('_episodes/01-introduction.md', EPISODES_INTRODUCTION_MD),
    ('_extras/about.md', EXTRAS_ABOUT_MD),
    ('_extras/discuss.md', EXTRAS_DISCUSS_MD),
    ('_extras/figures.md', EXTRAS_FIGURES_MD),
    ('_extras/guide.md', EXTRAS_GUIDE_MD),
    ('_includes/all_figures.html', INCLUDES_ALL_FIGURES_HTML)
)


def main():
    """Check for collisions, then create."""

    # Check.
    errors = False
    for (path, _) in BOILERPLATE:
        if os.path.exists(path):
            print('Warning: {0} already exists.'.format(path), file=sys.stderr)
            errors = True
    if errors:
        print('**Exiting without creating files.**', file=sys.stderr)
        sys.exit(1)

    # Create.
    for (path, content) in BOILERPLATE:
        with open(path, 'w') as writer:
            writer.write(content)


if __name__ == '__main__':
    main()
