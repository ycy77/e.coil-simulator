---
entity_id: "gene.b4131"
entity_type: "gene"
name: "cadA"
source_database: "NCBI RefSeq"
source_id: "gene-b4131"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4131"
  - "cadA"
---

# cadA

`gene.b4131`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4131`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cadA (gene.b4131) is a gene entity. It encodes cadA (protein.P0A9H3). Encoded protein function: FUNCTION: Inducible lysine decarboxylase that catalyzes the proton-dependent decarboxylation of L-lysine to produce the polyamine cadaverine and carbon dioxide (PubMed:4590109). Plays a role in pH homeostasis by consuming protons and neutralizing the acidic by-products of carbohydrate fermentation (PubMed:17209032). {ECO:0000269|PubMed:17209032, ECO:0000269|PubMed:4590109}. EcoCyc product frame: LYSDECARBOX-MONOMER. EcoCyc synonyms: ldcI. Genomic coordinates: 4356470-4358617.

## Biological Role

Repressed by ompR (protein.P0AA16), hns (protein.P0ACF8). Activated by soxS (protein.P0A9E2), lrp (protein.P0ACJ0), cadC (protein.P23890).

## Enriched Pathways

- `eco00310` Lysine degradation (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9H3|protein.P0A9H3]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `RegulonDB` `S` - regulator=Lrp; target=cadA; function=+
- `activates` <-- [[protein.P23890|protein.P23890]] `RegulonDB` `S` - regulator=CadC; target=cadA; function=+
- `represses` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=cadA; function=-
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=cadA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013526,ECOCYC:EG10131,GeneID:948643`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4356470-4358617:-; feature_type=gene
