---
entity_id: "gene.b4451"
entity_type: "gene"
name: "ryhB"
source_database: "NCBI RefSeq"
source_id: "gene-b4451"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4451"
  - "ryhB"
---

# ryhB

`gene.b4451`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4451`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ryhB (gene.b4451) is a gene entity. EcoCyc product frame: SRAI-RNA. EcoCyc synonyms: psrA18, IS176, sraI. Genomic coordinates: 3580922-3581016.

## Biological Role

Repressed by fur (protein.P0A9A9). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (29)

- `activates` --> [[gene.b1981|gene.b1981]] `RegulonDB` `S` - regulator=RyhB; target=shiA; function=+
- `activates` --> [[gene.b2155|gene.b2155]] `RegulonDB` `S` - regulator=RyhB; target=cirA; function=+
- `represses` --> [[gene.b0156|gene.b0156]] `RegulonDB` `S` - regulator=RyhB; target=erpA; function=-
- `represses` --> [[gene.b0683|gene.b0683]] `RegulonDB` `S` - regulator=RyhB; target=fur; function=-
- `represses` --> [[gene.b0724|gene.b0724]] `RegulonDB` `S` - regulator=RyhB; target=sdhB; function=-
- `represses` --> [[gene.b0729|gene.b0729]] `RegulonDB` `S` - regulator=RyhB; target=sucD; function=-
- `represses` --> [[gene.b1656|gene.b1656]] `RegulonDB` `S` - regulator=RyhB; target=sodB; function=-
- `represses` --> [[gene.b1778|gene.b1778]] `RegulonDB` `S` - regulator=RyhB; target=msrB; function=-
- `represses` --> [[gene.b2276|gene.b2276]] `RegulonDB` `S` - regulator=RyhB; target=nuoN; function=-
- `represses` --> [[gene.b2277|gene.b2277]] `RegulonDB` `S` - regulator=RyhB; target=nuoM; function=-
- `represses` --> [[gene.b2278|gene.b2278]] `RegulonDB` `S` - regulator=RyhB; target=nuoL; function=-
- `represses` --> [[gene.b2279|gene.b2279]] `RegulonDB` `S` - regulator=RyhB; target=nuoK; function=-
- `represses` --> [[gene.b2280|gene.b2280]] `RegulonDB` `S` - regulator=RyhB; target=nuoJ; function=-
- `represses` --> [[gene.b2281|gene.b2281]] `RegulonDB` `S` - regulator=RyhB; target=nuoI; function=-
- `represses` --> [[gene.b2282|gene.b2282]] `RegulonDB` `S` - regulator=RyhB; target=nuoH; function=-
- `represses` --> [[gene.b2283|gene.b2283]] `RegulonDB` `S` - regulator=RyhB; target=nuoG; function=-
- `represses` --> [[gene.b2284|gene.b2284]] `RegulonDB` `S` - regulator=RyhB; target=nuoF; function=-
- `represses` --> [[gene.b2285|gene.b2285]] `RegulonDB` `S` - regulator=RyhB; target=nuoE; function=-
- `represses` --> [[gene.b2286|gene.b2286]] `RegulonDB` `S` - regulator=RyhB; target=nuoC; function=-
- `represses` --> [[gene.b2287|gene.b2287]] `RegulonDB` `S` - regulator=RyhB; target=nuoB; function=-
- `represses` --> [[gene.b2288|gene.b2288]] `RegulonDB` `S` - regulator=RyhB; target=nuoA; function=-
- `represses` --> [[gene.b2528|gene.b2528]] `RegulonDB` `S` - regulator=RyhB; target=iscA; function=-
- `represses` --> [[gene.b2529|gene.b2529]] `RegulonDB` `S` - regulator=RyhB; target=iscU; function=-
- `represses` --> [[gene.b2530|gene.b2530]] `RegulonDB` `S` - regulator=RyhB; target=iscS; function=-
- `represses` --> [[gene.b2531|gene.b2531]] `RegulonDB` `S` - regulator=RyhB; target=iscR; function=-
- `represses` --> [[gene.b3365|gene.b3365]] `RegulonDB` `S` - regulator=RyhB; target=nirB; function=-
- `represses` --> [[gene.b3607|gene.b3607]] `RegulonDB` `S` - regulator=RyhB; target=cysE; function=-
- `represses` --> [[gene.b4637|gene.b4637]] `RegulonDB` `S` - regulator=RyhB; target=uof; function=-
- `represses` --> [[gene.b4764|gene.b4764]] `RegulonDB` `S` - regulator=RyhB; target=sdhX; function=-

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ryhB; function=+
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `C` - regulator=Fur; target=ryhB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0047271,ECOCYC:G0-8872,GeneID:2847761`
- `gbkey:Gene`
- `gene_biotype:ncRNA`

## Notes

NC_000913.3:3580922-3581016:-; feature_type=gene
