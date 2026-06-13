---
entity_id: "gene.b2078"
entity_type: "gene"
name: "baeS"
source_database: "NCBI RefSeq"
source_id: "gene-b2078"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2078"
  - "baeS"
---

# baeS

`gene.b2078`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2078`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

baeS (gene.b2078) is a gene entity. It encodes baeS (protein.P30847). Encoded protein function: FUNCTION: Member of the two-component regulatory system BaeS/BaeR which responds to envelope stress (PubMed:12354228, PubMed:21317898). Activates expression of periplasmic chaperone spy in response to spheroplast formation, indole and P pili protein PapG overexpression (PubMed:12354228). Activates BaeR by phosphorylation which then activates the mdtABCD (PubMed:12107134) and probably the CRISPR-Cas casABCDE-ygbT-ygbF operons (PubMed:21255106). {ECO:0000269|PubMed:12354228, ECO:0000269|PubMed:15522865, ECO:0000269|PubMed:21255106, ECO:0000269|PubMed:21317898}. EcoCyc product frame: PHOSPHO-BAES. Genomic coordinates: 2162876-2164279. EcoCyc protein note: BaeS is the sensor histidine kinase of the BaeSR two-component system. BaeS is a predicted integral membrane protein with sequence similarity to the sensor kinase family of proteins including a conserved histidine (His-250) which is presumed to be the site of autophosphorylation; overproduced BaeS autophosphorylates in the presence of ATP and transfers a phosphate to its cognate response regulator, BaeR in vitro; it is also able to phosphorylate purified OmpR with low efficiency (see also ). BaeSR is implicated in the adaption to envelope stress...

## Biological Role

Repressed by glaR (protein.P37338). Activated by cpxR (protein.P0AE88), baeR (protein.P69228).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30847|protein.P30847]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=baeS; function=+
- `activates` <-- [[protein.P69228|protein.P69228]] `RegulonDB` `S` - regulator=BaeR; target=baeS; function=+
- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=baeS; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0006882,ECOCYC:EG11617,GeneID:946611`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2162876-2164279:+; feature_type=gene
