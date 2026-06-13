---
entity_id: "protein.P0AA89"
entity_type: "protein"
name: "dosC"
source_database: "UniProt"
source_id: "P0AA89"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dosC dgcO yddV b1490 JW5241"
---

# dosC

`protein.P0AA89`

## Static

- Type: `protein`
- Source: `UniProt:P0AA89`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Globin-coupled heme-based oxygen sensor protein displaying diguanylate cyclase (DGC) activity in response to oxygen availability. Thus, catalyzes the synthesis of cyclic diguanylate (c-di-GMP) via the condensation of 2 GTP molecules. Is involved in the modulation of intracellular c-di-GMP levels, in association with DosP which catalyzes the degradation of c-di-GMP (PDE activity). Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. DosC regulates biofilm formation through the oxygen-dependent activation of the csgBAC operon, which encodes curli structural subunits, while not affecting the expression of the regulatory operon csgDEFG. DosC, but not the other DGCs in E.coli, also promotes the production of the exopolysaccharide poly-N-acetylglucosamine (PNAG) through up-regulation of the expression of the PNAG biosynthetic pgaABCD operon, independently of CsrA.; FUNCTION: Overexpression leads to an increased level of c-di-GMP, which leads to changes in the cell surface, to abnormal cell division, increased biofilm formation and decreased swimming (the latter 2 in strain W3110). In a strain able to produce cellulose (strain TOB1, a fecal isolate) overexpression leads to an increase in cellulose production.

## Biological Role

Component of DosC-DosP complex (complex.ecocyc.CPLX0-7823), diguanylate cyclase DosC (complex.ecocyc.CPLX0-8218).

## Annotation

FUNCTION: Globin-coupled heme-based oxygen sensor protein displaying diguanylate cyclase (DGC) activity in response to oxygen availability. Thus, catalyzes the synthesis of cyclic diguanylate (c-di-GMP) via the condensation of 2 GTP molecules. Is involved in the modulation of intracellular c-di-GMP levels, in association with DosP which catalyzes the degradation of c-di-GMP (PDE activity). Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. DosC regulates biofilm formation through the oxygen-dependent activation of the csgBAC operon, which encodes curli structural subunits, while not affecting the expression of the regulatory operon csgDEFG. DosC, but not the other DGCs in E.coli, also promotes the production of the exopolysaccharide poly-N-acetylglucosamine (PNAG) through up-regulation of the expression of the PNAG biosynthetic pgaABCD operon, independently of CsrA.; FUNCTION: Overexpression leads to an increased level of c-di-GMP, which leads to changes in the cell surface, to abnormal cell division, increased biofilm formation and decreased swimming (the latter 2 in strain W3110). In a strain able to produce cellulose (strain TOB1, a fecal isolate) overexpression leads to an increase in cellulose production.

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7823|complex.ecocyc.CPLX0-7823]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8218|complex.ecocyc.CPLX0-8218]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1490|gene.b1490]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AA89`
- `KEGG:ecj:JW5241;eco:b1490;ecoc:C3026_08630;`
- `GeneID:75171576;945835;`
- `GO:GO:0005525; GO:0005886; GO:0006950; GO:0019825; GO:0020037; GO:0042803; GO:0043709; GO:0046872; GO:0052621; GO:0070025; GO:0070482; GO:1902201`
- `EC:2.7.7.65`

## Notes

Diguanylate cyclase DosC (DGC) (EC 2.7.7.65) (Direct oxygen-sensing cyclase)
