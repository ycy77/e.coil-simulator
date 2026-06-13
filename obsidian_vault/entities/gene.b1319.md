---
entity_id: "gene.b1319"
entity_type: "gene"
name: "ompG"
source_database: "NCBI RefSeq"
source_id: "gene-b1319"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1319"
  - "ompG"
---

# ompG

`gene.b1319`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1319`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ompG (gene.b1319) is a gene entity. It encodes ompG (protein.P76045). Encoded protein function: FUNCTION: Forms channels functionally larger than those of classical porins. {ECO:0000269|PubMed:11758943}.; FUNCTION: May act as a regulator of the RCS-phosphorelay signal transduction pathway. {ECO:0000269|PubMed:11758943}. EcoCyc product frame: G6657-MONOMER. Genomic coordinates: 1381947-1382852. EcoCyc protein note: ompG encodes an outer membrane protein (OMP) in E. coli K-12. ompG is not expressed under normal laboratory conditions in many K-12 strains; deletions upstream of ompG which bring it under the control of an unrelated promoter induce expression . When expressed, OmpG functions as a nonspecific outer membrane channel; OmpG produces a larger channel than the classical outer membrane porins (OmpF and OmpC) - in addition to the efficient transport of monosaccharides, OmpG facilitates the diffusion of dissacharides (sucrose) and trisaccharides (raffinose); OmpG appears to function as a monomer; OmpG is predicted to contain 16 transmembrane β strands . OmpG is a monomeric porin . OmpG is a 14-stranded β-barrel porin with short periplasmic turns and seven extracellular loops; crystal structures in two different conformations suggest that extracellular loop 6 may be involved in pH dependent gating of the OmpG channel . When reconstituted into native E...

## Biological Role

Repressed by ycjW (protein.P77615).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76045|protein.P76045]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P77615|protein.P77615]] `RegulonDB` `S` - regulator=YcjW; target=ompG; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004425,ECOCYC:G6657,GeneID:945889`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1381947-1382852:+; feature_type=gene
