---
entity_id: "gene.b3008"
entity_type: "gene"
name: "metC"
source_database: "NCBI RefSeq"
source_id: "gene-b3008"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3008"
  - "metC"
---

# metC

`gene.b3008`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3008`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

metC (gene.b3008) is a gene entity. It encodes metC (protein.P06721). Encoded protein function: FUNCTION: Primarily catalyzes the cleavage of cystathionine to homocysteine, pyruvate and ammonia during methionine biosynthesis (PubMed:7049234). Also exhibits cysteine desulfhydrase activity, producing sulfide from cysteine (PubMed:12883870). In addition, under certain growth conditions, exhibits significant alanine racemase coactivity (PubMed:21193606). {ECO:0000269|PubMed:12883870, ECO:0000269|PubMed:21193606, ECO:0000269|PubMed:7049234}. EcoCyc product frame: CYSTATHIONINE-BETA-LYASE-MONOMER. Genomic coordinates: 3152236-3153423.

## Biological Role

Repressed by metJ (protein.P0A8U6). Activated by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00450` Selenocompound metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01230` Biosynthesis of amino acids (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P06721|protein.P06721]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A8U6|protein.P0A8U6]] `RegulonDB` `S` - regulator=MetJ; target=metC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009878,ECOCYC:EG10583,GeneID:946240`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3152236-3153423:+; feature_type=gene
