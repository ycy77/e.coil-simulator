---
entity_id: "protein.P0C0K3"
entity_type: "protein"
name: "srkA"
source_database: "UniProt"
source_id: "P0C0K3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01497, ECO:0000305|PubMed:17302814}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "srkA rdoA yihE b3859 JW3831"
---

# srkA

`protein.P0C0K3`

## Static

- Type: `protein`
- Source: `UniProt:P0C0K3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_01497, ECO:0000305|PubMed:17302814}.

## Enriched Summary

FUNCTION: A protein kinase that (auto)phosphorylates on Ser and Thr residues (PubMed:17302814). Probably acts to suppress the effects of stress linked to accumulation of reactive oxygen species. Protects cells from stress by antagonizing the MazE-MazF TA module, probably indirectly as it has not been seen to phosphorylate MazE, MazF or MazG (PubMed:23416055). Probably involved in the extracytoplasmic stress response (PubMed:9159398). {ECO:0000255|HAMAP-Rule:MF_01497, ECO:0000269|PubMed:17302814, ECO:0000269|PubMed:23416055, ECO:0000269|PubMed:9159398}. SrkA is a serine/threonine protein kinase that protects cells from several types of lethal stress . SrkA is able to autophosphorylate at serine and threonine, but not tyrosine residues . The protein kinase activity is required for stress protection by SrkA . SrkA is also able to phosphorylate a general kinase substrate, myelin basic protein, in vitro. The native substrate for SrkA has not been identified yet . A crystal structure of SrkA has been determined at 2.8 Å resolution and shows structural similarity to protein kinases . A D217A mutation abolishes catalytic activity . A ΔsrkA mutant is hypersusceptible to the lethal effects of UV light, hydrogen peroxide, nalidixic acid and certain other antibiotics, but does not affect their minimum inhibitory concentration (MIC)...

## Biological Role

Catalyzes PROTEIN-KINASE-RXN (reaction.ecocyc.PROTEIN-KINASE-RXN).

## Annotation

FUNCTION: A protein kinase that (auto)phosphorylates on Ser and Thr residues (PubMed:17302814). Probably acts to suppress the effects of stress linked to accumulation of reactive oxygen species. Protects cells from stress by antagonizing the MazE-MazF TA module, probably indirectly as it has not been seen to phosphorylate MazE, MazF or MazG (PubMed:23416055). Probably involved in the extracytoplasmic stress response (PubMed:9159398). {ECO:0000255|HAMAP-Rule:MF_01497, ECO:0000269|PubMed:17302814, ECO:0000269|PubMed:23416055, ECO:0000269|PubMed:9159398}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.PROTEIN-KINASE-RXN|reaction.ecocyc.PROTEIN-KINASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3859|gene.b3859]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0C0K3`
- `KEGG:ecj:JW3831;eco:b3859;ecoc:C3026_20860;`
- `GeneID:948346;`
- `GO:GO:0000287; GO:0004674; GO:0005524; GO:0005737; GO:0006950; GO:0106310`
- `EC:2.7.11.1`

## Notes

Stress response kinase A (EC 2.7.11.1) (Serine/threonine protein kinase YihE) (Serine/threonine-protein kinase SrkA)
