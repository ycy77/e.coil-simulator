---
entity_id: "protein.P76129"
entity_type: "protein"
name: "dosP"
source_database: "UniProt"
source_id: "P76129"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dosP dos pdeO yddU b1489 JW1484"
---

# dosP

`protein.P76129`

## Static

- Type: `protein`
- Source: `UniProt:P76129`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Heme-based oxygen sensor protein displaying phosphodiesterase (PDE) activity toward c-di-GMP in response to oxygen availability. Involved in the modulation of intracellular c-di-GMP levels, in association with DosC which catalyzes the biosynthesis of c-di-GMP (diguanylate cyclase activity). Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. Has very poor PDE activity on cAMP (PubMed:15995192) but is not active with cGMP, bis(p-nitrophenyl) phosphate or p-nitrophenyl phosphate (PubMed:11970957). Via its PDE activity on c-di-GMP, DosP regulates biofilm formation through the repression of transcription of the csgBAC operon, which encodes curli structural subunits. {ECO:0000269|PubMed:11970957, ECO:0000269|PubMed:15995192, ECO:0000269|PubMed:20553324}.

## Biological Role

Catalyzes cyclic bis(3->5')diguanylate 3-guanylylhydrolase (reaction.R08991). Component of DosC-DosP complex (complex.ecocyc.CPLX0-7823), oxygen-sensing cyclic di-GMP phosphodiesterase DosP (complex.ecocyc.CPLX0-8199).

## Annotation

FUNCTION: Heme-based oxygen sensor protein displaying phosphodiesterase (PDE) activity toward c-di-GMP in response to oxygen availability. Involved in the modulation of intracellular c-di-GMP levels, in association with DosC which catalyzes the biosynthesis of c-di-GMP (diguanylate cyclase activity). Cyclic-di-GMP is a second messenger which controls cell surface-associated traits in bacteria. Has very poor PDE activity on cAMP (PubMed:15995192) but is not active with cGMP, bis(p-nitrophenyl) phosphate or p-nitrophenyl phosphate (PubMed:11970957). Via its PDE activity on c-di-GMP, DosP regulates biofilm formation through the repression of transcription of the csgBAC operon, which encodes curli structural subunits. {ECO:0000269|PubMed:11970957, ECO:0000269|PubMed:15995192, ECO:0000269|PubMed:20553324}.

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R08991|reaction.R08991]] `KEGG` `database` - via EC:3.1.4.52
- `is_component_of` --> [[complex.ecocyc.CPLX0-7823|complex.ecocyc.CPLX0-7823]] `EcoCyc` `database` - EcoCyc component coefficient= | EcoCyc protcplxs.col coefficient=1
- `is_component_of` --> [[complex.ecocyc.CPLX0-8199|complex.ecocyc.CPLX0-8199]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1489|gene.b1489]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76129`
- `KEGG:ecj:JW1484;eco:b1489;`
- `GeneID:945815;`
- `GO:GO:0000287; GO:0005886; GO:0019826; GO:0020037; GO:0042803; GO:0070482; GO:0071111; GO:1900190`
- `EC:3.1.4.52`

## Notes

Oxygen sensor protein DosP (EC 3.1.4.52) (Direct oxygen-sensing phosphodiesterase) (Direct oxygen sensor protein) (Ec DOS) (Heme-regulated cyclic di-GMP phosphodiesterase)
