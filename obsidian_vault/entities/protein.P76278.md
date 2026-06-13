---
entity_id: "protein.P76278"
entity_type: "protein"
name: "yebZ"
source_database: "UniProt"
source_id: "P76278"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yebZ b1840 JW1829"
---

# yebZ

`protein.P76278`

## Static

- Type: `protein`
- Source: `UniProt:P76278`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:15919996}; Multi-pass membrane protein {ECO:0000255}.

## Enriched Summary

FUNCTION: Component of the AZY copper uptake system (PubMed:40108346). YebZ functions as an energy-dependent copper importer (PubMed:40108346). The AZY proteins link copper import to multiple antibiotic resistance (PubMed:40108346). They are necessary for the copper-dependent activation of the mar operon, thus leading to multidrug antibiotic resistance via the mar pathway (PubMed:40108346). The AZY proteins may also be involved in copper delivery to membrane proteins, but they are not involved in copper tolerance or antioxidant defense (PubMed:34822841). {ECO:0000269|PubMed:34822841, ECO:0000269|PubMed:40108346}. YebZ is a member of the CopD family of copper-sequestering proteins; YebZ is encoded in an operon with the G7014-MONOMER copper-binding protein YobA and a periplasmic protein G7012-MONOMER YebY (the AZY operon); YobA-YebZ-YebY (the AZY proteins) constitute a copper uptake system that is essential for activation of the TU00190 mar operon and for resistance to the antibiotics norfloxacin, ciprofloxacin, and ampicillin . YebZ functions as an energy-dependent copper importer; YebZ activity is enhanced by YobA and diminished by YebY . The AZY proteins are implicated in delivering copper to membrane targets such as copper-dependent NADH-DHII-MONOMER (NDH-2) . Membranes prepared from a strain that lacks all three proteins (E...

## Biological Role

Catalyzes TRANS-RXN0-639 (reaction.ecocyc.TRANS-RXN0-639). Transports Cu2+ (molecule.ecocyc.CU_2).

## Annotation

FUNCTION: Component of the AZY copper uptake system (PubMed:40108346). YebZ functions as an energy-dependent copper importer (PubMed:40108346). The AZY proteins link copper import to multiple antibiotic resistance (PubMed:40108346). They are necessary for the copper-dependent activation of the mar operon, thus leading to multidrug antibiotic resistance via the mar pathway (PubMed:40108346). The AZY proteins may also be involved in copper delivery to membrane proteins, but they are not involved in copper tolerance or antioxidant defense (PubMed:34822841). {ECO:0000269|PubMed:34822841, ECO:0000269|PubMed:40108346}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.TRANS-RXN0-639|reaction.ecocyc.TRANS-RXN0-639]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `transports` --> [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc transporters.col equation

## Incoming Edges (1)

- `encodes` <-- [[gene.b1840|gene.b1840]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76278`
- `KEGG:ecj:JW1829;eco:b1840;ecoc:C3026_10485;`
- `GeneID:947078;`
- `GO:GO:0005886; GO:0098705`

## Notes

Copper transporter YebZ
