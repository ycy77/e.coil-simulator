---
entity_id: "protein.P25906"
entity_type: "protein"
name: "pdxI"
source_database: "UniProt"
source_id: "P25906"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "pdxI ydbC b1406 JW1403"
---

# pdxI

`protein.P25906`

## Static

- Type: `protein`
- Source: `UniProt:P25906`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the NAD(P)H-dependent reduction of pyridoxal to pyridoxine in vitro. Is not able to reduce 4-pyridoxate, and to oxidize pyridoxine or pyridoxamine (PubMed:27941785). Has Kemp eliminase activity towards the non-physiological substrate 5-nitrobenzisoxazole, producing 4-nitro-2-cyanophenol; this activity is not considered to be physiologically relevant (PubMed:21332126). {ECO:0000269|PubMed:21332126, ECO:0000269|PubMed:27941785}. The NADPH-dependent pyridoxal reductase (PdxI) contributes to the PLPSAL-PWY (e.g. vitamin B6 salvage) pathway . The catalytic activity of PdxI was first discovered in a large-scale metabolomics screen for enzymatic activities of uncharacterized proteins in E. coli . Crystal structures of unliganded, NADPH-bound and NADPH-PL bound PdxI have been determined to resolutions of 2.0 - 2.3 Å PdxI belongs to aldo-keto reductase (AKR) superfamily with a TIM barrel-fold made of only 6 instead of 8 beta strands and with an Arg126 replacing the catalytic His residue. Kinetic and deletion mutant analyses indicate that the 2 distinct routes for PL conversion to PLP depend on the concentrations of PdxI relative to PdxK and PdxH, their regulatory properties and kinetic parameters . PdxI has Kemp eliminase activity towards the non-physiological substrate 5-nitrobenzisoxazole, producing 4-nitro 2-cyanophenol...

## Biological Role

Catalyzes PYRIDOXINE-4-DEHYDROGENASE-RXN (reaction.ecocyc.PYRIDOXINE-4-DEHYDROGENASE-RXN), RXN0-7143 (reaction.ecocyc.RXN0-7143).

## Enriched Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the NAD(P)H-dependent reduction of pyridoxal to pyridoxine in vitro. Is not able to reduce 4-pyridoxate, and to oxidize pyridoxine or pyridoxamine (PubMed:27941785). Has Kemp eliminase activity towards the non-physiological substrate 5-nitrobenzisoxazole, producing 4-nitro-2-cyanophenol; this activity is not considered to be physiologically relevant (PubMed:21332126). {ECO:0000269|PubMed:21332126, ECO:0000269|PubMed:27941785}.

## Pathways

- `eco00750` Vitamin B6 metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.PYRIDOXINE-4-DEHYDROGENASE-RXN|reaction.ecocyc.PYRIDOXINE-4-DEHYDROGENASE-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7143|reaction.ecocyc.RXN0-7143]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1406|gene.b1406]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P25906`
- `KEGG:ecj:JW1403;eco:b1406;ecoc:C3026_08195;`
- `GeneID:75203487;945980;`
- `GO:GO:0005737; GO:0005829; GO:0009443; GO:0050236`
- `EC:1.1.1.65`

## Notes

Pyridoxine 4-dehydrogenase (EC 1.1.1.65)
