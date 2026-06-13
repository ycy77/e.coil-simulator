---
entity_id: "protein.P0AFA2"
entity_type: "protein"
name: "narX"
source_database: "UniProt"
source_id: "P0AFA2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "narX narR b1222 JW1213"
---

# narX

`protein.P0AFA2`

## Static

- Type: `protein`
- Source: `UniProt:P0AFA2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: Acts as a sensor for nitrate/nitrite and transduces signal of nitrate availability to the NarL protein and of both nitrate/nitrite to the NarP protein. NarX probably activates NarL and NarP by phosphorylation in the presence of nitrate. NarX also plays a negative role in controlling NarL activity, probably through dephosphorylation in the absence of nitrate.

## Biological Role

Component of sensor histidine kinase NarX (complex.ecocyc.NARX-CPLX), NarX-N-phospho-L-histidine (complex.ecocyc.PHOSPHO-NARX).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Acts as a sensor for nitrate/nitrite and transduces signal of nitrate availability to the NarL protein and of both nitrate/nitrite to the NarP protein. NarX probably activates NarL and NarP by phosphorylation in the presence of nitrate. NarX also plays a negative role in controlling NarL activity, probably through dephosphorylation in the absence of nitrate.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.NARX-CPLX|complex.ecocyc.NARX-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PHOSPHO-NARX|complex.ecocyc.PHOSPHO-NARX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1222|gene.b1222]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AFA2`
- `KEGG:ecj:JW1213;eco:b1222;ecoc:C3026_07185;`
- `GeneID:75171335;75203337;945788;`
- `GO:GO:0000155; GO:0004721; GO:0005524; GO:0005886; GO:0006974; GO:0007165; GO:0030288; GO:0042128; GO:0042803; GO:0071249; GO:0071250`
- `EC:2.7.13.3`

## Notes

Nitrate/nitrite sensor protein NarX (EC 2.7.13.3)
