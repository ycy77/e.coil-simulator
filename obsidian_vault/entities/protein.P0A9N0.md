---
entity_id: "protein.P0A9N0"
entity_type: "protein"
name: "ptsO"
source_database: "UniProt"
source_id: "P0A9N0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ptsO npr rpoR yhbK b3206 JW3173"
---

# ptsO

`protein.P0A9N0`

## Static

- Type: `protein`
- Source: `UniProt:P0A9N0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Component of the phosphoenolpyruvate-dependent nitrogen-metabolic phosphotransferase system (nitrogen-metabolic PTS), that seems to be involved in regulating nitrogen metabolism. The phosphoryl group from phosphoenolpyruvate (PEP) is transferred to the phosphoryl carrier protein NPr by enzyme I-Ntr. Phospho-NPr then transfers it to EIIA-Ntr. Could function in the transcriptional regulation of sigma-54 dependent operons in conjunction with the NPr (PtsO) and EIIA-Ntr (PtsN) proteins. NPr is the second phosphotransfer protein of the nitrogen phosphoenolpyruvate (PEP)-dependent phosphotransferase system (PTSNtr) in E. coli K-12. The exact function of the PTSNtr is not clear - it has been implicated in the regulation of nitrogen metabolism and in potassium homeostasis (reviewed in but see also ). EG12188-MONOMER "PtsP", also known as enzyme INtr, phosphorylates NPr in vitro. This reaction occurs at an optimum pH of 8.0, is dependent on Mg2+, is stimulated by high ionic strength, and has two Km values for Npr of 2 and 10 μM . Purified Npr is active as a phosphoryl acceptor from EINtr and is capable of phosphotransfer to EG11682-MONOMER "PtsN" (also known as EIIANtr); a solution structure of Npr has been obtained...

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

FUNCTION: Component of the phosphoenolpyruvate-dependent nitrogen-metabolic phosphotransferase system (nitrogen-metabolic PTS), that seems to be involved in regulating nitrogen metabolism. The phosphoryl group from phosphoenolpyruvate (PEP) is transferred to the phosphoryl carrier protein NPr by enzyme I-Ntr. Phospho-NPr then transfers it to EIIA-Ntr. Could function in the transcriptional regulation of sigma-54 dependent operons in conjunction with the NPr (PtsO) and EIIA-Ntr (PtsN) proteins.

## Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b3206|gene.b3206]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9N0`
- `KEGG:ecj:JW3173;eco:b3206;ecoc:C3026_17445;`
- `GeneID:93778775;947914;`
- `GO:GO:0005737; GO:0009401; GO:0016772`

## Notes

Phosphocarrier protein NPr (Nitrogen-related HPr)
