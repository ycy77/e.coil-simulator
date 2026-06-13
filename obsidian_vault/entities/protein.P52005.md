---
entity_id: "protein.P52005"
entity_type: "protein"
name: "torY"
source_database: "UniProt"
source_id: "P52005"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250}; Single-pass type II membrane protein {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "torY yecK b1873 JW1862"
---

# torY

`protein.P52005`

## Static

- Type: `protein`
- Source: `UniProt:P52005`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250}; Single-pass type II membrane protein {ECO:0000250}.

## Enriched Summary

FUNCTION: Part of the anaerobic respiratory chain of trimethylamine-N-oxide reductase TorZ. Required for electron transfer to the TorZ terminal enzyme. The periplasmic oxidoreductase G7022-MONOMER "TorZ" and membrane anchored pentaheme c-type cytochrome TorY constitute an anaerobic respiratory system that can use several N and S-oxides, including TMAO and biotin sulfoxide as terminal electron acceptors . TorY is a c-type cytochrome that is anchored to the inner membrane; 5 predicted heme binding sites (CXXCH) have been identified. TorY has 36% identity with EG11815-MONOMER . torYZ expression is very low and is not induced by TMAO or DMSO .

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Part of the anaerobic respiratory chain of trimethylamine-N-oxide reductase TorZ. Required for electron transfer to the TorZ terminal enzyme.

## Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1873|gene.b1873]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P52005`
- `KEGG:ecj:JW1862;eco:b1873;ecoc:C3026_10660;`
- `GeneID:946490;`
- `GO:GO:0005506; GO:0005886; GO:0009055; GO:0009061; GO:0009276; GO:0016020; GO:0019645; GO:0020037`

## Notes

Cytochrome c-type protein TorY
