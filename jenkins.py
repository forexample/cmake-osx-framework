#!/usr/bin/env python3

import argparse
import glob
import os
import shutil
import subprocess
import sys

parser = argparse.ArgumentParser(description="Testing script")
parser.add_argument('--shared', action='store_true', help='Build shared libs')
parser.add_argument('--toolchain', help='Toolchain', default='default')
cmd_args = parser.parse_args()

def do_call(args):
  oneline = ''
  for i in args:
    oneline += ' "{}"'.format(i)
  print('[{}]>{}'.format(os.getcwd(), oneline))
  try:
    subprocess.check_call(args)
  except subprocess.CalledProcessError as error:
    print(error)
    print(error.output)
    sys.exit(1)

if os.path.exists('_builds'):
  shutil.rmtree('_builds')

if os.path.exists('_install'):
  shutil.rmtree('_install')

if os.path.exists('_framework'):
  shutil.rmtree('_framework')

do_call(['which', 'cmake'])

shared_opt = 'OFF'
if cmd_args.shared:
  shared_opt = 'ON'

do_call([
    'build.py',
    '--toolchain',
    cmd_args.toolchain,
    '--verbose',
    '--config' ,
    'Release',
    '--framework',
    '--home',
    'Foo',
    '--fwd',
    'BUILD_SHARED_LIBS={}'.format(shared_opt)
])

if os.path.exists('_builds'):
  shutil.rmtree('_builds')

if os.path.exists('_install'):
  shutil.rmtree('_install')

do_call([
    'build.py',
    '--toolchain',
    cmd_args.toolchain,
    '--verbose',
    '--config' ,
    'Release',
    '--test',
    '--home',
    'Boo'
])
