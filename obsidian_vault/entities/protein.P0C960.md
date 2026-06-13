---
entity_id: "protein.P0C960"
entity_type: "protein"
name: "emtA"
source_database: "UniProt"
source_id: "P0C960"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305|PubMed:9642199}; Lipid-anchor {ECO:0000305|PubMed:9642199}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "emtA mltE sltZ ycgP b1193 JW5821"
---

# emtA

`protein.P0C960`

## Static

- Type: `protein`
- Source: `UniProt:P0C960`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000305|PubMed:9642199}; Lipid-anchor {ECO:0000305|PubMed:9642199}.

## Enriched Summary

FUNCTION: Murein-degrading enzyme. May play a role in recycling of muropeptides during cell elongation and/or cell division. Preferentially cleaves at a distance of more than two disaccharide units from the ends of the glycan chain. Prefers cross-linked murein in vivo. emtA encodes a membrane bound lytic murein transglycosylase (EmtA or MltE) which cleaves the β-1 → 4 glycosidic bond between N-acetylglucosamine (GlcNAc) and N-acetylmuramic acid (MurNAc) residues of peptidoglycan with the concomitant formation of a 1,6-anhydro ring at the MurNAc residue. EmtA is a lipoprotein, predicted to reside in the outer membrane . EmtA degrades isolated murein glycan strands to release muropeptides with a 1,6-anhydroMurNAc terminus; EmtA has endotransglycosylase activity - it hydrolyses glycan strands in vitro to produce fragments with lengths of two and three disaccharide units but does not produce monomeric anhydrodisaccharide fragments; EmtA displays a preference for cross-linked murein; EmtA is unable to degrade purified murein sacculi in vitro . Purified EmtA (residues 17-203) cleaves Micrococcus luteus murein sacculi in vitro...

## Biological Role

Catalyzes RXN-17391 (reaction.ecocyc.RXN-17391), RXN-17392 (reaction.ecocyc.RXN-17392).

## Annotation

FUNCTION: Murein-degrading enzyme. May play a role in recycling of muropeptides during cell elongation and/or cell division. Preferentially cleaves at a distance of more than two disaccharide units from the ends of the glycan chain. Prefers cross-linked murein in vivo.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-17391|reaction.ecocyc.RXN-17391]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17392|reaction.ecocyc.RXN-17392]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1193|gene.b1193]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C960`
- `KEGG:ecj:JW5821;eco:b1193;ecoc:C3026_07020;`
- `GeneID:93776239;945655;`
- `GO:GO:0000270; GO:0008932; GO:0008933; GO:0009279; GO:0016998; GO:0051301; GO:0071555`
- `EC:4.2.2.n2`

## Notes

Endo-type membrane-bound lytic murein transglycosylase A (EC 4.2.2.n2) (Peptidoglycan lytic endotransglycosylase)
