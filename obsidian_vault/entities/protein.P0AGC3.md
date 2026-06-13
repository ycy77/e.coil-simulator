---
entity_id: "protein.P0AGC3"
entity_type: "protein"
name: "slt"
source_database: "UniProt"
source_id: "P0AGC3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm. Note=Tightly associated with the murein sacculus."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "slt sltY b4392 JW4355"
---

# slt

`protein.P0AGC3`

## Static

- Type: `protein`
- Source: `UniProt:P0AGC3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm. Note=Tightly associated with the murein sacculus.

## Enriched Summary

FUNCTION: Murein-degrading enzyme. Catalyzes the cleavage of the glycosidic bonds between N-acetylmuramic acid and N-acetylglucosamine residues in peptidoglycan. May play a role in recycling of muropeptides during cell elongation and/or cell division. slt encodes a soluble lytic murein transglycosylase (known as Slt70) which cleaves the β-1,4 glycosidic bond between N-acetylglucosamine (GlcNAc) and N-acetylmuramic acid (MurNAc) residues of peptidoglycan (PG) with the concomitant formation of a 1,6-anhydro ring at the MurNAc residue. Slt70 may function as a PG quality control enzyme - the primary physiological function of Slt70 may be the degradation of uncrosslinked glycan strands thus preventing their aberrant incorporation into the PG matrix . Purified Slt70 degrades murein into non-reducing low-molecular weight fragments and converts the glycosidic bond between GlcNAc and MurNAc into an internal 1,6-anhydroMurNAc bond; the enzyme has a Km of 200mg murein sacculi/L and activity is optimal at pH4.5 . Slt70 is present in the soluble fraction after mechanical breaking of the cells ; Slt70 localises to the cell envelope where it binds to the outer surface of the murein sacculus . Slt70 functions as an exotransglycosylase in vitro...

## Biological Role

Catalyzes RXN-17391 (reaction.ecocyc.RXN-17391), RXN-17392 (reaction.ecocyc.RXN-17392).

## Annotation

FUNCTION: Murein-degrading enzyme. Catalyzes the cleavage of the glycosidic bonds between N-acetylmuramic acid and N-acetylglucosamine residues in peptidoglycan. May play a role in recycling of muropeptides during cell elongation and/or cell division.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-17391|reaction.ecocyc.RXN-17391]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17392|reaction.ecocyc.RXN-17392]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4392|gene.b4392]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AGC3`
- `KEGG:ecj:JW4355;eco:b4392;ecoc:C3026_23735;`
- `GeneID:75202926;948908;`
- `GO:GO:0004553; GO:0008932; GO:0008933; GO:0009253; GO:0009274; GO:0016020; GO:0030288; GO:0071555`
- `EC:4.2.2.n1`

## Notes

Soluble lytic murein transglycosylase (EC 4.2.2.n1) (Exomuramidase) (Peptidoglycan lytic exotransglycosylase) (Slt70)
