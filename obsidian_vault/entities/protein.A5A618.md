---
entity_id: "protein.A5A618"
entity_type: "protein"
name: "ynhF"
source_database: "UniProt"
source_id: "A5A618"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:19121005, ECO:0000305|PubMed:21778229}; Single-pass membrane protein {ECO:0000269|PubMed:19121005, ECO:0000269|PubMed:21778229}. Note=May be able to insert into the membrane in both orientations."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ynhF b4602 JW1649.1"
---

# ynhF

`protein.A5A618`

## Static

- Type: `protein`
- Source: `UniProt:A5A618`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305|PubMed:19121005, ECO:0000305|PubMed:21778229}; Single-pass membrane protein {ECO:0000269|PubMed:19121005, ECO:0000269|PubMed:21778229}. Note=May be able to insert into the membrane in both orientations.

## Enriched Summary

Uncharacterized protein YnhF CydH (also called CydY) is a small, noncatalytic, single transmembrane accessory subunit of CYT-D-UBIOX-CPLX . In the cryo-EM structure of cytochrome bd-I, CydH binds to a hydrophobic cleft in CydA . CydH appears to block dioxygen access to heme b595 . CydH is a chloroform-soluble protein that extracts with the lipid fraction of E. coli . CydH contains a predicted transmembrane segment, and the protein can be found in the membrane fraction . Experimental topology analysis suggests that CydH may be inserted into the membrane with dual orientation . CydH is expressed during both exponential growth and stationary phase . The amount of CydH protein is approximately 4-fold greater when cells are grown under oxygen limited conditions compared to aerobic growth in rich media . Tandem mass spectrometry indicates that the formyl group attached to the N-terminal methionine is retained .

## Biological Role

Component of cytochrome bd-I ubiquinol:oxygen oxidoreductase (complex.ecocyc.CYT-D-UBIOX-CPLX).

## Annotation

Uncharacterized protein YnhF

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CYT-D-UBIOX-CPLX|complex.ecocyc.CYT-D-UBIOX-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b4602|gene.b4602]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:A5A618`
- `KEGG:eco:b4602;ecoc:C3026_09510;`
- `GeneID:5061505;86859578;93775812;`
- `GO:GO:0005886; GO:0016020; GO:0070069; GO:0071456`

## Notes

Uncharacterized protein YnhF
