---
entity_id: "gene.b3065"
entity_type: "gene"
name: "rpsU"
source_database: "NCBI RefSeq"
source_id: "gene-b3065"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3065"
  - "rpsU"
---

# rpsU

`gene.b3065`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3065`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rpsU (gene.b3065) is a gene entity. It encodes rpsU (protein.P68679). Encoded protein function: FUNCTION: Probbly involved in recognition of ribosome rescue factor SmrB in stalled/collided disomes; fusion of protein fragments to its N-terminus decreases ribosome rescue in the presence of SmrB (PubMed:35264790). {ECO:0000305|PubMed:35264790}. EcoCyc product frame: EG10920-MONOMER. Genomic coordinates: 3210781-3210996. EcoCyc protein note: The S21 protein is a component of the 30S subunit of the ribosome. S21 was found to associate with the 50S subunit of the ribosome as well as the 30S subunit . Interactions between S21 and 16S rRNA have been mapped . S21 also crosslinks to the 4.5S RNA of the signal recognition particle . Interactions between S21 and mRNA can be shown by fluorescence energy transfer and crosslinking . S21 is required for full activity of translation initiation . S21 was also shown to crosslink to IF3 . Processing and degradation of the rpsU-dnaG-rpoD operon mRNA has been studied; see for example and references therein. Review:

## Biological Role

Repressed by lexA (protein.P0A7C2), yfeC (protein.P0AD37). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco03010` Ribosome (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P68679|protein.P68679]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=rpsU; function=+
- `represses` <-- [[protein.P0A7C2|protein.P0A7C2]] `RegulonDB` `S` - regulator=LexA; target=rpsU; function=-
- `represses` <-- [[protein.P0AD37|protein.P0AD37]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0010063,ECOCYC:EG10920,GeneID:947577`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3210781-3210996:+; feature_type=gene
