---
entity_id: "protein.P17952"
entity_type: "protein"
name: "murC"
source_database: "UniProt"
source_id: "P17952"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "murC b0091 JW0089"
---

# murC

`protein.P17952`

## Static

- Type: `protein`
- Source: `UniProt:P17952`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Cell wall formation. {ECO:0000269|PubMed:7601127}.

## Biological Role

Catalyzes UDP-N-acetylmuramate:L-alanine ligase (ADP-forming) (reaction.R03193). Component of UDP-N-acetylmuramate—L-alanine ligase (complex.ecocyc.CPLX0-8014).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Cell wall formation. {ECO:0000269|PubMed:7601127}.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03193|reaction.R03193]] `KEGG` `database` - via EC:6.3.2.8
- `is_component_of` --> [[complex.ecocyc.CPLX0-8014|complex.ecocyc.CPLX0-8014]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0091|gene.b0091]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P17952`
- `KEGG:ecj:JW0089;eco:b0091;ecoc:C3026_00360;`
- `GeneID:75202092;946153;`
- `GO:GO:0000287; GO:0005524; GO:0005737; GO:0008360; GO:0008763; GO:0009252; GO:0042803; GO:0051301; GO:0071555`
- `EC:6.3.2.8`

## Notes

UDP-N-acetylmuramate--L-alanine ligase (EC 6.3.2.8) (UDP-N-acetylmuramoyl-L-alanine synthetase)
