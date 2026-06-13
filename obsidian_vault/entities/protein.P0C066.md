---
entity_id: "protein.P0C066"
entity_type: "protein"
name: "mltC"
source_database: "UniProt"
source_id: "P0C066"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305}; Lipid-anchor {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mltC yggZ b2963 JW5481"
---

# mltC

`protein.P0C066`

## Static

- Type: `protein`
- Source: `UniProt:P0C066`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305}; Lipid-anchor {ECO:0000305}.

## Enriched Summary

FUNCTION: Murein-degrading enzyme. May play a role in recycling of muropeptides during cell elongation and/or cell division. {ECO:0000255|HAMAP-Rule:MF_01616}. mltC encodes a membrane bound lytic murein transglycosylase which cleaves the β-1,4 glycosidic bond between N-acetylglucosamine (GlcNAc) and N-acetylmuramic acid (MurNAc) residues of peptidoglycan with the concomitant formation of a 1,6-anhydro ring at the MurNAc residue. mltC contains a putative lipoprotein signal sequence; MltC has peptidoglycan hydrolase activity . Purified MltC (residues 19-359) degrades the purified cell wall sacculus to produce the following major products (in order of abundance): tetra-A1 (GlcNAc-1,6-anhydro-MurNAc monomer with tetrapeptide stem); tetra2-A2 (a GlcNAc-1,6-anhydro-MurNAc dimer with crosslinked tetrapeptide stems); tri-A1 (GlcNAc-1,6-anhydro-MurNAc monomer with tripeptide stem) plus other variations in smaller amounts. The reaction generates both cross-linked and non-crosslinked products; it also generates a small amount of product that is indicative of an endolytic transglycosylase reaction and some products containing a reducing end (ie containing a terminal MurNAc residue rather than a 1,6-anhydro-MurNAc residue)...

## Biological Role

Catalyzes RXN-17391 (reaction.ecocyc.RXN-17391), RXN-17392 (reaction.ecocyc.RXN-17392).

## Annotation

FUNCTION: Murein-degrading enzyme. May play a role in recycling of muropeptides during cell elongation and/or cell division. {ECO:0000255|HAMAP-Rule:MF_01616}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-17391|reaction.ecocyc.RXN-17391]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17392|reaction.ecocyc.RXN-17392]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2963|gene.b2963]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C066`
- `KEGG:ecj:JW5481;eco:b2963;ecoc:C3026_16215;`
- `GeneID:86861053;945428;`
- `GO:GO:0008932; GO:0008933; GO:0009253; GO:0009279; GO:0016798; GO:0016998; GO:0030288; GO:0034599; GO:0051301; GO:0071236; GO:0071555`
- `EC:4.2.2.n1`

## Notes

Membrane-bound lytic murein transglycosylase C (EC 4.2.2.n1) (Murein lyase C)
