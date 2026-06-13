---
entity_id: "protein.P76004"
entity_type: "protein"
name: "ycgM"
source_database: "UniProt"
source_id: "P76004"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycgM b1180 JW1169"
---

# ycgM

`protein.P76004`

## Static

- Type: `protein`
- Source: `UniProt:P76004`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Tautomerase that converts enol-oxaloacetate to the keto form of oxaloacetate. {ECO:0000269|PubMed:38287013}. This protein belongs to a highly conserved fumarylacetoacetate hydrolase domain (FAHD)-containing protein family that carries out oxaloacetate (OAA) tautomerase (OAT) activity, which can run in reverse to convert enol-OAA to keto-OAA, thus removing the enol-OAA inhibition of CPLX0-8160 (SDH) within the TCA . A ΔycgM mutant showed significant growth defects and small cell size phenotypes relative to wild-type strains, whereas a double mutant with the catalytic subunit, EG10931, resulted in a similar phenotype that was less severe because the SDH couldn't form the SDH inhibitor, enol-OAA. Metabolic profiling results are consistent with SDH inhibition of the TCA cycle and with YcgM being a metabolite repair enzyme .

## Biological Role

Catalyzes oxaloacetate keto-enol-isomerase (reaction.R00363), OXALOACETATE-TAUTOMERASE-RXN (reaction.ecocyc.OXALOACETATE-TAUTOMERASE-RXN).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)

## Annotation

FUNCTION: Tautomerase that converts enol-oxaloacetate to the keto form of oxaloacetate. {ECO:0000269|PubMed:38287013}.

## Pathways

- `eco00620` Pyruvate metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00363|reaction.R00363]] `KEGG` `database` - via EC:5.3.2.2
- `catalyzes` --> [[reaction.ecocyc.OXALOACETATE-TAUTOMERASE-RXN|reaction.ecocyc.OXALOACETATE-TAUTOMERASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1180|gene.b1180]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76004`
- `KEGG:ecj:JW1169;eco:b1180;ecoc:C3026_06955;`
- `GeneID:946115;`
- `GO:GO:0006107; GO:0018773; GO:0046872; GO:0050163`
- `EC:5.3.2.2`

## Notes

Oxaloacetate tautomerase YcgM (EC 5.3.2.2)
