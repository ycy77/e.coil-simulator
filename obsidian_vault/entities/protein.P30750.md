---
entity_id: "protein.P30750"
entity_type: "protein"
name: "metN"
source_database: "UniProt"
source_id: "P30750"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01719, ECO:0000305}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01719, ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "metN abc b0199 JW0195"
---

# metN

`protein.P30750`

## Static

- Type: `protein`
- Source: `UniProt:P30750`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01719, ECO:0000305}; Peripheral membrane protein {ECO:0000255|HAMAP-Rule:MF_01719, ECO:0000305}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex MetNIQ involved in methionine import (PubMed:12169620, PubMed:12218041, PubMed:12819857, PubMed:18621668, PubMed:30352853). Responsible for energy coupling to the transport system (PubMed:18621668, PubMed:25678706). It has also been shown to be involved in formyl-L-methionine transport (PubMed:12819857). {ECO:0000269|PubMed:12169620, ECO:0000269|PubMed:12218041, ECO:0000269|PubMed:12819857, ECO:0000269|PubMed:18621668, ECO:0000269|PubMed:25678706, ECO:0000269|PubMed:30352853}. MetN is the ATP-binding component of a high affinity methionine ABC transporter. MetN contains a conserved nucleotide binding domain (NBD) linked to a C-terminal C2-domain; the C-2 domain binds selenomethionine and is implicated in the allosteric regulation of transporter activity; methionine binding to the C2-domain stabilizes an ATPase inactive conformation of the transporter . Overexpression of metN from an ASKA plasmid leads to a more than 3-fold increase in the MIC of hydrogen peroxide . abc: ATP-binding cassette

## Biological Role

Component of L-methionine/D-methionine ABC transporter (complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex MetNIQ involved in methionine import (PubMed:12169620, PubMed:12218041, PubMed:12819857, PubMed:18621668, PubMed:30352853). Responsible for energy coupling to the transport system (PubMed:18621668, PubMed:25678706). It has also been shown to be involved in formyl-L-methionine transport (PubMed:12819857). {ECO:0000269|PubMed:12169620, ECO:0000269|PubMed:12218041, ECO:0000269|PubMed:12819857, ECO:0000269|PubMed:18621668, ECO:0000269|PubMed:25678706, ECO:0000269|PubMed:30352853}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX|complex.ecocyc.METNIQ-METHIONINE-ABC-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0199|gene.b0199]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P30750`
- `KEGG:ecj:JW0195;eco:b0199;ecoc:C3026_00925;`
- `GeneID:944896;`
- `GO:GO:0005524; GO:0005886; GO:0009276; GO:0015191; GO:0016020; GO:0016887; GO:0033232; GO:0042626; GO:0048473; GO:0055052; GO:1903692; GO:1990197`
- `EC:7.4.2.11`

## Notes

Methionine import ATP-binding protein MetN (EC 7.4.2.11)
