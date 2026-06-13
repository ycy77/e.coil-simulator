---
entity_id: "gene.b0193"
entity_type: "gene"
name: "yaeF"
source_database: "NCBI RefSeq"
source_id: "gene-b0193"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0193"
  - "yaeF"
---

# yaeF

`gene.b0193`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0193`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yaeF (gene.b0193) is a gene entity. It encodes yaeF (protein.P37056). Encoded protein function: Probable lipoprotein peptidase YaeF (EC 3.4.-.-) (Uncharacterized lipoprotein YaeF) EcoCyc product frame: EG12138-MONOMER. EcoCyc synonyms: yaeK. Genomic coordinates: 216179-217003. EcoCyc protein note: The protein is a member of a family of bacterial proteins (the YaeF/YiiX family) that defines a permuted subset of the NlpC/P60 superfamily of cell wall peptidases; putative catalytic residues have been identified, but precise activity has not been determined . YaeF is a predicted lipoprotein

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37056|protein.P37056]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB` `S` - regulator=Nac; target=yaeF; function=-

## External IDs

- `Dbxref:ASAP:ABE-0000655,ECOCYC:EG12138,GeneID:944892`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:216179-217003:-; feature_type=gene
