---
entity_id: "protein.P45955"
entity_type: "protein"
name: "cpoB"
source_database: "UniProt"
source_id: "P45955"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_02066, ECO:0000269|PubMed:8763928}. Note=Targeting to the Sec-translocase for transport across the inner membrane is SecB-dependent (PubMed:16352602). Localizes to the septum concurrent with PBP1B-LpoB and Tol at the onset of constriction (PubMed:25951518). Localization is dependent on divisome assembly and requires ongoing septal peptidoglycan synthesis (PubMed:25951518). {ECO:0000269|PubMed:16352602, ECO:0000269|PubMed:25951518}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cpoB ybgF b0742 JW0732"
---

# cpoB

`protein.P45955`

## Static

- Type: `protein`
- Source: `UniProt:P45955`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000255|HAMAP-Rule:MF_02066, ECO:0000269|PubMed:8763928}. Note=Targeting to the Sec-translocase for transport across the inner membrane is SecB-dependent (PubMed:16352602). Localizes to the septum concurrent with PBP1B-LpoB and Tol at the onset of constriction (PubMed:25951518). Localization is dependent on divisome assembly and requires ongoing septal peptidoglycan synthesis (PubMed:25951518). {ECO:0000269|PubMed:16352602, ECO:0000269|PubMed:25951518}.

## Enriched Summary

FUNCTION: Mediates coordination of peptidoglycan synthesis and outer membrane constriction during cell division. Promotes physical and functional coordination of the PBP1B-LpoB and Tol machines, and regulates PBP1B activity in response to Tol energy state. {ECO:0000269|PubMed:25951518}. CpoB is a periplasmic protein that mediates physical and functional coordination between the peptidoglycan (PG) synthase CPLX0-3951 "PBP1B-LpoB" and the energy transducing Tol system; this coordination is required to properly synchronize PG synthesis and outer membrane (OM) constriction during cell division. CpoB, PBP1B-LpoB and the Tol proteins are recruited to the septum at the later stages of cell division and form a higher order complex that spatially links PG synthesis and OM invagination . CpoB interacts with TolA in vivo and in vitro . CpoB forms stable trimers in solution ; TolA binding disrupts trimeric CpoB to form CpoB-TolA heterodimers CpoB localizes to sites of envelope constriction in pre-divisional cellls; CpoB interacts with PBP1B in vivo; CpoB forms a ternery complex with TolA and PBP1B; CpoB forms a ternary compex with LpoB and PBP1B. CpoB is present at a copy number of 4550 ± 540 molecules per cell in growing cells...

## Annotation

FUNCTION: Mediates coordination of peptidoglycan synthesis and outer membrane constriction during cell division. Promotes physical and functional coordination of the PBP1B-LpoB and Tol machines, and regulates PBP1B activity in response to Tol energy state. {ECO:0000269|PubMed:25951518}.

## Outgoing Edges (1)

- `represses` --> [[reaction.ecocyc.RXN-16659|reaction.ecocyc.RXN-16659]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b0742|gene.b0742]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P45955`
- `KEGG:ecj:JW0732;eco:b0742;ecoc:C3026_03725;`
- `GeneID:947227;`
- `GO:GO:0030288; GO:0032991; GO:0043093; GO:0051301; GO:0070206`

## Notes

Cell division coordinator CpoB
