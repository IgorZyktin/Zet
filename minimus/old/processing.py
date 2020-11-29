# -*- coding: utf-8 -*-

"""Основной рабочий код приложения.
"""
from collections import defaultdict
from typing import List, Dict

import minimus.utils.text_processing
from minimus.old.abstract import AbstractDocument
from minimus.old.config import Config
from minimus.old.documents_html import (
    HypertextMetaDocument, HypertextIndexDocument,
)
from minimus.old.documents_markdown import (
    MarkdownMetaDocument, MarkdownIndexDocument,
)
from minimus.old.file_system import FileSystem
from minimus.old.markdown_parser import MarkdownParser
from minimus.old.syntax import Syntax
from minimus.old.text_file import TextFile





def ensure_each_tag_has_metafile(config: Config,
                                 tags_to_files: Dict[str, List[TextFile]],
                                 ) -> None:
    """Удостовериться, что для каждого тега есть персональная страничка.

    Вместо проверки правильности, она просто каждый раз создаётся заново.
    """
    total = len(tags_to_files) * 2
    prefix = minimus.utils.text_processing.make_prefix(total)

    i = 1
    for tag, tag_files in tags_to_files.items():
        # markdown форма
        create_meta_md(config, tag, tag_files, prefix, i, total)
        i += 1

        # html форма
        if config.render_html:
            create_meta_html(config, tag, tag_files, prefix, i, total)
            i += 1


def create_meta_md(config: Config, tag: str, files: List[TextFile],
                   prefix: str, num: int, total: int) -> None:
    """Создать markdown метадокумент.
    """
    document = MarkdownMetaDocument(tag, files)
    create_meta(config, document, prefix, num, total)


def create_meta_html(config: Config, tag: str, files: List[TextFile],
                     prefix: str, num: int, total: int) -> None:
    """Создать html метадокумент.
    """
    document = HypertextMetaDocument(config, tag, files)
    create_meta(config, document, prefix, num, total)


def create_meta(config: Config, document: AbstractDocument,
                prefix: str, num: int, total: int) -> None:
    """Создать метадокумент.
    """
    filename = config.target_directory / document.corresponding_filename
    FileSystem.write(filename, document.content)

    number = prefix.format(num=num, total=total)
    Syntax.stdout('\t{number}. File created: {filename}',
                  number=number, filename=filename.absolute())


def ensure_each_tag_has_link(files: List['TextFile']) -> None:
    """Удостовериться, что каждый тег является ссылкой, а не текстом.
    """
    update_required = []

    for file in files:
        existing_content = file.content
        new_content = MarkdownParser.replace_tags_with_hrefs(
            content=existing_content,
            tags=file.get_tags(),
            maker=MarkdownMetaDocument,
        )

        if new_content != existing_content:
            file.content = new_content
            update_required.append(file)

    for number, file in minimus.utils.text_processing.numerate(update_required):
        Syntax.stdout('\t{number}. File has been updated: {filename}',
                      number=number, filename=file.filename)


def ensure_index_exists(config: Config, files: List[TextFile]) -> None:
    """Удостовериться, что у нас есть стартовая страница.
    """
    if not files:
        return

    def make_index(some_index):
        filename = config.target_directory / some_index.corresponding_filename
        if FileSystem.write(filename, some_index.content):
            Syntax.stdout('\tNew file has been created: {filename}',
                          filename=filename.absolute())

    index = MarkdownIndexDocument('', files)
    make_index(index)

    if config.render_html:
        index = HypertextIndexDocument(config, '', files)
        make_index(index)
