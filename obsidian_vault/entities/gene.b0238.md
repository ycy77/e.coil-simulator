---
entity_id: "gene.b0238"
entity_type: "gene"
name: "gpt"
source_database: "NCBI RefSeq"
source_id: "gene-b0238"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0238"
  - "gpt"
---

# gpt

`gene.b0238`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0238`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gpt (gene.b0238) is a gene entity. It encodes gpt (protein.P0A9M5). Encoded protein function: FUNCTION: Purine salvage pathway enzyme that catalyzes the transfer of the ribosyl-5-phosphate group from 5-phospho-alpha-D-ribose 1-diphosphate (PRPP) to the N9 position of the 6-oxopurines guanine and xanthine to form the corresponding ribonucleotides GMP (guanosine 5'-monophosphate) and XMP (xanthosine 5'-monophosphate), with the release of PPi. To a lesser extent, also acts on hypoxanthine (PubMed:3886014, PubMed:9100006). Does not ribophosphorylate adenine (PubMed:3886014). {ECO:0000269|PubMed:3886014, ECO:0000269|PubMed:9100006}. EcoCyc product frame: GPT-MONOMER. EcoCyc synonyms: glyD, gpp, gxu. Genomic coordinates: 255977-256435.

## Biological Role

Repressed by lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9M5|protein.P0A9M5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0000814,ECOCYC:EG10414,GeneID:944817`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:255977-256435:+; feature_type=gene
