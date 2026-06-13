---
entity_id: "protein.P08401"
entity_type: "protein"
name: "creC"
source_database: "UniProt"
source_id: "P08401"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "creC phoM b4399 JW4362"
---

# creC

`protein.P08401`

## Static

- Type: `protein`
- Source: `UniProt:P08401`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system CreC/CreB involved in catabolic regulation. CreC may function as a membrane-associated protein kinase that phosphorylates CreB in response to environmental signals. CreC can also phosphorylate PhoB. {ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:2228961}.

## Biological Role

Component of sensor histidine kinase CreC (complex.ecocyc.CREC-CPLX), CreC-N-phospho-L-histidine (complex.ecocyc.PHOSPHO-CREC).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system CreC/CreB involved in catabolic regulation. CreC may function as a membrane-associated protein kinase that phosphorylates CreB in response to environmental signals. CreC can also phosphorylate PhoB. {ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:2228961}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CREC-CPLX|complex.ecocyc.CREC-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PHOSPHO-CREC|complex.ecocyc.PHOSPHO-CREC]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4399|gene.b4399]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08401`
- `KEGG:ecj:JW4362;eco:b4399;`
- `GeneID:948609;`
- `GO:GO:0000155; GO:0005524; GO:0005886; GO:0019660`
- `EC:2.7.13.3`

## Notes

Sensor protein CreC (EC 2.7.13.3)
