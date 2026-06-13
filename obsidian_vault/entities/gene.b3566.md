---
entity_id: "gene.b3566"
entity_type: "gene"
name: "xylF"
source_database: "NCBI RefSeq"
source_id: "gene-b3566"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3566"
  - "xylF"
---

# xylF

`gene.b3566`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3566`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

xylF (gene.b3566) is a gene entity. It encodes xylF (protein.P37387). Encoded protein function: FUNCTION: Involved in the high-affinity D-xylose membrane transport system. Binds with high affinity to xylose. EcoCyc product frame: XYLF-MONOMER. EcoCyc synonyms: xylT. Genomic coordinates: 3731131-3732123. EcoCyc protein note: XylF is the periplasmic binding protein of an ATP-dependent, high-affinity xylose uptake system. Purified XylF binds a sngle molecule of D-xylose with high affinity (Kd = 0.6 µM); XylF binds D-xylose specifically - in a wide range of sugars tested only methyl-α-D-xylofuranoside showed some inhibition of D-xylose binding . XylF consists of two similar globular domains connected by a three-stranded hinge; xylose (as the chair form β-pyranose) binds in the cleft between the two domains . Based on the comparison of XylF-open-apo, XylF-open-xyl and XylF-closed-xyl crystal structures, a description of the conformational change that accompanies ligand binding to XylF is available .

## Biological Role

Activated by xylR (protein.P0ACI3).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37387|protein.P37387]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACI3|protein.P0ACI3]] `RegulonDB` `S` - regulator=XylR; target=xylF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011646,ECOCYC:EG20252,GeneID:948090`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3731131-3732123:+; feature_type=gene
