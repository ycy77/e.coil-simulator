---
entity_id: "protein.P37019"
entity_type: "protein"
name: "clcA"
source_database: "UniProt"
source_id: "P37019"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "clcA eriC yadQ b0155 JW5012"
---

# clcA

`protein.P37019`

## Static

- Type: `protein`
- Source: `UniProt:P37019`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Multi-pass membrane protein {ECO:0000305}.

## Enriched Summary

FUNCTION: Proton-coupled chloride transporter. Functions as antiport system and exchanges two chloride ions for 1 proton. Probably acts as an electrical shunt for an outwardly-directed proton pump that is linked to amino acid decarboxylation, as part of the extreme acid resistance (XAR) response. {ECO:0000269|PubMed:12384697, ECO:0000269|PubMed:14985752, ECO:0000269|PubMed:16341087, ECO:0000269|PubMed:16905147, ECO:0000269|PubMed:18678918}.

## Biological Role

Component of chloride:H+ antiporter ClcA (complex.ecocyc.CPLX0-7961).

## Annotation

FUNCTION: Proton-coupled chloride transporter. Functions as antiport system and exchanges two chloride ions for 1 proton. Probably acts as an electrical shunt for an outwardly-directed proton pump that is linked to amino acid decarboxylation, as part of the extreme acid resistance (XAR) response. {ECO:0000269|PubMed:12384697, ECO:0000269|PubMed:14985752, ECO:0000269|PubMed:16341087, ECO:0000269|PubMed:16905147, ECO:0000269|PubMed:18678918}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7961|complex.ecocyc.CPLX0-7961]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0155|gene.b0155]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37019`
- `KEGG:ecj:JW5012;eco:b0155;ecoc:C3026_00705;`
- `GeneID:93777272;946715;`
- `GO:GO:0005247; GO:0005886; GO:0042802; GO:0062158; GO:1902476; GO:1902600; GO:1990451`

## Notes

H(+)/Cl(-) exchange transporter ClcA (ClC-ec1)
