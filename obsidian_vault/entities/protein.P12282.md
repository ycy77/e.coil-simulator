---
entity_id: "protein.P12282"
entity_type: "protein"
name: "moeB"
source_database: "UniProt"
source_id: "P12282"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "moeB chlN b0826 JW0810"
---

# moeB

`protein.P12282`

## Static

- Type: `protein`
- Source: `UniProt:P12282`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the adenylation by ATP of the carboxyl group of the C-terminal glycine of sulfur carrier protein MoaD. {ECO:0000269|PubMed:11290749, ECO:0000269|PubMed:11463785}.

## Biological Role

Component of molybdopterin synthase adenylyltransferase/sulfur transferase (complex.ecocyc.CPLX0-12611), molybdopterin synthase adenylyltransferase (complex.ecocyc.CPLX0-8164).

## Enriched Pathways

- `eco04122` Sulfur relay system (KEGG)

## Annotation

FUNCTION: Catalyzes the adenylation by ATP of the carboxyl group of the C-terminal glycine of sulfur carrier protein MoaD. {ECO:0000269|PubMed:11290749, ECO:0000269|PubMed:11463785}.

## Pathways

- `eco04122` Sulfur relay system (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-12611|complex.ecocyc.CPLX0-12611]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-8164|complex.ecocyc.CPLX0-8164]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0826|gene.b0826]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P12282`
- `KEGG:ecj:JW0810;eco:b0826;ecoc:C3026_05185;`
- `GeneID:945452;`
- `GO:GO:0004792; GO:0005524; GO:0005737; GO:0005829; GO:0006777; GO:0008146; GO:0008641; GO:0016779; GO:0042803; GO:0046872; GO:0061605; GO:1990133`
- `EC:2.7.7.80`

## Notes

Molybdopterin-synthase adenylyltransferase (EC 2.7.7.80) (MoaD protein adenylase) (Molybdopterin-converting factor subunit 1 adenylase) (Sulfur carrier protein MoaD adenylyltransferase)
