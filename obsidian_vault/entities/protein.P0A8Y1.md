---
entity_id: "protein.P0A8Y1"
entity_type: "protein"
name: "yjjG"
source_database: "UniProt"
source_id: "P0A8Y1"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yjjG b4374 JW4336"
---

# yjjG

`protein.P0A8Y1`

## Static

- Type: `protein`
- Source: `UniProt:P0A8Y1`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: Nucleotidase that shows high phosphatase activity toward non-canonical pyrimidine nucleotides and three canonical nucleoside 5'-monophosphates (UMP, dUMP, and dTMP), and very low activity against TDP, IMP, UDP, GMP, dGMP, AMP, dAMP, and 6-phosphogluconate. Appears to function as a house-cleaning nucleotidase in vivo, since the general nucleotidase activity of YjjG allows it to protect cells against non-canonical pyrimidine derivatives such as 5-fluoro-2'-deoxyuridine, 5-fluorouridine, 5-fluoroorotate, 5-fluorouracil, and 5-aza-2'-deoxycytidine, and prevents the incorporation of potentially mutagenic nucleotides into DNA. Its dUMP phosphatase activity that catalyzes the hydrolysis of dUMP to deoxyuridine is necessary for thymine utilization via the thymine salvage pathway. Is strictly specific to substrates with 5'-phosphates and shows no activity against nucleoside 2'- or 3'-monophosphates. {ECO:0000269|PubMed:15489502, ECO:0000269|PubMed:17189366, ECO:0000269|PubMed:17286574}. YjjG is a monophosphatase whose activity is essential for thymine salvage in a thyA (THYMIDYLATESYN-CPLX) mutant. The dUMP phosphatase activity of YjjG generates deoxyuridine, which can be used by DeoA to liberate the deoxyribose-1-phosphate required for salvage of thymine...

## Biological Role

Catalyzes 5-NUCLEOTID-RXN (reaction.ecocyc.5-NUCLEOTID-RXN), RXN-21067 (reaction.ecocyc.RXN-21067). Bound by Mn2+ (molecule.ecocyc.MN_2).

## Enriched Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Annotation

FUNCTION: Nucleotidase that shows high phosphatase activity toward non-canonical pyrimidine nucleotides and three canonical nucleoside 5'-monophosphates (UMP, dUMP, and dTMP), and very low activity against TDP, IMP, UDP, GMP, dGMP, AMP, dAMP, and 6-phosphogluconate. Appears to function as a house-cleaning nucleotidase in vivo, since the general nucleotidase activity of YjjG allows it to protect cells against non-canonical pyrimidine derivatives such as 5-fluoro-2'-deoxyuridine, 5-fluorouridine, 5-fluoroorotate, 5-fluorouracil, and 5-aza-2'-deoxycytidine, and prevents the incorporation of potentially mutagenic nucleotides into DNA. Its dUMP phosphatase activity that catalyzes the hydrolysis of dUMP to deoxyuridine is necessary for thymine utilization via the thymine salvage pathway. Is strictly specific to substrates with 5'-phosphates and shows no activity against nucleoside 2'- or 3'-monophosphates. {ECO:0000269|PubMed:15489502, ECO:0000269|PubMed:17189366, ECO:0000269|PubMed:17286574}.

## Pathways

- `eco00240` Pyrimidine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01232` Nucleotide metabolism (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.5-NUCLEOTID-RXN|reaction.ecocyc.5-NUCLEOTID-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `catalyzes` --> [[reaction.ecocyc.RXN-21067|reaction.ecocyc.RXN-21067]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b4374|gene.b4374]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A8Y1`
- `KEGG:ecj:JW4336;eco:b4374;ecoc:C3026_23630;`
- `GeneID:75169868;948899;`
- `GO:GO:0000166; GO:0002953; GO:0005737; GO:0008253; GO:0009222; GO:0009410; GO:0016791; GO:0019859; GO:0030145; GO:0043100`
- `EC:3.1.3.5`

## Notes

Pyrimidine 5'-nucleotidase YjjG (EC 3.1.3.5) (House-cleaning nucleotidase) (Non-canonical pyrimidine nucleotide phosphatase) (Nucleoside 5'-monophosphate phosphohydrolase) (dUMP phosphatase)
