---
entity_id: "protein.P77379"
entity_type: "protein"
name: "rclR"
source_database: "UniProt"
source_id: "P77379"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rclR ykgD b0305 JW0298"
---

# rclR

`protein.P77379`

## Static

- Type: `protein`
- Source: `UniProt:P77379`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Involved in reactive chlorine species (RCS) stress resistance. Up-regulates, in response to hypochlorous acid (HOCl), the expression of three genes essential for survival of RCS stress (rclA, rclB and rclC) and its own expression. {ECO:0000269|PubMed:24078635}. RclR (formerly YkgD) is a redox-sensitive transcriptional activator that belongs to the AraC family, whose highly conserved cysteine residues are highly specifically sensitive to oxidation by reactive chlorine species (RCS) . RclR relies on the reversible oxidation of conserved redox-sensitive cysteine residues to specifically sense RCS and control the expression of genes essential for survival under reactive chlorine (HOCl) stress . RclR is activated by hypochlorous acid (HOCl) or N-chlorotaurine, and that activation may involve formation of one disulfide bond. RclR contains two conserved cysteine residues (Cys-21 and Cys-89) and two conserved histidine residues (His-42 and His-75). Cys-21 and Cys-89 are important in the activation of RclR in vivo. Cys-21 could play the more critical role in the RclR redox response. Oxidation of both cysteines leads to strong, highly specific activation of expression of genes required for survival under RCS stress. The His residues are involved in preventing DNA binding when RclR levels are reduced...

## Annotation

FUNCTION: Involved in reactive chlorine species (RCS) stress resistance. Up-regulates, in response to hypochlorous acid (HOCl), the expression of three genes essential for survival of RCS stress (rclA, rclB and rclC) and its own expression. {ECO:0000269|PubMed:24078635}.

## Outgoing Edges (3)

- `activates` --> [[gene.b0301|gene.b0301]] `RegulonDB` `S` - regulator=RclR; target=rclC; function=+
- `activates` --> [[gene.b0303|gene.b0303]] `RegulonDB` `S` - regulator=RclR; target=rclB; function=+
- `activates` --> [[gene.b0304|gene.b0304]] `RegulonDB` `S` - regulator=RclR; target=rclA; function=+

## Incoming Edges (1)

- `encodes` <-- [[gene.b0305|gene.b0305]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77379`
- `KEGG:ecj:JW0298;eco:b0305;ecoc:C3026_01495;ecoc:C3026_24670;`
- `GeneID:945616;`
- `GO:GO:0000976; GO:0001216; GO:0003700; GO:0006355; GO:0045893; GO:0090347`

## Notes

RCS-specific HTH-type transcriptional activator RclR (Reactive chlorine resistance protein R)
