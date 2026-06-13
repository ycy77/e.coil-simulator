---
entity_id: "gene.b1570"
entity_type: "gene"
name: "dicA"
source_database: "NCBI RefSeq"
source_id: "gene-b1570"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1570"
  - "dicA"
---

# dicA

`gene.b1570`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1570`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dicA (gene.b1570) is a gene entity. It encodes dicA (protein.P06966). Encoded protein function: FUNCTION: This protein is a repressor of division inhibition gene dicB. EcoCyc product frame: EG10226-MONOMER. EcoCyc synonyms: ftsT. Genomic coordinates: 1647934-1648341. EcoCyc protein note: The transcription factor DicA, "Division control," is a temperature-sensitive repressor that controls the transcription of genes involved in the cell division process and activation of its own expression . Nevertheless, the signal to which DicA responds is still unknown. The family to which DicA belongs has not been established; it is a protein of 15 kDa with a hypothetical DNA-binding domain in the N-terminal domain . DicA is homologous in structure and function to RovA (Yersinia) and SlyA (Salmonella), both of which are activators for pathogenicity-related genes . Rem has been identified as a putative antirepressor of DicA, encoded in the cryptic prophage Qin, as it induces the derepression of dicBp, a promoter repressed by DicA . A dicA hypomorphic allele mutant strain had growth defects and long filamentation, and this phenotype was rescued to near-wild-type when the gene encoding the TF YjdC (DicD) was deleted. In a dicA hypomorphic allele mutant strain, the TF YjdC is transcriptionally downregulated...

## Biological Role

Repressed by yjdC (protein.P0ACU7). Activated by dicA (protein.P06966).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06966|protein.P06966]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P06966|protein.P06966]] `RegulonDB` `S` - regulator=DicA; target=dicA; function=+
- `represses` <-- [[protein.P0ACU7|protein.P0ACU7]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005248,ECOCYC:EG10226,GeneID:946241`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1647934-1648341:+; feature_type=gene
