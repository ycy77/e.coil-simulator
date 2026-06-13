---
entity_id: "gene.b3800"
entity_type: "gene"
name: "aslB"
source_database: "NCBI RefSeq"
source_id: "gene-b3800"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3800"
  - "aslB"
---

# aslB

`gene.b3800`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3800`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

aslB (gene.b3800) is a gene entity. It encodes aslB (protein.P25550). Encoded protein function: Anaerobic sulfatase-maturating enzyme homolog AslB (AnSME homolog) EcoCyc product frame: EG10090-MONOMER. EcoCyc synonyms: gppB, atsB. Genomic coordinates: 3982958-3984193. EcoCyc protein note: AslB is a member of the anaerobic sulfatase maturation enzyme subfamily of the Radical SAM superfamily of enzymes . AslB from E. coli BL21(DE3), which is 96% identical to AslB of E. coli K-12 MG1655 (shown here), has been studied experimentally. Co-expression of AslB with recombinant human sulfatases results in increased sulfatase activity . Both an aslB single and aslB ydeM double null mutant is still able to mature a heterologous sulfatase from Clostridium perfringens. Maturation of the C. perfringens enzyme appears to be dependent on a different enzyme that is present only under aerobic conditions . Expression of aslB is activated by the transcriptional regulator Rob .

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25550|protein.P25550]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0012408,ECOCYC:EG10090,GeneID:949013`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3982958-3984193:+; feature_type=gene
