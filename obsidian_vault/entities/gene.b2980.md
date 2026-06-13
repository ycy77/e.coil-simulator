---
entity_id: "gene.b2980"
entity_type: "gene"
name: "glcC"
source_database: "NCBI RefSeq"
source_id: "gene-b2980"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2980"
  - "glcC"
---

# glcC

`gene.b2980`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2980`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glcC (gene.b2980) is a gene entity. It encodes glcC (protein.P0ACL5). Encoded protein function: FUNCTION: Transcriptional activator of the glcDEFGB operon which is associated with glycolate utilization, and encodes malate synthase G and the genes needed for glycolate oxidase activity (PubMed:8606183, PubMed:9880556). Also negatively regulates the transcription of its own gene (PubMed:9880556). Glycolate acts as an effector, but GlcC can also use acetate as an alternative effector (PubMed:9880556). {ECO:0000269|PubMed:8606183, ECO:0000269|PubMed:9880556}. EcoCyc product frame: G7546-MONOMER. EcoCyc synonyms: yghN. Genomic coordinates: 3128272-3129036. EcoCyc protein note: GlcC (for "glycolate utilization") negatively controls the expression of genes involved in the utilization of glycolate as the sole source of carbon . It is negatively autoregulated and coordinately activated by transcription of the divergent operon glc, which is related to the transport and metabolism of glycolate . Synthesis of glc genes is induced when Escherichia coli is grown on glycolate . GlcC features an N-terminal domain containing a helix-turn-helix motif and a putative C-terminal domain that includes the key residues involved in coinducer recognition and oligomerization. Although little is known about the mechanism of regulation of the GlcC transcription factor, Pellicer et al...

## Biological Role

Repressed by fis (protein.P0A6R3), arcA (protein.P0A9Q1), glcC (protein.P0ACL5).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ACL5|protein.P0ACL5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `represses` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=glcC; function=-
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `C` - regulator=ArcA; target=glcC; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACL5|protein.P0ACL5]] `RegulonDB` `S` - regulator=GlcC; target=glcC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009777,ECOCYC:G7546,GeneID:947466`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3128272-3129036:+; feature_type=gene
