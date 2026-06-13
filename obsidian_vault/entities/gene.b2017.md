---
entity_id: "gene.b2017"
entity_type: "gene"
name: "yefM"
source_database: "NCBI RefSeq"
source_id: "gene-b2017"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2017"
  - "yefM"
---

# yefM

`gene.b2017`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2017`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yefM (gene.b2017) is a gene entity. It encodes yefM (protein.P69346). Encoded protein function: FUNCTION: Antitoxin component of a type II toxin-antitoxin (TA) system. Antitoxin that counteracts the effect of the YoeB toxin. YefM binds to the promoter region of the yefM-yeoB operon to repress transcription, YeoB acts as a corepressor. {ECO:0000269|PubMed:14672926, ECO:0000269|PubMed:15009896, ECO:0000269|PubMed:17170003, ECO:0000269|PubMed:19028895}. EcoCyc product frame: EG12844-MONOMER. Genomic coordinates: 2089462-2089713.

## Biological Role

Repressed by yefM (protein.P69346). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69346|protein.P69346]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yefM; function=+
- `represses` <-- [[protein.P69346|protein.P69346]] `RegulonDB` `S` - regulator=YefM; target=yefM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0006705,ECOCYC:EG12844,GeneID:946542`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2089462-2089713:-; feature_type=gene
