---
entity_id: "gene.b4195"
entity_type: "gene"
name: "ulaC"
source_database: "NCBI RefSeq"
source_id: "gene-b4195"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4195"
  - "ulaC"
---

# ulaC

`gene.b4195`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4195`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ulaC (gene.b4195) is a gene entity. It encodes ulaC (protein.P69820). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II UlaABC PTS system is involved in ascorbate transport. {ECO:0000269|PubMed:12644495, ECO:0000305|PubMed:11741871}. EcoCyc product frame: YJFU-MONOMER. EcoCyc synonyms: ptxA, yjfU, sgaA. Genomic coordinates: 4421708-4422172. EcoCyc protein note: ulaC contains a PTS Enzyme IIA domain with a predicted active site histidine (his68) that is phosphorylated by the general phosphocarrier protein, HPr . A ulaC deletion mutant is unable to transport or ferment L-ascorbate in vivo or to phosphorylate L-ascorbate in vitro . ulaC: utilization of L-ascorbate .

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

- `encodes` --> [[protein.P69820|protein.P69820]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ulaC; function=+
- `represses` <-- [[protein.P0A9W0|protein.P0A9W0]] `RegulonDB` `S` - regulator=UlaR; target=ulaC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0013727,ECOCYC:EG12495,GeneID:948715`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4421708-4422172:+; feature_type=gene
