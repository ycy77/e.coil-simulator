---
entity_id: "gene.b1835"
entity_type: "gene"
name: "rsmF"
source_database: "NCBI RefSeq"
source_id: "gene-b1835"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1835"
  - "rsmF"
---

# rsmF

`gene.b1835`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1835`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rsmF (gene.b1835) is a gene entity. It encodes rsmF (protein.P76273). Encoded protein function: FUNCTION: Specifically methylates the cytosine at position 1407 (m5C1407) of 16S rRNA (PubMed:16678201). In vitro, methylates the assembled 30S subunit, but not naked 16S rRNA or the 70S ribosome (PubMed:16678201). {ECO:0000269|PubMed:16678201}.; FUNCTION: In addition, during cellular stress, methylates the cytosine at position 49 (m5C49) of the tyrosine transfer RNA (tRNA Tyr-QUA-II). {ECO:0000269|PubMed:39495928}. EcoCyc product frame: G7008-MONOMER. EcoCyc synonyms: yebU. Genomic coordinates: 1920223-1921662. EcoCyc protein note: RsmF is a dual-substrate RNA-modifying methyltransferase responsible for methylation of 16S rRNA at the C5 position of the C1407 nucleotide and for m5c modification to the anticodon of TYR-tRNAs tRNATyr at position C49 . In vitro, the enzyme methylates 16S rRNA within the 30S ribosomal subunit, but not naked 16S rRNA or 70S ribosomes . The enzyme was identified by similarity to the RsmB methyltransferase, which is responsible for methylation of C967 of 16S rRNA . A crystal structure of RsmF has been solved at 2.9 Å resolution. The enzyme has an N-terminal catalytic domain that binds S-adenosylmethionine; the C-terminal domain has structural similarity to PUA domains of pseudouridine synthases and archaeosine-specific transglycosylases...

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76273|protein.P76273]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=rsmF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006106,ECOCYC:G7008,GeneID:946348`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1920223-1921662:+; feature_type=gene
