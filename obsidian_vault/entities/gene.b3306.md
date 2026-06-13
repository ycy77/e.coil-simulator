---
entity_id: "gene.b3306"
entity_type: "gene"
name: "rpsH"
source_database: "NCBI RefSeq"
source_id: "gene-b3306"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3306"
  - "rpsH"
---

# rpsH

`gene.b3306`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3306`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsH (gene.b3306) is a gene entity. It encodes rpsH (protein.P0A7W7). Encoded protein function: FUNCTION: One of the primary rRNA binding proteins, it binds directly to 16S rRNA central domain where it helps coordinate assembly of the platform of the 30S subunit. {ECO:0000250}.; FUNCTION: Protein S8 is a translational repressor protein, it controls the translation of the spc operon by binding to its mRNA. {ECO:0000269|PubMed:6262737}. EcoCyc product frame: EG10907-MONOMER. Genomic coordinates: 3446153-3446545. EcoCyc protein note: The S8 protein is a component of the 30S subunit of the ribosome and also functions in the post-transcriptional regulation of the ribosomal protein genes encoded in the spc operon. The S8 protein binds to 16S rRNA in the absence of other ribosomal proteins . S8 binding is not absolutely required for assembly of the 30S ribosomal subunit platform, but it influences the organization of the 16S rRNA central domain . Sites within 16S rRNA where S8 interacts have been determined , and the secondary and tertiary structure of the binding region has been investigated . The unique cysteine residue present in S8 is essential for 16S rRNA binding , although it may not be involved in RNA recognition . Other sequence determinants important for 16S rRNA binding have been investigated...

## Biological Role

Repressed by rpsH (protein.P0A7W7), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7W7|protein.P0A7W7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `represses` <-- [[protein.P0A7W7|protein.P0A7W7]] `RegulonDB` `S` - regulator=RpsH; target=rpsH; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010829,ECOCYC:EG10907,GeneID:947802`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3446153-3446545:-; feature_type=gene
