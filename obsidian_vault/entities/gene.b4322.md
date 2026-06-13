---
entity_id: "gene.b4322"
entity_type: "gene"
name: "uxuA"
source_database: "NCBI RefSeq"
source_id: "gene-b4322"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4322"
  - "uxuA"
---

# uxuA

`gene.b4322`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4322`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uxuA (gene.b4322) is a gene entity. It encodes uxuA (protein.P24215). Encoded protein function: FUNCTION: Catalyzes the dehydration of D-mannonate. {ECO:0000269|PubMed:3038546}. EcoCyc product frame: MANNONDEHYDRAT-MONOMER. Genomic coordinates: 4551636-4552820. EcoCyc protein note: D-mannonate dehydratase catalyzes the final reaction of the glucuronate branch of the hexuronate degradation pathway . UxuA is monomeric in solution. Crystal structures of the enzyme alone and in complex with D-mannonate have been solved . The enzyme is inducible by glucuronate and fructuronate . Expression of uxuA may be repressed by OxyR . UxuA: "utilization of hexuronate A"

## Biological Role

Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24215|protein.P24215]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=uxuA; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=uxuA; function=+

## External IDs

- `Dbxref:ASAP:ABE-0014173,ECOCYC:EG11066,GeneID:947082`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4551636-4552820:+; feature_type=gene
