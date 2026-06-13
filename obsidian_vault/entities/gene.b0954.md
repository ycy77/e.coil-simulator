---
entity_id: "gene.b0954"
entity_type: "gene"
name: "fabA"
source_database: "NCBI RefSeq"
source_id: "gene-b0954"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0954"
  - "fabA"
---

# fabA

`gene.b0954`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0954`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fabA (gene.b0954) is a gene entity. It encodes fabA (protein.P0A6Q3). Encoded protein function: FUNCTION: Necessary for the introduction of cis unsaturation into fatty acids (PubMed:8910376). Catalyzes the dehydration of (3R)-3-hydroxydecanoyl-ACP to (2E)-decenoyl-ACP and then its isomerization to (3Z)-decenoyl-ACP (PubMed:8910376). Can catalyze the dehydratase reaction for beta-hydroxyacyl-ACPs with saturated chain lengths up to 16:0, being most active on intermediate chain length (PubMed:10629181, PubMed:7592873, PubMed:8910376). Is inactive in the dehydration of long chain unsaturated beta-hydroxyacyl-ACP (PubMed:8910376). {ECO:0000269|PubMed:10629181, ECO:0000269|PubMed:7592873, ECO:0000269|PubMed:8910376}. EcoCyc product frame: FABA-MONOMER. Genomic coordinates: 1015952-1016470.

## Biological Role

Repressed by fabR (protein.P0ACU5). Activated by fadR (protein.P0A8V6).

## Enriched Pathways

- `eco00061` Fatty acid biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01212` Fatty acid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6Q3|protein.P0A6Q3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A8V6|protein.P0A8V6]] `RegulonDB` `S` - regulator=FadR; target=fabA; function=+
- `represses` <-- [[protein.P0ACU5|protein.P0ACU5]] `RegulonDB` `C` - regulator=FabR; target=fabA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003229,ECOCYC:EG10273,GeneID:945568`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1015952-1016470:-; feature_type=gene
