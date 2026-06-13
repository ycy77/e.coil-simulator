---
entity_id: "gene.b1521"
entity_type: "gene"
name: "uxaB"
source_database: "NCBI RefSeq"
source_id: "gene-b1521"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1521"
  - "uxaB"
---

# uxaB

`gene.b1521`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1521`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uxaB (gene.b1521) is a gene entity. It encodes uxaB (protein.P0A6L7). Encoded protein function: Altronate oxidoreductase (EC 1.1.1.58) (Tagaturonate dehydrogenase) (Tagaturonate reductase) EcoCyc product frame: ALTRO-OXIDOREDUCT-MONOMER. Genomic coordinates: 1609229-1610680. EcoCyc protein note: Altronate oxidoreductase is the second enzyme of the galacturonate catabolism pathway, catalyzing the reversible NADH-dependent reduction of D-tagaturonate to D-altronate . The reaction proceeds via an ordered bi-bi mechanism with NADH as the first substrate . Expression of uxaB is repressed by ExuR , induced by galacturonate , and is sensitive to catabolite repression . In a crp mutant selected for increased acetate tolerance, expression of uxaB is decreased during exposure to acetate. Overexpression of uxaB in a wild type strain decreases its growth rate under acetate stress .

## Biological Role

Activated by rpoD (protein.P00579), fur (protein.P0A9A9).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6L7|protein.P0A6L7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=uxaB; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=uxaB; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005076,ECOCYC:EG11065,GeneID:945542`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1609229-1610680:-; feature_type=gene
