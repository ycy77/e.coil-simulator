---
entity_id: "gene.b0782"
entity_type: "gene"
name: "moaB"
source_database: "NCBI RefSeq"
source_id: "gene-b0782"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0782"
  - "moaB"
---

# moaB

`gene.b0782`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0782`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

moaB (gene.b0782) is a gene entity. It encodes moaB (protein.P0AEZ9). Encoded protein function: FUNCTION: May be involved in the biosynthesis of molybdopterin. Can bind GTP and has low GTPase activity. Can bind MPT, but has no MPT adenylyl transferase activity. EcoCyc product frame: MONOMER0-1501. EcoCyc synonyms: chlA2. Genomic coordinates: 818055-818567.

## Biological Role

Activated by fnr (protein.P0A9E5), modE (protein.P0A9G8), csrA (protein.P69913).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)
- `eco04122` Sulfur relay system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEZ9|protein.P0AEZ9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=moaB; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `S` - regulator=ModE; target=moaB; function=+
- `activates` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `C` - regulator=CsrA; target=moaB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0002671,ECOCYC:EG11596,GeneID:945396`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:818055-818567:+; feature_type=gene
