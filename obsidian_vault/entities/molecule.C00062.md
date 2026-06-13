---
entity_id: "molecule.C00062"
entity_type: "small_molecule"
name: "L-Arginine"
source_database: "KEGG"
source_id: "C00062"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Arginine"
  - "(S)-2-Amino-5-guanidinovaleric acid"
  - "L-Arg"
---

# L-Arginine

`molecule.C00062`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00062`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Arginine; (S)-2-Amino-5-guanidinovaleric acid; L-Arg

## Biological Role

Consumed as substrate in 12 reaction(s). Produced in 5 reaction(s).

## Enriched Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: L-Arginine; (S)-2-Amino-5-guanidinovaleric acid; L-Arg

## Pathways

- `eco00220` Arginine biosynthesis (KEGG)
- `eco00261` Monobactam biosynthesis (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (21)

- `is_component_of` --> [[complex.ecocyc.CPLX0-228|complex.ecocyc.CPLX0-228]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_component_of` --> [[complex.ecocyc.CPLX0-7671|complex.ecocyc.CPLX0-7671]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.ecocyc.ABC-4-RXN|reaction.ecocyc.ABC-4-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.ARGSUCCINLYA-RXN|reaction.ecocyc.ARGSUCCINLYA-RXN]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-2162|reaction.ecocyc.RXN0-2162]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN0-3261|reaction.ecocyc.RXN0-3261]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.RXN66-448|reaction.ecocyc.RXN66-448]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00566|reaction.R00566]] `KEGG` `database` - C00062 <=> C00179 + C00011
- `is_substrate_of` --> [[reaction.R00567|reaction.R00567]] `KEGG` `database` - C00062 <=> C00792
- `is_substrate_of` --> [[reaction.R00832|reaction.R00832]] `KEGG` `database` - C00091 + C00062 <=> C00010 + C03296
- `is_substrate_of` --> [[reaction.ecocyc.ABC-4-RXN|reaction.ecocyc.ABC-4-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ARGDECARBOX-RXN|reaction.ecocyc.ARGDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ARGININE--TRNA-LIGASE-RXN|reaction.ecocyc.ARGININE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.ARGININE-N-SUCCINYLTRANSFERASE-RXN|reaction.ecocyc.ARGININE-N-SUCCINYLTRANSFERASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-19498|reaction.ecocyc.RXN-19498]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-2162|reaction.ecocyc.RXN0-2162]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-272|reaction.ecocyc.RXN0-272]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN0-5345|reaction.ecocyc.RXN0-5345]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN66-448|reaction.ecocyc.RXN66-448]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.AGMATIN-RXN|reaction.ecocyc.AGMATIN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.N-ACETYLTRANSFER-RXN|reaction.ecocyc.N-ACETYLTRANSFER-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (2)

- `transports` <-- [[complex.ecocyc.ABC-4-CPLX|complex.ecocyc.ABC-4-CPLX]] `EcoCyc` `database` - EcoCyc transporters.col equation
- `transports` <-- [[complex.ecocyc.CPLX0-7535|complex.ecocyc.CPLX0-7535]] `EcoCyc` `database` - EcoCyc transporters.col equation

## External IDs

- `KEGG:C00062`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
