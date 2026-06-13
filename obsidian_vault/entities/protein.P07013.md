---
entity_id: "protein.P07013"
entity_type: "protein"
name: "priB"
source_database: "UniProt"
source_id: "P07013"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "priB b4201 JW4159"
---

# priB

`protein.P07013`

## Static

- Type: `protein`
- Source: `UniProt:P07013`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the restart of stalled replication forks, which reloads the replicative helicase (DnaB) on sites other than the origin of replication; the PriA-PriB pathway is the major replication restart pathway (PubMed:11532137, PubMed:37169801, PubMed:22636770). There are several restart pathways, the PriA-PriB pathway is subdivided into 2 distinct pathways (PubMed:34423481). priB and priC have redundant roles in the cell (PubMed:10540288). During primosome assembly it facilitates complex formation between PriA and DnaT on DNA; stabilizes PriA on DNA, presumably by preventing or inhibiting PriA DNA translocation activity (PubMed:8663104, PubMed:8663105, PubMed:8663106). Forms a branched DNA-PriA-PriB complex when the lagging strand is single-stranded (ss)DNA (PubMed:16188886). Binds ssDNA in the presence and absence of ssDNA DNA-binding protein (SSB), does not bind branched structures (PubMed:8366072, PubMed:16188886). DNA binding, forming spiral filaments on ssDNA, is cooperative (PubMed:16899446). Stimulates the helicase activity of PriA (PubMed:16188886, PubMed:37169801, PubMed:34423481). The homodimer binds 12 nucleotides of ssDNA (PubMed:20156448). Binds homo-pyrimidine tracts better than homo-purine tracts (PubMed:15383524, PubMed:20156448)...

## Biological Role

Component of replication restart protein PriB (complex.ecocyc.CPLX0-3), DNA replication restart primosome (complex.ecocyc.CPLX0-3922).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: Involved in the restart of stalled replication forks, which reloads the replicative helicase (DnaB) on sites other than the origin of replication; the PriA-PriB pathway is the major replication restart pathway (PubMed:11532137, PubMed:37169801, PubMed:22636770). There are several restart pathways, the PriA-PriB pathway is subdivided into 2 distinct pathways (PubMed:34423481). priB and priC have redundant roles in the cell (PubMed:10540288). During primosome assembly it facilitates complex formation between PriA and DnaT on DNA; stabilizes PriA on DNA, presumably by preventing or inhibiting PriA DNA translocation activity (PubMed:8663104, PubMed:8663105, PubMed:8663106). Forms a branched DNA-PriA-PriB complex when the lagging strand is single-stranded (ss)DNA (PubMed:16188886). Binds ssDNA in the presence and absence of ssDNA DNA-binding protein (SSB), does not bind branched structures (PubMed:8366072, PubMed:16188886). DNA binding, forming spiral filaments on ssDNA, is cooperative (PubMed:16899446). Stimulates the helicase activity of PriA (PubMed:16188886, PubMed:37169801, PubMed:34423481). The homodimer binds 12 nucleotides of ssDNA (PubMed:20156448). Binds homo-pyrimidine tracts better than homo-purine tracts (PubMed:15383524, PubMed:20156448). {ECO:0000269|PubMed:11532137, ECO:0000269|PubMed:15383524, ECO:0000269|PubMed:16188886, ECO:0000269|PubMed:1646811, ECO:0000269|PubMed:16899446, ECO:0000269|PubMed:1856227, ECO:0000269|PubMed:20156448, ECO:0000269|PubMed:22636770, ECO:0000269|PubMed:34423481, ECO:0000269|PubMed:37169801, ECO:0000269|PubMed:8366072, ECO:0000269|PubMed:8663104, ECO:0000269|PubMed:8663105, ECO:0000269|PubMed:8663106}.; FUNCTION: Genetic interactions among priB, dam, lexA, nagC, polA, rdgB, rdgB, rep and uup link the PriA-PriB replication restart pathway to DNA double-strand break repair. {ECO:0000269|PubMed:36326440}.

## Pathways

- `eco03440` Homologous recombination (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3|complex.ecocyc.CPLX0-3]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.CPLX0-3922|complex.ecocyc.CPLX0-3922]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4201|gene.b4201]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07013`
- `KEGG:ecj:JW4159;eco:b4201;`
- `GeneID:948722;`
- `GO:GO:0003697; GO:0003723; GO:0006260; GO:0006269; GO:0006270; GO:0006276; GO:0009314; GO:0031297; GO:0042802; GO:1990077; GO:1990099; GO:1990158`

## Notes

Replication restart protein PriB (Primosomal replication protein n)
