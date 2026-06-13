---
entity_id: "gene.b4194"
entity_type: "gene"
name: "ulaB"
source_database: "NCBI RefSeq"
source_id: "gene-b4194"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4194"
  - "ulaB"
---

# ulaB

`gene.b4194`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4194`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ulaB (gene.b4194) is a gene entity. It encodes ulaB (protein.P69822). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II UlaABC PTS system is involved in ascorbate transport. {ECO:0000269|PubMed:12644495, ECO:0000305|PubMed:11741871}. EcoCyc product frame: YJFT-MONOMER. EcoCyc synonyms: yjfT, sgaB. Genomic coordinates: 4421393-4421698. EcoCyc protein note: ulaB encodes a hydrohilic protein that contains a PTS Enzyme IIB domain and a putative cysteine phosphorylation site (Cys9) . A ulaB deletion mutant is unable to transport or ferment L-ascorbate in vivo or to phosphorylate L-ascorbate in vitro . ulaB utilization of L-ascorbate

## Biological Role

Repressed by ulaR (protein.P0A9W0). Activated by crp (protein.P0ACJ8).

## Enriched Pathways

- `eco00053` Ascorbate and aldarate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69822|protein.P69822]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ulaB; function=+
- `represses` <-- [[protein.P0A9W0|protein.P0A9W0]] `RegulonDB` `C` - regulator=UlaR; target=ulaB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013725,ECOCYC:EG12494,GeneID:948716`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4421393-4421698:+; feature_type=gene
