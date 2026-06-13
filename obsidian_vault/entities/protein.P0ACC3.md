---
entity_id: "protein.P0ACC3"
entity_type: "protein"
name: "erpA"
source_database: "UniProt"
source_id: "P0ACC3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "erpA yadR b0156 JW0152"
---

# erpA

`protein.P0ACC3`

## Static

- Type: `protein`
- Source: `UniProt:P0ACC3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probably involved in the insertion of Fe-S clusters into apoproteins in vivo including IspG and/or IspH. Essential for growth under aerobic conditions and for anaerobic respiration but not for fermentation. In vitro it binds Fe-S clusters and transfers them to apo-IspG, which is involved in quinone biosynthesis among many other cell components. Experiments indicate that it is probably also involved in the insertion of other Fe-S clusters than IspG/IspH. ErpA is an A-type iron-sulfur carrier protein; it can bind both [2Fe-2S] and [4Fe-4S] clusters. In vitro, ErpA can transfer a [4Fe-4S] cluster to EG10370-MONOMER "apo-IspG" . Functional redundancy between the three A-type carriers (ATCs) in E. coli, ErpA (an ATC-I) and IscA and SufA (both belonging to the ATC-II family), has been investigated . ErpA is required for maturation of EG11212-MONOMER NsrR, but not G7326-MONOMER IscR . IscA and ErpA appear to have independent roles in the delivery of iron-sulfur clusters to individual subunits of the FHLMULTI-CPLX FHL complex . ErpA and G7748-MONOMER NfuA directly interact with each other. The half life of the ErpA Fe-S cluster upon oxygen exposure is 54 minutes; in the presence of NfuA, its half life increases to 90 minutes. ErpA also directly interacts with IscA and SufA as well as with client proteins...

## Biological Role

Component of [Fe-S] cluster insertion protein ErpA (complex.ecocyc.CPLX0-7617).

## Annotation

FUNCTION: Probably involved in the insertion of Fe-S clusters into apoproteins in vivo including IspG and/or IspH. Essential for growth under aerobic conditions and for anaerobic respiration but not for fermentation. In vitro it binds Fe-S clusters and transfers them to apo-IspG, which is involved in quinone biosynthesis among many other cell components. Experiments indicate that it is probably also involved in the insertion of other Fe-S clusters than IspG/IspH.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7617|complex.ecocyc.CPLX0-7617]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0156|gene.b0156]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ACC3`
- `KEGG:ecj:JW0152;eco:b0156;ecoc:C3026_00710;`
- `GeneID:86862668;93777270;944857;`
- `GO:GO:0005506; GO:0005829; GO:0009060; GO:0009061; GO:0016226; GO:0051537; GO:0051539; GO:0051604`

## Notes

Iron-sulfur cluster insertion protein ErpA
