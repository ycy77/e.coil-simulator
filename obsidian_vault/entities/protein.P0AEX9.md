---
entity_id: "protein.P0AEX9"
entity_type: "protein"
name: "malE"
source_database: "UniProt"
source_id: "P0AEX9"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:4215651}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "malE b4034 JW3994"
---

# malE

`protein.P0AEX9`

## Static

- Type: `protein`
- Source: `UniProt:P0AEX9`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:4215651}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex MalEFGK involved in maltose/maltodextrin import. Binds maltose and higher maltodextrins such as maltotriose. {ECO:0000269|PubMed:2026607, ECO:0000269|PubMed:2155217, ECO:0000269|PubMed:4215651, ECO:0000269|PubMed:776623}. malE encodes the periplasmic substrate-binding component of the maltose ABC transporter. MalE, or maltodextrin binding protein (MBP) can bind linear maltodextrins, cyclic maltodextrins and various maltodextrin analogues although only linear maltodextrins up maltoheptaose are substrates for transport . Non-polar malE deletion mutants do not show appreciable growth on media containing maltose concentrations up to 25 mM . MBP consists of two globular domains separated by a deep groove which contains the maltodextrin binding site. MBP adopts two distinct conformations - an open unliganded form in which the two globular domains are far apart and the binding groove is accessible and a closed liganded structure. Bound maltose is almost completely enclosed and is held in place by hydrogen bonds and Van der Waals interactions . Crystal structures of MalE bound to cyclomaltoheptaose , of MalE bound to the modified sugars maltotriitol and maltotetraitol , of MalE complexed with xenon and of various mutant MalE proteins are available...

## Biological Role

Component of maltose ABC transporter (complex.ecocyc.ABC-16-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex MalEFGK involved in maltose/maltodextrin import. Binds maltose and higher maltodextrins such as maltotriose. {ECO:0000269|PubMed:2026607, ECO:0000269|PubMed:2155217, ECO:0000269|PubMed:4215651, ECO:0000269|PubMed:776623}.

## Pathways

- `eco02010` ABC transporters (KEGG)
- `eco02030` Bacterial chemotaxis (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-16-CPLX|complex.ecocyc.ABC-16-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4034|gene.b4034]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEX9`
- `KEGG:ecj:JW3994;eco:b4034;ecoc:C3026_21795;`
- `GeneID:75169489;75204178;948538;`
- `GO:GO:0006974; GO:0008643; GO:0015144; GO:0015768; GO:0016020; GO:0030288; GO:0034289; GO:0042597; GO:0042956; GO:0043190; GO:0055052; GO:0060326; GO:1901982; GO:1990060`

## Notes

Maltose/maltodextrin-binding periplasmic protein (MMBP) (Maltodextrin-binding protein) (Maltose-binding protein) (MBP)
