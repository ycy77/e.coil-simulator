---
entity_id: "protein.P21515"
entity_type: "protein"
name: "acpH"
source_database: "UniProt"
source_id: "P21515"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "acpH yajB b0404 JW0394"
---

# acpH

`protein.P21515`

## Static

- Type: `protein`
- Source: `UniProt:P21515`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Converts holo-ACP to apo-ACP by hydrolytic cleavage of the phosphopantetheine prosthetic group from ACP. {ECO:0000255|HAMAP-Rule:MF_01950, ECO:0000269|PubMed:16107329}. Acyl carrier protein (ACP) phosphodiesterase is responsible for the cleavage of PANTETHEINE-P (4'-PP) from ACP by hydrolysis of the phosphodiester linkage between 4'-PP and the hydroxyl group of a serine residue of the ACP apoprotein . This reaction requires divalent cations . Monomeric and trimeric forms of the purified protein are present in solution . AcpH is responsible for turnover of the ACP prosthetic group in vivo, but is not essential for growth. The physiological role of AcpH is unknown . Review:

## Biological Role

Catalyzes 3.1.4.14-RXN (reaction.ecocyc.3.1.4.14-RXN). Bound by Zinc cation (molecule.C00038), Cobalt ion (molecule.C00175), Magnesium cation (molecule.C00305), Fe2+ (molecule.C14818), Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Converts holo-ACP to apo-ACP by hydrolytic cleavage of the phosphopantetheine prosthetic group from ACP. {ECO:0000255|HAMAP-Rule:MF_01950, ECO:0000269|PubMed:16107329}.

## Pathways

- `eco00770` Pantothenate and CoA biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.1.4.14-RXN|reaction.ecocyc.3.1.4.14-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (6)

- `binds` <-- [[molecule.C00038|molecule.C00038]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C14818|molecule.C14818]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0404|gene.b0404]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P21515`
- `KEGG:ecj:JW0394;eco:b0404;ecoc:C3026_01965;`
- `GeneID:949132;`
- `GO:GO:0006633; GO:0008770`
- `EC:3.1.4.14`

## Notes

Acyl carrier protein phosphodiesterase (ACP phosphodiesterase) (EC 3.1.4.14)
