from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Send spam'

    def add_arguments(self, parser):
        parser.add_argument('repeats', type=int)
        parser.add_argument('-w', '--words', default='spam')


    def handle(self, *args, **kwargs):
        repeats = kwargs['repeats']
        word = kwargs['words']
        print(word * repeats)