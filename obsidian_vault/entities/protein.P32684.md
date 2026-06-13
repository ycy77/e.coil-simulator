---
entity_id: "protein.P32684"
entity_type: "protein"
name: "rluF"
source_database: "UniProt"
source_id: "P32684"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rluF yjbC b4022 JW3982"
---

# rluF

`protein.P32684`

## Static

- Type: `protein`
- Source: `UniProt:P32684`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Dual specificity enzyme that catalyzes the synthesis of pseudouridine from uracil-2604 in 23S ribosomal RNA and from uracil-35 in the anticodon of tRNA(Tyr) (PubMed:11720289, PubMed:27551044). Can, to a small extent, also react with uracil-2605 (PubMed:11720289). {ECO:0000269|PubMed:11720289, ECO:0000269|PubMed:27551044}. RluF is the pseudouridine synthase that catalyzes formation of pseudouridine at position 2604 in 23S rRNA and position 35 within the anticodon of TYR-tRNAs tRNATyr . RluF belongs to the RsuA family of RNA pseudouridine synthases . Pseudouridine modification of tRNATyr appears to increase the translation efficiency of mRNAs rich in Tyr codons . Neither an rluF null mutant nor an rluB rluF double null mutant exhibit an obvious growth defect. The conserved active site residue Asp107 is essential for activity . The crystal structure of RluF bound to the 23S rRNA stem-loop it modifies has been solved at 3.0 Å resolution. The structure shows a conserved binding groove for the RNA stem-loop in the catalytic domain. The bulge normally located at A2602 is folded into the stem and causes U2604 to flip into the active site, accounting for the site specificity of RluF . A crystal structure of the catalytic domain of RluF from E. coli O157:H7 has been solved at 2.6 Å resolution. Analytical ultracentrifugation showed that RluF is a monomer in solution . Reviews:

## Biological Role

Catalyzes RXN-11835 (reaction.ecocyc.RXN-11835), RXN0-7253 (reaction.ecocyc.RXN0-7253).

## Annotation

FUNCTION: Dual specificity enzyme that catalyzes the synthesis of pseudouridine from uracil-2604 in 23S ribosomal RNA and from uracil-35 in the anticodon of tRNA(Tyr) (PubMed:11720289, PubMed:27551044). Can, to a small extent, also react with uracil-2605 (PubMed:11720289). {ECO:0000269|PubMed:11720289, ECO:0000269|PubMed:27551044}.

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN-11835|reaction.ecocyc.RXN-11835]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN0-7253|reaction.ecocyc.RXN0-7253]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b4022|gene.b4022]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32684`
- `KEGG:ecj:JW3982;eco:b4022;ecoc:C3026_21725;`
- `GeneID:948519;`
- `GO:GO:0000455; GO:0003723; GO:0009982; GO:0031119; GO:0106029; GO:0120159; GO:0160138`
- `EC:5.4.99.-; 5.4.99.21`

## Notes

Dual-specificity RNA pseudouridine synthase RluF (EC 5.4.99.-) (EC 5.4.99.21) (23S rRNA pseudouridine(2604) synthase) (Ribosomal large subunit pseudouridine synthase F) (rRNA pseudouridylate synthase F) (rRNA-uridine isomerase F) (tRNA(Tyr) pseudouridine(35) synthase)
