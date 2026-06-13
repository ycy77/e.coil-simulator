---
entity_id: "protein.P0AD59"
entity_type: "protein"
name: "ivy"
source_database: "UniProt"
source_id: "P0AD59"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ivy ykfE b0220 JW0210"
---

# ivy

`protein.P0AD59`

## Static

- Type: `protein`
- Source: `UniProt:P0AD59`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm.

## Enriched Summary

FUNCTION: Strong inhibitor of lysozyme C. Ivy acts as a homodimer that specifically binds and inhibits vertebrate C-type lysozyme, behaving like a slow tight binding inhibitor with a Ki of about 1 nM . Overproduction of Ivy stabilises a highly unstable MBP mutant; purified Ivy inhibits the aggregation of lactate dehydrogenase . Ivy has a signal peptide that is cleaved from the mature protein . Crystal structures of Ivy alone and in complex with hen egg white lysozyme have been solved, and site-directed mutagenesis confirms the importance of the His60 residue for inhibition . ivy is highly expressed during exponential and stationary phase . An ivy null mutant does not show increased sensitivity to hen egg white lysozyme due to protection of the peptidoglycan layer by the outer membrane. However, under conditions that permeabilize the outer membrane, such as high pressure or lactoferrin treatment or in a tolB mutant background , an ivy null mutant is sensitized to lysozyme. Ivy: "inhibitor of vertebrate lysozyme"

## Biological Role

Component of periplasmic chaperone, inhibitor of vertebrate C-type lysozyme (complex.ecocyc.CPLX0-921).

## Annotation

FUNCTION: Strong inhibitor of lysozyme C.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-921|complex.ecocyc.CPLX0-921]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0220|gene.b0220]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AD59`
- `KEGG:ecj:JW0210;eco:b0220;`
- `GeneID:946530;`
- `GO:GO:0030288; GO:0042803; GO:0060241`

## Notes

Inhibitor of vertebrate lysozyme
