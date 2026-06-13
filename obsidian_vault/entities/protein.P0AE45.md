---
entity_id: "protein.P0AE45"
entity_type: "protein"
name: "paeA"
source_database: "UniProt"
source_id: "P0AE45"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "paeA ytfL b4218 JW4177"
---

# paeA

`protein.P0AE45`

## Static

- Type: `protein`
- Source: `UniProt:P0AE45`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Involved in cadaverine and putrescine tolerance in stationary phase. May facilitate the efflux of both cadaverine and putrescine from the cytoplasm, reducing potentially toxic levels under certain stress conditions. {ECO:0000269|PubMed:33481283}. PaeA (formerly YtfL) is predicted to be an inner membrane protein with four transmembrane domains; experimental topology analysis suggests the C terminus is located in the cytoplasm . A paeA deletion mutant (ΔpaeA::kan) is more sensitive to nalidixic acid and kasugamycin than wild type . PaeA is implicated in the selective efflux of cadaverine and putrescine in Salmonella Typhimurium and is important for stationary phase survival when cells are grown in acidic medium; deletion of paeA in E. coli K-12 increases sensitivity to cadaverine and putrescine but not to spermidine and spermine . paeA: polyamine export

## Annotation

FUNCTION: Involved in cadaverine and putrescine tolerance in stationary phase. May facilitate the efflux of both cadaverine and putrescine from the cytoplasm, reducing potentially toxic levels under certain stress conditions. {ECO:0000269|PubMed:33481283}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b4218|gene.b4218]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE45`
- `KEGG:ecj:JW4177;eco:b4218;ecoc:C3026_22780;`
- `GeneID:75202458;948735;`
- `GO:GO:0005886; GO:0050660`

## Notes

Polyamine export protein
