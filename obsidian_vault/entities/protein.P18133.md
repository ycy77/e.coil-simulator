---
entity_id: "protein.P18133"
entity_type: "protein"
name: "pncB"
source_database: "UniProt"
source_id: "P18133"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pncB b0931 JW0914"
---

# pncB

`protein.P18133`

## Static

- Type: `protein`
- Source: `UniProt:P18133`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the synthesis of beta-nicotinate D-ribonucleotide from nicotinate and 5-phospho-D-ribose 1-phosphate at the expense of ATP. {ECO:0000255|HAMAP-Rule:MF_00570, ECO:0000269|PubMed:2211655}. Nicotinate phosphoribosyltransferase (NAPRTase) mediates the formation of nicotinate mononucleotide from exogenous nicotinate and PRPP. The product is then converted intracellularly into NAD . NAPRTase appears to be the rate-limiting enzyme in the biosynthesis of NAD from nicotinate . NAPRTase levels decrease in response to added extracellular nicotinate. Overexpression of pncB increases the intracellular level of NAD . NAPRTase was reported to localize to the periplasm . However, the enzyme does not have a recognizable signal sequence, and N-terminal sequencing of the partially purified protein gives no indication of N-terminal processing of the enzyme. Additional unpublished evidence for localization to the periplasm or cytoplasmic membrane is mentioned . pncB shows differential codon adaptation, resulting in differential translation efficiency signatures, in thermophilic microbes. It was therefore predicted to play a role in the heat shock response. A pncB deletion mutant was shown to be more sensitive than wild-type specifically to heat shock, but not other stresses . PncB: "pyridine nucleotide cycle"

## Biological Role

Catalyzes 5-phospho-alpha-D-ribose 1-diphosphate:nicotinate ligase (ADP, diphosphate-forming) (reaction.R01724), NICOTINATEPRIBOSYLTRANS-RXN (reaction.ecocyc.NICOTINATEPRIBOSYLTRANS-RXN).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the synthesis of beta-nicotinate D-ribonucleotide from nicotinate and 5-phospho-D-ribose 1-phosphate at the expense of ATP. {ECO:0000255|HAMAP-Rule:MF_00570, ECO:0000269|PubMed:2211655}.

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R01724|reaction.R01724]] `KEGG` `database` - via EC:6.3.4.21
- `catalyzes` --> [[reaction.ecocyc.NICOTINATEPRIBOSYLTRANS-RXN|reaction.ecocyc.NICOTINATEPRIBOSYLTRANS-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b0931|gene.b0931]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P18133`
- `KEGG:ecj:JW0914;eco:b0931;ecoc:C3026_05720;`
- `GeneID:75171005;946648;`
- `GO:GO:0004516; GO:0005829; GO:0009408; GO:0009435; GO:0016879; GO:0034355`
- `EC:6.3.4.21`

## Notes

Nicotinate phosphoribosyltransferase (NAPRTase) (EC 6.3.4.21)
