---
entity_id: "protein.P0ACM5"
entity_type: "protein"
name: "ggaR"
source_database: "UniProt"
source_id: "P0ACM5"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ggaR yegW b2101 JW2088"
---

# ggaR

`protein.P0ACM5`

## Static

- Type: `protein`
- Source: `UniProt:P0ACM5`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transcriptional regulator that regulates glycogen accumulation in response to the amount of glucose available to the cell (PubMed:38257942). Acts as a repressor of the yegTUV operon, which may be involved in glycogen accumulation (PubMed:38257942). Binds at two adjacent sites within the yegTUV upstream region (PubMed:38257942). {ECO:0000269|PubMed:38257942}. GgaR (repressor of glycogen accumulation) negatively regulates genes involved in glycogen accumulation in response to increased glucose concentration . This regulator is found in a constant concentration of approximately 10 molecules in the cell and appears to have just one target, the operon yegTUV, which it regulates by binding to two sites around the regulatory region of the operon. The molecule ADP-glucose, derived from the metabolism of glucose and a precursor of glycogen, appears to bind to GgaR to inactivate it, thus preventing the repression of the yegTUV operon . GgaR, which contains a helix-turn-helix motif to bind DNA in its N-terminal domain, appears to belong to the GntR family of transcription factors . The gene yegW (ggaR) is located in a divergent genomic position from its operon target yegTUV and its transcription is affected by cold shock and glucose-lactose shift...

## Biological Role

Component of YegW-ADP-α-D-glucose (complex.ecocyc.CPLX0-11559).

## Annotation

FUNCTION: Transcriptional regulator that regulates glycogen accumulation in response to the amount of glucose available to the cell (PubMed:38257942). Acts as a repressor of the yegTUV operon, which may be involved in glycogen accumulation (PubMed:38257942). Binds at two adjacent sites within the yegTUV upstream region (PubMed:38257942). {ECO:0000269|PubMed:38257942}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-11559|complex.ecocyc.CPLX0-11559]] `EcoCyc` `database` - EcoCyc component coefficient=

## Incoming Edges (1)

- `encodes` <-- [[gene.b2101|gene.b2101]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACM5`
- `KEGG:ecj:JW2088;eco:b2101;ecoc:C3026_11790;`
- `GeneID:93775093;946639;`
- `GO:GO:0003677; GO:0003700; GO:0045892`

## Notes

HTH-type transcriptional regulator GgaR (Repressor of glycogen accumulation) (Transcription factor GgaR)
