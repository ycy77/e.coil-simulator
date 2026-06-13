---
entity_id: "protein.P76341"
entity_type: "protein"
name: "hiuH"
source_database: "UniProt"
source_id: "P76341"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|Ref.3}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hiuH yedX b1970 JW1953"
---

# hiuH

`protein.P76341`

## Static

- Type: `protein`
- Source: `UniProt:P76341`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|Ref.3}.

## Enriched Summary

FUNCTION: Catalyzes the hydrolysis of 5-hydroxyisourate (HIU) to 2-oxo-4-hydroxy-4-carboxy-5-ureidoimidazoline (OHCU). {ECO:0000269|PubMed:16098976}. YedX belongs to the family of transthyretin-related proteins (TRP). Transthyretin is a transport protein in extracellular fluids of vertebrates, where it distributes thyroid hormones . YedX is othologous with Bacillus subtilis PucM, which functions to facilitate the hydrolysis of 5-hydroxyisourate (HIU), the end product of the uricase reaction; purified YedX has 5-hydroxyisourate hydrolase (HIUH) activity The physiological significance of HIUH activity in E. coli is unclear. The source of HIU is not known; E. coli degrades purines to form uric acid (see PWY-6608 and SALVADEHYPOX-PWY), which is a good source of nitrogen in many organisms, but uricase activity has not been identified in E.coli. Alternatively, suggests that uric acid functions as an antioxidant in enterobacteria and that the oxidative (nonenzymatic) decomposition of uric acid would also generate HIU which can spontaneously decompose into, and react with, a variety of free radical compounds. Enzymatic removal of 5-HIU (by periplasmic YedX) would thus prevent accumulation of potentially toxic compounds. YedX contains a cleaved signal sequence and may be located in the periplasm. The protein is a tetramer in solution. E...

## Biological Role

Component of hydroxyisourate hydrolase / transthyretin-related protein (complex.ecocyc.CPLX0-3961).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the hydrolysis of 5-hydroxyisourate (HIU) to 2-oxo-4-hydroxy-4-carboxy-5-ureidoimidazoline (OHCU). {ECO:0000269|PubMed:16098976}.

## Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-3961|complex.ecocyc.CPLX0-3961]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4

## Incoming Edges (1)

- `encodes` <-- [[gene.b1970|gene.b1970]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76341`
- `KEGG:ecj:JW1953;eco:b1970;ecoc:C3026_11130;`
- `GeneID:946485;`
- `GO:GO:0006144; GO:0032991; GO:0033971; GO:0042597; GO:0042802; GO:0051289`
- `EC:3.5.2.17`

## Notes

5-hydroxyisourate hydrolase (HIU hydrolase) (HIUHase) (EC 3.5.2.17) (Transthyretin-like protein) (TLP) (Transthyretin-related protein) (TRP)
