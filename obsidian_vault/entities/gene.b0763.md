---
entity_id: "gene.b0763"
entity_type: "gene"
name: "modA"
source_database: "NCBI RefSeq"
source_id: "gene-b0763"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0763"
  - "modA"
---

# modA

`gene.b0763`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0763`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

modA (gene.b0763) is a gene entity. It encodes modA (protein.P37329). Encoded protein function: FUNCTION: Part of the ABC transporter complex ModABC involved in the transport of molybdenum into the cell (PubMed:8576221). Binds molybdate with high affinity in vitro and with a similar affinity in vivo (PubMed:21784948, PubMed:21861186, PubMed:28150901, PubMed:8409926, PubMed:8576221, PubMed:9545596). Binds tungstate with high affinity in vitro (PubMed:21784948, PubMed:28150901, PubMed:8576221, PubMed:9545596). Binds unnatural anion perrhenate with high affinity in vitro (PubMed:21861186). Does not bind sulfate, phosphate, arsenate, selenate, chlorate, metavanadate, nitrate, perchlorate, permanganate or carbonate (PubMed:28150901, PubMed:8576221, PubMed:9545596). {ECO:0000269|PubMed:21784948, ECO:0000269|PubMed:21861186, ECO:0000269|PubMed:28150901, ECO:0000269|PubMed:8409926, ECO:0000269|PubMed:8576221, ECO:0000269|PubMed:9545596}. EcoCyc product frame: MODA-MONOMER. Genomic coordinates: 795089-795862. EcoCyc protein note: ModA is the periplasmic binding protein of an ABC transporter that mediates the high affinity uptake of molybdate. Purified ModA binds molybdate and tungstate with similar high affinities and in a 1:1 ratio; it does not bind sulfate, phosphate, selenate nor chlorate...

## Biological Role

Repressed by modE (protein.P0A9G8). Activated by rpoD (protein.P00579), lrp (protein.P0ACJ0).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37329|protein.P37329]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=modA; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=modA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0002601,ECOCYC:EG12427,GeneID:945364`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:795089-795862:+; feature_type=gene
