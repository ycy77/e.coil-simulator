---
entity_id: "protein.P67087"
entity_type: "protein"
name: "rsmI"
source_database: "UniProt"
source_id: "P67087"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rsmI yraL b3146 JW3115"
---

# rsmI

`protein.P67087`

## Static

- Type: `protein`
- Source: `UniProt:P67087`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Catalyzes the 2'-O-methylation of the ribose of cytidine 1402 (C1402) in 16S rRNA. In vitro, active on the assembled 30S subunit, but not naked 16S rRNA or 70S ribosomes. {ECO:0000269|PubMed:19965768}.

## Biological Role

Component of 16S rRNA 2'-O-ribose C1402 methyltransferase (complex.ecocyc.CPLX0-8231).

## Annotation

FUNCTION: Catalyzes the 2'-O-methylation of the ribose of cytidine 1402 (C1402) in 16S rRNA. In vitro, active on the assembled 30S subunit, but not naked 16S rRNA or 70S ribosomes. {ECO:0000269|PubMed:19965768}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8231|complex.ecocyc.CPLX0-8231]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3146|gene.b3146]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P67087`
- `KEGG:ecj:JW3115;eco:b3146;ecoc:C3026_17140;`
- `GeneID:93778838;947664;`
- `GO:GO:0005737; GO:0006364; GO:0042803; GO:0070677`
- `EC:2.1.1.198`

## Notes

Ribosomal RNA small subunit methyltransferase I (EC 2.1.1.198) (16S rRNA 2'-O-ribose C1402 methyltransferase) (rRNA (cytidine-2'-O-)-methyltransferase RsmI)
