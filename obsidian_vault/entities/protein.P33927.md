---
entity_id: "protein.P33927"
entity_type: "protein"
name: "ccmF"
source_database: "UniProt"
source_id: "P33927"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ccmF yejR b2196 JW2184"
---

# ccmF

`protein.P33927`

## Static

- Type: `protein`
- Source: `UniProt:P33927`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane; Multi-pass membrane protein.

## Enriched Summary

FUNCTION: Required for the biogenesis of c-type cytochromes. Possible subunit of a heme lyase. CcmF and EG12052 CcmH are the components of holocytochrome c synthase in the System I pathway of cytochome c maturation; CcmFH releases heme from holoCCME-MONOMER CcmE and transfers it to apocytochromes in the periplasm. ccmF is part of an 8 gene cluster (ccmABCDEFGH) which bears sequence similarity to Bradyrhizobium japonicum genes that are required for the biogenesis of Cytochromes-c "c-type cytochromes"; an E. coli ΔccmA-H mutant strain (EC06) is not able to produce mature c-type cytochromes under anaerobic, nonfermentative growth conditions (see also ). An in-frame ccmF deletion mutant is able to produce (plasmid-encoded) mature Cytochromes-B b-type cytochrome and apocytochrome c-550 but not holocytochrome c-550 . Heme-containing CcmE accumulates in a mutant that is unable to synthesize CcmF . Release of heme from CcmE is blocked in the absence of CcmFGH proteins . CcmF interacts with CcmE and with CcmH but not with apocytochrome c (and see )...

## Biological Role

Catalyzes RXN-21423 (reaction.ecocyc.RXN-21423), RXN0-7454 (reaction.ecocyc.RXN0-7454). Component of holocytochrome c synthase complex (complex.ecocyc.CPLX-9494). Bound by Heme (molecule.C00032).

## Annotation

FUNCTION: Required for the biogenesis of c-type cytochromes. Possible subunit of a heme lyase.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.ecocyc.RXN-21423|reaction.ecocyc.RXN-21423]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7454|reaction.ecocyc.RXN0-7454]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.CPLX-9494|complex.ecocyc.CPLX-9494]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (2)

- `binds` <-- [[molecule.C00032|molecule.C00032]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2196|gene.b2196]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P33927`
- `KEGG:ecj:JW2184;eco:b2196;ecoc:C3026_12275;`
- `GeneID:948783;`
- `GO:GO:0005886; GO:0015232; GO:0016491; GO:0016679; GO:0017004; GO:0020037`

## Notes

Cytochrome c-type biogenesis protein CcmF
