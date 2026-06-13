---
entity_id: "protein.P77585"
entity_type: "protein"
name: "ypdE"
source_database: "UniProt"
source_id: "P77585"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ypdE b2384 JW2381"
---

# ypdE

`protein.P77585`

## Static

- Type: `protein`
- Source: `UniProt:P77585`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Has a broad aminopeptidase activity on non-blocked peptides by progressively cleaving amino acids off the peptide substrate. Aminopeptidase activity stops at the residue before the first proline in the peptide. Cannot cleave when proline is the first N-terminal residue. {ECO:0000269|PubMed:15901689}. YpdE is a metalloaminopeptidase with broad activity on nonblocked peptides. Its is unable to cleave at Xaa-Pro or Pro-Xaa . A ypdE deletion mutant is more sensitive to kasugamycin than wild type .

## Biological Role

Catalyzes RXN0-5051 (reaction.ecocyc.RXN0-5051). Bound by Cobalt ion (molecule.C00175), Nickel(2+) (molecule.C19609), Cu2+ (molecule.ecocyc.CU_2), Mn2+ (molecule.ecocyc.MN_2).

## Annotation

FUNCTION: Has a broad aminopeptidase activity on non-blocked peptides by progressively cleaving amino acids off the peptide substrate. Aminopeptidase activity stops at the residue before the first proline in the peptide. Cannot cleave when proline is the first N-terminal residue. {ECO:0000269|PubMed:15901689}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5051|reaction.ecocyc.RXN0-5051]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (5)

- `binds` <-- [[molecule.C00175|molecule.C00175]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.C19609|molecule.C19609]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.CU_2|molecule.ecocyc.CU_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `binds` <-- [[molecule.ecocyc.MN_2|molecule.ecocyc.MN_2]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2384|gene.b2384]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P77585`
- `KEGG:ecj:JW2381;eco:b2384;ecoc:C3026_13255;`
- `GeneID:946848;`
- `GO:GO:0004177; GO:0006508; GO:0008237; GO:0046872; GO:0070006`
- `EC:3.4.11.-`

## Notes

Aminopeptidase YpdE (EC 3.4.11.-)
