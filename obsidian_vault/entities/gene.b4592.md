---
entity_id: "gene.b4592"
entity_type: "gene"
name: "appX"
source_database: "NCBI RefSeq"
source_id: "gene-b4592"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4592"
  - "appX"
---

# appX

`gene.b4592`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4592`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

appX (gene.b4592) is a gene entity. It encodes appX (protein.P24244). Encoded protein function: FUNCTION: Might be part of cytochrome bd-II oxidase (appB and appC). Able to restore reductant resistance to a cydX deletion mutant upon overexpression. CydX and this protein may have some functional overlap. {ECO:0000269|PubMed:23749980}. EcoCyc product frame: MONOMER0-2817. EcoCyc synonyms: yccB, cbdX. Genomic coordinates: 1040445-1040537. EcoCyc protein note: AppX is a small, single transmembrane, accessory subunit of cytochrome bd-II. AppX and MONOMER0-2663 "CydX" are paralogs and may have overlapping functions in E. coli K-12 . Analysis of intact protein complexes released directly from native membranes indicates that AppX and CydX are able to interact simultaneously with CydAB to form a heterotetramer . In the cryo-EM structure of AppBCX reported by (a homodimer of two AppBCX heterotrimers with inhibitor bound) AppX interacts with AppC and forms the major contact between the two heterotrimers. AppX is expressed during stationary phase . Expression of AppX is higher in minimal glucose medium than in rich medium, increases upon extended heat shock, and is dramatically increased during oxygen-limited growth . AppX is predicted to contain a single transmembrane region; the majority of AppX partitions into the outer membrane fraction using a sucrose fractionation protocol...

## Biological Role

Activated by ydeO (protein.P76135).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24244|protein.P24244]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=appX; function=+

## External IDs

- `Dbxref:ECOCYC:G0-10588,GeneID:948955`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1040445-1040537:+; feature_type=gene
