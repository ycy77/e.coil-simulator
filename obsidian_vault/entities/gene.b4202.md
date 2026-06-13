---
entity_id: "gene.b4202"
entity_type: "gene"
name: "rpsR"
source_database: "NCBI RefSeq"
source_id: "gene-b4202"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4202"
  - "rpsR"
---

# rpsR

`gene.b4202`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4202`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsR (gene.b4202) is a gene entity. It encodes rpsR (protein.P0A7T7). Encoded protein function: FUNCTION: Binds as a heterodimer with protein bS6 to the central domain of the 16S rRNA, where it helps stabilize the platform of the 30S subunit. EcoCyc product frame: EG10917-MONOMER. Genomic coordinates: 4425839-4426066. EcoCyc protein note: The S18 protein is a component of the 30S subunit of the ribosome. The N-terminal alanine residue of S18 is acetylated by the EG10850-MONOMER RimI enzyme . N-terminal acetylation of S18 and S5 correlates with correct folding of the platform and central pseudoknot domains of 16S rRNA . S18 interacts with the central domain of 16S rRNA; the interaction is dependent on S8 and S15 . S18 may be involved in binding of aminoacyl-tRNA to the P site of the ribosome . S18 is photoaffinity labeled by puromycin, an analog of the 3' end of aminoacylated tRNA . S18 was also shown to crosslink to IF3 , IF1 and 4.5S RNA . Expression analysis of rpsFp indicates that it may be autoregulated by one or more of its operon components . Coexpressed S6:S18 were found to bind to the rpsF 5'-UTR in a region with structural similarity to their binding site in 16S rRNA . The S6:S18 complex was shown to repress translation of rpsF . Review:

## Biological Role

Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A7T7|protein.P0A7T7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=rpsR; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013744,ECOCYC:EG10917,GeneID:948721`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4425839-4426066:+; feature_type=gene
