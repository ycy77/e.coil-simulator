---
entity_id: "gene.b4161"
entity_type: "gene"
name: "rsgA"
source_database: "NCBI RefSeq"
source_id: "gene-b4161"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4161"
  - "rsgA"
---

# rsgA

`gene.b4161`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4161`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

rsgA (gene.b4161) is a gene entity. It encodes rsgA (protein.P39286). Encoded protein function: FUNCTION: One of at least 4 proteins (Era, RbfA, RimM and RsgA/YjeQ) that assist in the late maturation steps of the functional core of the 30S ribosomal subunit (PubMed:18223068, PubMed:21102555, PubMed:21303937, PubMed:25904134, PubMed:27382067). Binds the 30S subunit contacting the head, platform, and rRNA helix 44, which may assist the last maturation stages (PubMed:21788480, PubMed:21960487). Removes RbfA from mature, but not immature 30S ribosomes in a GTP-dependent manner; 95% removal in the presence of GTP, 90% removal in GMP-PNP and 65% removal in the presence of GDP (PubMed:21102555, PubMed:25904134). Circulary permuted GTPase that catalyzes rapid hydrolysis of GTP with a slow catalytic turnover (PubMed:12220175). Dispensible for viability, but important for overall fitness. The intrinsic GTPase activity is stimulated by the presence of 30S (160-fold increase in kcat) or 70S (96-fold increase in kcat) ribosomes (PubMed:14973029). Mature 30S ribosomes stimulate intrinsic GTPase more than do immature 30S ribosomes (PubMed:25904134). Ribosome-associated GTPase activity is stimulated by RbfA (PubMed:21102555). The GTPase is inhibited by aminoglycoside antibiotics such as neomycin and paromycin (PubMed:15466596) streptomycin and spectinomycin (PubMed:15828870)...

## Biological Role

Repressed by glaR (protein.P37338).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39286|protein.P39286]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P37338|protein.P37338]] `RegulonDB` `S` - regulator=GlaR; target=rsgA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013626,ECOCYC:G7841,GeneID:948674`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4390457-4391509:-; feature_type=gene
