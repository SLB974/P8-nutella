#coding: utf-8

categories = ["Fromages blancs", "Poissons", "Nouilles",
              "Pizzas", "Boissons", "Epicerie", "Fromages"]

criterias = {
    'search_simple': 1,
    'action': 'process',
    'tagtype_0': 'countries',
    'tag_contains_0': 'contains',
    'tag_0': 'france',
    'tagtype_1': 'categories',
    'tag_contains_1': 'contains',
    'tag_1': None,
    'tagtype_2': 'brands',
    'tag_contains_2': 'does_not_contain',
    'tag_2': '',
    'tagtype_3': 'nutrition_grade_fr',
    'tag_contains_3': 'does not contain',
    'tag_3': None,
    'tagtype_4': 'product_name',
    'tag_contains_5': 'does_not_contain',
    'tag_4': None,
    'tagtype_5': 'categories_lc',
    'tag_contains_5': 'contains',
    'tag_5': 'fr',
    'tagtype_6': 'labels_lc',
    'tag_contains_6': 'contains',
    'tag_6': 'fr',
    'page_size': 150,
    'json': 1
}

def is_category_fr(category):
    """function to reject non fr languages."""

    return all((not category.startswith(lg) for lg in ("en:", "es:", "pl:")))


def format_category(category):
    """function to remove fr from categories known as fr."""
    return category.replace('fr:', '')
