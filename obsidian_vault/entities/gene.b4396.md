---
entity_id: "gene.b4396"
entity_type: "gene"
name: "rob"
source_database: "NCBI RefSeq"
source_id: "gene-b4396"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4396"
  - "rob"
---

# rob

`gene.b4396`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4396`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rob (gene.b4396) is a gene entity. It encodes rob (protein.P0ACI0). Encoded protein function: FUNCTION: Transcriptional regulator (By similarity). Binds to the right arm of the replication origin oriC of the chromosome (PubMed:8449900). Rob binding may influence the formation of the nucleoprotein structure, required for oriC function in the initiation of replication (PubMed:8449900). {ECO:0000250|UniProtKB:Q8ZJU7, ECO:0000269|PubMed:8449900}. EcoCyc product frame: PD04418. EcoCyc synonyms: cbpB, robA. Genomic coordinates: 4634441-4635310. EcoCyc protein note: Rob is a transcriptional dual regulator. Its N-terminal domain shares 49% identity with MarA and SoxS . These proteins activate a common set of about 50 target genes , the marA/soxS/rob regulon, which is involved in antibiotic resistance , superoxide resistance , and tolerance to organic solvents and heavy metals . Ciprofloxacin is one of the antibiotics against which Rob appears to be involved in resistance . Inhibition of rob expression by CRISPRi reduced cellular fitness under treatment with the antibiotics verapamil or carbonyl cyanide 3-chlorophenylhydrazone (CCCP)...

## Biological Role

Repressed by soxS (protein.P0A9E2), marA (protein.P0ACH5), rob (protein.P0ACI0). Activated by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), ompR (protein.P0AA16).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACI0|protein.P0ACI0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=rob; function=+
- `represses` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `S` - regulator=SoxS; target=rob; function=-
- `represses` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `C` - regulator=MarA; target=rob; function=-
- `represses` <-- [[protein.P0ACI0|protein.P0ACI0]] `RegulonDB` `S` - regulator=Rob; target=rob; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014420,ECOCYC:EG11366,GeneID:948916`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4634441-4635310:-; feature_type=gene
