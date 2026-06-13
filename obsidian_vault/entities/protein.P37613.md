---
entity_id: "protein.P37613"
entity_type: "protein"
name: "panZ"
source_database: "UniProt"
source_id: "P37613"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "panZ panM yhhK b3459 JW3424"
---

# panZ

`protein.P37613`

## Static

- Type: `protein`
- Source: `UniProt:P37613`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Controls both the activation and catalytic activity of PanD in a coenzyme A (CoA)-dependent fashion. Binding of CoA or a derivative to PanZ leads to interaction with PanD, which promotes the processing and activation of pro-PanD, and subsequent substrate-mediated inhibition of the active form of PanD (PubMed:23170229, PubMed:25910242). Inhibition of PanD activity is probably the primary metabolic role of PanZ, allowing negative feedback regulation of pantothenate biosynthesis by CoA (PubMed:25910242). {ECO:0000269|PubMed:23170229, ECO:0000269|PubMed:25910242}. Coenzyme A-bound PanZ promotes activation of the ASPDECARBOX-MONOMER "PanD" proenzyme and negatively regulates the aspartate α-decarboxylase activity of activated PanD . PanZ is not an enzyme but a stoichiometric facilitator of PanD activation. Formation of a PanD-PanZ complex stabilizes a conformation of PanD in which the serine-25 hydroxyl group moves to a close proximity to the adjacent carbonyl group, thus facilitating an attack on the G24-S25 peptide bond . Addition of PanZ to an assay of β-alanine synthesis by PanD enhances activity 24-fold . Coenzyme A is a pantothenate metabolite; regulation of PANTO-PWY by feedback inhibition of the committed input, PWY-5155 β-alanine, via the CoA-binding protein PanZ is a novel form of regulation...

## Annotation

FUNCTION: Controls both the activation and catalytic activity of PanD in a coenzyme A (CoA)-dependent fashion. Binding of CoA or a derivative to PanZ leads to interaction with PanD, which promotes the processing and activation of pro-PanD, and subsequent substrate-mediated inhibition of the active form of PanD (PubMed:23170229, PubMed:25910242). Inhibition of PanD activity is probably the primary metabolic role of PanZ, allowing negative feedback regulation of pantothenate biosynthesis by CoA (PubMed:25910242). {ECO:0000269|PubMed:23170229, ECO:0000269|PubMed:25910242}.

## Outgoing Edges (1)

- `represses` --> [[reaction.ecocyc.ASPDECARBOX-RXN|reaction.ecocyc.ASPDECARBOX-RXN]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b3459|gene.b3459]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37613`
- `KEGG:ecj:JW3424;eco:b3459;ecoc:C3026_18735;`
- `GeneID:947963;`
- `GO:GO:0015940; GO:0016485; GO:0016747; GO:0031638; GO:1905502`

## Notes

PanD regulatory factor
