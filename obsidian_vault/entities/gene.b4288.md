---
entity_id: "gene.b4288"
entity_type: "gene"
name: "fecD"
source_database: "NCBI RefSeq"
source_id: "gene-b4288"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4288"
  - "fecD"
---

# fecD

`gene.b4288`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4288`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fecD (gene.b4288) is a gene entity. It encodes fecD (protein.P15029). Encoded protein function: FUNCTION: Part of the ABC transporter complex FecBCDE involved in citrate-dependent Fe(3+) uptake (PubMed:17660286, PubMed:2651410). Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:17660286, ECO:0000269|PubMed:2651410, ECO:0000305}. EcoCyc product frame: FECD-MONOMER. Genomic coordinates: 4511458-4512414. EcoCyc protein note: FecD is one of two (along with FecC) integral membrane proteins of the iron dicitrate ABC transport system. fecD encodes a hydrophobic inner membrane protein; FecD has 34% identity with FecC and also shows similarity to FhuB of the iron(III) hydroxamate uptake system and BtuC of the Vitamin B uptake system

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by fecI (protein.P23484).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15029|protein.P15029]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P23484|protein.P23484]] `RegulonDB` `C` - sigma=sigma19; target=fecD; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=fecD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014059,ECOCYC:EG10289,GeneID:946816`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4511458-4512414:-; feature_type=gene
