#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import logging
import os
import sys

logger = logging.getLogger(__name__)   # module/class-scoped logger


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'coomberschats.settings')
    try:
        from django.core.management import execute_from_command_line
        execute_from_command_line(sys.argv)
    except Exception as exc:
        logger.exception(exc)


if __name__ == '__main__':
    main()
