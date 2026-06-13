---
entity_id: "protein.P0A9K7"
entity_type: "protein"
name: "phoU"
source_database: "UniProt"
source_id: "P0A9K7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:3536855}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "phoU nmpA b3724 JW3702"
---

# phoU

`protein.P0A9K7`

## Static

- Type: `protein`
- Source: `UniProt:P0A9K7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:3536855}.

## Enriched Summary

FUNCTION: Part of the phosphate (Pho) regulon, which plays a key role in phosphate homeostasis. Encoded together with proteins of the phosphate-specific transport (Pst) system in the polycistronic pstSCAB-phoU operon. PhoU is essential for the repression of the Pho regulon at high phosphate conditions. In this role, it may bind, possibly as a chaperone, to PhoR, PhoB or a PhoR-PhoB complex to promote dephosphorylation of phospho-PhoB, or inhibit formation of the PhoR-PhoB transitory complex. Is also part of complex networks important for bacterial virulence, tolerance to antibiotics and stress response. {ECO:0000269|PubMed:17420206, ECO:0000269|PubMed:6310121}.

## Biological Role

Component of phosphate signaling protein PhoU (complex.ecocyc.CPLX0-8113).

## Annotation

FUNCTION: Part of the phosphate (Pho) regulon, which plays a key role in phosphate homeostasis. Encoded together with proteins of the phosphate-specific transport (Pst) system in the polycistronic pstSCAB-phoU operon. PhoU is essential for the repression of the Pho regulon at high phosphate conditions. In this role, it may bind, possibly as a chaperone, to PhoR, PhoB or a PhoR-PhoB complex to promote dephosphorylation of phospho-PhoB, or inhibit formation of the PhoR-PhoB transitory complex. Is also part of complex networks important for bacterial virulence, tolerance to antibiotics and stress response. {ECO:0000269|PubMed:17420206, ECO:0000269|PubMed:6310121}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8113|complex.ecocyc.CPLX0-8113]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3724|gene.b3724]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9K7`
- `KEGG:ecj:JW3702;eco:b3724;ecoc:C3026_20185;`
- `GeneID:93778211;948233;`
- `GO:GO:0000287; GO:0001558; GO:0005737; GO:0006817; GO:0009267; GO:0010629; GO:0016036; GO:0030145; GO:0030643; GO:0034605; GO:0042803; GO:0045936; GO:0071236; GO:0071467; GO:2000186`

## Notes

Phosphate-specific transport system accessory protein PhoU (Pst system accessory protein PhoU) (Negative regulator of Pho regulon)
