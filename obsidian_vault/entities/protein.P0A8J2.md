---
entity_id: "protein.P0A8J2"
entity_type: "protein"
name: "dnaT"
source_database: "UniProt"
source_id: "P0A8J2"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dnaT b4362 JW4326"
---

# dnaT

`protein.P0A8J2`

## Static

- Type: `protein`
- Source: `UniProt:P0A8J2`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in the restart of stalled replication forks, which reloads the DnaB replicative helicase on sites other than the origin of replication (PubMed:8663104, PubMed:8663105, PubMed:8663106). Functions in the PriA-PriB and PriA-PriC restart pathways, but probably not in the PriC-Rep pathway (PubMed:15238512). Displaces ssDNA from a PriB-ssDNA complex (PubMed:25265331, PubMed:30659961). Also involved in inducing stable DNA replication during SOS response. It forms, in concert with DnaC protein and other prepriming proteins DnaB, PriA, PriB and PriC a prepriming protein complex on the specific site of the template DNA recognized by PriA (PubMed:8663104, PubMed:8663105). Binds single-stranded (ss)DNA in a cooperative manner; both the N- and C-terminal domains are required for cooperativity (PubMed:15238512, PubMed:25053836). Forms a spiral filament on ssDNA (PubMed:25053836). {ECO:0000269|PubMed:15238512, ECO:0000269|PubMed:25053836, ECO:0000269|PubMed:30659961, ECO:0000269|PubMed:8663104, ECO:0000269|PubMed:8663105, ECO:0000269|PubMed:8663106}.

## Biological Role

Component of replication restart protein DnaT (complex.ecocyc.CPLX0-0), DNA replication restart primosome (complex.ecocyc.CPLX0-3922).

## Enriched Pathways

- `eco03440` Homologous recombination (KEGG)

## Annotation

FUNCTION: Involved in the restart of stalled replication forks, which reloads the DnaB replicative helicase on sites other than the origin of replication (PubMed:8663104, PubMed:8663105, PubMed:8663106). Functions in the PriA-PriB and PriA-PriC restart pathways, but probably not in the PriC-Rep pathway (PubMed:15238512). Displaces ssDNA from a PriB-ssDNA complex (PubMed:25265331, PubMed:30659961). Also involved in inducing stable DNA replication during SOS response. It forms, in concert with DnaC protein and other prepriming proteins DnaB, PriA, PriB and PriC a prepriming protein complex on the specific site of the template DNA recognized by PriA (PubMed:8663104, PubMed:8663105). Binds single-stranded (ss)DNA in a cooperative manner; both the N- and C-terminal domains are required for cooperativity (PubMed:15238512, PubMed:25053836). Forms a spiral filament on ssDNA (PubMed:25053836). {ECO:0000269|PubMed:15238512, ECO:0000269|PubMed:25053836, ECO:0000269|PubMed:30659961, ECO:0000269|PubMed:8663104, ECO:0000269|PubMed:8663105, ECO:0000269|PubMed:8663106}.

## Pathways

- `eco03440` Homologous recombination (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-0|complex.ecocyc.CPLX0-0]] `EcoCyc` `database` - EcoCyc component coefficient=3 | EcoCyc protcplxs.col coefficient=3
- `is_component_of` --> [[complex.ecocyc.CPLX0-3922|complex.ecocyc.CPLX0-3922]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=3

## Incoming Edges (1)

- `encodes` <-- [[gene.b4362|gene.b4362]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8J2`
- `KEGG:ecj:JW4326;eco:b4362;ecoc:C3026_23565;`
- `GeneID:93777486;948813;`
- `GO:GO:0000287; GO:0003697; GO:0006260; GO:0006261; GO:0006269; GO:0031297; GO:0042802; GO:0070207; GO:1990077; GO:1990158; GO:1990159`

## Notes

Replication restart protein DnaT (Primosomal protein DnaT) (Primosomal protein i)
