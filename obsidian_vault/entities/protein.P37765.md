---
entity_id: "protein.P37765"
entity_type: "protein"
name: "rluB"
source_database: "UniProt"
source_id: "P37765"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rluB yciL b1269 JW1261"
---

# rluB

`protein.P37765`

## Static

- Type: `protein`
- Source: `UniProt:P37765`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Responsible for synthesis of pseudouridine from uracil-2605 in 23S ribosomal RNA. {ECO:0000269|PubMed:11720289}. RluB is the pseudouridine synthase that catalyzes formation of pseudouridine at position 2605 in 23S rRNA. RluB belongs to the RsuA family of RNA pseudouridine synthases . RluB is associated with a particle the migrates slightly slower than the 50S ribosomal subunit, suggesting that it acts during 50S subunit maturation . Pseudouridine residues outside of helix-loop 69, including Ψ2605, appear to be made during the early steps of large ribosome subunit assembly . Crystal structures of the catalytic domain alone and in a complex with the substrate stem-loop have been solved, revealing a covalent bond between the hydroxyl group of the active site Tyr140 and the C6 of the U2605 substrate with the base flipped into the active site. The authors propose a Michael addition reaction mechanism for pseudouridine synthesis . The conserved active site residue Asp110 is essential for activity , while a Tyr140Phe mutant retains 3% of wild-type enzymatic activity . An rluB null mutant or an rluB rluF double null mutant exhibits no obvious growth defect . Deletion of rluB leads to accumulation of free 30S and 50S ribosomal subunits . Reviews:

## Biological Role

Catalyzes RXN-11836 (reaction.ecocyc.RXN-11836).

## Annotation

FUNCTION: Responsible for synthesis of pseudouridine from uracil-2605 in 23S ribosomal RNA. {ECO:0000269|PubMed:11720289}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-11836|reaction.ecocyc.RXN-11836]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b1269|gene.b1269]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37765`
- `KEGG:ecj:JW1261;eco:b1269;ecoc:C3026_07435;`
- `GeneID:86859917;86946628;945840;`
- `GO:GO:0000455; GO:0003723; GO:0005829; GO:0120159; GO:0160139`
- `EC:5.4.99.22`

## Notes

Ribosomal large subunit pseudouridine synthase B (EC 5.4.99.22) (23S rRNA pseudouridine(2605) synthase) (rRNA pseudouridylate synthase B) (rRNA-uridine isomerase B)
