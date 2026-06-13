---
entity_id: "protein.P0A9I3"
entity_type: "protein"
name: "gcvR"
source_database: "UniProt"
source_id: "P0A9I3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "gcvR yffD b2479 JW2464"
---

# gcvR

`protein.P0A9I3`

## Static

- Type: `protein`
- Source: `UniProt:P0A9I3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Negative transcriptional regulator of the glycine cleavage system operon (GCV). Does not autoregulate its own expression. It is not yet known how GcvR acts as a repressor. It does not seem to bind DNA. It could interact with GcvA and suppress its activatory activity.

## Biological Role

Component of GcvR-gly (complex.ecocyc.MONOMER0-941).

## Enriched Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

FUNCTION: Negative transcriptional regulator of the glycine cleavage system operon (GCV). Does not autoregulate its own expression. It is not yet known how GcvR acts as a repressor. It does not seem to bind DNA. It could interact with GcvA and suppress its activatory activity.

## Pathways

- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.MONOMER0-941|complex.ecocyc.MONOMER0-941]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b2479|gene.b2479]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9I3`
- `KEGG:ecj:JW2464;eco:b2479;ecoc:C3026_13760;`
- `GeneID:93774659;946950;`
- `GO:GO:0005829; GO:0006351; GO:0006355`

## Notes

Glycine cleavage system transcriptional repressor (gcv operon repressor)
