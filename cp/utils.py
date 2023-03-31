from typing import List, Any, Callable

from thefuzz import fuzz
from thefuzz.utils import full_process


def fuzzy_search(query: str, choices: List[Any], score_cutoff: int = 70,
                 processor: Callable = full_process) -> List[Any]:
    return [x for x in choices if fuzz.token_set_ratio(query, processor(x)) > score_cutoff]


def title_processor(x: Any) -> Any:
    return x.titulo


def author_processor(x: Any) -> Any:
    return x.autor


def isbn_processor(x: Any) -> Any:
    return x.isbn
