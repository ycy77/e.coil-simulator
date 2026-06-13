---
entity_id: "protein.P76395"
entity_type: "protein"
name: "pphC"
source_database: "UniProt"
source_id: "P76395"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pphC yegK b2072 JW2057"
---

# pphC

`protein.P76395`

## Static

- Type: `protein`
- Source: `UniProt:P76395`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: PP2C-like phosphatase that can dephosphorylate YegI. In vitro, can hydrolyze p-nitrophenyl phosphate (pNPP) to p-nitrophenol. {ECO:0000269|PubMed:29967116}. PphC is a Mn2+-dependent protein phosphatase 2C (PP2C)-like protein-serine/threonine phosphatase . Both the protein sequence and the genome context differs between the otherwise closely related K-12 and B strains of E. coli. The PphC protein sequences are 93% identical. While the E. coli B REL606 genome encodes the YegI protein kinase immediatedly downstream of PphC, the two ORFs are separated by the divergently transcribed yegJ in E. coli K-12. It is notable that in long-term evolution experiments performed with E. coli B REL606, mutations in yegI have been found repeatedly. The E. coli B REL606 PphC was shown to dephosphorylate autophosphorylated YegI. The physiological role of the YegI/PphC kinase/phosphatase pair is so far unknown . PphC: "protein phosphatase C"

## Biological Role

Catalyzes 3.1.3.16-RXN (reaction.ecocyc.3.1.3.16-RXN). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Annotation

FUNCTION: PP2C-like phosphatase that can dephosphorylate YegI. In vitro, can hydrolyze p-nitrophenyl phosphate (pNPP) to p-nitrophenol. {ECO:0000269|PubMed:29967116}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.3.1.3.16-RXN|reaction.ecocyc.3.1.3.16-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2072|gene.b2072]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76395`
- `KEGG:ecj:JW2057;eco:b2072;`
- `GeneID:75205989;947269;`
- `GO:GO:0004722; GO:0016791`
- `EC:3.1.3.16`

## Notes

Serine/threonine-protein phosphatase 3 (EC 3.1.3.16) (PP2C-like Ser/Thr phosphatase) (Protein phosphatase C)
