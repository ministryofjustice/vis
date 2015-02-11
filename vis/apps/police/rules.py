from __future__ import absolute_import

import rules


@rules.predicate
def is_pcc_author(user, pcc=None):
    return not pcc or pcc.author == user


@rules.predicate
def is_superuser(user):
    return user.is_superuser


rules.add_rule('can_edit_pcc', is_pcc_author)

rules.add_perm('police', rules.always_allow)
rules.add_perm('police.change_pcc', is_pcc_author)
rules.add_perm('police.add_pcc', is_superuser)
rules.add_perm('police.delete_pcc', is_superuser)
