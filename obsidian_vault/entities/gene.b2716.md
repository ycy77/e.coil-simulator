---
entity_id: "gene.b2716"
entity_type: "gene"
name: "ascB"
source_database: "NCBI RefSeq"
source_id: "gene-b2716"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2716"
  - "ascB"
---

# ascB

`gene.b2716`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2716`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ascB (gene.b2716) is a gene entity. It encodes ascB (protein.P24240). Encoded protein function: FUNCTION: Can hydrolyze salicin, cellobiose, and probably arbutin. EcoCyc product frame: EG10085-MONOMER. EcoCyc synonyms: sac. Genomic coordinates: 2840990-2842414. EcoCyc protein note: ascB is thought to encode phospho-β-glucosidase as part of the cryptic asc operon . In a strain evolved for efficient cellobiose utilization , duplication of the ascB ribosome binding site leads to increased expression of AscB . sac: "salicin-arbutin-cellobiose" AscB: "arbutin, salicin, cellobiose"

## Biological Role

Repressed by ascG (protein.P24242). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00500` Starch and sucrose metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P24240|protein.P24240]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ascB; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ascB; function=+
- `represses` <-- [[protein.P24242|protein.P24242]] `RegulonDB` `C` - regulator=AscG; target=ascB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0008928,ECOCYC:EG10085,GeneID:947460`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2840990-2842414:+; feature_type=gene
