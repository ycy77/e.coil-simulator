---
entity_id: "protein.P13738"
entity_type: "protein"
name: "nhaA"
source_database: "UniProt"
source_id: "P13738"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:15988517, ECO:0000269|PubMed:1645730, ECO:0000269|PubMed:19396973, ECO:0000269|PubMed:25422503}; Multi-pass membrane protein {ECO:0000269|PubMed:15988517, ECO:0000269|PubMed:19396973, ECO:0000269|PubMed:25422503}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nhaA ant b0019 JW0018"
---

# nhaA

`protein.P13738`

## Static

- Type: `protein`
- Source: `UniProt:P13738`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:15988517, ECO:0000269|PubMed:1645730, ECO:0000269|PubMed:19396973, ECO:0000269|PubMed:25422503}; Multi-pass membrane protein {ECO:0000269|PubMed:15988517, ECO:0000269|PubMed:19396973, ECO:0000269|PubMed:25422503}.

## Enriched Summary

FUNCTION: Na(+)/H(+) antiporter that extrudes sodium in exchange for external protons (PubMed:1645730, PubMed:23836890, PubMed:2839489, PubMed:7737413, PubMed:8019504, PubMed:8383669). Plays an important role in the regulation of intracellular pH, cellular Na(+) content and cell volume (PubMed:33129932). Catalyzes the exchange of 2 H(+) per Na(+) (PubMed:23836890, PubMed:8383669). This stoichiometry applies at both neutral and alkaline pH values (PubMed:8383669). In addition, can also transport lithium and is involved in lithium detoxification (PubMed:22915592, PubMed:27021484, PubMed:7737413, PubMed:8019504). Binding of the Li(+) and H(+) ligands to NhaA is coupled and antagonistic (PubMed:27021484). {ECO:0000269|PubMed:1645730, ECO:0000269|PubMed:22915592, ECO:0000269|PubMed:23836890, ECO:0000269|PubMed:27021484, ECO:0000269|PubMed:2839489, ECO:0000269|PubMed:7737413, ECO:0000269|PubMed:8019504, ECO:0000269|PubMed:8383669, ECO:0000303|PubMed:33129932}. NhaA is an Na+:H+ antiporter with a prominent role in sodium ion and alkaline pH homeostasis. NhaA mediates the active uptake of protons in exchange for cytoplasmic Na+ - a crucial mechanism that supports the maintenance of cytoplasmic pH under alkali challenge (see ). Purified, reconstituted NhaA is an electrogenic antiporter with a stoichiometry of 2H+:Na+...

## Biological Role

Component of Na+:H+ antiporter NhaA (complex.ecocyc.CPLX0-7629).

## Annotation

FUNCTION: Na(+)/H(+) antiporter that extrudes sodium in exchange for external protons (PubMed:1645730, PubMed:23836890, PubMed:2839489, PubMed:7737413, PubMed:8019504, PubMed:8383669). Plays an important role in the regulation of intracellular pH, cellular Na(+) content and cell volume (PubMed:33129932). Catalyzes the exchange of 2 H(+) per Na(+) (PubMed:23836890, PubMed:8383669). This stoichiometry applies at both neutral and alkaline pH values (PubMed:8383669). In addition, can also transport lithium and is involved in lithium detoxification (PubMed:22915592, PubMed:27021484, PubMed:7737413, PubMed:8019504). Binding of the Li(+) and H(+) ligands to NhaA is coupled and antagonistic (PubMed:27021484). {ECO:0000269|PubMed:1645730, ECO:0000269|PubMed:22915592, ECO:0000269|PubMed:23836890, ECO:0000269|PubMed:27021484, ECO:0000269|PubMed:2839489, ECO:0000269|PubMed:7737413, ECO:0000269|PubMed:8019504, ECO:0000269|PubMed:8383669, ECO:0000303|PubMed:33129932}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7629|complex.ecocyc.CPLX0-7629]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2 | EcoCyc transporter component coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0019|gene.b0019]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P13738`
- `KEGG:ecj:JW0018;eco:b0019;ecoc:C3026_00090;`
- `GeneID:944758;`
- `GO:GO:0005886; GO:0009651; GO:0010446; GO:0015385; GO:0051453; GO:1901612`

## Notes

Na(+)/H(+) antiporter NhaA (Na(+)/H(+) exchanger) (Na(+)/Li(+)/H(+) antiporter) (Sodium/proton antiporter NhaA)
