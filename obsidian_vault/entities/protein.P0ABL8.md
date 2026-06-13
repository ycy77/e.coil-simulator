---
entity_id: "protein.P0ABL8"
entity_type: "protein"
name: "ccmB"
source_database: "UniProt"
source_id: "P0ABL8"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ccmB yejV b2200 JW2188"
---

# ccmB

`protein.P0ABL8`

## Static

- Type: `protein`
- Source: `UniProt:P0ABL8`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Required for the export of heme to the periplasm for the biogenesis of c-type cytochromes. CcmB is an integral membrane protein of the PWY-8147 "type I cytochrome c biogenesis system". ccmB is part of an 8 gene cluster (ccmABCDEFGH) which bears sequence similarity to Bradyrhizobium japonicum genes that are required for the biogenesis of Cytochromes-c "c-type cytochromes"; an E. coli ΔccmA-H mutant strain (EC06) is not able to produce mature c-type cytochromes under anaerobic, nonfermentative growth conditions (see also ). An in-frame ccmB deletion mutant cannot synthesize holocytochrome c but does produce heme-bound CCME-MONOMER CcmE (when CCMC-MONOMER CcmC is overproduced); CCMA-MONOMER CcmA and CcmB are implicated in heme transfer from holo-CcmE and attachment to apocytochrome c; CcmAB does not transport heme to the periplasm (and ). CcmB is predicted to be an integral membrane protein with six transmembrane helices; CcmA is detected in the membrane when CcmB is present and purified CcmAB has ATPase activity; inactivation of this activity does not abolish formation of holo-CcmE but does prevent production of c-type cytochromes . CcmA, CcmB and ATP hydrolysis (by CcmA) are required for the release of holoCcmE from CcmC; in the absence of CcmAB, CcmC binds holoCcmE tightly (see further ). ccm: cytochrome c maturation Related reviews:

## Biological Role

Component of CcmAB (complex.ecocyc.CPLX-9493), CcmABCD release complex (complex.ecocyc.CPLX-9495).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Required for the export of heme to the periplasm for the biogenesis of c-type cytochromes.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.CPLX-9493|complex.ecocyc.CPLX-9493]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX-9495|complex.ecocyc.CPLX-9495]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b2200|gene.b2200]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ABL8`
- `KEGG:ecj:JW2188;eco:b2200;`
- `GeneID:93774978;946692;`
- `GO:GO:0005886; GO:0015232; GO:0017004; GO:0043190; GO:1903607; GO:1904334`

## Notes

Heme exporter protein B (Cytochrome c-type biogenesis protein CcmB)
