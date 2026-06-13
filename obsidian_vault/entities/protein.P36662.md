---
entity_id: "protein.P36662"
entity_type: "protein"
name: "torD"
source_database: "UniProt"
source_id: "P36662"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:9632735}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "torD b0998 JW0983"
---

# torD

`protein.P36662`

## Static

- Type: `protein`
- Source: `UniProt:P36662`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000269|PubMed:9632735}.

## Enriched Summary

FUNCTION: Involved in the biogenesis of TorA. Acts on TorA before the insertion of the molybdenum cofactor and, as a result, probably favors a conformation of the apoenzyme that is competent for acquiring the cofactor. {ECO:0000269|PubMed:12766163, ECO:0000269|PubMed:9632735}. TorD is the TORA-MONOMER TorA-specific redox enzyme maturation protein (REMP). TorD is encoded by the terminal open reading frame of the torCAD operon, which is involved in anaerobic respiration of trimethylamine N-oxide (TMAO) . TorD belongs to a family of structurally related bacterial proteins which appear to have coevolved with their specific molybdoprotein partners . TorD interacts directly with the TorA protein, the TMAO reductase, before TorA acquires its molybdenum cofactor . TorD acts as a private chaperone for TorA, making it competent to receive the molybdenum cofactor; TorD was shown to be sufficient for activation of TorA . TorD specifically recognizes the twin-arginine signal peptide of TorA, performing a Tat proofreading function .

## Enriched Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

FUNCTION: Involved in the biogenesis of TorA. Acts on TorA before the insertion of the molybdenum cofactor and, as a result, probably favors a conformation of the apoenzyme that is competent for acquiring the cofactor. {ECO:0000269|PubMed:12766163, ECO:0000269|PubMed:9632735}.

## Pathways

- `eco00680` Methane metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02020` Two-component system (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0998|gene.b0998]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P36662`
- `KEGG:ecj:JW0983;eco:b0998;`
- `GeneID:945625;`
- `GO:GO:0005737; GO:0006457; GO:0042277; GO:0042802; GO:0043546; GO:0051259; GO:0051604`

## Notes

Chaperone protein TorD
