---
entity_id: "gene.b0523"
entity_type: "gene"
name: "purE"
source_database: "NCBI RefSeq"
source_id: "gene-b0523"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0523"
  - "purE"
---

# purE

`gene.b0523`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0523`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

purE (gene.b0523) is a gene entity. It encodes purE (protein.P0AG18). Encoded protein function: FUNCTION: Catalyzes the conversion of N5-carboxyaminoimidazole ribonucleotide (N5-CAIR) to 4-carboxy-5-aminoimidazole ribonucleotide (CAIR). {ECO:0000255|HAMAP-Rule:MF_01929, ECO:0000269|PubMed:8117684}. EcoCyc product frame: PURE-MONOMER. EcoCyc synonyms: ade(f), Pur2, ade3, ade. Genomic coordinates: 552591-553100.

## Biological Role

Repressed by purR (protein.P0ACP7). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AG18|protein.P0AG18]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=purE; function=+
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=purE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0001796,ECOCYC:EG10793,GeneID:949031`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:552591-553100:-; feature_type=gene
