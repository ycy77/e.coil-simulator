---
entity_id: "gene.b4240"
entity_type: "gene"
name: "treB"
source_database: "NCBI RefSeq"
source_id: "gene-b4240"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4240"
  - "treB"
---

# treB

`gene.b4240`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4240`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

treB (gene.b4240) is a gene entity. It encodes treB (protein.P36672). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. This system is involved in trehalose transport at low osmolarity. {ECO:0000269|PubMed:2160944, ECO:0000305|PubMed:7608078}. EcoCyc product frame: TREB-MONOMER. Genomic coordinates: 4464759-4466180. EcoCyc protein note: TreB contains PTS Enzyme IIB and IIC domains

## Biological Role

Repressed by treR (protein.P36673).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36672|protein.P36672]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P36673|protein.P36673]] `RegulonDB` `S` - regulator=TreR; target=treB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013872,ECOCYC:EG12127,GeneID:948761`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4464759-4466180:-; feature_type=gene
