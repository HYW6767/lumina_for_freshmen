import torch
import re
import unicodedata

class ExampleTokenizer:
    def __init__(self, vocab_file_path, do_lower_case=True,
                 strip_accents=None, max_input_chars_per_word=100):
        """
        Tokenizer 的构造函数

        :param vocab_file_path:
            词表文件路径

        :param do_lower_case: bool
            是否将输入文本中的大写字母转换为小写

        :param strip_accents: bool or None
            是否去除字符的重音符号

        :param max_input_chars_per_word: int
            单个 Basic Token 允许进行 WordPiece 切分的最大字符数

        📋📋📋📋
        请实现该类的构造函数：
        保存必要的配置参数；
        读取并解析词表文件；
        建立 token 与 token ID 之间的映射关系；
        初始化 Tokenizer 所需的特殊 token 信息。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer.__init__ 未实现")

    def __len__(self):
        return self.vocab_size

    def _clean_text(self, text):
        """
        清洗输入文本

        :param text: str
            原始输入文本

        :return: clean_text: str
            清洗后的文本

        📋📋📋📋
        请实现文本清洗方法：
        对输入文本进行必要的字符级预处理，
        并返回处理后的字符串。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer._clean_text 未实现")

    def _is_chinese_char(self, char):
        """
        判断单个字符是否属于中文字符

        :param char: str
            长度为 1 的单个字符

        :return: is_chinese: bool
            是否属于中文字符

        📋📋📋📋
        请实现中文字符判断方法，
        根据输入字符判断其是否属于规定的中文字符范围。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer._is_chinese_char 未实现")

    def _is_chinese_token(self, token):
        """
        判断 Token 是否属于中文字符 Token

        :param token: str
            待判断的 Token

        :return: is_chinese_token: bool
            是否属于中文字符 Token

        📋📋📋📋
        请实现该方法：
        根据输入 Token 判断其是否属于中文字符 Token。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer._is_chinese_token 未实现")

    def _is_punctuation_token(self, token):
        """
        判断 Token 是否属于标点符号 Token

        :param token: str
            待判断的 Token

        :return: is_punctuation_token: bool
            是否属于标点符号 Token

        📋📋📋📋
        请实现该方法：
        根据输入 Token 判断其是否属于标点符号 Token。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer._is_punctuation_token 未实现")

    def _add_spaces_around_chinese_chars(self, text):
        """
        对中文字符进行文本预处理

        :param text: str
            原始输入文本

        :return: processed_text: str
            处理后的文本

        📋📋📋📋
        请实现中文字符相关的文本预处理方法，
        返回处理后的字符串。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer._add_spaces_around_chinese_chars 未实现")

    def _whitespace_tokenize(self, text):
        """
        按空白字符进行 Token 切分

        :param text: str
            待处理的文本

        :return: token_list: list[str]
            根据空白字符切分得到的 Token 列表

        📋📋📋📋
        请实现空白 Token 切分方法，
        将输入文本转换为 Token 列表。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer._whitespace_tokenize 未实现")

    def _strip_accents(self, token):
        """
        去除 Token 中的重音符号

        :param token: str
            待处理的 Token

        :return: clean_token: str
            处理后的 Token

        📋📋📋📋
        请实现重音符号处理方法，
        返回处理后的 Token。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer._strip_accents 未实现")

    def _is_punctuation(self, char):
        """
        判断单个字符是否为标点符号

        :param char: str
            长度为 1 的单个字符

        :return: is_punctuation: bool
            是否为标点符号

        📋📋📋📋
        请实现标点符号判断方法，
        根据输入字符判断其是否属于标点符号。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer._is_punctuation 未实现")

    def _split_on_punctuation(self, token):
        """
        按标点符号对 Token 进行切分

        :param token: str
            待处理的 Token

        :return: final_tokens: list[str]
            切分后的 Token 列表

        📋📋📋📋
        请实现标点符号切分方法，
        将输入 Token 处理为最终的 Token 列表。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer._split_on_punctuation 未实现")

    def _basic_tokenize(self, text):
        """
        Basic Tokenizer 的文本切分方法

        :param text: str
            原始输入文本

        :return: token_list: list[str]
            基础 Token 切分后的 Token 列表

        📋📋📋📋
        请实现 Basic Tokenizer：
        将输入文本处理为后续 WordPiece Tokenizer 可以使用的 Token 列表。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer._basic_tokenize 未实现")

    def _wordpiece_tokenize(self, token):
        """
        WordPiece Tokenizer 的单 Token 切分方法

        :param token: str
            待进行 WordPiece 切分的单个 Token

        :return: sub_tokens: list[str]
            WordPiece 切分后的子 Token 列表

        📋📋📋📋
        请实现 WordPiece Token 切分方法：
        根据当前词表，将输入 Token 转换为对应的子 Token 列表。
        对无法处理的 Token 返回符合 Tokenizer 约定的结果。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer._wordpiece_tokenize 未实现")

    def tokenize(self, text, preserve_special_tokens=False):
        """
        Tokenizer 主方法

        :param text: str
            待处理的原始文本

        :param preserve_special_tokens: bool
            是否保留输入文本中的特殊 Token

        :return: final_token_list: list[str]
            Tokenizer 最终生成的 Token 列表

        📋📋📋📋
        请实现 Tokenizer 主方法：
        将输入文本转换为最终的 Token 列表，
        并根据 preserve_special_tokens 的设置处理特殊 Token。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer.tokenize 未实现")

    def convert_tokens_to_ids(self, tokens):
        """
        将 Token 转换为 Token ID

        :param tokens: list[str]
            Token 列表

        :return: ids_list: list[int]
            与输入 Token 一一对应的 Token ID 列表

        📋📋📋📋
        请实现 Token 到 Token ID 的转换方法，
        返回与输入 Token 顺序一致的 ID 列表。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer.convert_tokens_to_ids 未实现")

    def convert_ids_to_tokens(self, ids_list):
        """
        将 Token ID 转换为 Token

        :param ids_list: list[int]
            Token ID 列表

        :return: tokens_list: list[str]
            与输入 ID 一一对应的 Token 列表

        📋📋📋📋
        请实现 Token ID 到 Token 的转换方法，
        返回与输入 ID 顺序一致的 Token 列表。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer.convert_ids_to_tokens 未实现")

    def encode(
            self,
            text,
            add_special_tokens=True,
            truncation=False,
            padding=False,
            preserve_special_tokens=False,
            text_pair=None,
            max_length=None
    ):
        """
        将文本编码为模型输入格式

        :param text: str
            第一段输入文本

        :param add_special_tokens: bool
            是否添加模型所需的特殊 Token

        :param truncation: bool
            是否对超过指定长度的输入进行截断

        :param padding: bool
            是否将输入填充到指定长度

        :param preserve_special_tokens: bool
            是否保留输入文本中的特殊 Token

        :param text_pair: str or None
            第二段输入文本。
            用于需要同时处理两段文本的场景

        :param max_length: int or None
            输入序列允许的最大长度

        :return: encoded_dict: dict
            编码后的模型输入信息：
            {
                "input_ids": list[int],
                "token_type_ids": list[int],
                "attention_mask": list[int]
            }

        📋📋📋📋
        请实现文本编码方法：
        根据输入参数将文本转换为模型可以直接使用的编码结果，
        并将相关信息组织成字典返回。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer.encode 未实现")

    def decode(self, tokens, skip_special_tokens=True):
        """
        将 Token 列表还原为文本

        :param tokens: list[str]
            待还原的 Token 列表

        :param skip_special_tokens: bool
            是否跳过特殊 Token

        :return: result: str
            根据 Token 列表还原得到的文本

        📋📋📋📋
        请实现 Token 解码方法：
        将输入的 Token 列表转换为可读的文本字符串。

        请在下方完成你的实现
        """
        raise NotImplementedError("ExampleTokenizer.decode 未实现")

