---
entity_id: "protein.P0AB38"
entity_type: "protein"
name: "lpoB"
source_database: "UniProt"
source_id: "P0AB38"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}; Lipid-anchor {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}; Periplasmic side {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}. Note=Localizes to the divisome and to the lateral wall."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "lpoB ycfM b1105 JW5157"
---

# lpoB

`protein.P0AB38`

## Static

- Type: `protein`
- Source: `UniProt:P0AB38`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}; Lipid-anchor {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}; Periplasmic side {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}. Note=Localizes to the divisome and to the lateral wall.

## Enriched Summary

FUNCTION: Regulator of peptidoglycan synthesis that is essential for the function of penicillin-binding protein 1B (PBP1b). Stimulates transpeptidase and transglycosylase activities of PBP1b in vitro. May also contribute to outer membrane constriction during cell division, in complex with PBP1b. {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}. LpoB is an outer membrane lipoprotein that forms a complex with CPLX0-3951 "penicillin binding protein 1B (PBP1B)" and is essential for its peptidoglycan glycosyl transferase activity and/or transpeptidase activity . Purified LpoB interacts with PBPIB and stimulates both its glycosyltransferase and transpeptidase activitities in vitro . LpoB binds and allosterically activates both the transpeptidase and transglycosylase activities of PBP1B (see further ). An lpoB- mutant is synthetically lethal in a PBP1A defective strain and this phenotype can be corrected by the expression of lpoB from a plasmid . Depletion of LpoB in the absence of PBP1A results in the same terminal phenotype as PBP1A- PBP1B- cells and lpoB- mutants show a similar βlactam hypersensitivity phenotype to PBP1B- mutants . Purified LpoB activates PBP1B activity in vitro and affects the length of glycan chains with shorter polymers produced in the presence of LpoB...

## Annotation

FUNCTION: Regulator of peptidoglycan synthesis that is essential for the function of penicillin-binding protein 1B (PBP1b). Stimulates transpeptidase and transglycosylase activities of PBP1b in vitro. May also contribute to outer membrane constriction during cell division, in complex with PBP1b. {ECO:0000269|PubMed:21183073, ECO:0000269|PubMed:21183074}.

## Outgoing Edges (2)

- `activates` --> [[reaction.ecocyc.RXN-16650|reaction.ecocyc.RXN-16650]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity
- `activates` --> [[reaction.ecocyc.RXN-16659|reaction.ecocyc.RXN-16659]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b1105|gene.b1105]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AB38`
- `KEGG:ecj:JW5157;eco:b1105;ecoc:C3026_06670;`
- `GeneID:93776303;948536;`
- `GO:GO:0008047; GO:0008360; GO:0009252; GO:0009279; GO:0019899; GO:0030234; GO:0031241`

## Notes

Penicillin-binding protein activator LpoB (PBP activator LpoB) (Lipoprotein activator of PBP from the outer membrane B)
