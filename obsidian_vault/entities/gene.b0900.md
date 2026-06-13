---
entity_id: "gene.b0900"
entity_type: "gene"
name: "ycaN"
source_database: "NCBI RefSeq"
source_id: "gene-b0900"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0900"
  - "ycaN"
---

# ycaN

`gene.b0900`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0900`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ycaN (gene.b0900) is a gene entity. It encodes ycaN (protein.P75836). Encoded protein function: Uncharacterized HTH-type transcriptional regulator YcaN EcoCyc product frame: G6467-MONOMER. Genomic coordinates: 948660-949568. EcoCyc protein note: YcaN was predicted to be a LysR-type transcription factor , it contains a helix-turn-helix motif to bind DNA in its N-terminal domain , and it is probably involved in regulation of threonine and formate utilization . YcaN DNA-binding activity was probed in vivo in glucose M9 minimal medium by the chromatin immunoprecipitation method combined with lambda exonuclease digestion . However, the effect of YcaN on the transcription of any gene has not yet been demonstrated . YcaN was found transcriptionally upregulated in the presence of threonine (Thr) in M9 medium . The transcriptional response for the deletion of YcaN has been characterized by RNA-seq in M9 minimal medium supplemented with 7 mM l-threonine . In the YbdH knockout strain, the adjacent genes ycaD and focA were upregulated while the ycaC gene was downregulated; however, binding was not found under the growth conditions used in ChiP-exo studies. Additionally, in the YcaN knockout strain, various genes involved in amino acid transport and metabolism were strongly downregulated ; moreover, the strain was unable to grow in minimal medium with formate...

## Biological Role

Activated by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P75836|protein.P75836]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ycaN; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0003060,ECOCYC:G6467,GeneID:945523`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:948660-949568:-; feature_type=gene
