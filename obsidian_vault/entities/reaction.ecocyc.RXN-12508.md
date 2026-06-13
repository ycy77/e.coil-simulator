---
entity_id: "reaction.ecocyc.RXN-12508"
entity_type: "reaction"
name: "2-(α-hydroxyethyl)-TPP:[dihydrolipoyllysine-residue acetyltransferase]-lipoyllysine acetyltransferase"
source_database: "EcoCyc"
source_id: "RXN-12508"
default_state: "active"
allowed_states: "active|blocked"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/reaction
  - source/EcoCyc
aliases:
---

# 2-(α-hydroxyethyl)-TPP:[dihydrolipoyllysine-residue acetyltransferase]-lipoyllysine acetyltransferase

`reaction.ecocyc.RXN-12508`

## Static

- Type: `reaction`
- Source: `EcoCyc:RXN-12508`
- Default state: `active`
- Allowed states: `active|blocked`

## Enriched Summary

2-ALPHA-HYDROXYETHYL-THPP + Pyruvate-dehydrogenase-lipoate -> Pyruvate-dehydrogenase-acetylDHlipoyl + THIAMINE-PYROPHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT EcoCyc reaction equation: 2-ALPHA-HYDROXYETHYL-THPP + Pyruvate-dehydrogenase-lipoate -> Pyruvate-dehydrogenase-acetylDHlipoyl + THIAMINE-PYROPHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT.

## Biological Role

Substrates: 2-(alpha-Hydroxyethyl)thiamine diphosphate (molecule.C05125), Enzyme N6-(lipoyl)lysine (molecule.C15972). Products: Thiamin diphosphate (molecule.C00068), [Dihydrolipoyllysine-residue acetyltransferase] S-acetyldihydrolipoyllysine (molecule.C16255).

## Annotation

2-ALPHA-HYDROXYETHYL-THPP + Pyruvate-dehydrogenase-lipoate -> Pyruvate-dehydrogenase-acetylDHlipoyl + THIAMINE-PYROPHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT

## Outgoing Edges (0)

_None._

## Incoming Edges (4)

- `is_product_of` <-- [[molecule.C00068|molecule.C00068]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` <-- [[molecule.C16255|molecule.C16255]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` <-- [[molecule.C05125|molecule.C05125]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` <-- [[molecule.C15972|molecule.C15972]] `EcoCyc` `database` - EcoCyc reaction LEFT

## External IDs

- `EcoCyc:RXN-12508`

## Notes

2-ALPHA-HYDROXYETHYL-THPP + Pyruvate-dehydrogenase-lipoate -> Pyruvate-dehydrogenase-acetylDHlipoyl + THIAMINE-PYROPHOSPHATE; direction=PHYSIOL-LEFT-TO-RIGHT
