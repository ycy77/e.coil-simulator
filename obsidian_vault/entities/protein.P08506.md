---
entity_id: "protein.P08506"
entity_type: "protein"
name: "dacC"
source_database: "UniProt"
source_id: "P08506"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:3330754}; Peripheral membrane protein {ECO:0000269|PubMed:3330754}; Periplasmic side {ECO:0000269|PubMed:3330754}. Note=N-terminus lies in the periplasmic space, targeted there by the C-terminal amphiphilic helix (PMID:3330754)."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dacC b0839 JW0823"
---

# dacC

`protein.P08506`

## Static

- Type: `protein`
- Source: `UniProt:P08506`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000269|PubMed:3330754}; Peripheral membrane protein {ECO:0000269|PubMed:3330754}; Periplasmic side {ECO:0000269|PubMed:3330754}. Note=N-terminus lies in the periplasmic space, targeted there by the C-terminal amphiphilic helix (PMID:3330754).

## Enriched Summary

FUNCTION: Removes C-terminal D-alanyl residues from sugar-peptide cell wall precursors.

## Biological Role

Component of D-alanyl-D-alanine carboxypeptidase DacC (complex.ecocyc.CPLX0-8254).

## Enriched Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Removes C-terminal D-alanyl residues from sugar-peptide cell wall precursors.

## Pathways

- `eco00550` Peptidoglycan biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8254|complex.ecocyc.CPLX0-8254]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0839|gene.b0839]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P08506`
- `KEGG:ecj:JW0823;eco:b0839;ecoc:C3026_05250;`
- `GeneID:945455;`
- `GO:GO:0004180; GO:0005886; GO:0006508; GO:0008360; GO:0008658; GO:0009002; GO:0009252; GO:0009410; GO:0030288; GO:0042803; GO:0071555`
- `EC:3.4.16.4`

## Notes

D-alanyl-D-alanine carboxypeptidase DacC (DD-carboxypeptidase) (DD-peptidase) (EC 3.4.16.4) (Penicillin-binding protein 6) (PBP-6)
