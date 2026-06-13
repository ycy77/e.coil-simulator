---
entity_id: "protein.P0AAK1"
entity_type: "protein"
name: "hycB"
source_database: "UniProt"
source_id: "P0AAK1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "hycB hevB b2724 JW2694"
---

# hycB

`protein.P0AAK1`

## Static

- Type: `protein`
- Source: `UniProt:P0AAK1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Probable electron transfer protein for hydrogenase 3. The hycBCDEFG genes in E. coli K-12 encode the hydrogenase component (hydrogenase 3) of the formate hydrogenlyase (FHL) complex. HycB is believed to be a peptide of the [4Fe-4S] ferredoxin type, which functions as an intermediate electron carrier protein between the site of formate oxidation in FdhF and the site of H2 production in HycE; HycB is predicted to contain four [4Fe-4S] clusters . In the cryo-EM structures of FHL reported by , HycB interacts with FdhF, HycF, and HycE; an electron-relay containing eight [4Fe-4S] clusters connects the site of formate oxidation and H2 production. A hycB deletion mutant loses molecular hydrogen production and 2H+/K+ exchange abilities under anaerobic glucose-fermenting conditions. It is suggested that HycB is part of the formate-hydrogen lyase complex that interacts directly with the F0F1 ATPase complex and the TrkA system .

## Biological Role

Component of formate hydrogenlyase complex (complex.ecocyc.FHLMULTI-CPLX), hydrogenase 3 (complex.ecocyc.HYDROG3-CPLX).

## Annotation

FUNCTION: Probable electron transfer protein for hydrogenase 3.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.FHLMULTI-CPLX|complex.ecocyc.FHLMULTI-CPLX]] `EcoCyc` `database` - EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.HYDROG3-CPLX|complex.ecocyc.HYDROG3-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2724|gene.b2724]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AAK1`
- `KEGG:ecj:JW2694;eco:b2724;ecoc:C3026_14985;`
- `GeneID:86860821;948002;`
- `GO:GO:0006007; GO:0009061; GO:0009326; GO:0015944; GO:0019645; GO:0046872; GO:0051539`

## Notes

Formate hydrogenlyase subunit 2 (FHL subunit 2) (Hydrogenase-3 component B)
