---
entity_id: "gene.b0486"
entity_type: "gene"
name: "ybaT"
source_database: "NCBI RefSeq"
source_id: "gene-b0486"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0486"
  - "ybaT"
---

# ybaT

`gene.b0486`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0486`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ybaT (gene.b0486) is a gene entity. It encodes ybaT (protein.P77400). Encoded protein function: FUNCTION: Probable amino-acid or metabolite transport protein. EcoCyc product frame: B0486-MONOMER. Genomic coordinates: 512576-513868. EcoCyc protein note: ybaT encodes a putative transporter that is implicated in copper tolerance. ybaT is induced when a ΔcopA strain is grown in copper supplemented medium (ie. under conditions of copper stress); YbaT and CPLX0-7694 are required for the protective effect of exogenous glutamine in rescuing a ΔcopA mutant from copper stress at acid pH . An increase in intracellular copper impairs acid tolerance by disrupting glutamate synthesis via GLUTAMATESYN-CPLX; in the presence of exogenous glutamine, YbaT and glutaminase I may function to alleviate this block in glutamate synthesis . YbaT is a putative transporter belonging to the Archaeal/Bacterial Transporter (ABT) Family within the Amino Acid-Polyamine-Organocation (APC) Superfamily . ybaT is a member of the acid induced GadX regulon .

## Biological Role

Activated by rpoS (protein.P13445), gadX (protein.P37639).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P77400|protein.P77400]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ybaT; function=+
- `activates` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=ybaT; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001690,ECOCYC:G6262,GeneID:945363`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:512576-513868:+; feature_type=gene
