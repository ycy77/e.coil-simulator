---
entity_id: "gene.b4513"
entity_type: "gene"
name: "kdpF"
source_database: "NCBI RefSeq"
source_id: "gene-b4513"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4513"
  - "kdpF"
---

# kdpF

`gene.b4513`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4513`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

kdpF (gene.b4513) is a gene entity. It encodes kdpF (protein.P36937). Encoded protein function: FUNCTION: Part of the high-affinity ATP-driven potassium transport (or Kdp) system, which catalyzes the hydrolysis of ATP coupled with the electrogenic transport of potassium into the cytoplasm (PubMed:23930894). This subunit may be involved in stabilization of the complex (PubMed:10608856). {ECO:0000269|PubMed:10608856, ECO:0000269|PubMed:23930894}. EcoCyc product frame: MONOMER0-12. Genomic coordinates: 728732-728821. EcoCyc protein note: KdpF is a small membrane protein that is part of a potassium ion transporting P-type ATPase complex. KdpF may function to stabilise the transporter complex; inactivation of kdpF does not affect growth under low potassium conditions (0.1 mM K+) however the purified complex lacking KdpF exhibits significantly decreased K+-stimulated ATPase activity; addition of purified KdpF restores K+-stimulated ATPase activity to near wild type levels, as does the addition of E. coli lipids . KdpF is predicted to be a bitopic inner membrane protein .

## Biological Role

Activated by rpoD (protein.P00579), kdpE (protein.P21866).

## Enriched Pathways

- `eco02020` Two-component system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36937|protein.P36937]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=kdpF; function=+
- `activates` <-- [[protein.P21866|protein.P21866]] `RegulonDB` `C` - regulator=KdpE; target=kdpF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0285034,ECOCYC:G0-10439,GeneID:948946`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:728732-728821:-; feature_type=gene
