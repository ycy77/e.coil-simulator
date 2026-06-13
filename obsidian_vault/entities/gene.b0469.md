---
entity_id: "gene.b0469"
entity_type: "gene"
name: "apt"
source_database: "NCBI RefSeq"
source_id: "gene-b0469"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0469"
  - "apt"
---

# apt

`gene.b0469`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0469`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

apt (gene.b0469) is a gene entity. It encodes apt (protein.P69503). Encoded protein function: FUNCTION: Catalyzes a salvage reaction resulting in the formation of AMP, that is energically less costly than de novo synthesis. EcoCyc product frame: ADENPRIBOSYLTRAN-MONOMER. Genomic coordinates: 491412-491963. EcoCyc protein note: Adenine phosphoribosyltransferase is a purine salvage enzyme which catalyzes the transfer of the ribosyl-5-phosphate group from PRPP to the N9 position of adenine to yield AMP. APRT is one of three E. coli phosphoribosyltransferases (PRTases) that participate in purine salvage, Gpt, Hpt and Apt . Enzyme activity is induced by growth on purines, amethopterin, and thymine and is higher in stationary phase cultures. The enzyme is subject to negative regulation by uncyclized nucleoside 5'-phosphates and end product inhibition . Adenine phosphoribosyltransferase is cytoplasmic , but can be found associated with isolated membrane vesicles . Apt: "adenine phosphoribosyltransferase"

## Biological Role

Repressed by glaR (protein.P37338).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69503|protein.P69503]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=apt; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001628,ECOCYC:EG10051,GeneID:945113`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:491412-491963:+; feature_type=gene
