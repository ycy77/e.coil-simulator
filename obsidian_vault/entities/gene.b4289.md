---
entity_id: "gene.b4289"
entity_type: "gene"
name: "fecC"
source_database: "NCBI RefSeq"
source_id: "gene-b4289"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4289"
  - "fecC"
---

# fecC

`gene.b4289`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4289`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fecC (gene.b4289) is a gene entity. It encodes fecC (protein.P15030). Encoded protein function: FUNCTION: Part of the ABC transporter complex FecBCDE involved in citrate-dependent Fe(3+) uptake (PubMed:17660286, PubMed:2651410). Probably responsible for the translocation of the substrate across the membrane (Probable). {ECO:0000269|PubMed:17660286, ECO:0000269|PubMed:2651410, ECO:0000305}. EcoCyc product frame: FECC-MONOMER. Genomic coordinates: 4512411-4513409. EcoCyc protein note: FecC is one of two (along with FecD) integral membrane proteins of the iron dicitrate ABC transport system. fecC encodes a hydrophobic inner membrane protein; FecC has 34% identity with FecD and also shows similarity to FhuB of the iron(III) hydroxamate uptake system and BtuC of the Vitamin B uptake system

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by fecI (protein.P23484).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15030|protein.P15030]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P23484|protein.P23484]] `RegulonDB` `C` - sigma=sigma19; target=fecC; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=fecC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014063,ECOCYC:EG10288,GeneID:948826`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4512411-4513409:-; feature_type=gene
