---
entity_id: "gene.b2310"
entity_type: "gene"
name: "argT"
source_database: "NCBI RefSeq"
source_id: "gene-b2310"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2310"
  - "argT"
---

# argT

`gene.b2310`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2310`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

argT (gene.b2310) is a gene entity. It encodes argT (protein.P09551). Encoded protein function: FUNCTION: Part of the ABC transporter complex HisPMQ-ArgT involved in lysine/arginine/ornithine transport. Binds lysine, arginine and ornithine. Stimulates ATPase activity of HisP. {ECO:0000250|UniProtKB:P02911}. EcoCyc product frame: ARGT-MONOMER. Genomic coordinates: 2427009-2427791. EcoCyc protein note: ArgT is the periplasmic binding protein of an ATP-dependent uptake system for the basic amino acids lysine, arginine and ornithine. E. coli argT is 89% similar to argT from Salmonella typhimurium which encodes a lysing/arginine/ornithine (LAO) periplasmic binding protein . argT is a member of the NtrC regulon; expression is increased in response to nitrogen starvation . argT expression increases during the early response to glucose limitation ). The level of ArgT is decreased after 4hrs exposure to zinc stress . ArgT is induced during stationary phase and further induced in late stationary phase; this induction is reduced in clpP, clpA and clpX protease mutants .

## Biological Role

Repressed by arcA (protein.P0A9Q1). Activated by lrp (protein.P0ACJ0), glnG (protein.P0AFB8).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09551|protein.P09551]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=argT; function=+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB|EcoCyc` `S` - regulator=ArcA; target=argT; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007621,ECOCYC:EG10072,GeneID:949030`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2427009-2427791:-; feature_type=gene
