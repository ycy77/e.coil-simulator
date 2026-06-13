---
entity_id: "protein.P50466"
entity_type: "protein"
name: "aer"
source_database: "UniProt"
source_id: "P50466"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22380631}; Multi-pass membrane protein {ECO:0000269|PubMed:22380631}. Note=Predominantly localized to one cell pole in mid-to-late exponential phase, with a few smaller foci elsewhere in the cell."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "aer air yqjJ b3072 JW3043"
---

# aer

`protein.P50466`

## Static

- Type: `protein`
- Source: `UniProt:P50466`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:22380631}; Multi-pass membrane protein {ECO:0000269|PubMed:22380631}. Note=Predominantly localized to one cell pole in mid-to-late exponential phase, with a few smaller foci elsewhere in the cell.

## Enriched Summary

FUNCTION: Signal transducer for aerotaxis. The aerotactic response is the accumulation of cells around air bubbles. The nature of the sensory stimulus detected by this protein is the proton motive force or cellular redox state. It uses a FAD prosthetic group as a redox sensor to monitor oxygen levels. {ECO:0000269|PubMed:9190831, ECO:0000269|PubMed:9380671}.

## Biological Role

Component of aerotaxis receptor (complex.ecocyc.CPLX0-13346).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

FUNCTION: Signal transducer for aerotaxis. The aerotactic response is the accumulation of cells around air bubbles. The nature of the sensory stimulus detected by this protein is the proton motive force or cellular redox state. It uses a FAD prosthetic group as a redox sensor to monitor oxygen levels. {ECO:0000269|PubMed:9190831, ECO:0000269|PubMed:9380671}.

## Pathways

- `eco02020` Two-component system (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-13346|complex.ecocyc.CPLX0-13346]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3072|gene.b3072]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P50466`
- `KEGG:ecj:JW3043;eco:b3072;ecoc:C3026_16780;`
- `GeneID:945301;`
- `GO:GO:0004888; GO:0005886; GO:0006935; GO:0007165; GO:0042802; GO:0052131`

## Notes

Aerotaxis receptor
