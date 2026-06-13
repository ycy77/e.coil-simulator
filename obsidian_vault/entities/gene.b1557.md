---
entity_id: "gene.b1557"
entity_type: "gene"
name: "cspB"
source_database: "NCBI RefSeq"
source_id: "gene-b1557"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1557"
  - "cspB"
---

# cspB

`gene.b1557`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1557`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cspB (gene.b1557) is a gene entity. It encodes cspB (protein.P36995). Encoded protein function: Cold shock-like protein CspB (CSP-B) EcoCyc product frame: EG12203-MONOMER. Genomic coordinates: 1641339-1641554. EcoCyc protein note: CspB is a member of the CspA family of cold-shock proteins and is induced on transition to cold temperatures . cspB belongs to a small set of genes whose expression is upregulated and whose absence is a competitive disadvantage in long-term stationary phase (LTSP) . CspB was initially identified based on its similarity with CspA . Cold-shock proteins are typically involved in binding RNA to prevent formation of deleterious secondary structure at low temperatures. Based on an in vitro selection method, CspB preferentially binds to U/T stretches in target RNAs . Like CspA and CsdA, expression of CspB is regulated by a "cold box" in its 5' UTR . Full expression also depends on an internal sequence downstream from the initiation codon, termed the Downstream Box (DB). The DB may increase the affinity of cspB mRNA for 16S rRNA . Transcription of cspB is induced by a temperature shift to below 20°C, with maximal expression at 15°C . Cold induction of CspB increases in the absence of functional CspA and can occur even in the presence of antibiotics that block protein synthesis . cspB transcription levels change in response to temperature cycling...

## Biological Role

Activated by zraR (protein.P14375).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36995|protein.P36995]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P14375|protein.P14375]] `RegulonDB|EcoCyc` `S` - regulator=ZraR; target=cspB; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0005199,ECOCYC:EG12203,GeneID:946091`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1641339-1641554:-; feature_type=gene
