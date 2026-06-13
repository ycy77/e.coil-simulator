---
entity_id: "protein.P0ABK9"
entity_type: "protein"
name: "nrfA"
source_database: "UniProt"
source_id: "P0ABK9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:11863430, ECO:0000269|PubMed:7934939, ECO:0000269|PubMed:9593308}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nrfA b4070 JW4031"
---

# nrfA

`protein.P0ABK9`

## Static

- Type: `protein`
- Source: `UniProt:P0ABK9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:11863430, ECO:0000269|PubMed:7934939, ECO:0000269|PubMed:9593308}.

## Enriched Summary

FUNCTION: Catalyzes the reduction of nitrite to ammonia, consuming six electrons in the process (PubMed:11863430, PubMed:18311941, PubMed:20629638, PubMed:9593308). Has very low activity toward hydroxylamine (PubMed:11863430). Has even lower activity toward sulfite (PubMed:20629638). Sulfite reductase activity is maximal at neutral pH (By similarity). {ECO:0000250|UniProtKB:L0DSL2, ECO:0000269|PubMed:11863430, ECO:0000269|PubMed:18311941, ECO:0000269|PubMed:20629638, ECO:0000269|PubMed:9593308, ECO:0000305|PubMed:7934939}.

## Biological Role

Catalyzes ammonia:ferricytochrome-c oxidoreductase (reaction.R05712). Component of cytochrome c552 nitrite reductase (complex.ecocyc.CPLX0-12840), periplasmic nitrite reductase NrfAB (complex.ecocyc.NRFMULTI-CPLX).

## Enriched Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)

## Annotation

FUNCTION: Catalyzes the reduction of nitrite to ammonia, consuming six electrons in the process (PubMed:11863430, PubMed:18311941, PubMed:20629638, PubMed:9593308). Has very low activity toward hydroxylamine (PubMed:11863430). Has even lower activity toward sulfite (PubMed:20629638). Sulfite reductase activity is maximal at neutral pH (By similarity). {ECO:0000250|UniProtKB:L0DSL2, ECO:0000269|PubMed:11863430, ECO:0000269|PubMed:18311941, ECO:0000269|PubMed:20629638, ECO:0000269|PubMed:9593308, ECO:0000305|PubMed:7934939}.

## Pathways

- `eco00910` Nitrogen metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01310` Nitrogen cycle (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R05712|reaction.R05712]] `KEGG` `database` - via EC:1.7.2.2
- `is_component_of` --> [[complex.ecocyc.CPLX0-12840|complex.ecocyc.CPLX0-12840]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2
- `is_component_of` --> [[complex.ecocyc.NRFMULTI-CPLX|complex.ecocyc.NRFMULTI-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4070|gene.b4070]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABK9`
- `KEGG:ecj:JW4031;eco:b4070;ecoc:C3026_22000;`
- `GeneID:93777759;948571;`
- `GO:GO:0005506; GO:0005509; GO:0016966; GO:0019645; GO:0020037; GO:0030288; GO:0042128; GO:0042279`
- `EC:1.7.2.2`

## Notes

Cytochrome c-552 (EC 1.7.2.2) (Ammonia-forming cytochrome c nitrite reductase) (Cytochrome c nitrite reductase)
