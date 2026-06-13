---
entity_id: "protein.P75824"
entity_type: "protein"
name: "hcr"
source_database: "UniProt"
source_id: "P75824"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hcr ybjV b0872 JW5117"
---

# hcr

`protein.P75824`

## Static

- Type: `protein`
- Source: `UniProt:P75824`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: NADH oxidoreductase acting in concert with HCP. The hcr gene encodes an NADH oxidoreductase that catalyzes the reduction of the G6457-MONOMER (HCP). The physiological roles of HCP and the oxidoreductase are not known. They are detected only during anaerobic growth in the presence of nitrate and nitrite .

## Biological Role

Catalyzes RXN0-307 (reaction.ecocyc.RXN0-307). Bound by FAD (molecule.C00016), a [2Fe-2S] iron-sulfur cluster (molecule.ecocyc.CPD-6).

## Annotation

FUNCTION: NADH oxidoreductase acting in concert with HCP.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-307|reaction.ecocyc.RXN0-307]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (3)

- `binds` <-- [[molecule.C00016|molecule.C00016]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CPD-6|molecule.ecocyc.CPD-6]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0872|gene.b0872]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75824`
- `KEGG:ecj:JW5117;eco:b0872;ecoc:C3026_05420;`
- `GeneID:93776549;947660;`
- `GO:GO:0016491; GO:0016651; GO:0046872; GO:0050660; GO:0051537`
- `EC:1.-.-.-`

## Notes

NADH oxidoreductase HCR (EC 1.-.-.-)
