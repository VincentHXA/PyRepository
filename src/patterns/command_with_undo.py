
import os
from abc import ABCMeta, abstractmethod


verbose = True


class FileOps(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass


class RenameFile(FileOps):
    def __init__(self, path_src, path_dest):
        self.src, self.dest = path_src, path_dest

    def execute(self):
        if verbose:
            print('[renaming {} to {}]'.format(self.src, self.dest))
        os.rename(self.src, self.dest)

    def undo(self):
        if verbose:
            print('[renameing {} back to {}]'.format(self.dest, self.src))
        os.rename(self.dest, self.src)


class CreateFile(FileOps):
    def __init__(self, path, txt='hello world\n'):
        self.path = path
        self.txt = txt

    def execute(self):
        if verbose:
            print('[creating file {}]'.format(self.path))
        with open(self.path, mode='w', encoding='utf-8') as out_file:
            out_file.write(self.txt)
            out_file.flush()

    def undo(self):
        delete_file(self.path)


class ReadFile(FileOps):
    def __init__(self, path):
        self.path = path

    def execute(self):
        if verbose:
            print('[reading file {}]'.format(self.path))
        with open(self.path, mode='r', encoding='utf-8') as in_file:
            print(in_file.read())

    def undo(self):
        raise AttributeError('Unsupported operation')


def delete_file(path):
    if verbose:
        print('deleting file {}'.format(path))
    os.remove(path)


def demo():
    origin_path, dest_path = 'file1', 'file2'

    commands = []

    for cmd in CreateFile(origin_path), ReadFile(origin_path), RenameFile(origin_path, dest_path):
        commands.append(cmd)

    [cmd.execute() for cmd in commands]

    for cmd in reversed(commands):
        try:
            cmd.undo()
        except AttributeError as ae:
            print(ae)








