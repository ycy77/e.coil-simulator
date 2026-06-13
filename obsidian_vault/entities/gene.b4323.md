---
entity_id: "gene.b4323"
entity_type: "gene"
name: "uxuB"
source_database: "NCBI RefSeq"
source_id: "gene-b4323"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4323"
  - "uxuB"
---

# uxuB

`gene.b4323`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4323`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

uxuB (gene.b4323) is a gene entity. It encodes uxuB (protein.P39160). Encoded protein function: D-mannonate oxidoreductase (EC 1.1.1.57) (Fructuronate reductase) EcoCyc product frame: MANNONOXIDOREDUCT-MONOMER. Genomic coordinates: 4552901-4554361. EcoCyc protein note: D-mannonate oxidoreductase is an enzyme of the D-glucuronate degradation pathway, reducing D-fructuronate to D-mannonate. The reaction proceeds via a rapid-equilibrium random bi-bi + dead-end EBQ complex mechanism . Reports differ on whether or not the enzyme is able to use D-glucuronate as a substrate. Where it was measured, the reaction with D-glucuronate appears to proceed via a different mechanism . The enzyme is induced by both glucuronate and fructuronate ; the internal inducer is fructuronate .

## Biological Role

Repressed by uxuR (protein.P39161). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00040` Pentose and glucuronate interconversions (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P39160|protein.P39160]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=uxuB; function=+
- `represses` <-- [[protein.P39161|protein.P39161]] `RegulonDB` `C` - regulator=UxuR; target=uxuB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0014175,ECOCYC:EG20248,GeneID:946795`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4552901-4554361:+; feature_type=gene
