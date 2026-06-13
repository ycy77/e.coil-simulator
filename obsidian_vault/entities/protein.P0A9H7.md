---
entity_id: "protein.P0A9H7"
entity_type: "protein"
name: "cfa"
source_database: "UniProt"
source_id: "P0A9H7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cfa cdfA b1661 JW1653"
---

# cfa

`protein.P0A9H7`

## Static

- Type: `protein`
- Source: `UniProt:P0A9H7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm.

## Enriched Summary

FUNCTION: Transfers a methylene group from S-adenosyl-L-methionine to the cis double bond of an unsaturated fatty acid chain resulting in the replacement of the double bond with a methylene bridge. {ECO:0000250}. Cyclopropane fatty acyl phospholipid synthase (CFA) catalyzes a modification of the acyl chains of phospholipid bilayers through methylenation of unsaturated fatty acyl chains to their cyclopropane derivatives . It is one of the few enzymes known to act on the nonpolar portion of phospholipids dispersed in a vesicle. The enzyme acts on the double bond of a phospholipid unsaturated fatty acid residue, which must be 9-11 carbon atoms removed from the glycerol backbone of the molecule. Studies using analogs of S-adenosyl-L-methionine suggest that the reaction proceeds via methyl transfer followed by proton loss . CFA synthase is thought to operate via a carbocation mechanism . The presence of a bicarbonate ion in the active site was predicted by similarity to the M. tuberculosis cyclopropane synthases. The presence of bicarbonate enhances the Vmax of CFA synthase 3-fold . Mutants in residues predicted to interact with bicarbonate show reduced catalytic efficiency, and some mutants can be rescued by the addition of free bicarbonate. A reaction mechanism has been proposed...

## Biological Role

Catalyzes S-adenosyl-L-methionine:unsaturated-phospholipid methyltransferase (cyclizing) (reaction.R03411). Component of cyclopropane fatty acyl phospholipid synthase (complex.ecocyc.CFA-CPLX).

## Annotation

FUNCTION: Transfers a methylene group from S-adenosyl-L-methionine to the cis double bond of an unsaturated fatty acid chain resulting in the replacement of the double bond with a methylene bridge. {ECO:0000250}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R03411|reaction.R03411]] `KEGG` `database` - via EC:2.1.1.79
- `is_component_of` --> [[complex.ecocyc.CFA-CPLX|complex.ecocyc.CFA-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b1661|gene.b1661]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A9H7`
- `KEGG:ecj:JW1653;eco:b1661;ecoc:C3026_09530;`
- `GeneID:93775816;944811;`
- `GO:GO:0005829; GO:0006633; GO:0008610; GO:0008825; GO:0030258; GO:0031234; GO:0032259; GO:0042803; GO:0071890`
- `EC:2.1.1.79`

## Notes

Cyclopropane-fatty-acyl-phospholipid synthase (CFA synthase) (Cyclopropane fatty acid synthase) (EC 2.1.1.79)
