---
entity_id: "protein.P31060"
entity_type: "protein"
name: "modF"
source_database: "UniProt"
source_id: "P31060"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250}; Peripheral membrane protein {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "modF ORF6 phrA b0760 JW0743"
---

# modF

`protein.P31060`

## Static

- Type: `protein`
- Source: `UniProt:P31060`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000250}; Peripheral membrane protein {ECO:0000250}.

## Enriched Summary

FUNCTION: Probably not involved in the transport of molybdenum into the cell. {ECO:0000269|PubMed:8564363}. ModF contains sequence motifs conserved in ATP-binding cassette (ABC) proteins; ModF contains an ABC-ABC domain . modF is not essential for synthesis of molybdenum cofactor or for molybdenum uptake and is not involved in regulation of the mod operon: insertional inactivation of modF does not affect the activity of molybdoenzymes (nitrate reductase, formate dehydrogenase, trimethylamine-N-oxide reductase) . modF expression may be repressed by molybdate: expression of a plasmid borne φ(modF-lacZ) fusion increases when cells are grown in low molybdate glucose minimal media . modE and modF form a two-gene operon suggests that ModF is a component of a molybdate ABC transporter - ModABCF. phrA: photorepair

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Probably not involved in the transport of molybdenum into the cell. {ECO:0000269|PubMed:8564363}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b0760|gene.b0760]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P31060`
- `KEGG:ecj:JW0743;eco:b0760;ecoc:C3026_03855;`
- `GeneID:75204875;945368;`
- `GO:GO:0005524; GO:0006281; GO:0016887; GO:0042626; GO:0043190`

## Notes

ABC transporter ATP-binding protein ModF (Photorepair protein PhrA)
