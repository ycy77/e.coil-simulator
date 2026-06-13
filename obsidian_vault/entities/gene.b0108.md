---
entity_id: "gene.b0108"
entity_type: "gene"
name: "ppdD"
source_database: "NCBI RefSeq"
source_id: "gene-b0108"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0108"
  - "ppdD"
---

# ppdD

`gene.b0108`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0108`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ppdD (gene.b0108) is a gene entity. It encodes ppdD (protein.P36647). Encoded protein function: FUNCTION: Major component of the type IV pilus (T4P) that plays a role in cell adhesion and motility. Not produced when grown under standard laboratory conditions. {ECO:0000269|PubMed:10633126}. EcoCyc product frame: EG12107-MONOMER. Genomic coordinates: 117109-117549. EcoCyc protein note: ppdD encodes a putative Type IV major pilin subunit; ppdD is poorly expressed under standard conditions. Expression of cloned ppdD or cloned ppdD-hofB-hofC does not result in the production of detectable pili, but immunogold labeling suggests that PpdD is exposed on the cell surface. PpdD is able to form type IV pili when expressed in Pseudomonas aeruginosa . PpdD shares over 95% identity with the major type IV pilin subunit, HcpA from enterohemorrhagic E. coli O157:H7 . ppdD is not required for spontaneous plasmid transformation on nutrient plates with high agar concentration .

## Biological Role

Activated by crp (protein.P0ACJ8).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P36647|protein.P36647]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ppdD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000372,ECOCYC:EG12107,GeneID:945817`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:117109-117549:-; feature_type=gene
