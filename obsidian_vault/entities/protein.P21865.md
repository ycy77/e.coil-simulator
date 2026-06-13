---
entity_id: "protein.P21865"
entity_type: "protein"
name: "kdpD"
source_database: "UniProt"
source_id: "P21865"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:1532388}; Multi-pass membrane protein {ECO:0000269|PubMed:1532388}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kdpD b0695 JW0683"
---

# kdpD

`protein.P21865`

## Static

- Type: `protein`
- Source: `UniProt:P21865`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:1532388}; Multi-pass membrane protein {ECO:0000269|PubMed:1532388}.

## Enriched Summary

FUNCTION: Member of the two-component regulatory system KdpD/KdpE involved in the regulation of the kdp operon. KdpD may function as a membrane-associated protein kinase that phosphorylates KdpE in response to environmental signals. {ECO:0000269|PubMed:1532388}.

## Biological Role

Component of serine histidine kinase KdpD (complex.ecocyc.KDPD-CPLX), KdpD-N-phospho-L-histidine (complex.ecocyc.PHOSPHO-KDPD).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Member of the two-component regulatory system KdpD/KdpE involved in the regulation of the kdp operon. KdpD may function as a membrane-associated protein kinase that phosphorylates KdpE in response to environmental signals. {ECO:0000269|PubMed:1532388}.

## Pathways

- `eco02020` Two-component system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.KDPD-CPLX|complex.ecocyc.KDPD-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.PHOSPHO-KDPD|complex.ecocyc.PHOSPHO-KDPD]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0695|gene.b0695]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21865`
- `KEGG:ecj:JW0683;eco:b0695;ecoc:C3026_03470;`
- `GeneID:946744;`
- `GO:GO:0000155; GO:0005524; GO:0005829; GO:0005886; GO:0007165; GO:0030288; GO:0035865; GO:0042803; GO:0106310`
- `EC:2.7.13.3`

## Notes

Sensor protein KdpD (EC 2.7.13.3)
