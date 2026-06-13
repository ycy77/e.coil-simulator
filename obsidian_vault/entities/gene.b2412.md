---
entity_id: "gene.b2412"
entity_type: "gene"
name: "zipA"
source_database: "NCBI RefSeq"
source_id: "gene-b2412"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2412"
  - "zipA"
---

# zipA

`gene.b2412`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2412`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

zipA (gene.b2412) is a gene entity. It encodes zipA (protein.P77173). Encoded protein function: FUNCTION: Essential cell division protein that stabilizes the FtsZ protofilaments by cross-linking them and that serves as a cytoplasmic membrane anchor for the Z ring (PubMed:11847116, PubMed:22164258, PubMed:22304478, PubMed:23233671, PubMed:9008158). Also required for the recruitment to the septal ring of the downstream cell division proteins FtsK, FtsQ, FtsL and FtsN (PubMed:11847116, PubMed:11948172). ZipA overproduction protects FtsZ from degradation by ClpP by preventing recognition by ClpX (PubMed:23233671). Does not affect the GTPase activity of FtsZ (PubMed:10209756). {ECO:0000269|PubMed:10209756, ECO:0000269|PubMed:11847116, ECO:0000269|PubMed:11948172, ECO:0000269|PubMed:22164258, ECO:0000269|PubMed:22304478, ECO:0000269|PubMed:23233671, ECO:0000269|PubMed:9008158}. EcoCyc product frame: G7258-MONOMER. Genomic coordinates: 2530247-2531233. EcoCyc protein note: The ZipA protein is an essential component of the cell division machinery . ZipA localizes to the septal ring structure; this localization requires the presence of the FtsZ ring, but not FtsA , FtsQ , FtsL , or FtsI , indicating that FtsZ recruits ZipA to the cell division site...

## Biological Role

Activated by lrp (protein.P0ACJ0).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77173|protein.P77173]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007942,ECOCYC:G7258,GeneID:946869`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2530247-2531233:-; feature_type=gene
