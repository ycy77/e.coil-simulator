---
entity_id: "protein.P0ADA3"
entity_type: "protein"
name: "nlpD"
source_database: "UniProt"
source_id: "P0ADA3"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303}. Note=Localizes at the septal ring. {ECO:0000269|PubMed:19525345}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nlpD b2742 JW2712"
---

# nlpD

`protein.P0ADA3`

## Static

- Type: `protein`
- Source: `UniProt:P0ADA3`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000305}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303}. Note=Localizes at the septal ring. {ECO:0000269|PubMed:19525345}.

## Enriched Summary

FUNCTION: Activator of the cell wall hydrolase AmiC. Required for septal murein cleavage and daughter cell separation during cell division. {ECO:0000269|PubMed:19525345, ECO:0000269|PubMed:20300061}. NlpD is a divisome associated, outer membrane lipoprotein which activates the peptidoglycan (PG) hydrolase G7458-MONOMER "AmiC" involved in septal splitting . An NlpD-Mcherry fusion protein localises to the septal ring division site; envC nlpD double null mutants show significant defects in cell separation resulting in very long chain formation due to a defect in septal peptidoglycan splitting . NlpD contains a lipoprotein signal sequence, a LysM (lysin motif) domain (associated with peptidoglycan binding ) and a LytM (lysostaphin/M23 peptidase) domain (also found in EG12297-MONOMER EnvC, G7484-MONOMER YgeR and EG10013-MONOMER MepM) . NlpD (and EnvC) contain a degenerate LytM domain (dLytM) which is missing metal-binding and catalytic residues conserved in active LytM metallopeptidases . The LysM domain of NlpD is both required and sufficient for proper localization to the septal ring; the dLytM domain is required (but not sufficient) for amidase activation and cell separation in vivo; outer membrane localization is required for proper NlpD activity . NlpD contains an N-terminal, unstructured linker domain which is implicated in targeting to the outer membrane...

## Annotation

FUNCTION: Activator of the cell wall hydrolase AmiC. Required for septal murein cleavage and daughter cell separation during cell division. {ECO:0000269|PubMed:19525345, ECO:0000269|PubMed:20300061}.

## Outgoing Edges (1)

- `activates` --> [[reaction.ecocyc.RXN-16938|reaction.ecocyc.RXN-16938]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b2742|gene.b2742]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0ADA3`
- `KEGG:ecj:JW2712;eco:b2742;ecoc:C3026_15080;`
- `GeneID:947011;`
- `GO:GO:0004222; GO:0005886; GO:0009279; GO:0009410; GO:0032153; GO:0051301`

## Notes

Murein hydrolase activator NlpD
