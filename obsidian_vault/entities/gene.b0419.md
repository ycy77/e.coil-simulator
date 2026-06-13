---
entity_id: "gene.b0419"
entity_type: "gene"
name: "yajO"
source_database: "NCBI RefSeq"
source_id: "gene-b0419"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0419"
  - "yajO"
---

# yajO

`gene.b0419`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0419`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yajO (gene.b0419) is a gene entity. It encodes yajO (protein.P77735). Encoded protein function: FUNCTION: Catalyzes the conversion of ribulose 5-phosphate (Ru5P) to 1-deoxy-D-xylulose 5-phosphate (DXP), providing a direct route from pentoses to terpenes. May play a role in biosynthesis of DXP under conditions of thiamine starvation. {ECO:0000269|PubMed:25326299}. EcoCyc product frame: G6236-MONOMER. Genomic coordinates: 437161-438135. EcoCyc protein note: YajO is able to synthesize 1-deoxy-D-xylulose 5-phosphate (DXP) from ribulose 5-phosphate, providing a novel route from a pentose phosphate to DXP . Overexpression of YajO from a multicopy plasmid leads to resistance to the 4-amino-2-methyl-5-hydroxymethylpyrimidine (HMP) analog bacimethrin. The resistance mechanism is undetermined, but does not involve biosynthesis of HMP ; increased synthesis of DXP, a precursor of thiamine, is one of the possibilities . YajO is similar to the AKR7 family of aldo-keto reductases. Purified YajO showed 2-carboxybenzaldehyde reductase activity, but not methylglyoxal reductase activity . Growth of a yajO gloA double mutant is inhibited by 0.3 mM methylglyoxal, but expression of yajO is not increased in response to methylglyoxal . Overexpression of yajO from a plasmid supports cell viability in the absence of the essential dxs-encoded DXS-MONOMER . Review:

## Biological Role

Repressed by nac (protein.Q47005).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77735|protein.P77735]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=yajO; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001457,ECOCYC:G6236,GeneID:946903`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:437161-438135:-; feature_type=gene
