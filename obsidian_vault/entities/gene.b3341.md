---
entity_id: "gene.b3341"
entity_type: "gene"
name: "rpsG"
source_database: "NCBI RefSeq"
source_id: "gene-b3341"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3341"
  - "rpsG"
---

# rpsG

`gene.b3341`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3341`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsG (gene.b3341) is a gene entity. It encodes rpsG (protein.P02359). Encoded protein function: FUNCTION: One of the primary rRNA binding proteins, it binds directly to 16S rRNA where it nucleates assembly of the head domain of the 30S subunit (PubMed:2461734). Is located at the subunit interface close to the decoding center, where it has been shown to contact mRNA (PubMed:10606263). Has been shown to contact tRNA in both the P and E sites; it probably blocks exit of the E site tRNA (PubMed:8524654). {ECO:0000269|PubMed:10606263, ECO:0000269|PubMed:2461734, ECO:0000269|PubMed:8524654}.; FUNCTION: Protein S7 is also a translational repressor protein; it regulates the expression of the str operon members to different degrees by binding to its mRNA. {ECO:0000269|PubMed:7507167}. EcoCyc product frame: EG10906-MONOMER. Genomic coordinates: 3473542-3474081. EcoCyc protein note: The S7 protein is a component of the 30S subunit of the ribosome. S7 binds to 16S rRNA . The ability of both S4 and S7 to bind 16S rRNA by themselves indicates that they function as initiator proteins for the assembly of the 30S subunit of the ribosome. The S9, S13, S19, S10, S14, and S3 subunits depend on S7 for assembly . The K35 residue of S7 appears to be required for efficient assembly . S7 crosslinks to the anticodon loop of tRNAs, indicating its location close to the decoding site of the ribosome...

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02359|protein.P02359]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0010917,ECOCYC:EG10906,GeneID:947846`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3473542-3474081:-; feature_type=gene
