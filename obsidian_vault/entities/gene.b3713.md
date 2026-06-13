---
entity_id: "gene.b3713"
entity_type: "gene"
name: "yieF"
source_database: "NCBI RefSeq"
source_id: "gene-b3713"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3713"
  - "yieF"
---

# yieF

`gene.b3713`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3713`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yieF (gene.b3713) is a gene entity. It encodes chrR (protein.P0AGE6). Encoded protein function: FUNCTION: Catalyzes the reduction of quinones (PubMed:14766567). Acts by simultaneous two-electron transfer, avoiding formation of highly reactive semiquinone intermediates and producing quinols that promote tolerance of H(2)O(2). Quinone reduction is probably the primary biological role of ChrR (By similarity). Can also reduce toxic chromate to insoluble and less toxic Cr(3+). Catalyzes the transfer of three electrons to Cr(6+) producing Cr(3+) and one electron to molecular oxygen without producing the toxic Cr(5+) species and only producing a minimal amount of reactive oxygen species (ROS). Chromate reduction protects the cell against chromate toxicity, but is likely a secondary activity (PubMed:14766567, PubMed:17088379, PubMed:22558308). Can also reduce potassium ferricyanide, 2,6-dichloroindophenol, V(5+), Mo(6+), methylene blue, cytochrome c and U(6+) (PubMed:14766567, PubMed:17088379). During chromate reduction, is able to use both NAD or NADP equally well (PubMed:14766567). {ECO:0000250|UniProtKB:Q88FF8, ECO:0000269|PubMed:14766567, ECO:0000269|PubMed:17088379, ECO:0000269|PubMed:22558308}. EcoCyc product frame: EG11723-MONOMER. EcoCyc synonyms: chrR. Genomic coordinates: 3894652-3895218...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGE6|protein.P0AGE6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yieF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012146,ECOCYC:EG11723,GeneID:948225`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3894652-3895218:+; feature_type=gene
