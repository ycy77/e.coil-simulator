---
entity_id: "protein.P76242"
entity_type: "protein"
name: "nimT"
source_database: "UniProt"
source_id: "P76242"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nimT yeaN b1791 JW1780"
---

# nimT

`protein.P76242`

## Static

- Type: `protein`
- Source: `UniProt:P76242`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Involved in efflux of 2-nitroimidazole. {ECO:0000269|PubMed:25790494}. A ΔnimT mutant is more sensitive to the natural antibiotic, 2-nitroimidazole, than wild type under both aerobic and anaerobic conditions. nimT appears to be the single target gene of the G6976-MONOMER "NimR" transcriptional regulator . Overexpression of nimT from a plasmid confers resistance to the toxic chemical, bromoacetate . NimT (formerly YeaN) is a member of the Cyanate Porter (CP) family within the Major Facilitator Superfamily (MFS) of transporters .

## Biological Role

Catalyzes TRANS-RXN-273 (reaction.ecocyc.TRANS-RXN-273), TRANS-RXN0-596 (reaction.ecocyc.TRANS-RXN0-596).

## Annotation

FUNCTION: Involved in efflux of 2-nitroimidazole. {ECO:0000269|PubMed:25790494}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN-273|reaction.ecocyc.TRANS-RXN-273]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-596|reaction.ecocyc.TRANS-RXN0-596]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1791|gene.b1791]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76242`
- `KEGG:ecj:JW1780;eco:b1791;ecoc:C3026_10210;`
- `GeneID:946309;`
- `GO:GO:0005886; GO:0022857; GO:0046677`

## Notes

2-nitroimidazole transporter
