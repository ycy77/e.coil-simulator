---
entity_id: "protein.P0A935"
entity_type: "protein"
name: "mltA"
source_database: "UniProt"
source_id: "P0A935"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane; Lipid-anchor."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mltA mlt ygdM b2813 JW2784"
---

# mltA

`protein.P0A935`

## Static

- Type: `protein`
- Source: `UniProt:P0A935`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane; Lipid-anchor.

## Enriched Summary

FUNCTION: Murein-degrading enzyme. May play a role in recycling of muropeptides during cell elongation and/or cell division. Degrades murein glycan strands and insoluble, high-molecular weight murein sacculi. mltA encodes a membrane bound lytic murein transglycosylase which cleaves the β-1,4 glycosidic bond between N-acetylglucosamine (GlcNAc) and N-acetylmuramic acid (MurNAc) residues of peptidoglycan with the concomitant formation of a 1,6-anhydro ring at the MurNAc residue. MltA is an outer membrane lipoprotein . Purifed MltA degrades insoluble murein sacculi to produce soluble muropeptides and degrades isolated linear glycan strands (poly GlcNAc-MurNAc) to produce anhydro-disaccharide units . Purified MltA degrades the purified cell wall sacculus to produce the following major products (in order of abundance): tetra-A1 (GlcNAc-1,6-anhydro-MurNAc monomer with tetrapeptide stem); tetra2-A2 (a GlcNAc-1,6-anhydro-MurNAc dimer with crosslinked tetrapeptide stems); tri-A1 (GlcNAc-1,6-anhydro-MurNAc monomer with tripeptide stem) plus other variations in smaller amounts. The reaction generates both cross-linked and non-crosslinked products; it does not generate products that are indicative of an endolytic transglycosylase reaction...

## Biological Role

Catalyzes RXN-17391 (reaction.ecocyc.RXN-17391).

## Annotation

FUNCTION: Murein-degrading enzyme. May play a role in recycling of muropeptides during cell elongation and/or cell division. Degrades murein glycan strands and insoluble, high-molecular weight murein sacculi.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-17391|reaction.ecocyc.RXN-17391]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b2813|gene.b2813]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A935`
- `KEGG:ecj:JW2784;eco:b2813;ecoc:C3026_15460;`
- `GeneID:93779185;944964;`
- `GO:GO:0000270; GO:0004553; GO:0008933; GO:0009253; GO:0009254; GO:0009279; GO:0030288; GO:0071555`
- `EC:4.2.2.n1`

## Notes

Membrane-bound lytic murein transglycosylase A (EC 4.2.2.n1) (Mlt38) (Murein hydrolase A)
