---
entity_id: "protein.P37329"
entity_type: "protein"
name: "modA"
source_database: "UniProt"
source_id: "P37329"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:8409926, ECO:0000269|PubMed:8576221, ECO:0000269|PubMed:9545596}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "modA b0763 JW0746"
---

# modA

`protein.P37329`

## Static

- Type: `protein`
- Source: `UniProt:P37329`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:8409926, ECO:0000269|PubMed:8576221, ECO:0000269|PubMed:9545596}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex ModABC involved in the transport of molybdenum into the cell (PubMed:8576221). Binds molybdate with high affinity in vitro and with a similar affinity in vivo (PubMed:21784948, PubMed:21861186, PubMed:28150901, PubMed:8409926, PubMed:8576221, PubMed:9545596). Binds tungstate with high affinity in vitro (PubMed:21784948, PubMed:28150901, PubMed:8576221, PubMed:9545596). Binds unnatural anion perrhenate with high affinity in vitro (PubMed:21861186). Does not bind sulfate, phosphate, arsenate, selenate, chlorate, metavanadate, nitrate, perchlorate, permanganate or carbonate (PubMed:28150901, PubMed:8576221, PubMed:9545596). {ECO:0000269|PubMed:21784948, ECO:0000269|PubMed:21861186, ECO:0000269|PubMed:28150901, ECO:0000269|PubMed:8409926, ECO:0000269|PubMed:8576221, ECO:0000269|PubMed:9545596}. ModA is the periplasmic binding protein of an ABC transporter that mediates the high affinity uptake of molybdate. Purified ModA binds molybdate and tungstate with similar high affinities and in a 1:1 ratio; it does not bind sulfate, phosphate, selenate nor chlorate . Although an early study , indicated that ModA does not bind chromate, later work reported that purified ModA binds chromate with high affinity (Kd approx 100 nM)...

## Biological Role

Component of molybdate ABC transporter (complex.ecocyc.ABC-19-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex ModABC involved in the transport of molybdenum into the cell (PubMed:8576221). Binds molybdate with high affinity in vitro and with a similar affinity in vivo (PubMed:21784948, PubMed:21861186, PubMed:28150901, PubMed:8409926, PubMed:8576221, PubMed:9545596). Binds tungstate with high affinity in vitro (PubMed:21784948, PubMed:28150901, PubMed:8576221, PubMed:9545596). Binds unnatural anion perrhenate with high affinity in vitro (PubMed:21861186). Does not bind sulfate, phosphate, arsenate, selenate, chlorate, metavanadate, nitrate, perchlorate, permanganate or carbonate (PubMed:28150901, PubMed:8576221, PubMed:9545596). {ECO:0000269|PubMed:21784948, ECO:0000269|PubMed:21861186, ECO:0000269|PubMed:28150901, ECO:0000269|PubMed:8409926, ECO:0000269|PubMed:8576221, ECO:0000269|PubMed:9545596}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-19-CPLX|complex.ecocyc.ABC-19-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0763|gene.b0763]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37329`
- `KEGG:ecj:JW0746;eco:b0763;ecoc:C3026_03870;`
- `GeneID:945364;`
- `GO:GO:0015412; GO:0015689; GO:0016020; GO:0030151; GO:0030288; GO:0030973; GO:0046687; GO:0055052; GO:0070614; GO:1901359`

## Notes

Molybdate-binding protein ModA (Molybdate/tungstate-binding protein ModA)
