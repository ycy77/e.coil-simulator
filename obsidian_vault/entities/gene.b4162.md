---
entity_id: "gene.b4162"
entity_type: "gene"
name: "orn"
source_database: "NCBI RefSeq"
source_id: "gene-b4162"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4162"
  - "orn"
---

# orn

`gene.b4162`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4162`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

orn (gene.b4162) is a gene entity. It encodes orn (protein.P0A784). Encoded protein function: FUNCTION: 3'-to-5' exoribonuclease specific for small oligoribonucleotides 2 to 5 nucleotides in length, as well as small (2 to 5 nucleotides) ssDNA oligomers. Probably responsible for the final step in mRNA degradation. {ECO:0000269|PubMed:16682444, ECO:0000269|PubMed:7608090, ECO:0000269|PubMed:9573169}. EcoCyc product frame: G7842-MONOMER. EcoCyc synonyms: yjeR. Genomic coordinates: 4391604-4392149. EcoCyc protein note: Oligoribonuclease (Orn) is a processive 3'-to-5' exoribonuclease specific for short oligoribonucleotides . Short RNAs, from 2-7 nucleotides in length, accumulate in the cell during RNA degradation, because they are not good substrates for general exoribonucleases. Orn recycles these short RNA oligonucleotides into mononucleotides. The activity on very short oligoribonucleotides is not shared with other exoribonucleases in E. coli . Orn is the only known exoribonuclease enzyme that is essential for growth in E. coli, indicating the importance of its function . Orn from TAX-287 was shown to cleave the dinucleotide L-DI-GMP, which is formed from the second messanger C-DI-GMP by EC-3.1.4.52 . Orn binds adenosine-3',5'-bisphosphate (pAp), but does not hydrolyze it under the conditions tested . Crystal structures of Orn have been solved...

## Biological Role

Activated by glaR (protein.P37338).

## Enriched Pathways

- `eco03008` Ribosome biogenesis in eukaryotes (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A784|protein.P0A784]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=orn; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013631,ECOCYC:G7842,GeneID:948675`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4391604-4392149:+; feature_type=gene