class QATokenizer(ExampleTokenizer):

    def _clean_text_with_offsets(self, text):
        """
        清洗文本并生成字符级位置信息

        :param text: str
            原始输入文本

        :return:
            clean_text: str
                清洗后的文本

            char_offsets: list[tuple[int, int]]
                与处理后文本字符对应的原始文本位置

        📋📋📋📋
        请实现带位置信息的文本清洗方法：
        在完成文本清洗的同时，
        保留处理后文本与原始文本之间的位置对应关系。

        请在下方完成你的实现
        """
        raise NotImplementedError("QATokenizer._clean_text_with_offsets 未实现")

    def _add_spaces_around_chinese_chars_with_offsets(
            self, text, char_offsets
    ):
        """
        中文字符处理及位置信息同步

        :param text: str
            待处理的文本

        :param char_offsets: list[tuple[int, int]]
            与文本字符对应的原始文本位置

        :return:
            processed_text: str
                处理后的文本

            processed_char_offsets: list[tuple[int, int]]
                与处理后文本保持对应的位置列表

        📋📋📋📋
        请实现中文字符处理方法，
        同时维护文本与位置信息之间的对应关系。

        请在下方完成你的实现
        """
        raise NotImplementedError("QATokenizer._add_spaces_around_chinese_chars_with_offsets 未实现")

    def _whitespace_tokenize_with_offsets(self, text, char_offsets):
        """
        带位置信息的空白 Token 切分

        :param text: str
            待切分的文本

        :param char_offsets: list[tuple[int, int]]
            与文本字符对应的位置列表

        :return:
            token_list: list[str]
                切分后的 Token 列表

            token_offsets: list[list[tuple[int, int]]]
                每个 Token 对应的字符级位置信息

        📋📋📋📋
        请实现带位置信息的空白切分方法：
        在生成 Token 的同时，
        保持 Token 与原始文本位置之间的对应关系。

        请在下方完成你的实现
        """
        raise NotImplementedError("QATokenizer._whitespace_tokenize_with_offsets 未实现")

    def _split_on_punctuation_with_offsets(self, token, char_offsets):
        """
        带位置信息的标点切分

        :param token: str
            待处理的 Token

        :param char_offsets: list[tuple[int, int]]
            Token 中各字符对应的位置

        :return:
            final_tokens: list[str]
                切分后的 Token 列表

            final_offsets: list[list[tuple[int, int]]]
                与 Token 列表对应的字符级位置信息

        📋📋📋📋
        请实现带位置信息的标点切分方法：
        在完成 Token 切分的同时，
        保持 Token 与位置信息之间的对应关系。

        请在下方完成你的实现
        """
        raise NotImplementedError("QATokenizer._split_on_punctuation_with_offsets 未实现")

    def _basic_tokenize_with_offsets(self, text):
        """
        带位置信息的基础 Token 切分

        :param text: str
            原始输入文本

        :return:
            final_token_list: list[str]
                基础 Token 切分后的 Token 列表

            final_token_offsets: list[list[tuple[int, int]]]
                与 Token 列表对应的字符级位置信息

        📋📋📋📋
        请实现带位置信息的 Basic Tokenizer，
        在完成基础 Token 切分的同时维护对应的位置关系。

        请在下方完成你的实现
        """
        raise NotImplementedError("QATokenizer._basic_tokenize_with_offsets 未实现")

    def _wordpiece_tokenize_with_offsets(self, token, char_offsets):
        """
        带位置信息的 WordPiece Token 切分

        :param token: str
            待进行 WordPiece 切分的 Token

        :param char_offsets: list[tuple[int, int]]
            Token 中各字符对应的原始文本位置

        :return:
            sub_tokens: list[str]
                WordPiece 切分后的子 Token 列表

            sub_tokens_offsets: list[list[tuple[int, int]]]
                与子 Token 一一对应的字符级位置信息

        📋📋📋📋
        请实现带位置信息的 WordPiece Token 切分方法：
        在完成 WordPiece 切分的同时，
        保持每个子 Token 与原始文本位置之间的对应关系。

        请在下方完成你的实现
        """
        raise NotImplementedError("QATokenizer._wordpiece_tokenize_with_offsets 未实现")

    def _tokenize_text_part_with_offsets(self, text):
        """
        对文本片段进行带位置信息的 Token 化

        :param text: str
            待处理的文本片段

        :return:
            final_token_list: list[str]
                Token 化后的 Token 列表

            merged_offsets: list[tuple[int, int]]
                与 Token 一一对应的 Token 级位置信息

        📋📋📋📋
        请实现文本片段的完整 Token 化过程，
        并返回 Token 及其对应的位置信息。

        请在下方完成你的实现
        """
        raise NotImplementedError("QATokenizer._tokenize_text_part_with_offsets 未实现")

    def tokenize_with_offsets(self, text, preserve_special_tokens=False):
        """
        Tokenize 主方法，同时返回 Token 的位置信息

        :param text: str
            原始输入文本

        :param preserve_special_tokens: bool
            是否保留输入文本中的特殊 Token

        :return:
            final_token_list: list[str]
                Tokenizer 最终生成的 Token 列表

            merged_offsets: list[tuple[int, int]]
                与 Token 一一对应的原始文本字符位置

        📋📋📋📋
        请实现带位置信息的 Tokenizer 主方法：
        将输入文本转换为 Token 列表，
        并同时返回每个 Token 对应的原始文本位置。

        请在下方完成你的实现
        """
        raise NotImplementedError("QATokenizer.tokenize_with_offsets 未实现")

    def _merge_char_offsets(self, char_offsets):
        """
        将字符级位置信息转换为 Token 级位置信息

        :param char_offsets: list[tuple[int, int]]
            同一个 Token 中各字符对应的原始文本位置

        :return: token_offset: tuple[int, int]
            当前 Token 在原始文本中的起止位置

        📋📋📋📋
        请实现字符级位置信息的合并方法，
        将输入的位置列表转换为一个 Token 级位置范围。

        请在下方完成你的实现
        """
        raise NotImplementedError("QATokenizer._merge_char_offsets 未实现")

    def encode_with_offsets(
            self,
            text,
            add_special_tokens=True,
            truncation=False,
            padding=False,
            preserve_special_tokens=False,
            text_pair=None,
            max_length=None,
            stride=None,
            return_overflowing=False
    ):
        """
        将文本编码为模型输入格式，并保留 Token 位置信息

        :param text: str
            第一段输入文本

        :param add_special_tokens: bool
            是否添加模型所需的特殊 Token

        :param truncation: bool
            是否对超过指定长度的输入进行截断

        :param padding: bool
            是否将输入填充到指定长度

        :param preserve_special_tokens: bool
            是否保留输入文本中的特殊 Token

        :param text_pair: str or None
            第二段输入文本

        :param max_length: int or None
            输入序列允许的最大长度

        :param stride: int or None
            相邻文本窗口之间的重叠长度

        :param return_overflowing: bool
            是否返回超出单个序列长度限制后的多个编码结果

        :return: encoded_dict: dict
            编码后的模型输入信息。

            普通模式下包含：
            {
                "input_ids": list[int],
                "token_type_ids": list[int],
                "attention_mask": list[int],
                "offset_mapping": list[tuple[int, int]]
            }

            当需要返回多个编码结果时，
            还应包含与各窗口相关的结果信息。

        📋📋📋📋
        请实现带位置信息的文本编码方法：

        根据输入参数完成文本编码；
        保持 Token 与原始文本位置之间的对应关系；
        支持单文本和文本对输入；
        支持截断与 Padding；
        根据参数决定是否返回多个编码结果；
        将最终结果组织成字典返回。

        请在下方完成你的实现
        """
        raise NotImplementedError("QATokenizer.encode_with_offsets 未实现")
