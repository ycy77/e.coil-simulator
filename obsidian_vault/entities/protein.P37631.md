---
entity_id: "protein.P37631"
entity_type: "protein"
name: "rdsA"
source_database: "UniProt"
source_id: "P37631"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "rdsA yhiN b3492 JW3459"
---

# rdsA

`protein.P37631`

## Static

- Type: `protein`
- Source: `UniProt:P37631`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the synthesis of 5,6-dihydrouridine (D) at position 2449 in 23S rRNA (PubMed:39078675). Can use NADH as a source of reducing equivalents but not NADPH (PubMed:39078675). {ECO:0000269|PubMed:39078675}. The RdsA is responsible for the dihydrouridylation of uridine 2449 in 23S-rRNAs. Using the rhodamine labelling method (Rho-seq) for detecting dihydrouridine (D) in position 2449 of 23S rRNAs and rRNA from various mutant E. coli strains, only the ΔrdsA BW25113 strain lacked D2449. Characterization of RdsA using an AlphaFold model and homologous structures found it to be a flavoprotein with a conserved FAD binding pocket that binds FAD noncovalently . Kinetic analyses measured NADH rather than NADPH oxidase activity with hydride transfer being the likely chemical mechanism . RdsA = ribosomal dihydrouridine synthase A

## Biological Role

Catalyzes RXN-25215 (reaction.ecocyc.RXN-25215).

## Annotation

FUNCTION: Catalyzes the synthesis of 5,6-dihydrouridine (D) at position 2449 in 23S rRNA (PubMed:39078675). Can use NADH as a source of reducing equivalents but not NADPH (PubMed:39078675). {ECO:0000269|PubMed:39078675}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN-25215|reaction.ecocyc.RXN-25215]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3492|gene.b3492]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P37631`
- `KEGG:ecj:JW3459;eco:b3492;ecoc:C3026_18915;`
- `GeneID:947996;`
- `GO:GO:0000154; GO:0005829; GO:0106413`
- `EC:1.3.1.-`

## Notes

Ribosomal RNA dihydrouridine synthase (rRNA dihydrouridine synthase) (EC 1.3.1.-) (Ribosomal dihydrouridine synthase A)
