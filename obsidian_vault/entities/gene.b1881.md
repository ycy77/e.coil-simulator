---
entity_id: "gene.b1881"
entity_type: "gene"
name: "cheZ"
source_database: "NCBI RefSeq"
source_id: "gene-b1881"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1881"
  - "cheZ"
---

# cheZ

`gene.b1881`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1881`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cheZ (gene.b1881) is a gene entity. It encodes cheZ (protein.P0A9H9). Encoded protein function: FUNCTION: Plays an important role in bacterial chemotaxis signal transduction pathway by accelerating the dephosphorylation of phosphorylated CheY (CheY-P). {ECO:0000269|PubMed:10852888, ECO:0000269|PubMed:8820640}. EcoCyc product frame: CHEZ-MONOMER. Genomic coordinates: 1966393-1967037.

## Biological Role

Activated by fliA (protein.P0AEM6).

## Enriched Pathways

- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9H9|protein.P0A9H9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AEM6|protein.P0AEM6]] `RegulonDB` `S` - sigma=sigma28; target=cheZ; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006278,ECOCYC:EG10151,GeneID:946392`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1966393-1967037:-; feature_type=gene
