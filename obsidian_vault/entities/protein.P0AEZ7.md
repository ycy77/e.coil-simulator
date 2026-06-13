---
entity_id: "protein.P0AEZ7"
entity_type: "protein"
name: "mltD"
source_database: "UniProt"
source_id: "P0AEZ7"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Lipid-anchor {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mltD dniR yafG b0211 JW5018"
---

# mltD

`protein.P0AEZ7`

## Static

- Type: `protein`
- Source: `UniProt:P0AEZ7`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000305}; Lipid-anchor {ECO:0000305}.

## Enriched Summary

FUNCTION: Murein-degrading enzyme. May play a role in recycling of muropeptides during cell elongation and/or cell division (By similarity). {ECO:0000250}. mltD encodes a membrane bound lytic murein transglycosylase which cleaves the β-1,4 glycosidic bond between N-acetylglucosamine (GlcNAc) and N-acetylmuramic acid (MurNAc) residues of peptidoglycan with the concomitant formation of a 1,6-anhydro ring at the MurNAc residue. MltD contains an N-terminal transglycosylase domain and two lysin motif (LysM) repeats at its C-terminus . MltD is an outer membrane lipoprotein . A crystal structure of the LysM-type peptidoglycan-binding domain (residues 389 to 452) containing a βααβ secondary structure has been reported . Purified MltD (residues 18-452) degrades the purified cell wall sacculus to produce the following major products (in order of abundance): tetra-A1 (GlcNAc-1,6-anhydro-MurNAc monomer with tetrapeptide stem); tri-A1 (GlcNAc-1,6-anhydro-MurNAc monomer with tripeptide stem); di-A1 (GlcNAc-1,6-anhydro-MurNAc monomer with dipeptide stem) plus other variations in smaller amounts...

## Biological Role

Catalyzes RXN-17391 (reaction.ecocyc.RXN-17391), RXN-17392 (reaction.ecocyc.RXN-17392).

## Annotation

FUNCTION: Murein-degrading enzyme. May play a role in recycling of muropeptides during cell elongation and/or cell division (By similarity). {ECO:0000250}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-17391|reaction.ecocyc.RXN-17391]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-17392|reaction.ecocyc.RXN-17392]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0211|gene.b0211]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEZ7`
- `KEGG:ecj:JW5018;eco:b0211;ecoc:C3026_00985;`
- `GeneID:93777212;945694;`
- `GO:GO:0000270; GO:0005886; GO:0008932; GO:0008933; GO:0016020; GO:0071555`
- `EC:4.2.2.n1`

## Notes

Membrane-bound lytic murein transglycosylase D (EC 4.2.2.n1) (Murein hydrolase D) (Regulatory protein DniR)
