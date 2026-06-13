---
entity_id: "gene.b0760"
entity_type: "gene"
name: "modF"
source_database: "NCBI RefSeq"
source_id: "gene-b0760"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0760"
  - "modF"
---

# modF

`gene.b0760`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0760`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

modF (gene.b0760) is a gene entity. It encodes modF (protein.P31060). Encoded protein function: FUNCTION: Probably not involved in the transport of molybdenum into the cell. {ECO:0000269|PubMed:8564363}. EcoCyc product frame: MODF-MONOMER. EcoCyc synonyms: chlD, phrA. Genomic coordinates: 792316-793788. EcoCyc protein note: ModF contains sequence motifs conserved in ATP-binding cassette (ABC) proteins; ModF contains an ABC-ABC domain . modF is not essential for synthesis of molybdenum cofactor or for molybdenum uptake and is not involved in regulation of the mod operon: insertional inactivation of modF does not affect the activity of molybdoenzymes (nitrate reductase, formate dehydrogenase, trimethylamine-N-oxide reductase) . modF expression may be repressed by molybdate: expression of a plasmid borne φ(modF-lacZ) fusion increases when cells are grown in low molybdate glucose minimal media . modE and modF form a two-gene operon suggests that ModF is a component of a molybdate ABC transporter - ModABCF. phrA: photorepair

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P31060|protein.P31060]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0002582,ECOCYC:EG11677,GeneID:945368`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:792316-793788:-; feature_type=gene
