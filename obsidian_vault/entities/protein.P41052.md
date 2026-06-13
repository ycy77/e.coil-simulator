---
entity_id: "protein.P41052"
entity_type: "protein"
name: "mltB"
source_database: "UniProt"
source_id: "P41052"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane; Lipid-anchor; Periplasmic side."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mltB b2701 JW2671"
---

# mltB

`protein.P41052`

## Static

- Type: `protein`
- Source: `UniProt:P41052`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane; Lipid-anchor; Periplasmic side.

## Enriched Summary

FUNCTION: Murein-degrading enzyme. Catalyzes the cleavage of the glycosidic bonds between N-acetylmuramic acid and N-acetylglucosamine residues in peptidoglycan. May play a role in recycling of muropeptides during cell elongation and/or cell division. mltB encodes a membrane bound lytic murein transglycosylase which cleaves the β-1,4 glycosidic bond between N-acetylglucosamine (GlcNAc) and N-acetylmuramic acid (MurNAc) residues of peptidoglycan with the concomitant formation of a 1,6-anhydro ring at the MurNAc residue. MltB is an outer membrane lipoprotein . Proteolytic cleavage of MltB releases a soluble, active form of the protein (known as Slt35) . Purified Slt35 has peptidoglycan hydrolase activity, releasing 1,6-anhydromuropeptides from isolated peptidoglycan polymer . Purified, soluble MltB is able to degrade a synthetic peptidoglycan substrate containing a short chain backbone of only two repeats of GlcNAc-MurNAc . Purified MltB (residues 21-361) degrades the purified cell wall sacculus to produce the following major products (in order of abundance): tetra-A1 (GlcNAc-1,6-anhydro-MurNAc monomer with tetrapeptide stem); tetra2-A2 (a GlcNAc-1,6-anhydro-MurNAc dimer with crosslinked tetrapeptide stems); tri-A1 (GlcNAc-1,6-anhydro-MurNAc monomer with tripeptide stem) plus other variations in smaller amounts...

## Biological Role

Catalyzes RXN-17391 (reaction.ecocyc.RXN-17391), RXN-17392 (reaction.ecocyc.RXN-17392).

## Annotation

FUNCTION: Murein-degrading enzyme. Catalyzes the cleavage of the glycosidic bonds between N-acetylmuramic acid and N-acetylglucosamine residues in peptidoglycan. May play a role in recycling of muropeptides during cell elongation and/or cell division.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-17391|reaction.ecocyc.RXN-17391]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17392|reaction.ecocyc.RXN-17392]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2701|gene.b2701]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P41052`
- `KEGG:ecj:JW2671;eco:b2701;ecoc:C3026_14870;`
- `GeneID:75172783;947184;`
- `GO:GO:0005509; GO:0008932; GO:0008933; GO:0009253; GO:0009279; GO:0030288; GO:0031402; GO:0071555`
- `EC:4.2.2.n1`

## Notes

Membrane-bound lytic murein transglycosylase B (EC 4.2.2.n1) (35 kDa soluble lytic transglycosylase) (Murein hydrolase B) (Slt35)
