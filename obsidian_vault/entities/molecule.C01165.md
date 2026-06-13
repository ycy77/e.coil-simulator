---
entity_id: "molecule.C01165"
entity_type: "small_molecule"
name: "L-Glutamate 5-semialdehyde"
source_database: "KEGG"
source_id: "C01165"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Glutamate 5-semialdehyde"
  - "L-Glutamate gamma-semialdehyde"
---

# L-Glutamate 5-semialdehyde

`molecule.C01165`

## Static

- Type: `small_molecule`
- Source: `KEGG:C01165`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Glutamate 5-semialdehyde; L-Glutamate gamma-semialdehyde L-GLUTAMATE_GAMMA-SEMIALDEHYDE forms on spontaneous hydration of L-DELTA1-PYRROLINE_5-CARBOXYLATE in aqueous solutions. It can be converted to or be formed from the three amino acids GLT (EC-1.2.1.88), L-ORNITHINE (EC-2.6.1.13) and PRO (EC-1.5.5.2 and EC-1.5.1.2). It is also one of the few metabolites that can be a precursor to other metabolites of both the PWY-4984 and the TCA.

## Biological Role

Consumed as substrate in 3 reaction(s). Produced in 1 reaction(s).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)

## Annotation

KEGG compound: L-Glutamate 5-semialdehyde; L-Glutamate gamma-semialdehyde

## Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)

## Outgoing Edges (6)

- `is_product_of` --> [[reaction.ecocyc.SPONTPRO-RXN|reaction.ecocyc.SPONTPRO-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00245|reaction.R00245]] `KEGG` `database` - C01165 + C00003 + C00001 <=> C00025 + C00004 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.GLUTSEMIALDEHYDROG-RXN|reaction.ecocyc.GLUTSEMIALDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-14116|reaction.ecocyc.RXN-14116]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.CTPSYN-RXN|reaction.ecocyc.CTPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-RXN|reaction.ecocyc.L-GLN-FRUCT-6-P-AMINOTRANS-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C01165`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
