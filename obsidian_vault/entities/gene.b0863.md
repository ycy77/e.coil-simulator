---
entity_id: "gene.b0863"
entity_type: "gene"
name: "artI"
source_database: "NCBI RefSeq"
source_id: "gene-b0863"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0863"
  - "artI"
---

# artI

`gene.b0863`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0863`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

artI (gene.b0863) is a gene entity. It encodes artI (protein.P30859). Encoded protein function: FUNCTION: Part of the ABC transporter complex ArtPIQMJ involved in arginine transport. {ECO:0000269|PubMed:8801422}. EcoCyc product frame: ARTI-MONOMER. Genomic coordinates: 902257-902988. EcoCyc protein note: Sequence analysis indicates that ArtI has similarity to the histidine-binding periplasmic protein (HisJ) and lysine/arginine/ornithine binding periplasmic protein (ArgT), both from Salmonella typhimurium. ArtI is also similar to the ArtJ arginine binding periplasmic protein of E. coli. Purified ArtI does not bind any of 20 common amino acids nor does it bind labelled arginine nor putrescine . artI is part of the artMQIP operon which is regulated by the CPLX0-228 "ArgR" repressor in response to arginine . It is assumed to form an ABC transporter of unknown specificity with the ArtMQP membrane components . states that ArtI is the nearest match (followed by ArtJ and HisJ) to a low-affinity arginine-ornithine protein (AbpS) characterized and mapped to min 63 on the E. coli map; artI, artJ and hisJ are located at min 19.4, 19.4, and 52.3 respectively; no gene near min 63 matches the AbpS sequence published; it is possible that MG1655 does not contain abpS .

## Biological Role

Repressed by argR (protein.P0A6D0), lrp (protein.P0ACJ0). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0), rpoS (protein.P13445).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P30859|protein.P30859]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=artI; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=artI; function=+
- `represses` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `C` - regulator=ArgR; target=artI; function=-
- `represses` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0002937,ECOCYC:EG11625,GeneID:948988`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:902257-902988:-; feature_type=gene
