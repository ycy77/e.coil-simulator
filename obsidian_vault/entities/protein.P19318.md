---
entity_id: "protein.P19318"
entity_type: "protein"
name: "narY"
source_database: "UniProt"
source_id: "P19318"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "narY b1467 JW1462"
---

# narY

`protein.P19318`

## Static

- Type: `protein`
- Source: `UniProt:P19318`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein.

## Enriched Summary

FUNCTION: This is a second nitrate reductase enzyme which can substitute for the NRA enzyme and allows E.coli to use nitrate as an electron acceptor during anaerobic growth. The beta chain is an electron transfer unit containing four cysteine clusters involved in the formation of iron-sulfur centers. Electrons are transferred from the gamma chain to the molybdenum cofactor of the alpha subunit. narY encodes the β subunit of nitrate reductase Z; sequence analysis shows it has 75% identity with narH (which encodes the β subunit of nitrate reductase A); it is predicted to contain the iron-sulfur clusters (see also ) - one [3Fe-4S] cluster (FS4) and three [4Fe-4S] clusters (FS1, FS2 and FS3).

## Biological Role

Component of nitrate reductase Z (complex.ecocyc.NITRATREDUCTZ-CPLX).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: This is a second nitrate reductase enzyme which can substitute for the NRA enzyme and allows E.coli to use nitrate as an electron acceptor during anaerobic growth. The beta chain is an electron transfer unit containing four cysteine clusters involved in the formation of iron-sulfur centers. Electrons are transferred from the gamma chain to the molybdenum cofactor of the alpha subunit.

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.NITRATREDUCTZ-CPLX|complex.ecocyc.NITRATREDUCTZ-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1467|gene.b1467]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P19318`
- `KEGG:ecj:JW1462;eco:b1467;ecoc:C3026_08515;`
- `GeneID:946034;`
- `GO:GO:0005886; GO:0006974; GO:0008940; GO:0009055; GO:0009061; GO:0009325; GO:0016020; GO:0019645; GO:0042126; GO:0042128; GO:0046872; GO:0051536; GO:0051538; GO:0051539; GO:0160182`
- `EC:1.7.5.1`

## Notes

Respiratory nitrate reductase 2 beta chain (EC 1.7.5.1)
