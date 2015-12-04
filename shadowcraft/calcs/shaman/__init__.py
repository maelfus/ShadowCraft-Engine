import gettext
import __builtin__

__builtin__._ = gettext.gettext

from shadowcraft.calcs import DamageCalculator
from shadowcraft.core import exceptions

class ShamanDamageCalculator(DamageCalculator):
    # Functions of general use to shaman damage calculation go here. If a
    # calculation will reasonably used for multiple classes, it should go in
    # calcs.DamageCalculator instead. If its a specific intermediate
    # value useful to only your calculations, when you extend this you should
    # put the calculations in your object.

    default_ep_stats = ['agi', 'haste', 'crit', 'mastery', 'ap', 'multistrike', 'versatility'] #'readiness'
    melee_attacks = ['mh_autoattack_hits', 'oh_autoattack_hits', 'autoattack',
                     'mh_stormstrike', 'oh_stormstrike', 'lava_lash',
                     '']
    other_attacks = ['flame_shock', 'frost_shock']
    aoe_attacks = ['fire_nova']
    dot_ticks = ['flame_shock_ticks']
    ranged_attacks = ['shuriken_toss', 'throw']
    non_dot_attacks = melee_attacks + ranged_attacks + aoe_attacks
    all_attacks = melee_attacks + ranged_attacks + dot_ticks + aoe_attacks + other_attacks
