---
entity_id: "gene.b2499"
entity_type: "gene"
name: "purM"
source_database: "NCBI RefSeq"
source_id: "gene-b2499"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2499"
  - "purM"
---

# purM

`gene.b2499`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2499`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

purM (gene.b2499) is a gene entity. It encodes purM (protein.P08178). Encoded protein function: Phosphoribosylformylglycinamidine cyclo-ligase (EC 6.3.3.1) (AIR synthase) (AIRS) (Phosphoribosyl-aminoimidazole synthetase) EcoCyc product frame: AIRS-MONOMER. EcoCyc synonyms: purG, purI. Genomic coordinates: 2621197-2622234.

## Biological Role

Repressed by fnr (protein.P0A9E5), lrp (protein.P0ACJ0), purR (protein.P0ACP7). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P08178|protein.P08178]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=purM; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=purM; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=purM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008230,ECOCYC:EG10798,GeneID:946975`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2621197-2622234:+; feature_type=gene
