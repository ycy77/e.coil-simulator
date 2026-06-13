---
entity_id: "protein.P80644"
entity_type: "protein"
name: "ssuE"
source_database: "UniProt"
source_id: "P80644"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ssuE ycbP b0937 JW0920"
---

# ssuE

`protein.P80644`

## Static

- Type: `protein`
- Source: `UniProt:P80644`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes an NADPH-dependent reduction of FMN, but is also able to reduce FAD or riboflavin. The SsuE protein is an NAD(P)H-dependent FMN reductase that provides FMNH2 for SsuD, an FMNH2-dependent monooxygenase . FMN is the preferred flavin substrate of SsuE, but the enzyme is also active with FAD and riboflavin . Rapid reaction kinetic analysis was performed to investigate the reductive half-reaction by SsuE . The presence of SsuD and the octanesulfonate substrate changes the kinetics of FMN reduction catalyzed by SsuE . Further studies showed the formation of a stable complex between SsuD and SsuE, which changes the flavin environment of FMN-bound SsuE . These results support a model for direct transfer of the reduced flavin from SsuE to SsuD. SsuE belongs to the flavodoxin-like superfamily. Crystal structures of SsuE in the apo, FMN-bound, and FMNH2-bound forms have been solved . SsuE forms a dimer of dimers in the crystal structure; in solution, the protein is in a dimer-tetramer equilibrium that depends on the presence of FMN. A general catalytic cycle involving FMN binding before NADPH was proposed , thus revising the catalytic mechanism proposed earlier . Expression of SsuE appears to be induced by sulfate or cysteine starvation . Transcription of ssuE is repressed by sulfate or cysteine, and the effect requires the transcriptional regulator Cbl...

## Biological Role

Component of NADPH-dependent FMN reductase (complex.ecocyc.CPLX0-224).

## Enriched Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes an NADPH-dependent reduction of FMN, but is also able to reduce FAD or riboflavin.

## Pathways

- `eco00740` Riboflavin metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-224|complex.ecocyc.CPLX0-224]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0937|gene.b0937]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P80644`
- `KEGG:ecj:JW0920;eco:b0937;ecoc:C3026_05750;`
- `GeneID:75204028;945947;`
- `GO:GO:0006974; GO:0008752; GO:0009970; GO:0042803; GO:0046306; GO:0052873; GO:1990202`
- `EC:1.5.1.38`

## Notes

FMN reductase (NADPH) (EC 1.5.1.38) (FMN reductase) (Sulfate starvation-induced protein 4) (SSI4)
