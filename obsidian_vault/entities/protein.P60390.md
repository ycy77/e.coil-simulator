---
entity_id: "protein.P60390"
entity_type: "protein"
name: "rsmH"
source_database: "UniProt"
source_id: "P60390"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:10572301}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rsmH mraW yabC b0082 JW0080"
---

# rsmH

`protein.P60390`

## Static

- Type: `protein`
- Source: `UniProt:P60390`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:10572301}.

## Enriched Summary

FUNCTION: Specifically methylates the N4 position of cytidine in position 1402 (C1402) of 16S rRNA. In vitro, active on the assembled 30S subunit, but not naked 16S rRNA or 70S ribosomes. {ECO:0000269|PubMed:10572301, ECO:0000269|PubMed:19965768}.

## Biological Role

Component of 16S rRNA m4C1402 methyltransferase (complex.ecocyc.CPLX0-7977).

## Annotation

FUNCTION: Specifically methylates the N4 position of cytidine in position 1402 (C1402) of 16S rRNA. In vitro, active on the assembled 30S subunit, but not naked 16S rRNA or 70S ribosomes. {ECO:0000269|PubMed:10572301, ECO:0000269|PubMed:19965768}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7977|complex.ecocyc.CPLX0-7977]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0082|gene.b0082]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P60390`
- `KEGG:ecj:JW0080;eco:b0082;ecoc:C3026_00315;`
- `GeneID:86862592;944806;`
- `GO:GO:0005737; GO:0005829; GO:0042803; GO:0070475; GO:0071424`
- `EC:2.1.1.199`

## Notes

Ribosomal RNA small subunit methyltransferase H (EC 2.1.1.199) (16S rRNA m(4)C1402 methyltransferase) (rRNA (cytosine-N(4)-)-methyltransferase RsmH)
