---
entity_id: "molecule.C00079"
entity_type: "small_molecule"
name: "L-Phenylalanine"
source_database: "KEGG"
source_id: "C00079"
default_state: "low"
allowed_states: "absent|low|medium|high"
subcellular_location: ""
enriched_summary_quality: "placeholder"
tags:
  - entity/small_molecule
  - source/KEGG
aliases:
  - "L-Phenylalanine"
  - "(S)-alpha-Amino-beta-phenylpropionic acid"
---

# L-Phenylalanine

`molecule.C00079`

## Static

- Type: `small_molecule`
- Source: `KEGG:C00079`
- Default state: `low`
- Allowed states: `absent|low|medium|high`

## Enriched Summary

KEGG compound: L-Phenylalanine; (S)-alpha-Amino-beta-phenylpropionic acid

## Biological Role

Consumed as substrate in 10 reaction(s). Produced in 3 reaction(s).

## Enriched Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco02010` ABC transporters (KEGG)

## Annotation

KEGG compound: L-Phenylalanine; (S)-alpha-Amino-beta-phenylpropionic acid

## Pathways

- `eco00360` Phenylalanine metabolism (KEGG)
- `eco00400` Phenylalanine, tyrosine and tryptophan biosynthesis (KEGG)
- `eco00460` Cyanoamino acid metabolism (KEGG)
- `eco00470` D-Amino acid metabolism (KEGG)
- `eco00970` Aminoacyl-tRNA biosynthesis (KEGG)
- `eco00999` Biosynthesis of various plant secondary metabolites (KEGG)
- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (17)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-163|complex.ecocyc.MONOMER0-163]] `EcoCyc` `database` - EcoCyc component coefficient=
- `is_product_of` --> [[reaction.R00691|reaction.R00691]] `KEGG` `database` - C00826 <=> C00079 + C00001 + C00011
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-312|reaction.ecocyc.TRANS-RXN-312]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_product_of` --> [[reaction.ecocyc.TRANS-RXN-56|reaction.ecocyc.TRANS-RXN-56]] `EcoCyc` `database` - EcoCyc reaction RIGHT
- `is_substrate_of` --> [[reaction.R00693|reaction.R00693]] `KEGG` `database` - C00024 + C00079 <=> C00010 + C03519
- `is_substrate_of` --> [[reaction.R00694|reaction.R00694]] `KEGG` `database` - C00079 + C00026 <=> C00166 + C00025
- `is_substrate_of` --> [[reaction.R00698|reaction.R00698]] `KEGG` `database` - C00079 + C00007 <=> C02505 + C00011
- `is_substrate_of` --> [[reaction.R03660|reaction.R03660]] `KEGG` `database` - C00002 + C00079 + C01648 <=> C00020 + C00013 + C03511
- `is_substrate_of` --> [[reaction.ecocyc.PHENYLALANINE--TRNA-LIGASE-RXN|reaction.ecocyc.PHENYLALANINE--TRNA-LIGASE-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.R185-RXN|reaction.ecocyc.R185-RXN]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-10814|reaction.ecocyc.RXN-10814]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.RXN-23892|reaction.ecocyc.RXN-23892]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-312|reaction.ecocyc.TRANS-RXN-312]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `is_substrate_of` --> [[reaction.ecocyc.TRANS-RXN-56|reaction.ecocyc.TRANS-RXN-56]] `EcoCyc` `database` - EcoCyc reaction LEFT
- `represses` --> [[reaction.ecocyc.CHORISMATEMUT-RXN|reaction.ecocyc.CHORISMATEMUT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.DAHPSYN-RXN|reaction.ecocyc.DAHPSYN-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `represses` --> [[reaction.ecocyc.PREPHENATEDEHYDRAT-RXN|reaction.ecocyc.PREPHENATEDEHYDRAT-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (0)

_None._

## External IDs

- `KEGG:C00079`

## Notes

Included because it appears in at least one E. coli KEGG pathway.
