---
entity_id: "protein.P32672"
entity_type: "protein"
name: "frwC"
source_database: "UniProt"
source_id: "P32672"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "frwC yijJ b3949 JW3921"
---

# frwC

`protein.P32672`

## Static

- Type: `protein`
- Source: `UniProt:P32672`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255|PROSITE-ProRule:PRU00427, ECO:0000269|PubMed:15919996}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. {ECO:0000250}. Sequence analysis indicates that frwC encodes a hydrophobic protein containing 6 - 9 transmembrane regions. The frwC encoded protein shows similarity to the IIC domains of the PTS Enzymes II specific for fructose .

## Biological Role

Component of putative PTS enzyme II FrwCBDPtsA (complex.ecocyc.CPLX-160).

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (PTS), a major carbohydrate active -transport system, catalyzes the phosphorylation of incoming sugar substrates concomitant with their translocation across the cell membrane. {ECO:0000250}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-160|complex.ecocyc.CPLX-160]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3949|gene.b3949]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32672`
- `KEGG:ecj:JW3921;eco:b3949;`
- `GeneID:948448;`
- `GO:GO:0005351; GO:0005886; GO:0008982; GO:0009401; GO:0090563; GO:1902495; GO:1990539`

## Notes

Fructose-like permease IIC component 2 (PTS system fructose-like EIIC component 2)
