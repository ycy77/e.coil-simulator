---
entity_id: "protein.P55734"
entity_type: "protein"
name: "ygaP"
source_database: "UniProt"
source_id: "P55734"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:24958726}; Multi-pass membrane protein {ECO:0000269|PubMed:24958726}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ygaP b2668 JW2643"
---

# ygaP

`protein.P55734`

## Static

- Type: `protein`
- Source: `UniProt:P55734`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:24958726}; Multi-pass membrane protein {ECO:0000269|PubMed:24958726}.

## Enriched Summary

FUNCTION: Transferase that catalyzes the transfer of sulfur from thiosulfate to cyanide to form thiocyanate (PubMed:24958726, PubMed:25204500). May have a role in the detoxification of cyanide to the less toxic thiocyanate (PubMed:24958726). May also be involved, directly or indirectly, in the transport of the thiocyanate produced across the membrane from the cytoplasm to the periplasm (PubMed:24958726). {ECO:0000269|PubMed:24958726, ECO:0000269|PubMed:25204500}.

## Biological Role

Component of thiosulfate sulfurtransferase YgaP (complex.ecocyc.CPLX0-8219).

## Annotation

FUNCTION: Transferase that catalyzes the transfer of sulfur from thiosulfate to cyanide to form thiocyanate (PubMed:24958726, PubMed:25204500). May have a role in the detoxification of cyanide to the less toxic thiocyanate (PubMed:24958726). May also be involved, directly or indirectly, in the transport of the thiocyanate produced across the membrane from the cytoplasm to the periplasm (PubMed:24958726). {ECO:0000269|PubMed:24958726, ECO:0000269|PubMed:25204500}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8219|complex.ecocyc.CPLX0-8219]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b2668|gene.b2668]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P55734`
- `KEGG:ecj:JW2643;eco:b2668;ecoc:C3026_14705;`
- `GeneID:947135;`
- `GO:GO:0004792; GO:0005886`
- `EC:2.8.1.1`

## Notes

Thiosulfate sulfurtransferase YgaP (EC 2.8.1.1)
