---
entity_id: "gene.b2005"
entity_type: "gene"
name: "cbtA"
source_database: "NCBI RefSeq"
source_id: "gene-b2005"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2005"
  - "cbtA"
---

# cbtA

`gene.b2005`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2005`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cbtA (gene.b2005) is a gene entity. It encodes cbtA (protein.P64524). Encoded protein function: FUNCTION: Toxic component of a type IV toxin-antitoxin (TA) system (PubMed:14594833, PubMed:21166897, PubMed:22515815, PubMed:28257056, PubMed:28931012). Acts as a dual toxin inhibitor that blocks cell division and cell elongation in genetically separable interactions with FtsZ and MreB (PubMed:28931012). Interacts with cytoskeletal proteins FtsZ and MreB; inhibits FtsZ GTP-dependent polymerization and GTPase activity as well as MreB ATP-dependent polymerization (PubMed:21166897, PubMed:28931012). Binds to both the N- and C-terminus of FtsZ, likely blocking its polymerization and localization, leading to blockage of cell division (PubMed:21166897, PubMed:28931012). Overexpression results in inhibition of growth in liquid cultures and decrease in colony formation; these effects are overcome by concomitant expression of antitoxin CbeA (YeeU) (PubMed:14594833). In other experiments cells swell, by 6 hours are lemon-shaped and by 24 hours those that have not lysed are spherical with diminished polar regions (PubMed:21166897, PubMed:28931012). Toxic effects are neutralized by cognate antitoxin CbeA, although there is no direct interaction between the 2 proteins (PubMed:14594833, PubMed:22515815)...

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P64524|protein.P64524]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (0)

_None._

## External IDs

- `Dbxref:ASAP:ABE-0006659,ECOCYC:G7085,GeneID:946534`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2077569-2077943:+; feature_type=gene
