---
entity_id: "molecule.C03912"
entity_type: "small_molecule"
name: "(S)-1-Pyrroline-5-carboxylate"
source_database: "KEGG"
source_id: "C03912"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "(S)-1-Pyrroline-5-carboxylate"
  - "L-1-Pyrroline-5-carboxylate"
  - "1-Pyrroline-5-carboxylate"
---

# (S)-1-Pyrroline-5-carboxylate

`molecule.C03912`

## Static

- Type: `small_molecule`
- Source: `KEGG:C03912`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: (S)-1-Pyrroline-5-carboxylate; L-1-Pyrroline-5-carboxylate; 1-Pyrroline-5-carboxylate L-DELTA1-PYRROLINE_5-CARBOXYLATE is an enamine that forms on spontaneous dehydration of L-GLUTAMATE_GAMMA-SEMIALDEHYDE in aqueous solutions. It can be converted to or be formed from the three amino acids GLT (EC-1.2.1.88), L-ORNITHINE (EC-2.6.1.13) and PRO (EC-1.5.5.2 and EC-1.5.1.2). It is also one of the few metabolites that can be a precursor to other metabolites of both the PWY-4984 and the TCA.

## Biological Role

Consumed as substrate in 5 reaction(s). Produced in 2 reaction(s).

## Enriched Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)

## Annotation

KEGG compound: (S)-1-Pyrroline-5-carboxylate; L-1-Pyrroline-5-carboxylate; 1-Pyrroline-5-carboxylate

## Pathways

- `eco00250` Alanine, aspartate and glutamate metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00332` Carbapenem biosynthesis (KEGG)

## Outgoing Edges (7)

- `is_product_of` --> [[reaction.ecocyc.PYRROLINECARBREDUCT-RXN|reaction.ecocyc.PYRROLINECARBREDUCT-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-7008|reaction.ecocyc.RXN0-7008]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00707|reaction.R00707]] `KEGG` `database` - C03912 + C00003 + 2 C00001 <=> C00025 + C00004 + C00080
- `is_substrate_of` --> [[reaction.R00708|reaction.R00708]] `KEGG` `database` - C03912 + C00006 + 2 C00001 <=> C00025 + C00005 + C00080
- `is_substrate_of` --> [[reaction.ecocyc.PYRROLINECARBDEHYDROG-RXN|reaction.ecocyc.PYRROLINECARBDEHYDROG-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-7005|reaction.ecocyc.RXN0-7005]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.SPONTPRO-RXN|reaction.ecocyc.SPONTPRO-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C03912`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
