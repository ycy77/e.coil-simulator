---
entity_id: "gene.b3547"
entity_type: "gene"
name: "yhjX"
source_database: "NCBI RefSeq"
source_id: "gene-b3547"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3547"
  - "yhjX"
---

# yhjX

`gene.b3547`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3547`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yhjX (gene.b3547) is a gene entity. It encodes yhjX (protein.P37662). Encoded protein function: FUNCTION: Part of a nutrient-sensing regulatory network composed of the two-component regulatory systems BtsS/BtsR and YpdA/YpdB, and their respective target proteins, BtsT and YhjX. {ECO:0000269|PubMed:24659770}. EcoCyc product frame: YHJX-MONOMER. Genomic coordinates: 3710799-3712007. EcoCyc protein note: Expression of yhjX is induced in cells over-producing the G7244-MONOMER . A yhjX-lux reporter construct is not expressed in a pyrSRypdC deletion mutant; yhj-lux expression is induced in response to pyruvate and in medium containing gluconate or glucuronate as the sole carbon source . yhjX is expressed transiently at the onset of stationary phase during growth in an amino acid rich medium . yhjX shows heterogeneous activation at the onset of stationary phase during growth in LB medium; the degree of heterogeneity is influenced by external pyruvate concentration . The PyrR binding site in the yhjX promoter has been characterised . In the Transporter Classification Database, YhjX is a member of the Oxalate:Formate Antiporter (OFA) Family within the Major Facilitator Superfamily (MFS) . YhjX is implicated in pyruvate reassimilation in an n-butanol producing strain of E. coli...

## Biological Role

Activated by rpoD (protein.P00579), ypdB (protein.P0AE39).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37662|protein.P37662]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yhjX; function=+
- `activates` <-- [[protein.P0AE39|protein.P0AE39]] `RegulonDB` `C` - regulator=PyrR; target=yhjX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011586,ECOCYC:EG12268,GeneID:948066`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3710799-3712007:-; feature_type=gene
