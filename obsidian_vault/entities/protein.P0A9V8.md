---
entity_id: "protein.P0A9V8"
entity_type: "protein"
name: "yihU"
source_database: "UniProt"
source_id: "P0A9V8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yihU b3882 JW3853"
---

# yihU

`protein.P0A9V8`

## Static

- Type: `protein`
- Source: `UniProt:P0A9V8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Reduces 3-sulfolactaldehyde (SLA) to 2,3-dihydroxypropane 1-sulfonate (DHPS) (PubMed:24463506, Ref.6). Metabolite profiling studies showed that the enzyme also catalyzes in vitro the NADH-dependent reduction of succinic semialdehyde (SSA) to 4-hydroxybutyrate (GHB), and that it could be involved in the metabolism of SSA, and other potentially toxic intermediates that may accumulate under stress conditions (PubMed:19372223). However, the enzyme exhibits a 42,000-fold greater catalytic efficiency for the reduction of SLA over SSA (Ref.6). Shows no detectable activity on the analogous glycolytic intermediate glyceraldehyde-3-phosphate (Ref.6). {ECO:0000269|PubMed:19372223, ECO:0000269|PubMed:24463506, ECO:0000269|Ref.6}.

## Biological Role

Component of 3-sulfolactaldehyde reductase (complex.ecocyc.CPLX0-7794).

## Enriched Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

FUNCTION: Reduces 3-sulfolactaldehyde (SLA) to 2,3-dihydroxypropane 1-sulfonate (DHPS) (PubMed:24463506, Ref.6). Metabolite profiling studies showed that the enzyme also catalyzes in vitro the NADH-dependent reduction of succinic semialdehyde (SSA) to 4-hydroxybutyrate (GHB), and that it could be involved in the metabolism of SSA, and other potentially toxic intermediates that may accumulate under stress conditions (PubMed:19372223). However, the enzyme exhibits a 42,000-fold greater catalytic efficiency for the reduction of SLA over SSA (Ref.6). Shows no detectable activity on the analogous glycolytic intermediate glyceraldehyde-3-phosphate (Ref.6). {ECO:0000269|PubMed:19372223, ECO:0000269|PubMed:24463506, ECO:0000269|Ref.6}.

## Pathways

- `eco00566` Sulfoquinovose metabolism (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7794|complex.ecocyc.CPLX0-7794]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b3882|gene.b3882]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9V8`
- `KEGG:ecj:JW3853;eco:b3882;ecoc:C3026_20985;`
- `GeneID:75204553;948372;`
- `GO:GO:0009407; GO:0016616; GO:0032991; GO:0042802; GO:0047577; GO:0050661; GO:0051287; GO:0051289; GO:0061596; GO:0061720; GO:1902777`
- `EC:1.1.1.373; 1.1.1.61`

## Notes

3-sulfolactaldehyde reductase (SLA reductase) (EC 1.1.1.373) (4-hydroxybutyrate dehydrogenase) (EC 1.1.1.61) (Gamma-hydroxybutyrate dehydrogenase) (GHBDH) (Succinic semialdehyde reductase) (SSA reductase)
