---
entity_id: "gene.b3931"
entity_type: "gene"
name: "hslU"
source_database: "NCBI RefSeq"
source_id: "gene-b3931"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3931"
  - "hslU"
---

# hslU

`gene.b3931`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3931`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hslU (gene.b3931) is a gene entity. It encodes hslU (protein.P0A6H5). Encoded protein function: FUNCTION: ATPase subunit of a proteasome-like degradation complex; this subunit has chaperone activity. The binding of ATP and its subsequent hydrolysis by HslU are essential for unfolding of protein substrates subsequently hydrolyzed by HslV. HslU recognizes the N-terminal part of its protein substrates and unfolds these before they are guided to HslV for hydrolysis. {ECO:0000269|PubMed:10419524, ECO:0000269|PubMed:10452560, ECO:0000269|PubMed:15696175, ECO:0000269|PubMed:8650174, ECO:0000269|PubMed:8662828, ECO:0000269|PubMed:9288941, ECO:0000269|PubMed:9393683}. EcoCyc product frame: EG11881-MONOMER. EcoCyc synonyms: clpY, htpI. Genomic coordinates: 4120416-4121747.

## Biological Role

Activated by rpoH (protein.P0AGB3).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6H5|protein.P0A6H5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=hslU; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012843,ECOCYC:EG11881,GeneID:948430`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4120416-4121747:-; feature_type=gene
